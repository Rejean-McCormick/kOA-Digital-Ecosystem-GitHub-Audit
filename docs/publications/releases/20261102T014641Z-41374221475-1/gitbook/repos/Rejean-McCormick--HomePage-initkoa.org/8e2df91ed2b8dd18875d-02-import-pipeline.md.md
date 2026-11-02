<!-- Frozen source: https://github.com/Rejean-McCormick/HomePage-initkoa.org/blob/3b952d1da199b8ff827141022576775e8c8c9f34/docs/reading-db-upgrade/02-import-pipeline.md | commit: 3b952d1da199b8ff827141022576775e8c8c9f34 | SHA-256: e22eb65b8d1f3771344975e31e10b496f5657efe64df2315cd300f2269b68ab3 -->

---
docSet: "reading-db-upgrade"
docStatus: "draft"
project: "initkOA"
canonicalTermsVersion: "2026-05-25"
docPath: "docs/reading-db-upgrade/02-import-pipeline.md"
dependsOn:
  - "docs/reading-db-upgrade/00-overview.md"
  - "docs/reading-db-upgrade/01-data-model.md"
relatedDocs:
  - "docs/reading-db-upgrade/03-nextjs-reading-ui.md"
  - "docs/reading-db-upgrade/04-ai-accessibility.md"
---

# 02 — Import Pipeline

## Purpose

This document defines the import pipeline for the `reading-db-upgrade`.

The goal is to move from a link-based resource catalog to a DB-backed reading library where full documents are stored, rendered, searched, and exposed to AI systems.

The import pipeline must support:

- Medium RSS metadata;
- local Medium HTML exports;
- Markdown documents;
- future PDF imports;
- future manual/admin-created documents;
- deduplication;
- canonical source preservation;
- DB writes;
- AI/search chunk generation.

## Core Decision

The central source of truth for full readable documents is:

```txt
Supabase Postgres
```

The current `/play` catalog remains a resource index. The new `/reading` section becomes the full-text document library.

```txt
/play    = resource catalog
/reading = full-text document library
```

## Current State

The existing system already has:

```txt
scripts/import-medium-rss.mjs
public/inventory.articles.catalog.json
content/medium/source/*.html
```

The current Medium import writes catalog metadata into:

```txt
public/inventory.articles.catalog.json
```

This is useful for `/play`, but it does not make complete article bodies available as internal readable pages.

## Target State

The new pipeline writes full document records into the central DB.

```txt
Medium RSS
Medium HTML exports
Markdown files
PDF files
manual/admin entries
        ↓
import scripts
        ↓
Supabase Postgres
        ↓
/reading
/reading/[slug]
        ↓
AI corpus / search / chunks
```

## Terminology

| Term | Meaning |
|---|---|
| `resource` | A catalog reference, usually a link or external item. |
| `document` | A full-text readable item stored in the central DB. |
| `canonical_url` | Original external source URL, such as a Medium URL. |
| `internal_path` | The initkOA route where the document is rendered. |
| `body_markdown` | Normalized Markdown body stored in DB. |
| `body_text` | Plain text extracted from Markdown for search and AI. |
| `chunk` | A smaller section of a document prepared for AI/search. |
| `asset` | Original source file or related media object. |

## Pipeline Sources

| Source | Status | Target Script | Notes |
|---|---:|---|---|
| Medium RSS | existing / transitional | `scripts/import-medium-to-reading-db.mjs` | Discovers recent Medium items and canonical URLs. |
| Medium local HTML | existing / important | `scripts/import-medium-to-reading-db.mjs` | Imports historical Medium exports from `content/medium/source/*.html`. |
| Markdown files | planned | `scripts/import-reading-md-to-db.mjs` | Imports `.md` documents from a local inbox. |
| PDF files | future | `scripts/import-reading-pdf-to-db.mjs` | Stores original PDF and extracted text. |
| Manual/admin entries | future | admin UI | Creates or edits DB documents directly. |

## Environment Variables

```txt
DATABASE_URL
NEXT_PUBLIC_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY
SUPABASE_SERVICE_ROLE_KEY

MEDIUM_RSS_URL
MEDIUM_SOURCE_DIR
READING_IMPORT_DIR
```

## Package Scripts

Target scripts:

```json
{
  "reading:import": "node scripts/import-reading-md-to-db.mjs",
  "reading:medium": "node scripts/import-medium-to-reading-db.mjs",
  "reading:sync": "npm run reading:medium && npm run reading:import"
}
```

Current transitional script:

```json
{
  "import:medium": "node scripts/import-medium-rss.mjs"
}
```

## Import Lifecycle

Every importer should follow the same lifecycle.

