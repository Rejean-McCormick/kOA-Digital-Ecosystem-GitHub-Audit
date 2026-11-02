<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Scope-Explorer | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 91ad764422295762c969cc570ba4057f32c60b4b4a1e760011547023f40cb638 -->

# Scope Explorer: bounded graph and convergence preview

The graph explorer uses only the **existing compact SQLite discovery index**. It does not load full Wikidata entity JSON.

## Selection logic

1. Check that `root` exists and validate the recipe.
2. Read the first-hop edges and group them by `PID:direction` branches.
3. Traverse the requested depths, retaining per-branch inclusion reasons.
4. Detect outside candidates linked to distinct selected internal nodes, applying `min_support` and `threshold_percent`.
5. Expand **only explicitly included** convergence candidates, for the configured extra depth.
6. Apply optional *presentation-time* geography annotation/filtering and return induced edges among displayed nodes.

## Controls and output

The explorer displays **Graph**, **Entities**, **Convergence** and **Manifest** tabs. A density visualization offers inspect/pin/magnifier controls. The UI does not imply that node position represents real-world latitude or longitude.

The `POST /api/preview` response includes `nodes`, `edges`, `candidates`, `counts`, `geography_coverage`, `source_snapshot_digest`, `truncated`, `preview_budget`, `requested_max_entities`, `preview_only`, and limitations.

## Hard limits and interpretation

- Maximum preview budget is **10,000** selected nodes, including when `max_entities` is `0` or greater than 10,000.
- A `truncated: true` response is a partial view. Do not export it as a complete list of scope entities.
- `preview_only: true` means the requested scope exceeds the preview budget or is unlimited; the actual inventory must use the separate collection workflow.
- `statement_id` is absent from compact graph edges; statement counts/ranks are aggregated discovery attributes.
- The external-convergence review is a **single wave**, not automatic semantic expansion or proof of relevance.

For large scopes, [QID Collection](QID-Collection) describes the persistent disk-backed alternative. For provenance see [Safety and Provenance](Safety-and-Provenance).
