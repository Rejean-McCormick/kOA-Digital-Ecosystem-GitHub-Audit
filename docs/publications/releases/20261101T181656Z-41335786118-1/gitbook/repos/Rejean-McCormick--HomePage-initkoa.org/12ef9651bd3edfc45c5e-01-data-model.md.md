<!-- Frozen source: https://github.com/Rejean-McCormick/HomePage-initkoa.org/blob/3b952d1da199b8ff827141022576775e8c8c9f34/docs/reading-db-upgrade/01-data-model.md | commit: 3b952d1da199b8ff827141022576775e8c8c9f34 | SHA-256: 4c74c9d606ffa87a8a2d1533e5a0a58d7e1ec69637a2f4bada2c65bfaf9a8ecc -->

  document_id uuid not null references documents(id) on delete cascade,

  chunk_index integer not null,
  heading text,
  content text not null,

  token_estimate integer,
  char_count integer,

  metadata jsonb not null default '{}'::jsonb,

  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),

  unique (document_id, chunk_index)
);
```

Future migration:

```sql
create extension if not exists vector;

alter table document_chunks
add column embedding vector(1536);
```

Embedding dimension may change depending on the chosen embedding model.

---

# `document_assets`

Stores references to original source files and related media.

Examples:

```txt
original .md file
original Medium HTML export
PDF source
image
attachment
audio
```

```sql
create table document_assets (
  id uuid primary key default gen_random_uuid(),

  document_id uuid not null references documents(id) on delete cascade,

  asset_type text not null,
  storage_provider text not null default 'supabase',
  storage_path text,
  public_url text,

  original_filename text,
  mime_type text,
  byte_size bigint,

  alt_text text,
  source_url text,

  metadata jsonb not null default '{}'::jsonb,

  created_at timestamptz not null default now(),

  constraint document_assets_type_check check (
    asset_type in ('source_md', 'source_html', 'source_pdf', 'image', 'attachment', 'other')
  )
);
```

---

# `import_runs`

Logs each import execution.

```sql
create table import_runs (
  id uuid primary key default gen_random_uuid(),

  importer text not null,
  source text not null,

  status text not null default 'running',

  started_at timestamptz not null default now(),
  finished_at timestamptz,

  read_count integer not null default 0,
  created_count integer not null default 0,
  updated_count integer not null default 0,
  skipped_count integer not null default 0,
  error_count integer not null default 0,

  metadata jsonb not null default '{}'::jsonb,

  constraint import_runs_status_check check (
    status in ('running', 'success', 'partial_success', 'failed')
  )
);
```

Importer examples:

```txt
medium_rss
medium_local_html
markdown_drop
pdf_import
manual_admin
```

---

# `import_items`

Logs per-document import results.

```sql
create table import_items (
  id uuid primary key default gen_random_uuid(),

  import_run_id uuid not null references import_runs(id) on delete cascade,
  document_id uuid references documents(id) on delete set null,

  external_id text,
  source_url text,
  source_path text,

  action text not null,
  status text not null,

  title text,
  slug text,

  error_message text,
  metadata jsonb not null default '{}'::jsonb,

  created_at timestamptz not null default now(),

  constraint import_items_action_check check (
    action in ('created', 'updated', 'skipped', 'failed')
  ),

  constraint import_items_status_check check (
    status in ('success', 'warning', 'error')
  )
);
```

---

# Search Model

## Phase 1 — Postgres Full-Text Search

Add generated search vector to `documents`.

```sql
alter table documents
add column search_vector tsvector generated always as (
  to_tsvector(
    'simple',
    coalesce(title, '') || ' ' ||
    coalesce(description, '') || ' ' ||
    coalesce(body_text, '') || ' ' ||
    coalesce(author, '') || ' ' ||
    coalesce(source, '')
  )
) stored;
```

Index:

```sql
create index documents_search_idx
on documents using gin(search_vector);
```

Basic query:

```sql
select *
from documents
where status = 'published'
and search_vector @@ plainto_tsquery('simple', 'governance knowledge')
order by published_at desc nulls last;
```

Topic search should use `document_topics` directly.

Example:

```sql
select distinct documents.*
from documents
join document_topics
  on document_topics.document_id = documents.id
