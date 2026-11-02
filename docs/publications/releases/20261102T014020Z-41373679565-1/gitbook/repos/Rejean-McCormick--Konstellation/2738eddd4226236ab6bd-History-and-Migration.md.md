<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/History-and-Migration | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: e85dfe3e359eb498a25c9dbd1d1a006f2c5c2b0b94279438a22ba70c06696cbb -->

# History, Compatibility, and Cleanup

## Why were there so many launchers?

Several stages accumulated: the Théophile prototype, v6 readers, v9 experiments, the Catho local v10 prototype, improved exploration paths, and finally the neutral selector. There is no requirement to keep all those entry points at the repository root.

## Recommended path

```text
Before: Konstellation_Launcher.cmd / Launch_My_Kristals.cmd /
        Ouvrir_Kristal_Catho_v10.cmd / Ouvrir_Theophile_demo.cmd
After:  Konstellation.cmd → My Kristals → Explorer
```

- Keep a **backup** of historical scripts while testing.
- Tests and corpus-generation utilities belong in `tools/` or `scripts/`, not the everyday navigation path.
- `tools/legacy-root/` in the package may contain historical copies. Do not use it to reactivate older default profiles inadvertently.
- `config/active-reader.json` remains a **legacy direct-reader configuration**, not the source of neutral startup.

## Key fixes from October 16, 2026

1. Kept Catho in its original location.
2. Fixed opening with fresh Discovery (`skippedOversize`).
3. Showed a domain perspective first instead of `V9 state` when a derived projection is declared.
4. Fixed `relation-registry` when the graph has more than 10 types in a domain.
5. Added the `kristal-local-catalog-v10` selector and a single launcher.

These were successive changes: **use a recent full snapshot**, or apply fixes in the documented order. Do not blindly stack older patches onto a newer repository.

See [[Quick Start|Quick-Start]] and [[Testing and Qualification|Testing-and-Qualification]].

## October 17, 2026 — French semantic-display iteration

The `znapshot_Konstellation_10171209.zip` baseline received a **presentation-only** patch (`Konstellation_lecteur_v10_presentation_FR_2026-10-17.zip`). It introduced a bounded French predicate/status dictionary, clearer display of unverified hypotheses, word-aware Astrolabe ranking, diversification of identical visible titles, filtering of empty/technical facets, and less prominence for `v9:node_kind` in constellations. The v9 state and Catho corpus were not rewritten.

See [[Semantic Labels and Localization|Semantic-Labels-and-Localization]] and [[Testing and Qualification|Testing-and-Qualification]] for implemented scope and test limits.
