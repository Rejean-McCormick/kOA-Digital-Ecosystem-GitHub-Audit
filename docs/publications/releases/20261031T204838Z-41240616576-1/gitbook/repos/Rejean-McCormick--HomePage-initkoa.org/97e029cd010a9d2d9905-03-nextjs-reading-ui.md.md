<!-- Frozen source: https://github.com/Rejean-McCormick/HomePage-initkoa.org/blob/3b952d1da199b8ff827141022576775e8c8c9f34/docs/reading-db-upgrade/03-nextjs-reading-ui.md | commit: 3b952d1da199b8ff827141022576775e8c8c9f34 | SHA-256: 7e170d894464c48a79f2e68773bdb0cb457e9d8843ec8e5da828326da2e8a4cc -->

---
docSet: "reading-db-upgrade"
docStatus: "draft"
project: "initkOA"
canonicalTermsVersion: "2026-05-25"
title: "Next.js Reading UI"
description: "Next.js UI architecture for the DB-backed Reading section."
docPath: "docs/reading-db-upgrade/03-nextjs-reading-ui.md"
dependsOn:
  - "docs/reading-db-upgrade/00-overview.md"
  - "docs/reading-db-upgrade/01-data-model.md"
  - "docs/reading-db-upgrade/02-import-pipeline.md"
relatedDocs:
  - "docs/reading-db-upgrade/04-ai-accessibility.md"
---

# Next.js Reading UI

## Purpose

This document defines the Next.js UI architecture for the new `Reading` section.

The goal is to expose full-text documents stored in the central database as readable, styled, server-rendered pages.

The `Reading` section is distinct from the existing `/play` section.

```txt
/play    = resource catalog
/reading = full-text document library
```

## Core decision

The `Reading` UI must read from the central document database.

```txt
Source of truth: Supabase Postgres
Public UI: Next.js App Router
Document route: /reading/[slug]
```

Documents are not primarily managed as static MDX files inside `app/`. They are stored in the database and rendered through dynamic Next.js routes.

## Route structure

Target routes:

```txt
/reading
/reading/[slug]
/reading/source/[source]
/reading/topic/[topic]
```

Route decisions:

```txt
/reading/[slug] is the canonical internal document route.
/reading/source/[source] is a filter/index route only.
/reading/topic/[topic] is a filter/index route only.
```

Do not use this as the canonical document route:

```txt
/reading/source/[source]/[slug]
```

Future admin route:

```txt
/admin/reading
```

## Route responsibilities

### `/reading`

Main document library index.

Responsibilities:

- list published documents;
- expose filters;
- expose full-text search;
- group or filter by source;
- group or filter by topic;
- show reading metadata;
- link to `/reading/[slug]`.

The index should not load full document bodies by default.

It should load only document metadata:

```ts
type ReadingIndexItem = {
  id: string;
  slug: string;
  title: string;
  description: string | null;
  source: DocumentSource;
  canonicalUrl: string | null;
  author: string | null;
  language: string;
  status: "published";
  publishedAt: string | null;
  updatedAt: string;
  topics: string[];
  readingTimeMinutes: number | null;
  wordCount: number | null;
};
```

### `/reading/[slug]`

Full document page.

Responsibilities:

- fetch one published document by slug;
- render the full document body server-side;
- expose canonical/source link when relevant;
- render metadata;
- render topics;
- render reading navigation;
- expose clean HTML for humans, crawlers, and AI.

The document body must be rendered on the server.

Avoid client-only document body rendering.

### `/reading/source/[source]`

Filtered index by source.

This route lists documents from a source. It is not a canonical document route.

Examples:

```txt
/reading/source/medium
/reading/source/markdown
/reading/source/pdf
/reading/source/manual
```

### `/reading/topic/[topic]`

Filtered index by topic.

This route lists documents assigned to a topic. It is not a canonical document route.

Examples:

