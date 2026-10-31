<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/adrs/ADR-IK-03-decision-record.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: 7e08fceb8b1be6c999aba0e8933629d98af5b8970b1972d7449fc5674809c9a0 -->

# ADR-IK-03 — DecisionRecord handoff

**Status:** Accepted

`DecisionRecord` is the immutable/read-model canonical handoff contract from Konnaxion to Orgo. Decision publication does not itself imply execution; the `governance.decision.execute` Profile plus governance authority claim makes execution intent explicit.
