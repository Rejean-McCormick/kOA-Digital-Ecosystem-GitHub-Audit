<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Artifact-Federation-Manifest | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: bbf42b73cd54fc7edd1514d3547071722ef914351ab597bc17b38c779dcf1d42 -->

# Artifact: Federation Manifest

> **Legacy compatibility surface:** this page describes the historical v5-era Federation Manifest contract. Kristal v9 does not promote this historical schema to its semantic core. For the inherited v9 semantic-state architecture see [[Artifacts]], [[Exchange-and-Runtime-v9]], [[State-Snapshots-v9]] and [[Federation-and-Coverage-v9]]; for the v10 hosted network see [[Architecture-v10]].

A **Federation Manifest** defines deterministic composition across shards, authority channels, validation policies, reader policies, and disagreement-preserving rules.

Federation does not rewrite shards or erase disagreement. It preserves shard identity, source authority, validation status, certainty level, and scope.

---

## What it is for

Use a Federation Manifest when you need to:

- combine multiple shards into one federated Kristal view;
- preserve the authority channel behind each shard;
- expose different views through reader policies;
- keep conflicts visible rather than silently resolving them;
- update one shard without rebuilding every other shard;
- distribute a single composition entrypoint.

---

## What it contains conceptually

A Federation Manifest typically records:

- federation identity;
- shard references;
- shard scopes;
- authority channel references;
- validation report references;
- authority recognition references;
- reader policy references;
- validation policy references;
- composition policy;
- trust requirements;
- publisher signatures;
- optional conflict summaries.

---

## Conflict strategy

Kristal v5’s default federation strategy is:

```text
preserve_disagreement
```

This means a federation may contain multiple claims or positions about the same topic when their authority, certainty, validation status, or scope differs.

Reader policies decide which material is visible.

---

## Relationship to other artifacts

- **Shard Manifest**: referenced by the federation.
- **Authority Registry**: defines which authority channels are acceptable.
- **Validation Report**: records validation findings for shards or the federation.
- **Reader Policy**: selects which federated material is visible.

---

## Technical details

- Schema: `kristal-docs-v5/02-schemas/exchange-federation-manifest.schema.json`
- Example: `kristal-docs-v5/10-examples/exchange-federation-manifest.example.json`
- Overview: `kristal-docs-v5/00-overview/sharding-and-federation.md`
