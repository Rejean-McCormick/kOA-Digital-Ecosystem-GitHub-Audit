<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Scope-Recipes | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: bb9dfb2f0873af8377c63e5c2b34ffc8c4b05ec3b3c591f320f9fbcd5f629e45 -->

# Scope recipe reference

A recipe describes **how to traverse the compact Wikidata graph**. It does not contain the entities themselves and cannot execute Python or change canonical data.

## Minimal example

```json
{
  "root": "Q192154",
  "direction": "out",
  "allowed_properties": ["P171"],
  "default_depth": 2,
  "branches": {},
  "max_entities": 1000,
  "convergence": {
    "threshold_percent": 10,
    "min_support": 3,
    "extra_depth": 0,
    "include": []
  },
  "geography": {"mode": "off"}
}
```

`Q192154` and `P171` are drawn from the bundled botany configuration; **verify applicability to your intended domain and traversal direction** before running anything. For one-property QID inventory, choose a single direction `in` or `out` (the example is illustrative, not a guarantee of intended coverage).

## Fields and enforced constraints

| Field | Meaning | Validation |
| --- | --- | --- |
| `root` | Wikidata starting item | `Q` followed by digits; must exist in local index to preview/collect |
| `direction` | Traversal orientation | `in`, `out`, or `both` for preview; **not** `both` for batch collection |
| `allowed_properties` | Relation filter | Array of `P` identifiers; **nonempty** for batch collector and catalog passes |
| `default_depth` | Traversal depth | Integer 0–8 |
| `branches` | First-hop `P123:in` / `P123:out` depth override | Maximum 500 overrides, each depth 0–8 |
| `max_entities` | Requested selection cap | `0` = unlimited mass job; previews **still cap at 10,000** |
| `convergence.threshold_percent` | External-candidate threshold component | Greater than 0, at most 100 |
| `convergence.min_support` | Minimum supporting internal nodes | 1–10,000 |
| `convergence.extra_depth` | Approved-candidate expansion depth | 0–6 |
| `convergence.include` | Explicitly accepted outside QIDs | Valid QID list; **must be empty** for mass collector profiles |
| `geography` | Evidence annotation/filter policy | See [Geography](Geography) |

For previews, branch provenance is retained, a candidate's support counts distinct selected internal nodes, and convergence generates **one wave** of outside candidates. A candidate is not automatically accepted.

## Preview versus collection

`max_entities: 0` **does not** produce an unlimited HTTP preview. It produces a 10,000-node preview budget and a separate plan ZIP when exported. Batch collection persists a traversal to disk but does not apply convergence expansion or geographic exclusion. Choosing `documented_only` can filter the displayed preview, but it is rejected by the mass collector.

## Contract file caveat

`contracts/scope.recipe.schema.json` is a descriptive draft. The operational validator is **`skope/scope.py::validate_recipe`**, with stricter catalog/batch restrictions in `skope/scope_profiles.py` and `skope/massive.py`. Always trust runtime validation over assumptions made from the draft schema alone.

See [Scope Catalog](Scope-Catalog), [Scope Explorer](Scope-Explorer), [QID Collection](QID-Collection).
