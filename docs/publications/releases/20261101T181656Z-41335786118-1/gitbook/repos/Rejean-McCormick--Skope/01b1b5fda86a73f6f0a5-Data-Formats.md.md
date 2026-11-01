<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Data-Formats | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 15650e9aa8aacbcffc404fc320c4bad40f8f8314a3063dd42cdf4936226215ef -->

# Data model and file formats

## Input: finalized discovery index

Required SQLite tables: `entity`, `name`, `entity_edge`, `meta`. The `meta` table must declare `complete=1` (or equivalent recognized true value). `name.norm` is queried via an existing `idx_name_norm` index. Encoded identifiers map QID, PID and LID ranges to integer keys. `entity_edge` stores aggregate edge counts/ranks, *not* original Wikidata statement records.

## Input: recipes and profiles

| Format | Files | Description |
| --- | --- | --- |
| Traversal recipe | `scopes/*.json`, `fixtures/demo.recipe.json` | Root, direction, PIDs, depths, convergence, budget, geography |
| Multi-pass catalog | `scopes/*.json` | `skope.scope-campaign/1.0`; passes selected independently |
| Catho author orchestration | `scopes/catho-recognised-authors.json` | `skope.author-works-campaign/1.0` |
| Full extraction | `config/extraction-profiles/*.json` | `skope.extraction-profile/draft-1`; source/selection/output/safety contracts |
| v11 Kristal portfolio | `ZIP` or local project folder with `.kristal/v11/dik.project.json` and curated dictionaries | Read-only source for native `skope portfolio` |
| Kristal workspace | `<workspace>/kristal.workspace.json` | `kristal.local-workspace/...`; read-only context |

`contracts/scope.recipe.schema.json` is a draft contract, not a substitute for the stricter runtime validators.

## Native portfolio formats (0.15.0-alpha.1)

`portfolio.sqlite` stores projects, scoped `(namespace, KQ/KP)` lexemes, bounded search cache, tentative seeds and **Skope-local** documented mapping decisions; it is a working-state database, not a source authority. `inventory.json` stores counts and input SHA-256.

`review-candidates.csv` contains listed Q/P candidates plus reviewer fields. `portfolio-selected-qids.jsonl`, `reviewed-mappings.jsonl` and `extraction-intent.json` describe the *intent* to fetch full data. `skope portfolio acquire` writes `part-NNNNNN.jsonl.gz` and matching `.manifest.json` with SHA-256 checks and a completed `snapshot-manifest.json` when all QIDs are retrieved.

`propose` outputs `skope.portfolio-wikidata-claim-proposal/1.0` JSONL: namespace, KQ subject, external Q/P, optionally mapped KP, entire `full_source_claim`, statement `id`, rank and source identity. A second `.related-qids.jsonl` file contains **unapproved discovery seeds**; a `.report.json` gives totals. This format is **not** a Kristal v11 KA assertion schema. See [Portfolio Enrichment](Portfolio-Enrichment).

## Output: QID inventory

One JSON object per line, sorted in numerical QID order, no duplicates:

```json
{"wikidata_qid":"Q192154"}
```

Persistent `state.sqlite` has selected/queue/status data for resumable traversal. It is operational state, not source evidence.

## Output: source record evidence

Full original Wikidata JSON objects are compressed into `part-000000.jsonl.gz` and subsequent parts. For each part, a manifest associates expected QIDs with record SHA-256, raw byte lengths and batch hash. `snapshot-manifest.json` records the source SHA-1 claim, inventory/profile/recipe hashes, record counts and part digests.

`source_sha1` is the verified-manifest identifier; hashes of output bytes establish local integrity. Neither establishes external correctness of an entity's claims.

## Output: Catho and identity work

- `matched-people.jsonl` / `unresolved-people.jsonl`: local roster-to-QID matching state and recognition source context.
- `author-work-links.jsonl`: aggregate P50 author→work links.
- `decisions.sqlite`: human decisions, unverified batch proposals, append-only audit/revisions.
- `batch-analysis.json`: ranked candidates and bucket classification, tagged with `source_roster_sha256`.
- `batch-progress.json`: active/completed/failed analysis progress.
- `human-review-template.csv`: editable reviewer input with a revision per person.

## Terminology

- **QID:** Wikidata item identifier, e.g. `Q16`.
- **PID:** Wikidata property identifier, e.g. `P50`.
- **Claim/source JSON:** original record content, unlike aggregated compact edges.
- **Proposal:** working material awaiting review, not publishable canon.
- **Attested confirmation:** reviewer states they checked identity evidence; Skope does not automatically validate the linked web pages.

See [Exports and Handoff](Exports-and-Handoff), [API Reference](API-Reference), [Safety and Provenance](Safety-and-Provenance).
