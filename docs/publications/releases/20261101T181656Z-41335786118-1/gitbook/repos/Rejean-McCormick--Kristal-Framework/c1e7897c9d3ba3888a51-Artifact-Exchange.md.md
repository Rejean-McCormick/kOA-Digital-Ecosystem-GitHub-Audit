<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Artifact-Exchange | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 9b7af2f7818e379daf23ff260446ddc2aed823f2e4499d81f854717f3415ed73 -->

# Artifact: Exchange

> **Legacy compatibility surface:** this page describes the historical v5-era Exchange contract. Kristal v9 does not promote this historical schema to its semantic core. For the inherited v9 semantic-state architecture see [[Artifacts]], [[Exchange-and-Runtime-v9]], [[State-Snapshots-v9]] and [[Federation-and-Coverage-v9]]; for the v10 hosted network see [[Architecture-v10]].

An **Exchange** is a compiled Kristal artifact.

It may be a **Working Exchange** or a **Reference Exchange**.

A Working Exchange is portable, immutable, content-addressed, and queryable, but it may contain unvalidated, disputed, low-certainty, fictional, mythological, speculative, or incomplete assertions when those statuses are explicit.

A Reference Exchange is recognized under one or more authority channels for declared scopes.

---

## What it is for

Use an Exchange when you need:

- a portable compiled artifact;
- stable content identity;
- reproducible build metadata;
- queryable assertion payloads;
- preserved provenance and evidence references;
- validation, certainty, authority, and scope labels;
- a source artifact for Runtime Packs.

---

## What it contains conceptually

An Exchange typically records:

- artifact identity and status;
- technical canonicalization and hashing metadata;
- source Structured Epistemic State or input references;
- build metadata;
- assertions or compiled payload references;
- validation report references;
- authority recognition references;
- reader policy references;
- lineage and provenance;
- signatures where applicable.

---

## Working vs Reference Exchange

### Working Exchange

Used for drafting, review, research, internal collaboration, partial validation, disputed positions, or material awaiting authority recognition.

### Reference Exchange

Used when an authority channel recognizes the artifact for a declared scope.

Reference status is scoped. It does not imply universal truth or universal agreement.

---

## Who produces and consumes it

**Produced by**

- compiler/build pipeline;
- ingestion workflows;
- federation or shard builders.

**Consumed by**

- validators;
- Runtime Pack builders;
- query services;
- renderers;
- Konnaxion distribution/activation flows;
- authority and governance workflows.

---

## Related pages

- [[Artifacts]]
- [[Artifact-Runtime-Pack]]
- [[Artifact-Validation-Report]]
- [[Trust-Authority-and-Signatures]]
- [[Workflow-Build-and-Validate]]

---

## Technical details

- Schema: `kristal-docs-v5/02-schemas/exchange-manifest.schema.json`
- Example: `kristal-docs-v5/10-examples/exchange.example.json`
- Core spec: `kristal-docs-v5/01-core-spec/kristal-v5-core-spec.md`
