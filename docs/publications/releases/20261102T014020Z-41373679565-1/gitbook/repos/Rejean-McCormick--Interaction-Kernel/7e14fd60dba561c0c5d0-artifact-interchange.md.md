<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/artifact-interchange.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: f946f7d58c640a19692f4b3c27d25d8aaccffe06c0b3c22464ef886fd7f912ea -->

# Artifact Interchange

`ArtifactRef` references an owner-defined artifact identity, optional SHA-256 integrity digest, opaque locator and contract metadata. It never transfers ownership, authority or validation status.

`ExportManifest` is source-owned and pins snapshots/revisions/digests for reproducible external consumption. It represents a boundary snapshot of source-owned state; it is not a shared mutable database contract.

## Operational-state boundary

Operational records remain authoritative in their owning system. When those records contribute to an external artifact, the owner exports an immutable snapshot or revision and exposes it through `ExportManifest` and/or `ArtifactRef`.

Consumers MUST treat the exported representation as a versioned artifact input, not as permission to mutate the owner's underlying database.

IK is not an artifact store. Artifact bytes remain in owner-defined storage and are located through opaque locators or other owner-defined retrieval mechanisms.

## Derived materializations

An artifact may have query-oriented or deployment-oriented materializations such as tables, indexes, Parquet files, SQLite databases, search indexes or Runtime Packs. These are not authoritative operational state unless a separate owning contract explicitly says otherwise. Their presence does not change the authority semantics of `ArtifactRef`.

Locators must not embed credentials.

See [ADR-IK-05](adrs/ADR-IK-05-operational-state-artifact-boundary.md).
