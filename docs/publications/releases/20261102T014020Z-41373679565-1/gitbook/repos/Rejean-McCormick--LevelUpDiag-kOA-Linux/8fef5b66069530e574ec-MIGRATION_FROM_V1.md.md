<!-- Frozen source: https://github.com/Rejean-McCormick/LevelUpDiag-kOA-Linux/blob/5a7d7c51dbbb9591c153323a6f7ab3248c36f2f5/docs/MIGRATION_FROM_V1.md | commit: 5a7d7c51dbbb9591c153323a6f7ab3248c36f2f5 | SHA-256: f322541d47fea81a45bb2b11fc1371d289f7dbc129adf130c6f7c44ad575365c -->

# Migration notes — v2.1 debug-first policy

Version 2.1 retains N00-N11 and the existing Koali validators but changes orchestration semantics.

Key changes:

1. `debug` is the default campaign and mode.
2. N02 Repository/Structure and N03 Documentation are removed from the primary debug campaign.
3. N04-N10 no longer depend transitively on N02.
4. DEBUG has no dependency-blocking verdict set: independent evidence continues to be collected.
5. DEBUG does not snapshot or compare tracked Git state.
6. VALIDATION keeps conformance checks and strict dependency semantics without global Git cleanliness enforcement.
7. RELEASE keeps strict tracked-state protection and delivery/finalization checks.
8. Campaign summaries separate diagnostic execution, testability, and conformance.

Historical campaign names remain available for compatibility, but new automation should use `debug`, `structure`, `validation`, or `release` explicitly.
