<!-- Frozen source: https://github.com/Rejean-McCormick/HomePage-initkoa.org/blob/3b952d1da199b8ff827141022576775e8c8c9f34/docs/reading-db-upgrade/99-ai-drift-guardrails.md | commit: 3b952d1da199b8ff827141022576775e8c8c9f34 | SHA-256: 5390b704bee473c51673cc5d84ae7418070b6557edc16775c02046f3aa0bcf70 -->

---

docSet: "reading-db-upgrade"
docStatus: "draft"
project: "initkOA"
repo: "HomePage"
canonicalTermsVersion: "2026-05-25"
title: "99 — AI Drift Guardrails"
description: "Canonical guardrails that prevent AI-assisted branches from redefining the Reading DB upgrade architecture."
docPath: "docs/reading-db-upgrade/99-ai-drift-guardrails.md"
dependsOn: []
relatedDocs:

* "docs/reading-db-upgrade/00-overview.md"
* "docs/reading-db-upgrade/01-data-model.md"
* "docs/reading-db-upgrade/02-import-pipeline.md"
* "docs/reading-db-upgrade/03-nextjs-reading-ui.md"
* "docs/reading-db-upgrade/04-ai-accessibility.md"

---

# 99 — AI Drift Guardrails

## Purpose

This document prevents drift across parallel AI-assisted branches and conversations.

It defines the canonical decisions that must remain stable unless explicitly changed by a human maintainer.

The goal is to avoid situations where different AI branches redefine:

* routes;
* database ownership;
* source-of-truth rules;
* terminology;
* import behavior;
* AI accessibility policy;
* public footer exposure;
* `/play` versus `/reading` responsibilities.

This document is the guardrail layer for the `reading-db-upgrade` documentation set.

---

# Authority

This document is authoritative for consistency.

If another document conflicts with this one, use this document as the default source of truth until a human maintainer updates the decision explicitly.

Related docs may add implementation detail, but they should not redefine the decisions below.

---

# Canonical Project Model

```txt
/play    = resource catalog
/reading = full-text document library
```

The upgrade does not replace `/play`.

The upgrade adds `/reading` as a new DB-backed reading system.

---

# Canonical Source of Truth

```txt
Supabase Postgres = central source of truth for readable documents
```

The central DB owns:

```txt
documents
document_topics
document_versions
document_chunks
document_assets
import_runs
import_items
```

The DB, not Markdown files in the repo, is the canonical source for published Reading documents.

Markdown files may exist as:

* import sources;
* staging input;
* backups;
* authoring material;
* migration material;
* generated mirrors;
* test fixtures.

But after import, the DB-backed document record is the canonical runtime source.

---

# Canonical Routes

## Public routes

```txt
/reading
/reading/[slug]
/reading/topic/[topic]
/reading/source/[source]
```

`/reading/[slug]` is the canonical public full-text route for each readable document.

## Not canonical document routes

The following must not become canonical document routes:

```txt
/play/[slug]
/resources/[slug]
/documents/[slug]
/library/[slug]
/articles/[slug]
```

These may exist for other purposes, but not as the canonical Reading document route.

---

# `/play` versus `/reading`

`/play` remains the resource catalog.

It may include:

* tools;
* projects;
* initiatives;
* external resources;
* learning resources;
* documents as catalog entries.

`/reading` is the full-text document library.

It owns:

* readable page rendering;
* long-form document display;
* document metadata;
* topics;
* source links;
* canonical URLs;
* AI-readable reading indexes;
* document-level search and discovery.

Do not merge `/play` and `/reading`.

Do not move full-text Reading pages into `/play`.

Do not make `/play` the source of truth for Reading documents.

---

# Canonical Document Identity

Every readable document must have a stable internal identity.

Required identity fields:

```txt
id
slug
title
status
source
```

The `slug` is the public route identifier.

```txt
/reading/[slug]
```

The `id` is the database identifier.

The `canonical_url` is the original external source URL when applicable.

The `canonical_url` is not the same thing as the internal route.

---

# Canonical URL Semantics

Use:

```txt
canonical_url = original external source URL
```

Examples:

```txt
https://medium.com/...
https://example.org/original-paper
https://github.com/...
```

Use:

```txt
/reading/[slug] = internal initkOA reading page
```

Do not overwrite `canonical_url` with the initkOA route.

Do not treat `canonical_url` as the internal route.

Do not use `canonical_url` for internal routing.

---

# Canonical Visibility Model

Documents have a `status`.

Canonical statuses:

```txt
draft
published
archived
```

Only `published` documents are public by default.

AI indexes and public discovery artifacts must include only published documents unless a human maintainer explicitly creates a private/internal artifact.

Default visibility:

```txt
draft     = not public
published = public
archived  = not public by default
```