```txt
/reading/topic/governance
/reading/topic/semantic_systems
/reading/topic/knowledge
```

## Relationship to `/play`

The existing `/play` section should remain a resource catalog.

A Medium article may appear in both systems:

```txt
/play item:
  title: "Cartographer of Ideas"
  type: "medium_article"
  url: "/reading/cartographer-of-ideas"
  canonicalUrl: "https://medium.com/..."

reading document:
  slug: "cartographer-of-ideas"
  source: "medium"
  body_markdown: full copied article
  canonical_url: original Medium URL
```

The public click target should become the internal reading page when the article has been imported as a full document.

External source links should still be preserved as canonical/source references.

## Data source

The UI should not read from `public/inventory.articles.catalog.json` for full reading content.

The reading UI reads from database tables:

```txt
documents
document_topics
document_assets
document_chunks
```

Minimum required query for `/reading`:

```sql
select
  documents.id,
  documents.slug,
  documents.title,
  documents.description,
  documents.source,
  documents.canonical_url,
  documents.author,
  documents.language,
  documents.status,
  documents.published_at,
  documents.updated_at
from documents
where documents.status = 'published'
order by documents.published_at desc nulls last, documents.updated_at desc;
```

Minimum required query for `/reading/[slug]`:

```sql
select
  id,
  slug,
  title,
  description,
  body_markdown,
  body_text,
  source,
  canonical_url,
  author,
  language,
  status,
  published_at,
  updated_at
from documents
where slug = $1
and status = 'published'
limit 1;
```

## Rendering rule

Document pages must be server-rendered.

Good:

```txt
Server component fetches document
↓
Markdown rendered to HTML on server
↓
HTML page contains full text
```

Avoid:

```txt
Empty page shell
↓
Client-side fetch
↓
Document body injected after hydration
```

Reason:

- AI crawlers may not execute client-side JavaScript;
- search engines may see incomplete content;
- `ai-corpus.txt` / `llms.txt` workflows require stable server-visible text;
- long documents should be readable without interactive dependencies.

## Proposed file structure

```txt
app/reading/
  layout.tsx
  page.tsx
  [slug]/
    page.tsx
  source/
    [source]/
      page.tsx
  topic/
    [topic]/
      page.tsx

components/reading/
  ReadingCard.tsx
  ReadingFilters.tsx
  ReadingHeader.tsx
  ReadingMetadata.tsx
  ReadingProse.tsx
  ReadingToc.tsx
  ReadingSourceLink.tsx

lib/reading/
  db.ts
  markdown.ts
  queries.ts
  types.ts
  slug.ts
```

## Page layout

All reading pages should share a central layout.

```tsx
// app/reading/layout.tsx

export default function ReadingLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <main className="min-h-screen bg-white text-slate-900">
      <div className="mx-auto max-w-6xl px-6 py-12">
        {children}
      </div>
    </main>
  );
}
```

Document pages should use a narrower reading width:

```tsx
<article className="mx-auto max-w-3xl">
  ...
</article>
```

## Central prose style

All full documents should share one prose wrapper.

```tsx
// components/reading/ReadingProse.tsx

export function ReadingProse({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="prose prose-slate max-w-none prose-headings:scroll-mt-24 prose-a:text-[#1e6864]">
      {children}
    </div>
  );
}
```

The goal is to avoid custom styling per document.

All document types should render inside the same central style:

```txt
Medium article
Markdown document
PDF text extraction
Manual document
Imported HTML
```

## Document metadata display

Each document page should show:

```txt
title
description
author
source
published date
language
topics
canonical/source link
reading time
```

Example visual structure:

```txt
[Source: Medium] [Language: EN] [Published: 2026-05-01]

# Cartographer of Ideas

A short description of the article.

Topics:
knowledge · governance · semantic_systems

Read original source: Medium
```

## Search and filters

The `/reading` index should support filters over database fields.

Minimum filters:

```txt
search query
source
topic
language
status = published only
```

Future filters:

```txt
author
date range
reading time
document type
has canonical URL
has assets
```

Search should check:

```txt
title
description
body_text
topics
source
author
```

Phase 1 search:

```txt
Postgres full-text search
```

Phase 2 search:

```txt
hybrid full-text + pgvector chunk search
```

## Pagination

The index should be paginated.

Recommended default:

```txt
20 documents per page
```

Reason:

- 300+ documents should not load all at once;
- some documents may have long metadata;
- filters should remain fast;
- the index should not include full bodies.

Suggested query params:

```txt
/reading?q=governance
/reading?source=medium
/reading?topic=knowledge
/reading?language=en
/reading?page=2
```

## URL conventions

Canonical internal document route:

```txt
/reading/[slug]
```

Source and topic routes are discovery/filter routes only:

```txt
/reading/source/[source]
/reading/topic/[topic]
```

Slug rules:

```txt
lowercase
kebab-case
stable after publication
unique
short hash on collision
```

Examples:

```txt
/reading/cartographer-of-ideas
/reading/the-sacrificial-pole
/reading/war-is-not-a-defect-of-peoples-it-is-a-defect-of-governance
```

## Source conventions

Allowed source values:

```txt
medium
markdown
pdf
manual
imported_html
```

Source pages:

```txt
/reading/source/medium
/reading/source/markdown
/reading/source/pdf
```

Source pages must list documents. They must not become per-document canonical routes.

## Topic conventions

Topics should use canonical topic keys.

Examples:

```txt
knowledge
governance
semantic_systems
social_cohesion
data_sovereignty
```

Topic pages:

```txt
/reading/topic/governance
/reading/topic/semantic_systems
```

Topic keys should use snake_case to align with the data model.

## Empty states

The UI must handle empty states clearly.

Examples:

```txt
No published documents found.
No documents match this search.
No documents found for this topic.
This document is not published.
```

For unpublished or missing documents, return Next.js `notFound()`.

## Draft and private documents

Only published documents should appear publicly.

Rules:

```txt
status = draft     → not visible publicly
status = archived  → not visible in normal browsing
status = published → visible at /reading/[slug]
```

Admin preview can be added later.

## SEO rules

Each document page should define metadata:

```ts
export async function generateMetadata({ params }) {
  const document = await getPublishedDocumentBySlug(params.slug);

  return {
    title: document.title,
    description: document.description ?? undefined,
    alternates: document.canonicalUrl
      ? { canonical: document.canonicalUrl }
      : undefined,
  };
}
```

Important distinction:

- `/reading/[slug]` is the canonical internal initkOA route.
- `canonical_url` is a database field preserving the original external source URL when applicable.
- For original Medium articles, `canonical_url` should remain the Medium URL.
- The UI should expose the original source link, but the readable copy lives at `/reading/[slug]`.

## AI accessibility rules

The document body must be visible in server-rendered HTML.

Each published document should eventually be exposed through:

```txt
HTML page: /reading/[slug]
AI manifest: md-manifest.json
AI corpus: ai-corpus.txt
LLM discovery: llms.txt
```

The UI must avoid hiding the document body behind:

```txt
client-only rendering
auth-only access
pagination inside a single document
collapsed sections that are not present in HTML
```

## Long document handling

Documents may range from 1 to 100 pages.

The UI should support:

```txt
table of contents
anchor links
reading width
section headings
back-to-top links
chunk-aware AI extraction
```

Long documents should still be one canonical page unless they are intentionally split.

Optional future route for very long documents:

```txt
/reading/[slug]/section/[sectionSlug]
```

Do not implement section routes in phase 1 unless necessary.

## Components

### `ReadingCard`

Used in indexes.

Fields:

```ts
type ReadingCardProps = {
  title: string;
  description?: string | null;
  href: string;
  source: string;
  language: string;
  publishedAt?: string | null;
  topics: string[];
  readingTimeMinutes?: number | null;
};
```

