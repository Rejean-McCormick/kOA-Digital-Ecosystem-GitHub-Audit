<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Scenario-Mosaic/blob/4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03/docs/32_REGULAR_HONEYCOMB_AND_SINGLE_HOVER.md | commit: 4ac4e787ef01295c9100c73d8b5bbf9a19d9ef03 | SHA-256: e41ad5f1e952b4cd4ce6b3ee7e8cad96b6af36950d77441d6d588e5bd0c5ce25 -->

# v3.3 — Regular honeycomb + single hover

> **Geometry superseded in v3.7.** The single-highlight rule remains active, but the 12 × 10 geometry described here was replaced by the 20 × 6 panoramic spread in [`36_PANORAMIC_SPREAD_AND_COLOR_LEGEND.md`](36_PANORAMIC_SPREAD_AND_COLOR_LEGEND.md).


Only one cell receives `is-active`. Related-scenario highlighting is removed. The 120 current cells are generated on a pointy-top hex lattice: horizontal spacing `sqrt(3)×s`, vertical spacing `1.5×s`, odd-row offset `sqrt(3)×s/2`. There are no row-specific drifts.