where documents.status = 'published'
and document_topics.topic = 'governance'
order by documents.published_at desc nulls last;
```

If topic search needs to be included inside `search_vector`, add a future materialized topic field such as:

```txt
documents.search_topics
```

or build a materialized view that combines:

```txt
documents
document_topics
```

Do not attempt to reference `document_topics` directly inside a generated column on `documents`.

## Language-Aware Search

Phase 1 uses the Postgres `simple` text search configuration.

Reason:

```txt
The corpus may contain English and French documents.
A single 'english' configuration is too narrow for mixed-language search.
```

Phase 2 can add language-aware search.

Possible future strategy:

```txt
language = en → english text search configuration
language = fr → french text search configuration
fallback    → simple text search configuration
```

## Phase 2 — Hybrid Search

Hybrid search combines:

```txt
title/description/body_text full-text search
metadata filters
topic filters
vector search over document_chunks
```

---

# Indexes

Recommended initial indexes:

```sql
create index documents_status_idx
on documents(status);

create index documents_source_idx
on documents(source);

create index documents_language_idx
on documents(language);

create index documents_published_at_idx
on documents(published_at desc nulls last);

create index documents_canonical_url_idx
on documents(canonical_url);

create index document_topics_topic_idx
on document_topics(topic);

create index document_chunks_document_id_idx
on document_chunks(document_id);

create index import_runs_source_idx
on import_runs(source);

create index import_items_source_url_idx
on import_items(source_url);
```

---

# Status Rules

## `draft`

Document exists in DB but is not publicly visible.

Rules:

```txt
not listed on /reading
not exposed in public AI corpus
can be edited/imported
```

## `published`

Document is public.

Rules:

```txt
visible on /reading
visible at /reading/[slug]
eligible for AI/discovery artifacts
eligible for search
```

## `archived`

Document is retained but hidden from normal browsing.

Rules:

```txt
not listed on /reading by default
not included in public AI artifacts by default
can be accessed by admin
```

---

# Source Rules

## `medium`

Imported from Medium RSS or local Medium HTML export.

Required:

```txt
canonical_url
published_at if available
author if available
```

## `markdown`

Imported from local `.md` source.

Required:

```txt
title
body_markdown
```

Optional:

```txt
canonical_url
source_path
topics
description
```

## `pdf`

Imported from PDF source.

Required:

```txt
title
body_text
body_markdown generated from extracted text, even if plain/basic
document_assets entry for source PDF
```

Optional:

```txt
extraction_quality
extraction_method
asset_original_path
```

Rule:

```txt
body_markdown is still required for PDF imports because documents.body_markdown is not nullable.
```

## `manual`

Created manually through a future admin UI.

## `imported_html`

Imported from generic HTML source not specifically Medium.

---

# Markdown Storage Rules

The DB stores:

```txt
body_markdown = canonical readable source
body_text     = normalized plain text for search/AI
```

The original file may also be stored as an asset.

Do not rely only on external files for the published reading page.

The DB must be able to render `/reading/[slug]` without needing the original local file.

---

# AI Accessibility Rules

Only documents with:

```txt
status = published
```

are eligible for public AI discovery.

The reading page must render full text server-side.

Do not make document body client-only.

Good:

```txt
/reading/cartographer-of-ideas
→ HTML includes full document body
```

Avoid:

```txt
/reading/cartographer-of-ideas
→ empty shell
→ client fetches body after load
```

---

# RLS Policy Direction

Supabase Row Level Security should be enabled.

Recommended rule:

```txt
public anonymous users can read published documents only
service role can insert/update/delete
future authenticated admin can manage documents
```

Example direction:

```sql
alter table documents enable row level security;