### `ReadingMetadata`

Used on document pages.

Fields:

```ts
type ReadingMetadataProps = {
  source: string;
  author?: string | null;
  language: string;
  publishedAt?: string | null;
  updatedAt?: string | null;
  topics: string[];
};
```

### `ReadingSourceLink`

Used when a document has a canonical external source.

Fields:

```ts
type ReadingSourceLinkProps = {
  canonicalUrl: string;
  source: string;
};
```

### `ReadingFilters`

Used on `/reading`.

Fields:

```ts
type ReadingFiltersProps = {
  query?: string;
  source?: string;
  topic?: string;
  language?: string;
};
```

## Markdown rendering

Documents store `body_markdown`.

The UI should render Markdown server-side.

Rendering requirements:

```txt
headings
links
lists
blockquotes
code blocks
tables
images later
```

The Markdown renderer should sanitize or control HTML.

Raw HTML from imports should not be blindly rendered.

## Images and assets

Phase 1 can ignore images or keep external image URLs.

Phase 2 should support assets:

```txt
document_assets
Supabase Storage
```

Asset fields:

```txt
document_id
asset_type
storage_path
public_url
alt_text
source_url
```

## Caching

Reading pages can be cached, but cache invalidation must be simple.

Phase 1 recommendation:

```txt
dynamic rendering with conservative caching
```

Later:

```txt
revalidate by tag
revalidate document on update
```

Potential cache tags:

```txt
reading
reading:document:{slug}
reading:source:{source}
reading:topic:{topic}
```

## Error handling

Database unavailable:

```txt
show server error
do not show empty library as if valid
```

Document not found:

```txt
notFound()
```

Draft document requested publicly:

```txt
notFound()
```

Invalid source/topic:

```txt
empty filtered page or notFound(), depending on final product decision
```

## Migration behavior from `/play`

When a Medium article is imported into `documents`, the corresponding `/play` resource may be updated:

```txt
old url: https://medium.com/...
new url: /reading/cartographer-of-ideas
canonicalUrl: https://medium.com/...
```

This keeps `/play` useful as a discovery surface while moving reading to `/reading`.

## Implementation phases

### Phase 1 — Public reading MVP

Create:

```txt
app/reading/page.tsx
app/reading/[slug]/page.tsx
app/reading/layout.tsx
components/reading/*
lib/reading/*
```

Support:

```txt
published documents only
source filter
topic filter
basic text search
server-rendered body
central prose style
```

### Phase 2 — Medium migration

Connect imported Medium articles to `/reading`.

Support:

```txt
source = medium
canonical_url = Medium URL
body_markdown from local Medium HTML or imported Markdown
/play item points to internal reading URL
```

### Phase 3 — Markdown bulk import

Support dropping many `.md` files into an import folder and importing to DB.

```txt
content/reading-inbox/**/*.md
↓
scripts/import-reading-md-to-db.mjs
↓
documents table
```

### Phase 4 — AI corpus integration

Expose reading documents to AI assets.

Support:

```txt
document_chunks
body_text
ai-corpus integration
llms.txt references
md-manifest entries
```

### Phase 5 — Admin UI

Create:

```txt
/admin/reading
```

Support:

```txt
edit metadata
publish/unpublish
view import status
rebuild chunks
manage topics
```

## Acceptance criteria

The Reading UI is acceptable when:

```txt
/reading lists published documents from the DB
/reading/[slug] renders full document body server-side
documents have a consistent central style
filters work by source, topic, language, and search
Medium documents keep their original external canonical_url
/play remains a resource catalog
source/topic routes remain filter/index routes only
AI/crawlers can see full document text in HTML
```

## Non-goals

This document does not define:

```txt
Supabase schema details
import parser internals
PDF extraction details
embedding strategy
admin permissions
billing/security policy
```

Those belong in:

```txt
01-data-model.md
02-import-pipeline.md
04-ai-accessibility.md
```