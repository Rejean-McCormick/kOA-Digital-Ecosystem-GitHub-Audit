<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/10-system/authority-map.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 33a117faaa4d213fcb7a9170cd76d8f2f3b97a66f6854fa6e1842ebe94a30b6d -->

# Ecosystem authority map

**Status:** current ecosystem-level reference map

This page answers one question: **where does authoritative state live?** It is an index, not a competing source of truth.

## Authority map

| State / decision | Authoritative owner | Allowed ecosystem role of others | Explicit non-authority |
|---|---|---|---|
| Civic/public domain state, participation, deliberation, finalized `DecisionRecord` | **Konnaxion** | Consumers may receive authenticated projections/events | Orgo, Kristal, Koali and IK do not become civic-state owners |
| Workflow, Signal, WorkflowVersion, Case, Task, IntegrationOperation, outbox/reconciliation | **Orgo** | Other systems may trigger work or consume durable results | Konnaxion/Koali do not write Orgo work tables |
| Source discovery, provider resolution, lossless acquisition evidence and immutable harvest handoff | **EncyKlopedia** | Da’at/Kristal consume pinned exports/evidence | Acquisition does not validate epistemic truth or own Moodle projections |
| Ecosystem/IK-facing mapping into Kristal-native contracts | **Da’at** | Maps/adapts payloads under ACL while preserving provenance | Da’at owns neither source state nor Kristal authority semantics |
| Referent Registry semantics, Kristal State, typed valuations/coordinates/applicability, validation/recognition, Reader Policy, record-role/actionability semantics and derived runtime projections | **Kristal** | Consumers derive read/projection/runtime materializations | Kristal is not source acquisition, a live app DB, or UCKK presentation state |
| Univers-Cité scope/projection configuration, Moodle/campus state, derived glossary/media presentation, local Assembly decisions | **UCKK / Univers-Cité** | Consumes pinned Kristal artifacts and optional external readings | UCKK does not own Kristal assertions/referents or Konnaxion civic decisions |
| Platform profiles, trust/policy/resources, artifact admission, release channels and Release Sets | **kOA-Linux** | Admits/co-ordinates product artifacts under platform policy | Product apps do not acquire platform release authority |
| Runtime Pack verification/compatibility, active Runtime Pack state, activation/rollback receipts, runtime health | **`kristal_runtime`** | Platform coordinates compatibility; Node Agent may execute narrow privilege | Digital Ecosystem does not create a parallel runtime-activation state |
| Narrow authorized node-local privileged lifecycle / activation / recovery operation | **kOA Node Agent** | Executes authorized host transitions and emits receipts | Node Agent does not own release or epistemic authority |
| Shell, routing, Space lifecycle and admitted application presentation | **Koali Spaces** | Composes owner surfaces | Rendering/routing does not transfer business/epistemic authority |
| Cross-system Profile/envelope semantics where explicitly adopted | **Interaction Kernel** | Carries commands, queries, events, receipts and ArtifactRefs | IK is not participant operational state and is not automatically universal |
| Human-readable communication planning/realization, SA↔GF bridge, RuntimeSet/capability/conformance semantics | **SemantiK Architect** | Realizes complete upstream meaning faithfully | Does not choose truth, civic outcomes or omit supplied facts |
| RuntimeSet release ordering, integrity transfer, promotion/rollback and activation sequencing | **SemantiK Runtime Orchestrator** | Coordinates independent GF/SA/diagnostic owners | Does not own grammar, semantic truth or diagnostic truth |
| Federated identity credentials/assertions | **Identity Provider** for IdP assertions | Apps map identity into local accounts | IdP identity does not imply cross-product roles |
| Local memberships, roles, permissions, sessions and app audit | **Each application** | OIDC may authenticate; app authorizes locally | No universal role table |

## Tandem Linux VPS / Capsule Agent owner supplement (2026-10-18)

The user selected **Linux VPS + Docker + Capsule Agent** as the first Konnaxion↔Orgo deployment target. [C0 profile](../40-integration/tandem-vps-capsule-agent/README.md). The **Capsule Manager** is the nonprivileged orchestration/UI layer; the **Capsule Agent** is the actual VPS-side privileged PEP for its typed Docker/Compose operations; **KonnaxionDiag** owns independent qualification/Ed25519 `verify-activation`. Manager claims and a signature alone cannot replace Agent-controlled measurement. The original kOA-Linux/Node Agent and `kristal_runtime` owners remain unchanged for their own release/Runtime Pack profiles.

