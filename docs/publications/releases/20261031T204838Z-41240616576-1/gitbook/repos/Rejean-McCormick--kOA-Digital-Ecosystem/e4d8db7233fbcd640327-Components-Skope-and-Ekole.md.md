<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Components-Skope-and-Ekole.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 78ef66de22d63df9f3607d56dc08b84cfe37cd5613eebcf69f4ebc38be2f02c2 -->

# Skope & Ékole — nouvelles applications cartographiées

**Status: owner-snapshot reconciliation / proposal; no claim of production integration.**

## Skope

- **Owner:** Skope repository (generic repository `Skope`).
- **Role:** visually scopes a Wikidata-derived working skeleton for a future Kristal, preserving QIDs/PIDs and source assertions.
- **Capabilities evidenced:** local Python/SQLite index from supported Wikibase JSON formats, per-branch depth controls, directional/property filters, external convergence candidates with explicit acceptance, offline preview, reproducible *prototype* ZIP export.
- **Does not own:** EncyKlopedia's acquisition authority, Da’at mapping/ACL, Kristal canonical identity/validation, UCKK pedagogical decisions, publishing.
- **State:** operational local prototype with synthetic fixture; the user clone `D:` format and end-to-end v9/v10 qualification are **not established**.

## Kristal Iroquoiens — working model indépendant

- **Owner :** `Kristal-Iroquoiens-Working`, dépôt distinct de Skope.
- **Possède :** `Q110654499` en seed éditorial, ses recettes, archives documentaires, axes, mappings candidats, règles de revue culturelle et ses propres zones working/canon.
- **Relation :** appelle Skope par `--db` + `--recipe` externe. Aucun code Skope copié et aucun couplage entre l’UI générique et la racine iroquoienne.
- **Statut :** projet non canonique; démonstration synthétique; vraie extraction depuis le clone utilisateur `D:` non établie.

## Ékole

- **Owner:** Ékole repository.
- **Role:** Québec primary-school authoring/catalogue and learner/teacher projections over 202 Kristal authoring workspaces.
- **Evidence in supplied snapshot:** 202 workspaces identified as Authoring Kit stubs, derived pedagogical catalogue and graph (252 relations), Core/Élève and Enseignant applications, OpsConsole, local build/preview, Moodle projection **plan** (`moodle-plan`).
- **Does not own:** Kristal authority or v9/v10 qualification, live Moodle course IDs, global source acquisition, host privileges or publication authority.
- **State:** documented local applications and checks; **no verified published v10 states**, Moodle write path or qualified Skope→Ékole handoff.

## Local coexistence

| Service | Default | Notes |
| --- | --- | --- |
| Ékole Core + Élève | `127.0.0.1:8765` | Portal `/`, learner `/eleve/` |
| Ékole Enseignant | `127.0.0.1:8766` | Launched from Ékole three-app batch |
| Ékole OpsConsole | `127.0.0.1:8766` | Alternative/admin launch; **collides with Enseignant** when both use defaults |
| Skope | `127.0.0.1:8767` | Default in accompanying updated Skope repo; overridable |

The port convention is local documentation, **not** an OIDC/Koali/IK service registration or an assertion that every Ékole interface can run concurrently. Only Ékole can resolve the internal teacher/OpsConsole collision.

See [contracts & evidence](../2-Technical-Reference/40-integration/skope-ekole/index.md) and [app inventory](../inventory/apps-skope-ekole.json).
