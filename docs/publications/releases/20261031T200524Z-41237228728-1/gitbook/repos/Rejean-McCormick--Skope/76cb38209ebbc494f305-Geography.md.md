<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Geography | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 0ab839df7266b1a52ffff01b8f0c4dff99187f85c85a91ea2504c5c56e60e85e -->

# Geography: document signals, not occurrence proof

Skope supports geography **annotations** attached to a scope recipe, chiefly the Botany North America / Canada priority scenario. Wikidata properties are incomplete and do not establish biological presence/absence by themselves.

## Example

```json
"geography": {
  "mode": "annotate",
  "focus": "north-america",
  "priority": "canada",
  "region_qid": "Q49",
  "priority_qid": "Q16",
  "evidence_properties": ["P9714", "P183", "P2341"]
}
```

Supported modes:

- **`off`** — no geography classification.
- **`annotate`** — annotate/prioritize displayed entities without excluding unknown ones; recommended for research.
- **`documented_only`** — in **preview only**, display entities with region/priority signals (plus root context). Risk: many false negatives; **not accepted** by batch collector.

## Implementation

Skope inspects compact links for P9714 (*taxon range*), P183 (*endemic to*) and P2341 (*indigenous to*). To classify linked places, it follows at most **two geographic hops** using P17/P131/P30, with bounded queries. The labels `priority`, `region`, `outside_only` and `unknown` describe *indexed signals*, not ecological conclusions.

Geographic annotation happens **after** graph traversal. An unvisited branch cannot be recovered by a Canada-first presentation rule. In the massive QID collection, neither the geographic priority nor `documented_only` acts as a filter.

**Never infer:** “no Canadian link” ⇒ “absent from Canada”; “P9714 exists” ⇒ “verified occurrence”; “the whole scope is complete” ⇒ “a complete flora”. Independent flora/occurrence evidence, e.g. authoritative botanical data, is still needed.

See [Scope Recipes](Scope-Recipes), [QID Collection](QID-Collection), [Safety and Provenance](Safety-and-Provenance).