```txt
discover
extract
normalize
dedupe
classify
validate
write
chunk
log
publish
```

### 1. Discover

Find candidate source items.

Examples:

```txt
MEDIUM_RSS_URL
content/medium/source/*.html
content/reading-inbox/**/*.md
content/pdf-inbox/**/*.pdf
```

Discovery should not write to the DB.

### 2. Extract

Extract raw fields from the source.

Common extracted fields:

```txt
title
description
body_markdown
body_text
canonical_url
author
language
source
published_at
topics
assets
```

### 3. Normalize

Normalize the extracted content into the canonical document model.

Required normalization:

```txt
HTML → Markdown
Markdown → body_text
title → slug
topics → lowercase stable keys
dates → ISO timestamps
URLs → canonical normalized URLs
language → en/fr/other
status → draft/published/archived
```

### 4. Dedupe

Deduplication must happen before insert.

Deduplication priority:

```txt
1. canonical_url exact match
2. slug exact match
3. title + published_at match
4. content hash match
```

A document should not be duplicated just because it appears in both:

```txt
Medium RSS
content/medium/source/*.html
```

### 5. Classify

Add source and metadata.

Valid `source` values:

```txt
medium
markdown
pdf
manual
imported_html
```

Valid `status` values:

```txt
draft
published
archived
```

Default values:

```txt
status = "published" for Medium imports
status = "draft" for Markdown, PDF, and manual imports unless explicitly set
language = "en" unless inferred or provided
source = inferred from importer
```

### 6. Validate

Validation must happen before DB write.

Minimum validation:

```txt
title exists
slug exists
body_markdown exists
body_text exists
source is valid
status is valid
slug is unique or collision-safe
canonical_url is valid when present
```

For public documents:

```txt
status = "published"
internal_path = "/reading/{slug}"
```

### 7. Write

Write to Supabase Postgres.

Target tables:

```txt
documents
document_topics
document_versions
document_chunks
document_assets
import_runs
import_items
```

The importer should use upsert behavior.

Primary upsert key:

```txt
canonical_url
```

Fallback upsert key:

```txt
slug
```

### 8. Chunk

Chunking is required for future AI/search workflows.

Initial chunking can be simple:

```txt
1 chunk per heading section
max 1,000–1,500 words per chunk
preserve document_id
preserve chunk_index
preserve heading path
```

Target table:

```txt
document_chunks
```

Fields:

```txt
document_id
chunk_index
heading
content
token_estimate
embedding
created_at
updated_at
```

The `embedding` field is optional in phase 1 and can be added later with `pgvector`.

### 9. Log

Every import run should be auditable.

Target table:

```txt
import_runs
```

Suggested fields:

```txt
id
source
started_at
finished_at
status
items_discovered
items_created
items_updated
items_skipped
error_message
```

Optional per-item audit table:

```txt
import_items
```

Suggested fields:

```txt
id
import_run_id
source_identifier
document_id
status
message
```

### 10. Publish

A document is publicly visible only when:

```txt
status = "published"
```

The reading UI must not render:

```txt
draft
archived
```

unless explicitly requested in an admin context.

## Medium Import Pipeline

### Inputs

```txt
MEDIUM_RSS_URL
content/medium/source/*.html
```

### Output

Rows in:

```txt
documents
document_topics
document_versions
document_chunks
import_runs
import_items
```

### Medium RSS Role

Medium RSS is used for:

```txt
recent article discovery
canonical URL discovery
publication date
categories/tags when available
description snippets
```

It should not be treated as the only source of truth, because RSS may not contain the full article history.

### Medium Local HTML Role

Local Medium HTML exports are used for:

```txt
historical article recovery
full article body extraction
stable local source import
```

This is currently the most important source for importing the existing Medium archive.

### Medium Deduplication

If the same article appears in both RSS and local HTML:

```txt
merge into one document
prefer local HTML body
prefer RSS categories when useful
preserve canonical_url
preserve published_at
```

### Medium Canonical URL

The importer should extract canonical URLs from:

```html
<a class="p-canonical" href="...">
```

Fallbacks:

```txt
RSS link
Medium /p/{id} link
filename hash
```

### Medium Body Extraction

Preferred extraction order:

```txt
1. article body from exported HTML
2. content:encoded from RSS
3. description/snippet only as fallback
```

The DB should store:

```txt
body_markdown
body_text
```

not just a URL or description.

## Markdown Import Pipeline

### Input

```txt
content/reading-inbox/**/*.md
```

### Markdown Metadata

Markdown may include frontmatter, but the DB is the source of truth after import.

Example:

```md
---
title: "Document Title"
description: "Short summary."
date: "2026-05-01"
author: "Réjean McCormick"
source: "markdown"
language: "en"
topics:
  - governance
  - knowledge
status: "published"
---

# Document Title

Document body...
```

### Markdown Import Rule

The importer should:

```txt
parse frontmatter
extract body_markdown
derive body_text
generate slug if missing
upsert into documents
sync topics
generate chunks
log result
```

## PDF Import Pipeline

PDF import is future phase.

### Input

```txt
content/pdf-inbox/**/*.pdf
```

### Target Behavior

```txt
store original PDF as asset
extract text
convert extracted text to body_markdown
store body_text
generate chunks
link asset to document
```

### PDF Warning

PDF text extraction may be imperfect. The pipeline should preserve the original file and mark extracted text as machine-derived.

Suggested metadata:

```txt
extraction_quality
extraction_method
asset_original_path
```

## Manual/Admin Pipeline

Future admin UI:

```txt
/admin/reading
```

Capabilities:

```txt
create document
edit document
publish/unpublish
assign topics
edit slug
view import history
regenerate chunks
```

Manual edits must not be overwritten by automated import unless explicitly configured.

## Preserve Manual Curation

Importers must preserve manually curated fields when they already exist.

Preserve:

```txt
slug
title overrides
description overrides
topics
status
featured flags
manual notes
primary topic/source classification
```

Safe to update automatically:

```txt
body_markdown
body_text
canonical_url
published_at
source
updated_at
chunks
```

## Conflict Rules

When importer and DB disagree:

| Field | Rule |
|---|---|
| `slug` | Preserve DB value. |
| `status` | Preserve DB value. |
| `topics` | Merge; do not erase manual topics. |
| `description` | Preserve DB value unless empty. |
| `body_markdown` | Update from source if changed. |
| `canonical_url` | Preserve if valid; fill if missing. |
| `published_at` | Fill if missing; avoid overwriting manually fixed dates. |

## Decisions

### 1. Should imported Medium documents default to `published` or `draft`?

Decision:

```txt
Medium imports default to published.
```

Reason:

Medium articles are already public. The `/reading` copy is an internal readable mirror, not a private draft.

Rule:

```txt
source = "medium" → status = "published"
source = "markdown" → status = "draft" by default unless explicitly marked published
source = "pdf" → status = "draft" by default
source = "manual" → status = "draft" by default
```

Exception:

If an importer receives an explicit status value, preserve it.

```txt
explicit status always wins
```

### 2. Should `/play` Medium resources point to Medium or `/reading/[slug]`?

Decision:

```txt
/play Medium resources should point to /reading/[slug]
```

Reason:

The internal `/reading/[slug]` page makes the document readable by humans, search engines, and AI. Medium remains the canonical external source.

Rule:

```txt
primary URL = /reading/[slug]
canonical_url = original Medium URL
external_source_url = original Medium URL
```

UI behavior:

```txt
/play card click → /reading/[slug]
/reading/[slug] page → shows "Original on Medium" link
```

This keeps `/play` as a resource catalog while making the full text available internally.

### 3. Should original `.html` and `.md` files be stored in Supabase Storage?

Decision:

```txt
Yes, but not in phase 1.
```

Phase 1:

```txt
Store normalized body_markdown and body_text in Postgres.
Keep original local files in Git/repo during migration.
```

Phase 2:

```txt
Store original .html, .md, .pdf files in Supabase Storage.
Link them through document_assets.
```

Reason:

Postgres should hold the normalized readable content. Storage should hold original source files for audit, recovery, and reprocessing.

Rule:

```txt
documents.body_markdown = normalized reading body
documents.body_text = searchable plain text
document_assets = original source files
```

### 4. Should article images be imported or hotlinked?

Decision:

```txt
Phase 1: hotlink images.
Phase 2: import images into storage.
```

Reason:

Hotlinking is faster and simpler for the first working version. Importing images is better long-term because it avoids broken external images and gives full control.

Phase 1 rule:

```txt
Keep image URLs as they appear in the source.
```

Phase 2 rule:

```txt
Download images.
Store in Supabase Storage or Vercel Blob.
Rewrite image URLs to internal asset URLs.
Track image assets in document_assets.
```

Important:

If an image is essential to the argument of the article, it should eventually be imported, not only hotlinked.

### 5. Should document chunks be generated during import or as a separate job?

Decision:

```txt
Generate basic chunks during import.
Generate embeddings as a separate job.
```

Reason:

Chunks are structural and deterministic. They can be created immediately. Embeddings depend on provider, model, cost, rate limits, and retries, so they should be decoupled.

Phase 1:

```txt
import document
generate body_text
generate heading-based chunks
write document_chunks without embeddings
```

Phase 2:

```txt
run embedding job
fill document_chunks.embedding
```

Rule:

```txt
importers must always generate chunks
embedding generation is optional and async
```

Suggested scripts:

```json
{
  "reading:import": "node scripts/import-reading-md-to-db.mjs",
  "reading:medium": "node scripts/import-medium-to-reading-db.mjs",
  "reading:chunks": "node scripts/generate-reading-chunks.mjs",
  "reading:embed": "node scripts/embed-reading-chunks.mjs"
}
```

### 6. Should AI artifacts include full `/reading` text immediately or only summaries first?

Decision:

```txt
Start with summaries + metadata in global AI artifacts.
Expose full text through individual /reading/[slug] pages.
```

Reason:

A single global `ai-corpus.txt` can become too large if it includes hundreds of full documents. The AI discovery layer should help agents find documents, then read the specific pages.

Phase 1 AI artifacts:

```txt
/llms.txt
/md-manifest.json
/ai-corpus.txt
```

should include:

```txt
title
description
slug
source
topics
language
published_at
canonical_url
internal_path
short summary
```

But not necessarily the full body of every document.

Each individual page should include the full text:

```txt
/reading/[slug] = full server-rendered document body
```

Phase 2:

Add segmented AI files:

```txt
/reading/ai-index.json
/reading/corpus/medium.txt
/reading/corpus/topic-governance.txt
/reading/corpus/document-slug.md
```

Rule:

```txt
global AI files = discovery and summaries
individual reading pages = full text
optional segmented corpus files = full text grouped safely
```

## Search Preparation

The importer must prepare:

```txt
body_text
document_chunks
```

Phase 1 search:

```txt
Postgres full-text search
```

Phase 2 search:

```txt
pgvector embeddings in document_chunks
```

Phase 3 search:

```txt
hybrid full-text + vector + filters
```

## AI Accessibility Requirements

Published documents must be rendered server-side at:

```txt
/reading/[slug]
```

Do not rely on client-side-only fetching for the document body.

Required:

```txt
HTML contains the full document body
canonical_url is available in metadata
internal route is stable
document is discoverable from /reading
AI artifacts can include /reading content
```

## Validation Commands

Future validation commands:

```bash
npm run reading:medium
npm run reading:import
npm run reading:sync
```

Expected output shape:

```txt
Import complete.
Source: medium
Discovered: 31
Created: 21
Updated: 10
Skipped: 0
Published documents: 31
Chunks generated: ...
```

## Migration Plan

### Phase 0 — Documentation

Create:

```txt
docs/reading-db-upgrade/00-overview.md
docs/reading-db-upgrade/01-data-model.md
docs/reading-db-upgrade/02-import-pipeline.md
docs/reading-db-upgrade/03-nextjs-reading-ui.md
docs/reading-db-upgrade/04-ai-accessibility.md
```

### Phase 1 — DB Schema

Create Supabase tables:

```txt
documents
document_topics
document_versions
document_chunks
document_assets
import_runs
import_items
```

### Phase 2 — Medium DB Import

Create:

```txt
scripts/import-medium-to-reading-db.mjs
```

Import from:

```txt
content/medium/source/*.html
MEDIUM_RSS_URL
```

### Phase 3 — Reading UI

Create:

```txt
app/reading/page.tsx
app/reading/[slug]/page.tsx
app/reading/layout.tsx
lib/reading-db.ts
```

### Phase 4 — Markdown Import

Create:

```txt
scripts/import-reading-md-to-db.mjs
content/reading-inbox/
```

### Phase 5 — AI Chunks

Create or extend:

```txt
document_chunks
```

Add:

```txt
token estimates
heading paths
optional embeddings
```

### Phase 6 — Admin UI

Create:

```txt
app/admin/reading/page.tsx
```

## Final Policy Summary

```txt
Medium imports default to published.
Markdown/PDF/manual imports default to draft.
Explicit status always wins.
/play Medium cards point to /reading/[slug].
Original Medium URLs stay in canonical_url.
Original files move to Storage in phase 2.
Images are hotlinked in phase 1, imported in phase 2.
Chunks are generated during import.
Embeddings are generated separately.
Global AI artifacts expose summaries and metadata first.
Full text is exposed through /reading/[slug].
```

## Non-Goals

This pipeline does not replace `/play`.

This pipeline does not remove `public/inventory.articles.catalog.json` immediately.

This pipeline does not require all documents to be public.

This pipeline does not require vector search in phase 1.

This pipeline does not require a full CMS on day one.

This pipeline does not require storing original source files in Supabase Storage during phase 1.