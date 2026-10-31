<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Exchange-and-Runtime-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: aa054b62109410e6f6274962c04f9786c6cfca76b56258000dfc713599f3dafd -->

# Exchange and Runtime

## Exchange

A v9 Exchange package transports enough information to reconstruct or consume a State Snapshot and selected materializations.

It may contain:

- State Snapshot;
- Artifact descriptors;
- Materialization Manifests;
- physical blobs;
- optional Derivation records;
- optional signatures/attestations.

```text
EXCHANGE PACKAGE != LOGICAL STATE
```

Different Exchange packages may represent the same Logical State.

## Repack invariance

Changing:

- segment boundaries;
- compression;
- blob location;
- local dictionary assignment;
- packaging layout;

must not alter a Logical Commitment if reconstructed logical content is unchanged.

## Runtime Pack

A Runtime Pack is a derived representation optimized for access or computation. It may use SQLite, Arrow, Parquet, graph indexes, search indexes, vectors or custom structures.

```text
RUNTIME PACK != CANONICAL STATE
```

A Runtime Pack should bind to the source State/Artifact commitment so consumers can detect staleness.

## Index rebuild

```text
DELETE INDEX + REBUILD = SAME LOGICAL STATE
```

If deleting an index destroys unique canonical knowledge, the supposed index was actually carrying canon and the authority model must be corrected.
