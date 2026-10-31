<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/QID-Collection | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: cc877f153e90542461faadcd29533b3eccbcb0a75d9eba18350be7c5498e3aee -->

# Large QID collection: resumable on-disk traversal

**Purpose:** write a complete *within-policy* inventory of Wikidata identifiers to a job directory without loading a massive selection into the browser. It is **not** original source JSON extraction.

## Preconditions

- A finalized, compatible compact index under `<data-root>/30_working/wikidata/`.
- A validated root QID and an explicit nonempty `allowed_properties` list.
- Exactly one traversal direction, `in` **or** `out` (no `both`).
- No accepted convergence candidates (`convergence.include` must be empty).
- No `geography.mode: documented_only`; geographic priorities are **not** filters for batch jobs.
- At least **2 GiB free disk space** at start and during the worker's progress checks.
- Explicit operator action; opening or calculating a profile alone does not start collection.

## Procedure

1. Configure the scope and review the bounded preview.
2. In **Data acquisition**, start **batch QID collection**; the API equivalent is `POST /api/large/start` with `{"recipe": <validated-recipe>}`.
3. Inspect `/api/large/status?job=<32-hex-id>`; pause with `POST /api/large/pause` and `{"job": "<id>"}`.
4. Resume via `/api/large/start`, passing the **same recipe** and `resume` job ID. Only `max_entities` may be increased (or set to `0` for unlimited).
5. When status becomes `completed`, download `/api/large/result.zip?job=<id>` or use **Open Results folder** (Windows).

A requested cap may end the run in `limit_reached`, not `completed`. **A job that reached a budget limit is not exhaustive.** An `interrupted` or `failed` job must be assessed and explicitly resumed.

## Files on disk

```text
30_working/skope-large-scopes/<job-id>/
  recipe.json                validated exact recipe
  state.sqlite              selected/QID queue/status
  selected-qids.jsonl       one {"wikidata_qid":"Q..."} object per line (completed job)
  results.zip               generated on explicit result export
```

The generated ZIP contains `selected-qids.jsonl`, `recipe.json`, `summary.json` and `README.txt` for a normal scope. Specialized author jobs use the same general job root but export additional roster/work evidence files.

## Guarantees and non-guarantees

Selection is driven by indexed relation direction, PIDs and depth; non-Q entity identifiers are excluded. Persisted queue/selected tables protect against an in-memory-only huge inventory. The compact index remains read-only.

**Not guaranteed:** completeness of Wikidata; accurate science; geographic coverage; included preview convergence nodes; provenance of original claims; full source JSON. Consult [Full-Record Extraction](Full-Record-Extraction) for verified source preservation.
