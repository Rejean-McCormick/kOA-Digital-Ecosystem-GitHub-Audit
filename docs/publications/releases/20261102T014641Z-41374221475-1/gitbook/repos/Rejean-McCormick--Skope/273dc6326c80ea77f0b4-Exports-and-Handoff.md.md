<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Exports-and-Handoff | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 717046e323dc88528cd5e139cf1a7582cccdf44655288cf708ccf44600900e9b -->

# Exports, research artifacts and downstream handoff

Skope exports are intentionally distinguished by purpose. Do not promote a graph preview or QID list directly as validated source evidence.

| Export | Trigger | Contents | Status |
| --- | --- | --- | --- |
| Small scope proposal | `POST /api/export` or CLI `export` with capped recipe | `manifest.json`, review recipe/report, `staged/` proposed EncyK files, README | **Non-canonical**; human handoff required |
| Large-scope plan | `POST /api/export` or CLI export when `max_entities=0` or above 10,000 | Manifest + review recipe (+ optional guidance/target) | **Plan only**, not complete QIDs |
| QID results | `/api/large/result.zip?job=<id>` | `selected-qids.jsonl`, recipe, summary, README | Complete **only for specified collection policy**, no original JSON |
| Catho results | Author campaign results | Matched/unresolved people, P50 links, inventory, provenance | Indexed discovery / roster research material |
| Full-record evidence | Explicit extraction | `.jsonl.gz` parts, record SHA-256, part manifests, snapshot manifest | Source record preservation; not independent claim verification |
| Single identity review ZIP | `/api/reconciliation/export.zip` | Decisions/audit/roster digest | Human review record, non-canonical |
| Portfolio inventory/candidates | `skope portfolio inventory/prepare/review-csv` | `portfolio.sqlite`, source digest, review CSV | **Working, unverified** research; no accepted crosswalk |
| Portfolio verified raw evidence | `skope portfolio acquire` | Source-checked `part-*.jsonl.gz`, chunk hashes, `snapshot-manifest.json` | Source-preserving evidence, not domain truth |
| Portfolio claim proposals | `skope portfolio propose` | Full Wikidata claims JSONL, linked QID queue and report | **Non-canonical**; requires diK + Authoring Kit |
| Batch identity review ZIP | `/api/reconciliation/batch/export.zip` | Triage, staged proposals and reviewer CSV | Candidate research material; later confirmation explicit |

## Portfolio versus canonical publication

Portfolio results preserve a source statement and its references but do **not** replace KQ/KP with Q/P, create a semantic KP where none was reviewed, or produce a published KA. A `lexical_only_unverified` draft seed must never become a diK `exactMatch` without independent review; even `review_attested` in Skope is a *working decision*, not a diK crosswalk write. There is no integrated Authoring Kit publication path yet. See [Portfolio Enrichment](Portfolio-Enrichment).

## Small-scope proposal contract

For a small, non-truncated preview, `export.py` prepares a reviewed `skope-encyk-proposal/1.0` ZIP. The generated `staged/` files describe proposed seed records and an `encyklopedia-scope/v3` configuration. `publication_authorized` and `activation_authorized` remain false. A source fingerprint binds selected QIDs, recipe and indexed source digest.

The historical EncyK handoff instructions require the operator to compare source fingerprints, inspect the selection and explicitly stage compatible files in the separate EncyK workflow. That is an **external process**, not an autonomous action Skope performs.

## Large exports are intentionally not silently complete

A requested unlimited or >10,000-node scope produces `skope-encyk-large-scope-plan/1.0` with `selected_entities: null`, because the HTTP preview cannot enumerate the entire universe. Only the separate disk-backed QID collection can produce a full *within-policy* inventory.

## Arketype context

`config/arketype/botany.scope-guidance.json` and compatible guidance documents may accompany a proposal. They are **documentary guidance**, not a request to update Arketype, Kristal or a canonical state. `docs/MIGRATION_SKOPE_ARKETYPE.md` is historical integration context; it should not be interpreted as a current standalone automatic migration.

See [Architecture](Architecture), [Data Formats](Data-Formats) and [Safety and Provenance](Safety-and-Provenance).
