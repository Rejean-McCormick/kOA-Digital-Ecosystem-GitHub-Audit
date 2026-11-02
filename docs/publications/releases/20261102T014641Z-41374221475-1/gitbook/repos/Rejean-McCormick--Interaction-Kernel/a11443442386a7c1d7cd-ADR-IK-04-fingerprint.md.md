<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/adrs/ADR-IK-04-fingerprint.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: 57e08d3f48b84107e78f69d2d251c7dd36cdd5c63590a33c6781aa5228e57db2 -->

# ADR-IK-04 — Canonical reliable fingerprint

**Status:** Accepted

Fingerprint = SHA-256 over RFC 8785 JCS of the semantic request projection. The projection excludes volatile transport/trace/correlation/time fields. Python and TypeScript must match TCK golden vectors exactly.
