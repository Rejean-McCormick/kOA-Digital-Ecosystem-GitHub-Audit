<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/adrs/ADR-IK-01-runtime-pack-activation-owner.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: 4d9387d959df2bbb0df4873167ef04e988137e2e1c8043aeb49bad966ecd087f -->

# ADR-IK-01 — Runtime Pack activation owner

**Status:** Accepted

Konnaxion owns desired/application selection. When kOA-Linux is present, kOA-Linux owns physical verify/stage/activate/rollback state through `RuntimePackActivationPort`. Standalone Konnaxion may supply its own implementation. There must be exactly one authoritative activation state per deployment.
