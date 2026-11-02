<!-- Frozen source: https://github.com/Rejean-McCormick/Daat/blob/24d288b040d345405c508eb650d40a6c8856cf2a/docs/decisions/ADR-0002-ALIGNMENT-MEASUREMENT.md | commit: 24d288b040d345405c508eb650d40a6c8856cf2a | SHA-256: 802290b3958a89599c2030f976bf47fabe90bee745afb6b64ab800ffb1a6b96e -->

# ADR-0002 — Transparent scoped adapter burden measurement

**Status:** Proposed for review · **Date:** 2026-10-12

## Decision proposed

Measure per capability and pinned contract edge: coverage, transformation classes, total burden points, burden per semantic obligation, disclosed loss, unsupported mandatory obligations and unresolved ambiguities. An adapter with high burden can still fully conform; no opacity or universal ranking.

## Method

Use the transform class weights and definitions in `../07-ALIGNMENT-METRICS.md` with mandatory golden fixtures and reproducible reports. An opt-in public badge may assert a specific **tested capability+contract version**, not overall superiority.

## Tradeoffs

Weighted costs can be imperfect, change with schemas, and obscure hidden upstream transforms; review actual native source fixtures and publish raw rule inventories. Never hide changed denominator/scope. Security overhead is never counted as semantic mapping burden.

## Rejected alternatives

- Lines of code alone.
- Number of fields mapped alone.
- Opaque 0–100 score without coverage/context.
- Rejection of valid non-native systems based on distance.
