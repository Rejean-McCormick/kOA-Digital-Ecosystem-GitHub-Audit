<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/09_INFRASTRUCTURE_SCOPING.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: 444e0e804e103472a69687eb743df2e929143aa862a3c4044980cbbea1efdbb9 -->

# Infrastructure scoping

The standalone repository is intentionally lightweight. Its runtime state is
`runtime/orgo-worlds-state.json` unless a future explicit control-plane storage
backend replaces it. It does not require the main Orgo PostgreSQL/Prisma schema,
worker, outbox or provider adapters.

Main Orgo infrastructure remains owned and operated by the `Orgo` repository.
