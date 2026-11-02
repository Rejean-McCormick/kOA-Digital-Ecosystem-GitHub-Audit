<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Version-Stack-v6-v7-v8-v9-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: b452ad233f48a6b59883122dec979a98d0852a3e5f73f93dc1b498dfc3113352 -->

# Version Stack: v6 → v7 → v8 → v9 → v10

Kristal evolves through **compatible layers of responsibility**, not a succession of incompatible file formats.

| Layer | Responsibility | Invariant / anchor |
| --- | --- | --- |
| v6 | Portable epistemic state (`kristal_state/6.0`) | evidence, valuations, provenance and certainty |
| v7 | Semantic identity (KQ/KP/KA/KS), registries, Kristall | semantic identity is not content identity |
| v8 | Language, query and AI read models | `READ MODEL != CANONICAL STATE` |
| v9 | Polymorphic logical state, snapshots, commitments and materializations | `LOGICAL STATE != PHYSICAL MATERIALIZATION` |
| v10 | Hosted nodes, bindings, publication and discovery | `HOST LOCATION != SEMANTIC IDENTITY` |

## Dependency direction

```text
v10 hosting/publication/discovery
                │ refers to
                ▼
v9 exact logical state + commitments
                │ inherits
                ▼
v6/v7/v8 semantic/query compatibility surfaces
```

- V10 does not invalidate a v9 State Snapshot.
- Moving a repository, creating a mirror or changing a read index is not a logical revision by itself.
- V10 directories help **find** nodes; v9 pinned references define exact **federation membership**.
- Host attestation and conformance evidence do not grant semantic authority.

For detail: [[Version-Stack-v6-v7-v8-v9]] (historical), [[Compatibility-v9-v10]], [[Architecture-v10]].
