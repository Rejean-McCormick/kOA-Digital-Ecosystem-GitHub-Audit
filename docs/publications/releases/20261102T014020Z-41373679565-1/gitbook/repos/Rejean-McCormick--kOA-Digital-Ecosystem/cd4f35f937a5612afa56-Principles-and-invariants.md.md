<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Principles-and-invariants | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: b55b3a611623fd672b081b83e44e0afeca71cb1de50a363114b1a1b773c4623e -->

# Principles and invariants

1. **Unique authoritative owner.** Every authoritative state has one declared logical owner.
2. **No direct cross-system writes.** Integrations use explicit versioned contracts and owner APIs.
3. **Presentation is not authority.** Koali rendering, routing or Space activation does not transfer business, epistemic or host authority.
4. **Integrity is not authority.** Valid bytes/signatures do not imply validation, recognition or activation eligibility.
5. **Workflow state is not epistemic state.** Orgo statuses do not replace Kristal assertion/validation/recognition states.
6. **Compilation is not validation.** Kristal v5 may compile Working Exchanges before final validation/recognition where policy permits.
7. **Recognition is scoped.** Reference status is authority/scope-specific, not universal truth.
8. **Reader Policy does not rewrite underlying state.** Visibility preserves labels and lineage.
9. **Runtime Pack state has a precise owner.** On kOA-Linux, `kristal_runtime` owns verification/compatibility/active Runtime Pack state and activation/rollback receipts; Node Agent performs only the narrow privileged host transition when required.
10. **Release Set is not activation state.** It binds compatible release-channel versions; it does not replace component active-state records.
11. **Space activation is not Runtime Pack activation.** Koali Space lifecycle is presentation/application composition.
12. **`accepted != succeeded`.** Durable asynchronous operations require terminal reconciliation.
13. **Idempotency survives retry/redrive.** Same logical key with different semantic content is a conflict.
14. **IK adoption is explicit.** Interaction Kernel is the target cross-system Profile layer, but it does not silently replace kOA-Linux internal/component contracts.
15. **No forced Kristal hop.** Konnaxion↔Orgo remains direct unless an adopted Profile explicitly requires Kristal.
16. **Operational databases remain product-owned.** Kristal is not a shared transactional store and no integration creates a second writable authority for an Orgo/Konnaxion record.
17. **Operational-to-Kristal flow is snapshot/export based.** Knowledge compilation consumes immutable source-owned exports/references with provenance; it does not rely on cross-system database writes or distributed commits.
18. **Runtime query stores are materializations.** Any Runtime Pack table/index/columnar/read-only database representation is derived, non-authoritative and rebuildable from the referenced Kristal artifact and declared inputs.
19. **No bidirectional authority synchronization.** Product state may produce knowledge and consume ArtifactRefs/projections, but the product database, Kristal artifact and runtime projection do not form peer writable sources of truth.
20. **Consumer lens is not ontology.** A people-first, process-first, place-first or other primary view is owned by the consumer projection, not imposed by kOA.
21. **Derived indexes are not a second canon.** Glossaries, chronologies and media views may link referents/assertions but remain rebuildable consumer structures.