create policy "Public can read published documents"
on documents
for select
using (status = 'published');
```

Child tables should use parent-document visibility.

```sql
alter table document_topics enable row level security;
alter table document_assets enable row level security;
alter table document_chunks enable row level security;

create policy "Public can read topics for published documents"
on document_topics
for select
using (
  exists (
    select 1
    from documents
    where documents.id = document_topics.document_id
    and documents.status = 'published'
  )
);

create policy "Public can read assets for published documents"
on document_assets
for select
using (
  exists (
    select 1
    from documents
    where documents.id = document_assets.document_id
    and documents.status = 'published'
  )
);

create policy "Public can read chunks for published documents"
on document_chunks
for select
using (
  exists (
    select 1
    from documents
    where documents.id = document_chunks.document_id
    and documents.status = 'published'
  )
);
```

For write operations:

```txt
Use service role key only from server-side scripts or secure server routes.
Never expose SUPABASE_SERVICE_ROLE_KEY to the browser.
```

---

# Environment Variables

Required later:

```txt
DATABASE_URL
NEXT_PUBLIC_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY
SUPABASE_SERVICE_ROLE_KEY
```

Import-specific:

```txt
MEDIUM_RSS_URL
MEDIUM_SOURCE_DIR
READING_IMPORT_DIR
```

---

# Migration Phases

## Phase 0 — Documentation

Define architecture and data model.

## Phase 1 — Supabase Schema

Create:

```txt
documents
document_topics
import_runs
import_items
```

Optional but recommended:

```txt
document_versions
document_assets
```

## Phase 2 — Medium Import

Import from:

```txt
content/medium/source/*.html
Medium RSS
```

Write to:

```txt
documents
document_topics
document_assets
import_runs
import_items
```

## Phase 3 — Reading UI

Create:

```txt
/reading
/reading/[slug]
```

## Phase 4 — Markdown Import

Import local `.md` files into DB.

## Phase 5 — AI Chunks

Generate:

```txt
document_chunks
body_text
search_vector
```

Optional later:

```txt
embeddings
pgvector search
```

## Phase 6 — Admin UI

Create future:

```txt
/admin/reading
```

---

# Non-Goals For This Phase

Do not build the full admin editor yet.

Do not replace `/play`.

Do not require vector search for the first version.

Do not store private documents publicly.

Do not use the DB as an unstructured dump without metadata.

---

# Resolved Decisions

## Slug Scope

Decision:

```txt
Slugs are globally unique.
```

Use:

```txt
/reading/[slug]
```

Do not scope slugs by source.

Reason:

- simpler URLs;
- easier sharing;
- cleaner AI references;
- avoids duplicate-looking routes;
- keeps `/reading` as one unified library.

If a collision occurs, append a short stable hash.

Examples:

```txt
/reading/cartographer-of-ideas
/reading/cartographer-of-ideas-d362d695
```

This aligns with the existing slug rule in this document:

```txt
unique globally
append short hash on collision
```

---

## Canonical Reading Route

Decision:

```txt
/reading/[slug] is the canonical internal route.
```

Do not use this as the canonical document route:

```txt
/reading/source/[source]/[slug]
```

Source routes are index/filter routes only.

Use:

```txt
/reading/source/medium
/reading/source/markdown
/reading/source/pdf
```

for browsing by source.

Document pages stay flat:

```txt
/reading/cartographer-of-ideas
```

---

## `/play` Medium URLs

Decision:

```txt
Old Medium URLs in /play should be replaced with internal reading URLs when a document copy exists.
```

Before import into the Reading DB:

```txt
/play item url = https://medium.com/...
```

After import into the Reading DB:

```txt
/play item url = /reading/cartographer-of-ideas
/play item canonicalUrl = https://medium.com/...
```

Reason:

- `/play` remains a discovery catalog;
- `/reading` becomes the place where the full text is read;
- Medium remains preserved as canonical/source URL;
- AI can access the internal full-text copy.

This aligns with the import pipeline policy:

```txt
/play Medium cards point to /reading/[slug].
Original Medium URLs stay in canonical_url.
```

---

## Medium Article Storage Format

Decision:

```txt
Store Markdown + plain text in documents.
Store original HTML as an asset/snapshot.
```

Use:

```txt
documents.body_markdown = canonical readable body
documents.body_text     = normalized text for search/AI
document_assets         = original Medium HTML export
```

Do not render raw Medium HTML directly as the main document body.

Reason:

- Markdown is cleaner for rendering;
- body_text is better for search and AI;
- original HTML remains auditable;
- raw imported HTML can contain unwanted formatting/noise.

Recommended asset entry:

```txt
asset_type = source_html
storage_provider = supabase
storage_path = original Medium HTML path or Supabase Storage path
original_filename = exported Medium filename
mime_type = text/html
```

Phase alignment:

```txt
Phase 1: keep normalized body_markdown/body_text in Postgres and keep local originals in Git/repo.
Phase 2: move original .html/.md/.pdf files into Supabase Storage and reference them through document_assets.
```

---

## Topic Reuse

Decision:

```txt
Document topics should reuse existing inventory topics where they match.
```

But topics must represent subject matter, not format or origin.

Good topics:

```txt
governance
semantic_systems
knowledge_infrastructure
data_sovereignty
social_cohesion
```

Avoid as topics:

```txt
medium_article
pdf
markdown
```

Those belong in:

```txt
documents.source
documents.metadata
/play resource type
```

Rule:

```txt
source = where it came from
topic  = what it is about
type   = resource/document classification when needed
```

If existing inventory topics are noisy or inconsistent, define a normalized topic registry later.

---

## Long Document Display

Decision:

```txt
Display long documents as one canonical page in phase 1.
Chunk internally for AI/search.
Do not visually paginate by default.
```

Use:

```txt
/reading/[slug]
```

for the whole document.

Support long-document usability with:

```txt
table of contents
heading anchors
reading width
back-to-top
section navigation
server-rendered HTML
```

Use `document_chunks` for:

```txt
AI retrieval
search
summaries
embeddings
internal navigation
```

Do not split public routes unless a document is intentionally authored as a multi-part work.

Optional future route:

```txt
/reading/[slug]/section/[sectionSlug]
```

Only add this later for extremely long or deliberately structured documents.

---

## Resolved Questions Summary

```txt
Slugs: globally unique
Canonical route: /reading/[slug]
Source routes: filter/index only
/play Medium URLs: replace with internal /reading URL when full copy exists
Medium storage: Markdown + plain text in DB, original HTML as asset
Topics: reuse existing subject topics, but do not use source/type as topic
Long docs: one canonical page, internal chunks for AI/search
```

---

# Decision Summary

The Reading DB upgrade uses:

```txt
Supabase Postgres = central source of truth
documents = readable full-text entities
document_topics = metadata filtering
document_chunks = future AI/search retrieval
document_assets = original files and media
import_runs/import_items = import observability
```

The site keeps:

```txt
/play = resources and external links
/reading = full-text public library
```

The resolved data-model decisions are:

```txt
slugs are globally unique
/reading/[slug] is the canonical internal document route
/reading/source/[source] and /reading/topic/[topic] are filter/index routes only
/play Medium resources point to /reading/[slug] when a full DB copy exists
canonical_url preserves the original external source URL
body_markdown and body_text are stored in Postgres
original HTML/Markdown/PDF sources are tracked through document_assets
topics describe subject matter, not file format or source type
long documents render as one canonical page and are chunked internally
phase 1 search uses the simple Postgres text search configuration
topic search uses document_topics joins or a future materialized topic field
document_chunks has created_at and updated_at
document_assets stores alt_text and source_url when available
PDF imports always generate body_markdown from extracted text
RLS child tables inherit public visibility from published parent documents
```
