<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Conformance-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 7aa7d548036d8444eb91589e355e29be1028695d2b1d43ab1ca21c66af6c4489 -->

# v9 Conformance

V9 conformance is capability-based.

## V9-State-Reader

Must:

- validate Logical Artifacts and State Snapshots;
- reproduce normative commitment vectors;
- reject false declared commitments;
- preserve semantic ID versus Logical Commitment distinction;
- preserve pinned reference/ownership boundaries.

## V9-Builder

Adds:

- Derivation validation;
- exact-input discipline;
- deterministic build claims;
- verified output commitments.

## V9-Materializer

Adds:

- Materialization Manifest validation;
- exact source commitment binding;
- reconstruction/losslessness checks;
- repack/resegmentation invariance.

## V9-Publisher

Adds:

- immutable publication;
- Build/Publish/Activate separation;
- atomic activation within the claimed transport/profile;
- crash-safe previous-state preservation;
- rollback by selecting retained snapshots.

## V9-Full

Combines all v9 profiles plus inherited v6/v7/v8 compatibility.

## Polymorphism gate

Conformance must not be demonstrated only with a large relation. Reference workloads cover relations, procedure DAGs, multiplex graphs, formal ASTs, epistemic corpora and federated state composition.

## Qualification boundary

A conformance PASS demonstrates contract behavior. It does not grant epistemic authority, deployment authorization, recognition or factual truth.
