<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Scope-Catalog | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 9cee4503e8ab997740a99cd8ac772c25070f2ee21b34bdc16a6a4cf7f75835e8 -->

# Scope catalog and drop-in profiles

Place JSON files directly in the repository's `scopes/` directory. The UI refreshes this library on demand (and periodically while visible). **Refreshing is read-only; it never runs a job.** JSON is validated as data, never imported as Python code.

## Supported profile kinds

| Format | Structure | Behavior |
| --- | --- | --- |
| Simple recipe | top-level traversal or `{"recipe": {...}}` | One pass |
| `skope.scope-campaign/1.0` | `id`, `title`, `passes` | Independently selected passes |
| `skope.author-works-campaign/1.0` | Catho author/works orchestration | Explicit dedicated start; requires active Catho workspace |

Bundled, valid profiles as observed in this snapshot:

| Profile id | Type | Passes |
| --- | --- | --- |
| `botany` | Campaign | 2 |
| `catho-authors-persons` | Campaign | 7 |
| `catho-recognised-authors` | Specialized author/works | Dedicated orchestration, no generic passes |
| `catho` | Campaign | 3 |
| `economics` | Campaign | 2 |

## Multi-pass example

```json
{
  "format": "skope.scope-campaign/1.0",
  "id": "sample-topic",
  "title": "Sample topic",
  "scope_context": "Example scope, review before use",
  "passes": [{
    "id": "base",
    "title": "Base traversal",
    "intent": "Inspect related Wikidata QIDs",
    "risk": "Aggregated edges do not prove source statements",
    "recipe": {
      "root": "Q192154", "direction": "out",
      "allowed_properties": ["P171"], "default_depth": 1,
      "branches": {}, "max_entities": 1000,
      "convergence": {"threshold_percent": 10, "min_support": 2, "extra_depth": 0, "include": []},
      "geography": {"mode": "off"}
    }
  }],
  "safety": {
    "auto_run": false, "write_kristal_canon": false,
    "write_original_dump": false, "new_fast_index": false,
    "collect_qid_only": true
  }
}
```

Validate the root/direction semantics for your research before using this illustrative example. `scopes/AI_SCOPE_PROMPT.md` contains the project's prompt template for generating new profiles.

## Catalog safety bounds

- Up to **256** `.json` files are scanned; each up to **256 KiB**.
- At most **32** passes per campaign.
- Duplicate JSON keys, duplicate profile IDs, symlinked files, bad identifiers and unsafe `safety` flags are rejected.
- A bad file is isolated as a catalog error, not allowed to take down all valid profiles.
- Catalog batch passes require one direction, explicit properties, no accepted external convergence and no strict geographic exclusion.
- `*.template` is not scanned.

**Steps:** save `your-topic.json` → **Refresh profiles** → select profile/pass → **Apply scope settings** → **Calculate scope** → manually decide whether to collect QIDs.

See [Scope Recipes](Scope-Recipes), [Getting Started](Getting-Started).
