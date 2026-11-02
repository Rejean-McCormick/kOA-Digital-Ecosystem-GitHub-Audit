<!-- Frozen source: https://github.com/Rejean-McCormick/HomePage-initkoa.org/blob/3b952d1da199b8ff827141022576775e8c8c9f34/README.txt | commit: 3b952d1da199b8ff827141022576775e8c8c9f34 | SHA-256: 6ef6ba061721903d81c2a2059545458839a0df7281aba6f17690be31010ee643 -->

INITKOA Context Pack pipeline

Primary AI entrypoint:
- /llms.txt

Context Pack source of truth:
- tools/context_pack_policy.json        corpus selection/classification policy
- public/context-packs/index.json       generated authoritative catalog
- public/context-packs/sitemap.xml      generated crawler discovery surface

Builder:
- tools/context_pack_builder.pyw

Corpus policy documentation:
- docs/context-packs/corpus-policy.md

Build guard:
- scripts/validate-context-packs.mjs
- npm run context-packs:validate

Public build behavior:
- default repositories: committed Markdown only
- curated repositories: committed files selected by policy globs
- clean selected source state required
- policy exclusions/classification applied before packaging
- exact duplicate source content removed by SHA-256
- corpus metrics and policyVersion written into each pack and index.json
- index.json and sitemap.xml generated from the published pack set
- /llms.txt discovers Context Packs from index.json only
- historical public Context Pack URLs redirect permanently to stable URLs
- kOA-Linux uses its native AI layer instead of concatenating the full Markdown corpus:
  docs/AI_CONTEXT.md + ai-navigation contract + declared canonical source contracts + generated AI contexts/indexes
- two legacy general packs are explicitly exempt from builder-format checks until migrated

Generated outputs (never edit manually):
- public/context-packs/*.txt
- public/context-packs/index.json
- public/context-packs/sitemap.xml
- public/llms.txt

Workflow:
1. Update tools/context_pack_policy.json when corpus rules change.
2. Ensure Markdown working trees are clean.
3. Run the builder's Build All (or Build All + Sync).
4. Run npm run context-packs:validate.
5. Commit/push the site code changes and generated Context Pack outputs.
6. Vercel runs the validator before generating AI assets and building Next.js.
