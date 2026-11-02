<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Full-Record-Extraction | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: ca142629d6b58868ccc57ff8b337cc730ea4a46c4936c008dc0ac4257dd736e3 -->

# Full Wikidata record extraction

Unlike the compact-index preview or a QID inventory, this optional workflow retrieves the **original full entity JSON** from a pre-existing Wikidata dump by **verified random access**. It is deliberately blocked rather than falling back to a large dump scan.

## Mandatory prerequisites

1. An **already completed** QID job with a sorted, unique `selected-qids.jsonl` and consistent count.
2. A configured extraction profile in `config/extraction-profiles/*.json` (`skope.extraction-profile/draft-1`).
3. A matching local source dump, and a manifest declaring the dump verified with SHA-1, filename and byte size.
4. An **existing** QID locator and appropriate compression-sidecar index, matching the configured dump.
5. A random-access-capable reader in the *running server process*: for `.bz2` files, the optional `indexed_bzip2` package; for supported `.gz` paths, `rapidgzip` may apply.
6. Sufficient free space in the configured data volume; bundled profiles specify **20 GiB minimum**.
7. Explicit review/confirmation by the operator.

**Source identity subtlety:** preflight trusts an existing verified manifest and checks metadata; it does **not** rehash a 96 GiB dump or independently revalidate that prior manifest's factual assertion on each run. Do not describe preflight as a fresh end-to-end source certification.

## Preflight and run

1. Select an extraction profile and completed QID job.
2. Click **Check sources** or call `POST /api/extract/preflight` with `{"profile":"<installed-profile>","source_job":"<qid-job>"}`.
3. Read `ready`, `blockers`, `source`, `inventory_sha256`, `profile_sha256`, `qid_recipe_sha256`, `batch_size` and free-space warnings.
4. Start extraction **only when `ready` is true**, using a separate explicit `POST /api/extract/start` request with `confirmed: true`.
5. Monitor `GET /api/extract/status?job=<extract-id>`. Pause via `/api/extract/pause` and resume using the same profile/source/resume ID, when eligible.

Resume checks the source SHA-1, inventory SHA-256, recipe and profile digests. A changed source or inventory is grounds to refuse reuse of prior batches.

## Storage and outputs

```text
30_working/skope-extractions/<extract-job>/
  profile.json
  state.json
  chunks/part-000000.jsonl.gz            (during collection)
  chunks/part-000000.manifest.json        (during collection)
  missing-qids.json                       (if missing source entities)

20_evidence/scope-snapshots/<scope-key>/wikidata-<digest>/
  part-000000.jsonl.gz
  part-000000.manifest.json
  snapshot-manifest.json
```

Each gzip JSONL line contains an original source entity JSON record. QID identity is checked against the expected identifier; per-record and per-batch SHA-256 values are stored. Finalization verifies parts and performs a same-volume directory promotion, refusing an incompatible existing snapshot.

## Scope of the evidence

Preserved source JSON includes labels, descriptions, aliases, claims, ranks, qualifiers, references, identifiers and sitelinks. This is stronger preservation than an aggregated edge preview, but **not** independent validation of claims, ecological presence, medical efficacy or historical authorship. Integration into a Kristal still requires review by its separate canonical process.

## Common blockers

- `indexed_bzip2` imports in another interpreter but not **the server's** interpreter → use `/api/diagnostics/reader` and restart/update accordingly.
- Locator/sidecar missing or mismatch → verify existing data pipeline; **do not instruct Skope to build a new index**.
- Source manifest missing or wrong size/filename → correct provenance inputs, not code.
- Missing QIDs during random-access fetch → extraction pauses with a missing-QID report, no dump-scan fallback.
- Changed profile/inventory/recipe on resume → start a separately reviewed operation.

See [Configuration and Paths](Configuration-and-Paths), [Testing and Validation](Testing-and-Validation), [Safety and Provenance](Safety-and-Provenance).


## 0.15.0-alpha.1: full-source acquisition for a Kristal portfolio

The new **CLI** `skope portfolio acquire` is a second consumer of Skope's verified source-profile checks and random-access reader. It accepts QID seeds from a v11 Kristal portfolio working database, rather than requiring a prior Skope `massive.py` scope job. It writes separately hashed gzip JSONL chunks and a completed `snapshot-manifest.json` under its `--out` directory. Chunk-level resume requires matching selection, profile, source identity and hashes. There is **no fallback full dump scan** when the verified locator is missing.

The indexed `discover` stage **does not** produce original Wikidata statements. Only full entities acquired from the verified dump can support claim-level proposals with `id`, `rank`, `qualifiers` and `references` (or a clearly marked unverified development fixture). See [Portfolio Enrichment](Portfolio-Enrichment) and [Portfolio CLI Reference](Portfolio-CLI-Reference).