---

# Canonical Content Fields

The DB should preserve both Markdown and plain text.

```txt
body_markdown = canonical rendered source
body_text     = plain text for indexing, search, AI snippets, and summaries
```

`body_markdown` is used for page rendering.

`body_text` is used for discovery, indexing, summaries, and search.

Do not treat generated HTML as the canonical stored body.

Generated HTML is a rendering output.

---

# Canonical Rendering Rule

Reading document pages are server-rendered.

The route:

```txt
/reading/[slug]
```

must render the document body in HTML from stored Markdown or equivalent DB-backed content.

The page must not depend on client-side fetching for primary document content.

Client-side enhancements are allowed, but the main document content must be available in the server-rendered response.

---

# Canonical Topic Semantics

Topics are subject-matter labels.

Examples:

```txt
ai
governance
kristal
ethics
reading
markdown
```

Topics must not be used for:

* document status;
* source channel;
* import source;
* publication state;
* audience;
* access control.

Use explicit fields for those concepts.

---

# Canonical Source Semantics

`source` identifies the origin or import channel.

Examples:

```txt
markdown
medium
manual
pdf
external
```

`source` is not a topic.

Do not duplicate `source` values into `document_topics` unless the value is also genuinely a subject-matter topic.

---

# Canonical Import Model

The import pipeline may read from:

```txt
content/reading-inbox
content/medium/source
content/pdf-inbox
external APIs
manual scripts
```

But the result must be inserted or updated in Supabase Postgres.

The import pipeline should be idempotent when possible.

Repeated imports of the same source should not create accidental duplicate public documents.

---

# Canonical Markdown Import Behavior

Markdown imports should support frontmatter.

Recommended fields:

```yaml
title:
slug:
description:
source:
canonical_url:
author:
language:
topics:
status:
published_at:
```

The body after frontmatter becomes `body_markdown`.

A plain text version should be derived as `body_text`.

If `slug` is missing, the importer may derive it from the title or filename.

If `status` is missing, the importer should default to `draft` unless an explicit import policy says otherwise.

---

# Canonical Asset Model

Original files may be preserved in `document_assets`.

Examples:

```txt
original markdown file
original PDF
downloaded HTML
source metadata JSON
images
attachments
```

Assets are supporting material.

They do not replace the canonical `documents` row.

---

# Canonical Versioning Model

Substantial document changes should create entries in `document_versions`.

Version records may include:

```txt
document_id
version_number
body_markdown
body_text
change_summary
created_at
created_by
metadata
```

The current document state remains in `documents`.

Historical states belong in `document_versions`.

---

# Canonical Chunking Model

`document_chunks` is an internal retrieval/search layer.

It may be used for:

* search;
* AI retrieval;
* future embeddings;
* previews;
* passage-level citation;
* topic extraction;
* summarization.

It is not the canonical public full-text surface.

The public full-text surface remains:

```txt
/reading/[slug]
```

---

# Canonical Vector Search Position

Vector search is a future phase.

The first DB-backed Reading upgrade does not require vector search.

Do not redefine the current upgrade as an embeddings/vector project unless a human maintainer explicitly changes the roadmap.

Allowed now:

* schema preparing for embeddings;
* chunking;
* text search;
* metadata search;
* future-facing documentation.

Not required now:

* OpenAI embedding generation;
* pgvector setup;
* semantic search UI;
* vector ranking.

---

# Canonical AI Accessibility Model

The Reading system should support AI access through multiple layers.

The canonical layers are:

```txt
/reading/[slug]              = full-text public document page
/reading/ai-index.json       = machine-readable Reading document discovery index
/llms.txt                    = primary AI entrypoint for the site
/llms-full.txt               = auxiliary expanded AI context bundle
/ai-corpus.txt               = auxiliary corpus/discovery text
/md-manifest.json            = machine-readable Markdown mirror manifest
/md-sitemap.xml              = machine-readable Markdown mirror sitemap
/context-packs/index.json    = authoritative Context Pack catalog
/context-packs/sitemap.xml   = Context Pack crawler sitemap
/context-packs/*.txt         = specialized machine-readable reference bundles
/index.html.md and mirrors   = Markdown mirrors of public pages
```

These artifacts have different roles and must not be collapsed into a single conceptual object.

---

# Canonical AI Entrypoint Policy

`/llms.txt` is the primary AI entrypoint.

It should be:

* concise enough to inspect quickly;
* structured enough for agents to navigate;
* stable enough to bookmark;
* explicit about available auxiliary artifacts;
* the only AI artifact normally linked from the visible public footer.

`/llms.txt` may point to larger auxiliary artifacts.

It does not need to contain every full-text document inline.

---

# Canonical Auxiliary AI Artifact Policy

