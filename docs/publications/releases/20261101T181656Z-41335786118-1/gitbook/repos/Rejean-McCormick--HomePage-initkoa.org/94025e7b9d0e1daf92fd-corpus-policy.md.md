<!-- Frozen source: https://github.com/Rejean-McCormick/HomePage-initkoa.org/blob/3b952d1da199b8ff827141022576775e8c8c9f34/docs/context-packs/corpus-policy.md | commit: 3b952d1da199b8ff827141022576775e8c8c9f34 | SHA-256: b27288e19a2b2c9ebf291517e68657f288f672471de3abf131bfa2732bad2aaf -->

# Context Pack Corpus Policy

## Purpose

Context Packs are public, machine-readable reference bundles. This policy defines which Markdown files may enter a public pack and how the builder must record corpus quality.

The authoritative executable policy is:

```txt
tools/context_pack_policy.json
```

This document explains that policy. The JSON file controls the builder and validator.

## Public corpus contract

A public Context Pack must be reproducible from committed source material and must not silently mix current canonical material with backups, drafts, proposals, diagnostics, or historical snapshots.

Default rules:

```txt
default selection       = committed Markdown only
curated selection       = committed files matching repository policy globs
working source state    = clean before public build
exact duplicates        = removed by SHA-256 of normalized file content
canonical               = included
reference               = included unless a repository rule marks it on-demand
proposal                = excluded from the public pack by default
historical              = excluded from the public pack by default
plain non-Git wiki      = ignored for public builds
```

Repositories that already publish a dedicated AI navigation/context layer SHOULD use `selectionMode: curated` instead of recompiling their complete Markdown corpus. Curated mode remains policy-driven and fail-closed: required patterns must resolve to committed files, and selected tracked files must be clean.

## Authority classes

`canonical`
: Current normative or primary documentation for the repository.

`reference`
: Supporting material that is useful for interpretation but is not itself the primary normative description.

`proposal`
: Planned, TODO, migration, design-option, or future-state material. It must not be presented as current behavior.

`historical`
: Archives, backups, deployment snapshots, replaced versions, diagnostics, and other material retained for history rather than current authority.

Repository rules may classify a path and independently decide whether that path is included in the public pack.

## Selection order

For each repository, the builder must:

1. resolve the repository selection mode from `tools/context_pack_policy.json`;
2. in `markdown` mode, refuse a public build when Markdown state is dirty and enumerate committed Markdown only;
3. in `curated` mode, resolve `includePatterns`, verify every `requiredPatterns` entry has at least one committed match, and refuse the build when a selected tracked source differs from `HEAD`;
4. include a Git-backed wiki only when the repository policy allows it;
5. apply global exclusion rules and repository-specific authority/include rules;
6. order curated sources using `readFirst` before deterministic path ordering;
7. normalize text to UTF-8/LF;
8. remove exact duplicate content using SHA-256, keeping the first deterministic source;
9. build the pack from the remaining files;
10. record corpus metrics, selection mode, selected-source cleanliness, and policy version in the pack header and manifest.

`working_tree_markdown` remains in the pack header for compatibility with the site validator. Curated packs additionally emit `working_tree_selected`; for curated mode both fields represent cleanliness of the selected committed source set rather than the whole Markdown tree.

Untracked files are never included in a public Context Pack because the source enumeration is Git-committed-only. Dirty selected source state is an error because the local bytes and the committed source identity would otherwise diverge.

## Wikis

A GitHub wiki may be folded into its repository Context Pack under the stable `wiki/` prefix when the local wiki directory is a Git repository.

A plain local wiki directory has no commit identity and therefore is not included in a public build. It may be used by other local tooling, but it is not a public Context Pack source.


## AI-native curated repositories

A repository that already owns a generated AI context/navigation layer should expose that layer directly rather than forcing the public Context Pack builder to concatenate the entire documentation tree.

The current kOA-Linux policy uses:

