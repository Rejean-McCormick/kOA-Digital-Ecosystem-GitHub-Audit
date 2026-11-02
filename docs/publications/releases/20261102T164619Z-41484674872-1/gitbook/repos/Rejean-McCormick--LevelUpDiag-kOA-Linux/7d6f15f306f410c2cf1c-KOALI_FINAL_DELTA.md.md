<!-- Frozen source: https://github.com/Rejean-McCormick/LevelUpDiag-kOA-Linux/blob/5a7d7c51dbbb9591c153323a6f7ab3248c36f2f5/docs/KOALI_FINAL_DELTA.md | commit: 5a7d7c51dbbb9591c153323a6f7ab3248c36f2f5 | SHA-256: 5470e62edbb322ccdd2e7142b7132eff0a5602cd82ae199538eb35ecb371637a -->

# N14 — Koali Final Integration Delta

N14 is a read-only diagnostic for the parts of the finalized Koali integration that are not established by already-green component suites.

It verifies catalog topology, web/headless owner roles, required source authorities, Kristal reference-only policy, absence of Diag products, bootstrap contract/evidence, launcher files/ports, and Médiathèque sibling-instance persistence.

A successful `CHECK_KOALI.cmd` alone is not accepted as final bootstrap evidence: N14 requires a real bootstrap status with `checkOnly=false` and all required events `ready`.
