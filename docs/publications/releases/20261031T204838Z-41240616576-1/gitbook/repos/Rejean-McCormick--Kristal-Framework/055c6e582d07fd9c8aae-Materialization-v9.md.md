<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Materialization-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 0b6d3e06d58a5fa5844986ee82c3e8d7b3d167b3ce55afc7da55dc8a73fe3f3a -->

# Materialization

A **Materialization** is a physical representation of a Logical Artifact.

```text
Logical Artifact
      ↓
Materialization Profile
      ↓
Physical Representation
```

## Explicit profiles

Reference profiles include concepts such as:

```text
kristal.materialization/inline-json/1
kristal.materialization/native-blob/1
kristal.materialization/segmented-jsonl/1
kristal.materialization/kristal-state-v6/1
```

Advanced columnar/runtime profiles may evolve independently from the core.

## Factorization

Repeated logical metadata may be stored once and applied to many records if reconstructability is preserved.

```text
DEFAULTED METADATA != LOST METADATA
```

## Dictionaries

A physical representation may replace repeated semantic IDs with local ordinals.

```text
LOCAL ORDINAL != SEMANTIC IDENTITY
```

Ordinals may change during repack and must never become external stable IDs.

## Segments

A **Segment** is an immutable physical unit. Segment boundaries are not semantic boundaries by default.

```text
SHARD != SEGMENT
```

## Partitioning

Physical partition strategies are hidden implementation/materialization choices. A logical query must not depend on whether an artifact uses 16, 256 or 1024 physical buckets.

## Planner boundary

The Standard defines valid profiles, not a mandatory optimizer. Tooling may recommend a profile, but the chosen profile must be explicit and reproducible.
