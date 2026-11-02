<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/10-system/architecture.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 806374496b38718f65963bd910ac3ed7dbc698bafb96fc8a47a1751addf609a8 -->

# Architecture

## Architectural thesis

kOA is a system of independently owned systems and platform components. Integration coordinates them without collapsing their authoritative states.

## Owner map

| Responsibility | Owner |
|---|---|
| civic/public state and DecisionRecord | Konnaxion |
| workflow/work state and durable external operations | Orgo |
| epistemic artifact semantics | Kristal |
| platform profiles/trust/policy/resources/release channels | kOA-Linux |
| Runtime Pack verification/compatibility/active state/receipts/runtime health | `kristal_runtime` |
| narrow privileged node-local lifecycle transition | kOA Node Agent |
| presentation composition and Space lifecycle | Koali Spaces |
| target cross-system protocol/Profile semantics | Interaction Kernel, where explicitly adopted |
| ecosystem-to-Kristal mapping/ACL | Da’at |

## State and artifact planes

kOA separates mutable operational state, epistemic artifacts and runtime/query materializations:

```text
Operational state (product-owned, mutable, transactional)
        │ immutable export/snapshot + digest/revision
        ▼
Da’at mapping / ACL boundary
        ▼
Kristal knowledge artifact (content-addressed epistemic state/Exchange)
        │ deterministic build
        ▼
Runtime Pack / query materialization (derived, read-oriented, rebuildable)
```

Ownership does not move upward through this pipeline. Orgo/Konnaxion remain authoritative for the live domain record. Kristal owns the resulting epistemic artifact. Runtime/query structures do not become a third authoritative copy. There is no required distributed transaction or bidirectional database synchronization across these layers.

## Release architecture

kOA-Linux separates `system`, `services`, `governance` and `knowledge` release channels. A Release Set binds tested-compatible versions across channels.

Kristal Runtime Packs are platform artifacts in the `knowledge` channel. The kOA-Linux artifact classification (`artifact_class = runtime_pack`) is distinct from Kristal's own scoped manifest discriminator.

## Runtime Pack activation architecture

```text
Runtime Pack candidate
  -> kOA-Linux artifact / knowledge-channel admission
  -> kristal_runtime verification + compatibility + activation eligibility
  -> active_runtime_pack_record transition
  -> activation/rollback receipt

when privileged host mutation is required:
  -> kOA Node Agent executes the narrow authorized node-local transition
```

`kristal_runtime` does not own governance policy, resource scheduling, host privilege or workflow state. kOA Node Agent does not own release authority or epistemic semantics.

## Koali Spaces placement

Koali Spaces sits above admitted applications as optional presentation infrastructure. It owns shell/routing/presentation/Space lifecycle only. Removing Koali must not transfer or delete owner-system business state.

## Interaction Kernel placement

IK is a target system-of-systems protocol/Profile layer for selected cross-product boundaries. kOA-Linux already has canonical internal/component communication contracts; Digital Ecosystem must not claim those have been replaced by IK until explicit adoption/mapping is published.

## Kristal v9/v10 hosted-network overlay — C0 coordination (2026-10-12)

The state and Runtime Pack planes above remain relevant. **Kristal v9 owns logical knowledge commitments**, and the Framework **v10 draft GitHub host profile** adds discovery and publication without replacing those commitments. This lane is distinct from kOA-Linux Runtime Pack activation and the historical v6 projection contract.

```text
Authoring Kit → state v9 → read-surface → Manager → controlled GitHub collection
             independent C1  +  owner-scoped C2   → verified C3 publication
                                                 → Konstellation / Kompiler readers
Arketype → optional design-only archetype/pattern metadata
Kristal-Kollection → legacy mapping only
```

**Navigation ownership:** Konstellation is the user-facing explorer **across** Kristals and **within** a selected Kristal; Manager maintains local instance inventory; Arketype catalogs structural types. The planned fleet aggregator is not yet implemented/qualified. Hosting topology is not generic semantic concept decoding. C0 tracks these contracts only; see [v10 alignment](../40-integration/kristal-v10-alignment/README.md).