The site may generate auxiliary AI artifacts.

Canonical auxiliary artifacts include:

```txt
/llms-full.txt
/ai-corpus.txt
/md-manifest.json
/md-sitemap.xml
/ai-sitemap.json
/reading/ai-index.json
/context-packs/index.json
/context-packs/sitemap.xml
/context-packs/*.txt
```

These artifacts may remain public and fetchable.

They may be exposed in `<head>` discovery links.

They may be referenced from `/llms.txt`.

They should not all be displayed as separate visible footer links.

Auxiliary artifacts must not redefine the canonical source of truth.

The DB-backed Reading page remains the full-text source for public documents.

## Canonical Context Pack Delivery Policy

Context Packs are auxiliary machine artifacts specialized by repository/system. They remain behind `/llms.txt`; they do not become a second visible AI entrypoint.

Canonical delivery surfaces are:

```txt
/context-packs/index.json    = authoritative current-pack catalog
/context-packs/sitemap.xml   = crawler discovery surface
/context-packs/*.txt         = stable fetchable pack resources
```

Rules:

* `/llms.txt` should link the catalog and relevant packs.
* `index.json` is the source of truth for the current published set.
* `sitemap.xml` must be generated from that same published set.
* a previously published pack URL must not silently become a 404 after a rename; use a permanent redirect to the stable replacement;
* Context Pack machine responses must have explicit content type, CORS, indexing, and bounded cache behavior;
* missing or invalid catalog state must fail closed rather than trigger an implicit directory scan.

## Canonical Context Pack Corpus Policy

Context Pack corpus selection is governed by:

```txt
docs/context-packs/corpus-policy.md
tools/context_pack_policy.json
```

Context Packs must not redefine source authority or expose draft, proposal, backup, private, or historical material as current canonical material. Public packs must be reproducible from committed source material, record their policy version and corpus metrics, and pass the build validator before publication.

---

# Canonical Footer Exposure Policy

The public footer should not expose every machine artifact as a human navigation item.

The footer should expose a single clear AI entrypoint:

```txt
AI access -> /llms.txt
```

The following should not normally appear as separate visible footer links:

```txt
/llms-full.txt
/ai-corpus.txt
/md-manifest.json
/md-sitemap.xml
/ai-sitemap.json
/index.html.md
```

They may still exist, be fetchable, be listed in `/llms.txt`, or be discoverable through machine metadata.

This keeps the public interface clean while preserving machine access.

---

# Canonical SEO and Indexing Policy

`/llms.txt` may be indexable.

Auxiliary AI artifacts should usually be fetchable but not treated as primary search landing pages. Stable Context Pack text resources are the explicit exception: they may be indexed as technical discovery targets while `/llms.txt` remains the primary AI entrypoint.

Recommended behavior:

```txt
/llms.txt          = indexable AI entrypoint
/llms-full.txt     = noindex, fetchable
/ai-corpus.txt     = noindex, fetchable
/md-manifest.json  = noindex, fetchable
/ai-sitemap.json   = noindex, fetchable
/md-sitemap.xml    = sitemap/discovery artifact
/context-packs/index.json  = noindex, fetchable
/context-packs/sitemap.xml = sitemap/discovery artifact
/context-packs/*.txt       = indexable, fetchable, noarchive
```

The goal is not to hide auxiliary artifacts.

The goal is to prevent most generated machine bundles from becoming primary human landing pages while still allowing stable Context Packs to be directly discoverable. Context Pack text responses should use `X-Robots-Tag: index, follow, noarchive`.

---

# Canonical `llms-full.txt` Position

`/llms-full.txt` remains a valid auxiliary artifact.

It may contain:

* selected full page content;
* expanded page summaries;
* route metadata;
* Markdown mirror references;
* high-value context for offline agent use.

It should not replace `/llms.txt`.

It should not be the only AI artifact.

It should not become the public footer entrypoint.

If a future maintainer decides to remove `/llms-full.txt`, that decision must be reflected in this guardrail document and in `04-ai-accessibility.md` before changing the generator.

---

# Canonical `ai-corpus.txt` Position

`/ai-corpus.txt` is an auxiliary corpus artifact.

It may include:

* cleaned page text;
* selected summaries;
* discovery metadata;
* source route references;
* generated page blocks.

It should support retrieval and corpus ingestion.

It should not be treated as the canonical public full-text source for Reading documents.

---

# Canonical Markdown Mirror Policy

Markdown mirrors are generated artifacts.

They exist to make public site pages easier to inspect, quote, diff, index, and ingest.

Markdown mirrors are not the source of truth for DB-backed Reading documents.

They are public derived outputs.

The source for Reading documents remains Supabase Postgres.

The source for normal site pages remains the app source files.

