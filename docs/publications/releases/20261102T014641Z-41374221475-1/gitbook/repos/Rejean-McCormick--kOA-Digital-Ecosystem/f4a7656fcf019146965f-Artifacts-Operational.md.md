<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Artifacts-Operational.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 50d95b6d935c50d45e29e287be87cf0eadaa87b3f145889065f87f3ce6738f67 -->

# Operational integration artifacts

Operational state is mutable, transactional state owned by the product/component responsible for the domain. It remains outside Kristal even when knowledge is derived from it.

Examples include Orgo Signal/WorkflowVersion/Case/Task/IntegrationOperation state, Konnaxion consultations/participants/votes/DecisionRecords, product identity/session state, outbox/retry/idempotency state and local activation/job state.

Cross-system flows use owner APIs, versioned contracts, immutable exports/snapshots and ArtifactRefs. They do not implement a bidirectional database synchronization model and do not dual-write the same authoritative domain record into Kristal.

## Build Record

A Build Record may remain as **ecosystem correlation/reproducibility evidence**. It must not replace Kristal artifacts, kOA-Linux Release Sets, component active-state records or lifecycle receipts.

It should keep independent statuses for compilation, validation, recognition, publication and activation and reference the owning artifacts rather than re-declaring them.

## Source-owned export/snapshot

An operational owner may publish an immutable export/snapshot for knowledge compilation or cross-system processing. The export remains evidence of source state at a declared revision/digest; it does not transfer ownership of the live source record.

Da’at may transform such an export into Kristal State or another explicitly supported Kristal-native input. The resulting Kristal artifact is a new knowledge artifact with provenance back to the source export, not a replacement operational record.

## kOA-Linux Release Set

Release Set is the platform release compatibility artifact. It binds versions across independent release channels and carries compatibility/activation metadata under the kOA-Linux contract.

Release compatibility is represented by the kOA-Linux Release Set and owner receipts; Digital Ecosystem defines no parallel release authority.

## Runtime Pack local state

For kOA-Linux deployments, `kristal_runtime` owns:

- Runtime Pack verification/compatibility record;
- active Runtime Pack record;
- activation receipt;
- rollback receipt;
- runtime health state.

kOA Node Agent may execute the narrow privileged host transition required by the profile. A receipt does not replace the owner component's active-state record.

## Koali Space state

Koali Space activation/rollback/deactivation belongs to Koali Spaces and is unrelated to Kristal Runtime Pack active state.