```txt
selectionMode = curated
includeWiki   = false

read first:
  docs/AI_CONTEXT.md
  docs/contracts/ai-navigation.contract.json
  docs/generated/ai-context/koa-navigation.json
  docs/generated/ai-context/*.json

canonical source-contract globs declared by ai-navigation:
  docs/contracts/*.contract.json
  docs/contracts/components/*.component.json
  docs/contracts/subsystems/*.subsystem.json
  docs/contracts/profiles/*.profile.json
  docs/contracts/integrations/*.integration.json
  docs/contracts/toolchains/*.toolchain.json

structured discovery/context:
  docs/generated/authority-manifest.json
  docs/generated/document-index.json
  docs/generated/component-catalog.json
  docs/generated/subsystem-catalog.json
  docs/generated/profile-catalog.json
  docs/generated/requirements-index.json
  docs/generated/assertion-index.json
  docs/generated/traceability.json
```

This preserves kOA-Linux's own contract-first AI architecture. `AI_CONTEXT.md` is the visible read-first entrypoint, `ai-navigation.contract.json` owns navigation rules, its declared source-contract globs provide the canonical structured authority needed for follow-up work, generated AI context files provide scoped packages, and generated indexes are discovery projections rather than independent authority. The initkoa Context Pack is therefore a transport wrapper around the repository's AI-native layer, not a second full documentation compilation.

Curated generated files should normally be classified as `reference`; source contracts can remain `canonical`. The policy must not relabel generated indexes as canonical authority.

## Exact deduplication

Deduplication is content-based, not filename-based.

The builder hashes each normalized Markdown file. When two files have identical content, only the first file in deterministic path order is included. The duplicate count is recorded.

Deduplication does not attempt semantic similarity. Near-duplicates require an explicit policy or source-repository cleanup.

## Required metrics

Every generated Context Pack and `public/context-packs/index.json` must expose enough information to audit the corpus:

```txt
policyVersion
sourceFileCount
includedFileCount
excludedFileCount
duplicateFileCount
contentBytes
authorityCounts
```

The manifest also records the final pack SHA-256.

## Size policy

The executable policy defines:

```txt
warningBytes
maxBytes
```

Crossing `warningBytes` produces a builder/validator warning. Crossing `maxBytes` is a validation failure and blocks publication.

Size limits are safety bounds, not a substitute for corpus curation.

## Repository-specific rules

Repository-specific rules belong in `tools/context_pack_policy.json`, not in ad-hoc Python branches.

Examples currently covered include:

```txt
Konnaxion      .kx_deploy_backups/**                         -> historical, excluded
kOA-Linux      AI-native curated selection                  -> AI_CONTEXT + generated AI/index layer
Kristal Farms  archive/**                                    -> historical, excluded
Orgo           Architecture upgrade(to do)/**                -> proposal, excluded
UCKK Moodle    string_inventory/**                           -> reference/on-demand, excluded
```

The policy file should be updated when a repository introduces a new stable archival, generated, backup, proposal, or on-demand path convention.

## Legacy general packs

Two currently published general-purpose packs are produced by older external pipelines rather than `context_pack_builder.pyw`:

```txt
grammatical-framework-context-pack--rgl-router-and-reference--v1.0.txt
senior-architect-context-pack--systems-patterns-and-resilience--v1.0.txt
```

They are listed explicitly in `legacyExemptFiles` in the executable policy. The site validator still verifies their presence, manifest SHA-256, sitemap membership, and size bound, but does not require builder-specific corpus headers or FILE-section format from them.

This exemption must remain explicit and narrow. Any new general pack should use the current corpus contract, and these two should be migrated if their source pipelines are brought under the Context Pack builder.

## Generated files

These are generated outputs and must not be manually edited:

```txt
public/context-packs/*.txt
public/context-packs/index.json
public/context-packs/sitemap.xml
```

The builder owns them. The validator verifies them before the site build.

## Publication invariant

A Context Pack may be published only when:

```txt
policy is present and valid
source Markdown state is declared clean
pack policyVersion matches the active policy
manifest and files agree
sitemap and manifest agree
no forbidden path is included
no exact duplicate remains
pack size is within the configured maximum
```

If these conditions cannot be verified, publication must fail closed.
