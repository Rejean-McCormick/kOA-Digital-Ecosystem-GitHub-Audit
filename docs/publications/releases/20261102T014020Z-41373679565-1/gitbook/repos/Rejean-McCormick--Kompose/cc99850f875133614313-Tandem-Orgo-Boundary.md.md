<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Tandem-Orgo-Boundary | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: daa8e2c061fbefe0211fe42ffcb3a155d253fcbe96904c7767312733415b6008 -->

# Tandem — Orgo Operational Authority (ADR 0008)

**Adopted decision:** in real Tandem operations, **Orgo is the sole owner** of Cases, Tasks, Signals, workflow transitions, dispatch, operational authorization, and reconciliation. **KOMPOSE does not implement a parallel live orchestrator.** The older pure `lifecycle` and `coordination` functions remain valid for reference tests and fictional simulations only.

This is separate from **ADR 0006**: KOMPOSE can be independent of the optional KOR interface while still having **no authority to replace Orgo**.

| Component | Owns | KOMPOSE involvement |
|---|---|---|
| Kontexte | Mission, role, step, curriculum and fragment *references* | Read and validate synthetic sources; compile a plan without changes |
| KOMPOSE | Local rules, validation, preview and simulated receipt checks | No operational Case/Task/Signal state, no real pupil assignment |
| Orgo | Actual task state, transitions, dispatch, authorization and reconciliation | Future integration only, no network API here |
| Orgo_Worlds | Tenant/World/WorldRelease | Fixture UUID syntax checks do not verify tenancy or release |
| Ekole | Authorized teacher and learning projections | Strict synthetic preview shape check only |
| KOR | Optional narrative presentation | Non-operational example manifest only |

## No accidental authority transfer

- An `authority: orgo` value in a local JSON file is **not** a signed authorization token.
- `teacher_authorized: true` in `orgo_mock_fixture` receipts is a **test assertion**, not proof that a teacher approved an operation.
- A simulated `step_completed` or `done` cannot prove a learning competency was acquired.
- `verify-ekole-preview` reports `runtime_admitted: false`, `permissions_verified: false`, and `world_release_verified: false` even for structurally valid input.
- No real learner identities, confidential teacher constraints, content of hidden fragments, or live rights are accepted by the P1 preview contract.

## To connect a real Orgo environment

A separate authorized project must supply authenticated tenant/World boundaries, verified workflow and release versions, teacher review, transactional state, anti-replay/idempotence, delivery controls, negative authorization tests, and a rollback plan. **No automatic `apply` behavior is justified by this wiki or by the existing CLI.**

**Repository references:** `docs/adr/0008-tandem-orgo-operational-authority.md`, `docs/TANDEM_P1_ORGO_EKOLE_ALIGNMENT.md`, `docs/b6/ARCHITECTURE.md`, and `docs/CURRENT_IMPLEMENTATION_AND_BOUNDARIES.md`.

[[Home|← Home]] · [[Kontexte-B6-Preview|B6 preview]] · [[Ekole-P1-Preview|Ekole preview]]
