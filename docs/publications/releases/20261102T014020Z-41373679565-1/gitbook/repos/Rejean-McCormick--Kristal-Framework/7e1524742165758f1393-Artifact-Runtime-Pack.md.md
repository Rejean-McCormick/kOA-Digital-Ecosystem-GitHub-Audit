<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Artifact-Runtime-Pack | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 0d11f39815ab56c6f7d46de1b4fd425b8702836dbd642ecd8d6e48b9a299bbd8 -->

# Artifact: Runtime Pack

> **Legacy compatibility surface:** this page describes the historical v5-era Runtime Pack contract. Kristal v9 does not promote this historical schema to its semantic core. For the inherited v9 semantic-state architecture see [[Artifacts]], [[Exchange-and-Runtime-v9]], [[State-Snapshots-v9]] and [[Federation-and-Coverage-v9]]; for the v10 hosted network see [[Architecture-v10]].

A **Runtime Pack** is an offline-capable runtime/query artifact derived from an Exchange or shard set.

It is optimized for activation and query performance while preserving the Kristal v5 labels needed for validation, certainty, authority, scope, provenance, and reader policy.

---

## What it is for

Use a Runtime Pack when you need to:

- activate a Kristal in a local or service runtime;
- serve queries efficiently;
- support offline operation;
- record runtime policies that affect reproducibility;
- preserve labels required by reader policies;
- support safe rollout, rollback, and compatibility checks.

---

## What it contains conceptually

A Runtime Pack typically includes:

- manifest identity;
- source Exchange or federation reference;
- source artifact status;
- data files;
- indexes and auxiliary structures;
- query contract reference;
- reader policy references;
- runtime policies;
- validation and authority labels;
- integrity and signature metadata.

---

## What it must preserve

Runtime Pack construction must preserve or faithfully index:

- artifact status;
- assertion status;
- validation status;
- certainty level;
- `validated_as`;
- authority channel;
- recognition status;
- scope;
- provenance references;
- evidence references;
- lineage.

A Runtime Pack must not flatten scoped validation into universal truth.

---

## Activation

Runtime activation is separate from artifact existence and validation.

A pack may exist and verify technically, but still be unavailable under a deployment’s reader policy, authority policy, environment, tenant, or rollback constraints.

---

## Related pages

- [[Artifact-Exchange]]
- [[Query-Basics]]
- [[Workflow-Activate-Rollback-Downgrade]]
- [[Operations-Release-Strategy]]

---

## Technical details

- Schema: `kristal-docs-v5/02-schemas/runtime-pack-manifest.schema.json`
- Example: `kristal-docs-v5/10-examples/runtime-pack-manifest.example.json`
- Runtime policies: `kristal-docs-v5/03-reproducibility/allowed-runtime-pack-policies.md`
