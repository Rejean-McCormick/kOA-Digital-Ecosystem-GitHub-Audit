<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/40-integration/kristal-v10-alignment/architecture.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 6d5bd1cf1f5a4b27586aeae771fe0e3c482ac2b60b9f8d48a90c19c37e9a349f -->

# Kristal v10 — Ownership and navigation architecture

```text
Kristal Framework v10 (contracts, semantic state identity, v9 commitments)
  ├─ Authoring Kit 3.2.4+ → local check/build/read-surface
  ├─ KristalDiag / C1 → independently scoped qualification evidence
  ├─ C2 / GitHub Bootstrap → revocable owner-authorized write & release policy
  ├─ Kristal Manager → local inventory, controlled read-surface sync and derived index
  │     ├─ kristal-public     (hosted read surfaces; C3 gate)
  │     └─ kristal-private    (hosted read surfaces; separately governed access)
  ├─ Arketype → non-normative structural design patterns & neutral workspaces
  ├─ Konstellation → My Kristals fleet explorer + in-Kristal Lens/graph navigation
  ├─ Kompiler → authorized read-only Context Packs (provenance/coverage)
  └─ Konstellation Light → optional static public projection from approved releases

kOA Digital Ecosystem/C0: versions + ownership + evidence + unresolved decisions
Kristal-Kollection: historical registry / provenance crosswalk only
```

## Ownership, not a monolith

| Concern | Owning repository / service | Not owned by C0 |
|---|---|---|
| Normative schema, identity, commitments and compatibility | Kristal Framework | Canonical artifacts, decisions to publish |
| Local workspace and v9 build/reader projection | Kristal Authoring Kit | A separate Framework definition |
| Independent qualification | KristalDiag (C1) | C0 documentation or CLI success badges |
| Approval, trust, visibility and network setup | GitHub Bootstrap / C2 (owner policy) | A silent public push |
| Operational inventory, scoped sync/read-surface index | Manager | Semantic interpretation of every domain |
| Hosted collections and C3 integrity | kristal-public / kristal-private | A universal local registry |
| Instance navigation and concept exploration | Konstellation | Domain canon, inventory authority or publication |
| Template and visual archetype catalogue | Arketype | Actual instance list or fact qualification |
| Context Pack/read-only reasoning assistance | Kompiler | Build/publish/activate |
| Historical crosswalk and archives | Kristal-Kollection | New v10 collection-index authority |

**Important invariants:** Logical State != materialization; State Commitment != Git SHA; Reference != ownership transfer; read surface != canon; sync != immutable publication != activation; repository visibility != authorization; missing remote file != absence of knowledge.

## Two kinds of navigation

1. **Across Kristals:** Konstellation's proposed *My Kristals* view consumes authorized Manager inventory and verified GitHub index metadata, reconciles by **explicit `state_ref` and exact revision**, and preserves source/visibility/readiness.
2. **Inside a Kristal:** Konstellation uses existing Lens/query/renderer features where the particular state has a supported semantic reader. GitHub v10 manifest topology alone does **not** decode arbitrary polymorphic v9 concepts.

**Proof boundary:** Existing Konstellation v10 tests cover its derived GitHub host topology; they do not prove universal polymorphic semantic reading or a complete 126-local-workspace fleet integration.
