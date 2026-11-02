<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Operations-Observability | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: 102771b57aae44f94b44098082462aa029736821113f1e9ee065d3c1c6c04da9 -->

# Observability

Observability follows authoritative owners rather than creating a synthetic global state.

## Runtime Pack

Observe `kristal_runtime` verification, active Runtime Pack identity, activation/rollback receipts and runtime health. Observe kOA Node Agent receipts separately when a privileged host transition occurs.

## Release

Observe Release Set/channel compatibility independently from Runtime Pack verification/activation.

## Koali Spaces

Observe Space activation, runtime registration, readiness and presentation state separately from product business state and Kristal Runtime Pack state.

## Cross-system protocol

Where Interaction Kernel Profiles are adopted, observe delivery/retry/idempotency/reconciliation independently from target-domain completion. Until product/platform adoption is explicit, do not label all kOA-Linux internal interactions as IK traffic.
