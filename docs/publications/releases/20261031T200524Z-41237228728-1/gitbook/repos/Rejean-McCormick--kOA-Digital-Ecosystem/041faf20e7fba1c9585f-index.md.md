<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/skope-ekole/index.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 5612aa8d1719d773270d77dd85d1c4fcc2f222b7af89afd8415c909b9127f328 -->

# Skope ↔ kOA ↔ Ékole — integration boundary

**Classification:** current documentary mapping; adapter/handoff **proposed**, not qualified. Owner repositories are authoritative for product logic. The supplied snapshots are the evidence baseline.

## Data flow (current vs target)

```text
Wikidata dump / SQLite containing Wikibase entity JSON
    |
    v
Skope (generic tool): external project recipe + QID -> typed scope -> approved convergence
    |
    +-- CURRENT: working ZIP + recipe + entity JSON + selection report
    +-- PROJECT OWNER: Kristal-Iroquoiens-Working (own seed, recipe and working storage)
    |
    +-- PROPOSED: source-custody handoff -> Da’at mapping/ACL -> Kristal Authoring Kit
                                                -> Kristal owner validation/qualification
                                                -> consumer read surface (Ékole / UCKK / Konstellation)
```

No endpoint/API contract between Skope and Ékole is implemented or accepted merely by their inclusion in this map. Skope extracts/suggests; Ékole structures educational content and read-only projections. Kristal preserves epistemic ownership.

## Contract status

| Boundary | Producer | Candidate artifact | Intended consumer | Status |
| --- | --- | --- | --- | --- |
| Wikibase export → local working index | local Wikidata clone | native entity JSON / Skope SQLite | Skope | **Implemented for supported JSON shapes**; user D: clone not tested |
| Project recipe → Skope | project repository | `--db` + `--recipe` / `GET /api/config` | Skope UI / engine | **Implemented in separated Skope prototype; domain repo owns recipe** |
| Skope → working export | Skope | `scope.recipe.json`, `scope.report.json`, `skeleton.graph.json`, entity JSON, snapshot manifest | offline local reader / human | **Implemented prototype; not Framework-v5 normative recipe** |
| Skope → source acquisition/custody | Skope / origin source | pin + digest + scope + raw evidence | EncyKlopedia / Médiathèque (according to adopted owner contract) | **Proposed; receiving adapter/receipts not qualified** |
| Skope → semantic compilation | reviewed working export | approved candidate mappings and sources | Da’at / Authoring Kit / Kristal | **Proposed; not qualified** |
| Qualified Kristal → Ékole/UCKK | Kristal owner | pinned, qualified semantic/read artifact | Ékole-derived pedagogical projection; UCKK/Moodle | **No Skope-specific or Ékole-v10 E2E qualification** |
| Ékole → Moodle | Ékole | `moodle-plan` / explicit bindings | Moodle `local_uckk` candidate | **Dry-run only; no confirmed live write** |

Frozen historical v6 contract names in `contract-map.md` remain **unaltered**. Current C0 handoff reconciliation remains a separate track. No invented `IK` profile or universal Skope/Ékole API is authorized here.

## Guards

- **Domain recipe ≠ Skope code.** The QID for an Iroquoian prototype is held in `Kristal-Iroquoiens-Working`, never in the generic Skope code.
- **Skope working ≠ Kristal canon.** The snapshot retains source provenance and original QIDs; it does not validate history.
- **Snapshot ID ≠ semantic commitment.** JCS v5 recipe equivalence and v9/v10 qualifications require their owner gate.
- **Education ≠ publication.** Ékole 202 authoring stubs and website do not imply 202 qualified v9 states.
- **Projection ≠ Moodle write.** A planned projection does not create course IDs or evaluation banks.
- **Local ports ≠ service discovery contract.** Only bind to loopback in standalone mode; admission by Koali/kOA-Linux is separate.
- **Indigenous cultural claims** require contextual sourcing and appropriate cultural review; model output alone is not validation.

[Local port matrix](local-ports.md) · [Overview](../../../1-Overview/Components-Skope-and-Ekole.md) · [Maturity map](../../../status/current.md)
