<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/GitHub-Publishing | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 17987ef6402b4a77186393cf11b9087f67da598b0f9e6eb0feb90e65ea7344e3 -->

# GitHub Publishing

## Principle

**Compile locally. Publish approved static artifacts. Never compile or activate Kristal in GitHub Actions.**

## CI preview

The `quality.yml` workflow validates the project and uploads a **private workflow artifact** for preview. It is not a public website and never publishes GitHub Pages.

## Controlled public deployment

1. Obtain actual scientific, linguistic and disclosure approvals and upstream Kristal release authorization.
2. Create a `production_candidate` build locally using qualified real inputs and `--state-snapshot`. This is a technical preflight only, not a grant of approval.
3. Review and verify `published-site/` and force-add **only these approved derived assets** to an authorized commit.
4. In GitHub repository settings, configure Pages to use Actions and create protected environment `public-pages` with required reviewers. Add environment secret `KRISTAL_PUBLICATION_GATE=authorized` only for approved releases.
5. Run `Deploy locally compiled qualified publication` manually from the approved `main` revision.

The workflow checks the manifest and environment secret before uploading; the deployment job needs `pages: write` and `id-token: write`. A push alone does **not** deploy.

## Public Kristal Wiki composition (optional overlay)

The optional `build-wiki` command creates **private Markdown drafts**. A collection aggregation in `kristal-public/tools/wiki_spek_collection.py` can assemble approved inputs by indexed Kristal slug, but neither operation authenticates C1/C2 signatures or pushes a Wiki. The upstream Manager must coordinate actual publication gates.

See [[Kristal Wiki Architecture]], [[Wiki Draft Workflow]] and [[Publishing the Wiki]].

## The separate GitHub wiki

Main code and wiki are different Git repositories. See [[Publishing the Wiki]] for first-page initialization and controlled sync.

**Security:** make sure public output does not contain canonical private blobs, credentials, or sensitive provenance. The compiler cannot decide whether information may be disclosed.
