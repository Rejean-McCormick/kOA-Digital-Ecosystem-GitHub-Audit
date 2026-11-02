<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Integrations-and-KOR | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 9ce63c879b5a49a20043b26443710e5e3d973e2d601bdd2f598dcd08dc5202c8 -->

# Integrations — KOR, Kontexte, Ekole, and Orgo

**KOMPOSE is independent of KOR** (ADR 0006). KOR can eventually present an authorized narrative interface; there is **no live KOR adapter** in this repository. Independence from KOR does **not** imply that KOMPOSE can operate real Tandem Tasks: **Orgo is the sole operational authority** (ADR 0008).

## Implemented local integration examples

| Source / audience | Local operation | Not implemented |
|---|---|---|
| Kontexte `kontexte.mission/1` and role definitions | B6 synthetic scenario plan, role projection, fallback proposal, mock replay | Orgo Case/Task creation, learner identity, actual fragment delivery |
| Ekole `ekole.tandem-teacher-preview/1.0` | Strict JSON structure and field whitelist | Authentication, verified WorldRelease, operational admission or competency |
| KOR narrative client | `examples/integrations/kor.adapter.example.json` manifest | Runtime transport, student views, permission-filtered API |

## Future client-facing privacy boundaries

Only audience-authorized missions, roles and scripted prompts should be sent by a real server. Never send pupil diagnostics, rankings, accommodations, affinities/aversions, hidden fragment bodies, or sensitive teacher decisions to narrative clients. UI hiding alone is not authorization.

## Required steps for any live integration

1. Identify the authoritative owner of each operation and data field.
2. Establish signed/authenticated teacher and institutional identity, tenant/World scoping and versioned contracts.
3. Perform real Orgo permission checks and enforce recipient filtering before delivery.
4. Test negative access, duplicate/replayed events, out-of-order transitions, offline recovery and rollback.
5. Obtain educational and privacy approval before any child or real-world content appears.

**No HTTP calls or deployed adapters are included** in the current examples.

[[Home|← Home]] · [[Tandem-Orgo-Boundary|Operational authority]] · [[Architecture|Architecture →]]
