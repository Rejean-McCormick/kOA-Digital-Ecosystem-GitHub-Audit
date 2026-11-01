<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/GitHub-Read-Surfaces-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 03cc73e24280291f64c8e03b628707d21209c2939ad9fe9cbcda0c3443b2b7d3 -->

# GitHub AI/Read Surfaces & Collection Index — draft.3

Draft.3 adds **derived and verifiable reader navigation**, not a new semantic model. The three operational contracts are:

| Contract | Purpose |
| --- | --- |
| `kristal.github-read-surface/1.0` | exact Local Kit projection of files to publish as a GitHub reader surface |
| `kristal.github-sync-manifest/1.0` | Manager-owned hosted file inventory and integrity metadata |
| `kristal.github-collection-index/1.0` | derived navigation for large collections |

## Local-to-hosted file selection

```text
Local Kit 3.2.4+ (historical draft.3 workflow; 3.3.0 adds reader discovery)
  ├─ build-v9 (semantic state)
  ├─ build-ai (explicit derived AI capsule)
  └─ read-surface --require-ready
                  │ exact path/role/size/SHA-256 + surface digest
                  ▼
Kristal Manager alpha.11: Validate → Sync
                  ▼
collection repo
  kristals/index.json
  kristals/<slug>/
    AI_START_HERE.md
    AI_MANIFEST.json
    ai/INDEX.json
    canon/ | docs/ | sources/
    state/state-snapshot.json
    .kristal/sync-manifest.json
    ...exact files declared by Local Kit
```

The authoritative file set is emitted by the **Local Kit**, not guessed by Manager. The Manager synchronizes the declared subtree, preserves unmanaged files according to its ownership rules and maintains the collection index. A sync is mutable read-side transport, **not** a v10 immutable publication and not activation.

## Integrity & scale

- `AI_START_HERE.md` is the preferred reader entrypoint.
- The AI manifest/index tie the reader projection to an exact v9 State Snapshot.
- File sizes and SHA-256 digests, read-surface digest, state commitment and consistency of derived manifests/indexes are checked by the hosted collection ingest validator.
- Manager can prepare multiple Kristals in parallel, then perform a single shared repository transaction per collection batch.
- Collection ingest can validate changed Kristals in sharded jobs.
- Materialization manifests and references may be indexed without forcing large blobs into ordinary Git; transport may use Release assets, GHCR, LFS or another permitted locator.

```text
READ SURFACE != SEMANTIC STATE
COLLECTION INDEX != AUTHORITY
SYNC != PUBLICATION != ACTIVATION
```

See [[Workflow-GitHub-v10]], [[Toolchain-v10]], [[Publication-and-Discovery-v10]].

*Sources: Framework `spec/v10/GitHub-Reference-Profile.md` and `profiles/github/schemas/`; Authoring Kit `docs/18_PORTABLE_AI_CAPSULE.md` and `docs/20_TOOLCHAIN_INTEROP.md`; Manager `ARCHITECTURE.md`; Bootstrap `README.md`.*

## Distinguish local Reader Discovery

Local Kit 3.3.0 may include `kristal.discovery.json` and two `derived/reader-*.json` files in an explicit `read-surface`. These are *separate* from GitHub `read-surface`, `sync-manifest` and collection-index profiles. Public synchronization of local inventories is not automatically appropriate; classification metadata is not a publication or authority grant. See [[Reader-Discovery-and-Arketype-v10]].
