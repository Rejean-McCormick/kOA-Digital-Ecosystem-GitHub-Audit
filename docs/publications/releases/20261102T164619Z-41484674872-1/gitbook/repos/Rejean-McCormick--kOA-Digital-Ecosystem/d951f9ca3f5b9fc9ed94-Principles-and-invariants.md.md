<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/1-Overview/Principles-and-invariants.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: d434c8b0d0c429d9a4d0a77adebd33c5a3f4f155b2dac33b192d83ec9df8b068 -->

# Principles and invariants

1. **Unique authoritative owner.** Every authoritative state has one declared logical owner.
2. **No direct cross-system writes.** Integrations use explicit versioned contracts and owner APIs.
3. **Presentation is not authority.** Koali rendering, routing or Space activation does not transfer business, epistemic or host authority.
4. **Integrity is not authority.** Valid bytes/signatures do not imply validation, recognition or activation eligibility.
5. **Workflow state is not epistemic state.** Orgo statuses do not replace Kristal assertion/validation/recognition states.
6. **Artifact status is not validation.** Kristal v6 keeps `artifact_status`, validation and authority recognition separate; derived projections do not upgrade the source state.
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
18. **Runtime query stores are materializations.** Any Runtime Pack table/index/columnar/read-only database representation is derived, non-authoritative and deterministically rebuildable from the referenced Kristal artifact and declared build inputs.
19. **No bidirectional authority synchronization.** Product state may produce knowledge and consume ArtifactRefs/projections, but the product database, Kristal Exchange and Runtime Pack do not form peer writable sources of truth.

10. **Actionability is not execution authority.** Kristal v6 may classify an action as automatic or human-gated, but cross-system mutation still requires the receiving owner's explicit contract, admission and authority.