## Non-transfer rules

```text
integration              != ownership transfer
projection               != authority
acquisition evidence     != validation
external identifier      != authority
cache/read model         != source of truth
artifact                 != live operational state
transport                != business state
Space activation         != Runtime Pack activation
accepted                 != succeeded
```

## Authority-preserving knowledge flow

```text
source/provider
    → EncyKlopedia evidence + referent candidates
    → Da’at mapping/ACL
    → Kristal-owned referent/Kristal State artifact
    → derived Runtime Pack or UCKK projection
```

No step silently transfers ownership of the upstream state.

## Related references

- [`architecture.md`](./architecture.md)
- [`trust-boundaries.md`](./trust-boundaries.md)
- [`../40-integration/contract-map.md`](../40-integration/contract-map.md)
- [`../40-integration/knowledge-projection.md`](../40-integration/knowledge-projection.md)
- [`../../status/current.md`](../../status/current.md)

## Kristal v6 actionability invariant

Actionability classification is knowledge/policy metadata. It does not transfer execution authority from an operational owner to Kristal, Da’at or a consumer projection.

## C0 ownership supplement — GitHub Kristal v10 (2026-10-08)

This is an **interface coordination supplement**, not a reassignment of system authority:

| State / decision | Owner | Coordination consequence |
|---|---|---|
| Source acquisition/candidates | EncyKlopedia | Not durable Médiathèque custody; not semantic identity |
| Durable source/snapshot/representation acceptance | Médiathèque kOA | Receiver owns acceptance, replay and storage receipt |
| Kristal semantic canon and commitments | Kristal owners under Framework contracts | v10 hosting cannot redefine v9 identity or v6 payload |
| Local build/read surface | Authoring Kit | Read model is derived, must be verified against canonical commitments |
| Independent conformity determination | KristalDiag / owner-designated qualifier | UI green checks alone are not release qualification |
| GitHub sync/inventory | Kristal Manager | A sync is not an immutable release and not activation |
| GitHub release and activation | Kristal GitHub Bootstrap / publisher | Separate explicit stages; per-Kristal permission before public writes |
| Public explorer / IA Context Pack | Konstellation Light / Kompiler | Read-only projections, no canonical state modification |
| Cross-owner version/evidence registry | **C0 in kOA Digital Ecosystem** | Coordination metadata only; does not approve or publish a Kristal |

[Coordination register](../40-integration/orchestration-c0/README.md) records the owner contracts and outstanding tests.

## Owner supplement — Skope / Ékole (October 2026)

| State | Product owner | Explicit limit |
| --- | --- | --- |
| Scope recipe, convergence selections, local working snapshot | **Skope** | No validated assertion/semantic identity authority or platform admission |
| Educational workspaces, pedagogy, site projections, preview/ops state | **Ékole** | No qualification or publication of Kristal v9/v10; no Moodle write without its owner bridge |

See [integration supplement](../40-integration/skope-ekole/index.md). This records product-local ownership, not a new global control plane.

## Updated C0 responsibilities — v10 and global navigation (2026-10-12)

| Responsibility / decision | Owner | Boundary kept explicit |
|---|---|---|
| Local workspaces and local v9 builds/read surfaces | Authoring Kit | Does not grant public visibility or qualify truth |
| Actual local Kristal instances and sync eligibility | Kristal Manager | Does not own domain canon or global visualization |
| Independent C1 evidence | KristalDiag | Must concern the exact candidate/source revision |
| GitHub admission, authorization and release gates | GitHub Bootstrap / C2/C3 | Approval must precede public write; sync != publication != activation |
| Global Kristal fleet browser and selected-state conceptual navigation | **Konstellation** | Read-only, policy-first; unsupported semantic views remain unavailable |
| Structural archetype and diagram patterns | **Arketype** | Descriptive hints only, not canonical or actual instance registry |
| Historical registry crosswalk | **Kristal-Kollection** | Not a replacement for `kristal.github-collection-index/1.0` |

[Detailed owner boundaries and gate register](../40-integration/kristal-v10-alignment/architecture.md).
