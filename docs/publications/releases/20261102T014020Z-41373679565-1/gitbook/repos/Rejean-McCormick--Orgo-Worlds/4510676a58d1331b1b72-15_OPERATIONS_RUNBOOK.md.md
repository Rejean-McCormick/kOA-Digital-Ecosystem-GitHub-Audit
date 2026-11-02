<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/15_OPERATIONS_RUNBOOK.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: 286ffb922de38c56674428921a4c7b4e9d3c59c3602d069d2919789eee6a899b -->

# Operations runbook

## State

Back up `runtime/orgo-worlds-state.json` together with the repository/configuration.
No operational Orgo task/case/signal tables belong to this repository.

## Validation

Run `npm run validate`. The architecture check fails if main-product operational
dependencies such as Interaction Kernel, intake or work modules are reintroduced.
