<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Workflow-Publish-and-Distribute | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: ab1d4528b52d9d7b6dbcb9fd7183597fba3377f9bc33f0c8d2a09f3be6f432de -->

# Workflow: Publish & Distribute

V9 publication creates immutable logical snapshots and distributes physical representations without confusing the two.

## Publish immutable state

A publisher should first verify:

- Logical Artifact commitments;
- pinned external references;
- required validations/recognition policy;
- materialization bindings;
- inherited compatibility surfaces.

Then create/publish a new immutable State Snapshot.

## Distribute Exchange separately

A portable Exchange may package the State Snapshot, Materialization Manifests and required blobs.

```text
EXCHANGE PACKAGE != LOGICAL STATE
```

Repacking or recompressing an Exchange must not silently create a new logical revision.

## Publish lexical/read artifacts independently

V8 lexical Kristals, indexes and AI bundles can continue to evolve on their own lifecycle when their source commitments are explicit.

## Required lineage for derived material

Include enough information to identify:

- source artifact/state commitment;
- build/materialization profile;
- completeness/coverage where partial;
- lexical stack if rendering was applied;
- integrity metadata.

## Do not flatten semantic distinctions

Distribution must not turn:

- `unknown` into false;
- `not_applicable` into zero;
- partial into complete;
- missing lexicalization into a guessed label;
- similarity into equivalence;
- validation into authority;
- model output into execution permission.
