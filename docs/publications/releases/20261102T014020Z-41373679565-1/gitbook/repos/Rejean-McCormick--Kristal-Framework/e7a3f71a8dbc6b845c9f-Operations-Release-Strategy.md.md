<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Operations-Release-Strategy | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 565465a8257a623a2d8c9a74c4dcbf6d6e9f1561d0ac3e57eeca6bc032f12155 -->

# Operations: Release Strategy

A v9 release strategy treats **logical state**, **physical materialization** and **activation** as separate release concerns.

## Release units may include

- v9 State Snapshot;
- Logical Artifact descriptors/content;
- Derivation records;
- Materialization Manifests and blobs;
- Exchange manifest/package;
- v6 portable projections;
- v7 registries/Mesh/KOS material;
- v8 lexical/query capability artifacts;
- validation/recognition/trust material;
- activation record/channel update.

## Recommended stages

1. validate inherited v6/v7/v8 contracts;
2. validate domain Logical Artifacts;
3. recompute Logical Commitments independently;
4. build and verify materializations;
5. construct/verify immutable State Snapshot;
6. publish snapshot and Exchange artifacts;
7. build/rebuild runtime indexes;
8. canary query/language/runtime behavior;
9. atomically activate the target State commitment;
10. monitor and retain rollback targets.

## Canary checks

Verify:

- inherited identity rules remain unchanged;
- Logical Commitments match recomputation;
- repack/recompression does not change logical identity;
- indexes bind to the correct source state;
- partial results are not treated as negatives;
- external child refs remain pinned;
- model output does not bypass authorization;
- rollback can reselect a retained snapshot without rewriting history.

## Release qualification

Use the Framework's native validators/TCK plus an independent examiner such as [[KristalDiag-v9]]. A disagreement must remain visible until explicitly resolved.