---

# Canonical Public Artifact Relationship

The relationship between user-facing pages and machine-facing artifacts is:

```txt
Human primary:
  /reading/[slug]
  normal app routes

Machine primary:
  /llms.txt
  /reading/ai-index.json

Machine auxiliary:
  /llms-full.txt
  /ai-corpus.txt
  /md-manifest.json
  /md-sitemap.xml
  /ai-sitemap.json
  Markdown mirrors
```

Do not invert this relationship.

Do not make generated machine artifacts the canonical human surface.

Do not make footer navigation mirror every machine artifact.

---

# Canonical AI Artifact Generation Rule

The build may generate AI artifacts before `next build`.

The expected build order is:

```txt
npm run reading:ai-index
node scripts/generate-ai-assets.mjs
next build
```

`reading:ai-index` must fail visibly if required Supabase configuration is missing or invalid.

Do not bypass `reading:ai-index` silently in production builds.

If the Reading AI index cannot be generated, the build should fail unless a human maintainer explicitly changes the policy.

---

# Canonical Error Handling Rule

Do not hide source-of-truth errors.

Examples of errors that should remain visible:

```txt
missing NEXT_PUBLIC_SUPABASE_URL
missing SUPABASE_SERVICE_ROLE_KEY
Supabase project paused
invalid Supabase project URL
failed published document query
schema mismatch
```

Temporary local diagnostics may be used, but they should not become permanent bypasses.

---

# Canonical AI Drift Rule

An AI assistant must not:

* move the Reading source of truth back to Markdown files;
* replace `/reading/[slug]` with another canonical route;
* merge `/play` and `/reading`;
* make draft documents public by default;
* treat `canonical_url` as the internal route;
* use topics for status/source/access control;
* redefine vector search as required for the current phase;
* delete auxiliary AI artifacts without updating the guardrails;
* expose every machine artifact as public footer navigation;
* silently bypass failed Reading index generation.

If a change requires redefining one of these decisions, the assistant must identify it as a governance decision and update this guardrail document together with the implementation.

---

# Allowed Changes

The following changes are allowed without changing the architecture:

* improving UI layout;
* improving Reading typography;
* improving metadata display;
* adding filters;
* adding pagination;
* improving slug generation;
* improving Markdown rendering;
* adding source links;
* adding topic pages;
* adding source pages;
* improving `llms.txt` readability;
* improving `llms-full.txt` structure;
* improving `ai-corpus.txt` structure;
* improving the footer to show only the primary AI entrypoint;
* adding tests;
* adding migrations;
* adding import validation;
* adding admin-only tooling.

---

# Changes Requiring Explicit Maintainer Decision

The following changes require explicit maintainer decision:

* removing `/llms-full.txt`;
* removing `/ai-corpus.txt`;
* removing Markdown mirrors;
* removing `/reading/ai-index.json`;
* replacing Supabase Postgres as source of truth;
* making Markdown files the runtime source of truth again;
* renaming `/reading`;
* merging `/reading` into `/play`;
* changing public visibility defaults;
* making embeddings required for the current phase;
* changing `canonical_url` semantics;
* making generated machine bundles the public full-text source;
* exposing all machine artifacts as primary footer navigation;
* adding private/draft documents to public AI artifacts.

---

# Canonical Terminology

Use these terms consistently:

```txt
/play = resource catalog
/reading = full-text document library
/reading/[slug] = canonical internal public document route
canonical_url = original external source URL
internal_path = initkOA reading route
body_markdown + body_text = stored in Postgres
original files = document_assets
topics = subject matter only, snake_case
source = origin/import channel
published documents = public
draft/archived documents = not public by default
document body = server-rendered
AI entrypoint = /llms.txt
AI artifacts = discovery/context/metadata layers
auxiliary AI artifacts = llms-full, ai-corpus, manifests, sitemaps, mirrors, context packs
Context Pack catalog = /context-packs/index.json
Context Pack sitemap = /context-packs/sitemap.xml
Context Pack corpus policy = docs/context-packs/corpus-policy.md + tools/context_pack_policy.json
full text = /reading/[slug]
document_chunks = internal AI/search retrieval layer
vector search = future phase
```

---

# Acceptance Criteria

The documentation set is aligned when:

```txt
all docs use /reading/[slug] as the canonical document route
all docs distinguish /play from /reading
all docs treat Supabase Postgres as the document source of truth
all docs preserve canonical_url as the original external source
all docs use topics for subject matter only
all docs keep full text in DB-rendered reading pages
all docs treat /llms.txt as the primary AI entrypoint
all docs allow auxiliary AI artifacts without making them primary footer links
all docs treat AI artifacts as discovery/context/metadata layers
all docs keep vector search as a future phase
```
