<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/1-Overview/Operations-Rollbacks.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: d26d872b31acdd51b29f4dcb453743125e67e120946840af6889188b18a554e9 -->

# Rollbacks

Rollback is owned by the component/runtime whose authoritative active state is being restored.

## Kristal Runtime Pack rollback on kOA-Linux

`kristal_runtime` owns the last-valid/current Runtime Pack state and rollback result. It validates the rollback target and restores the declared last valid runtime state atomically according to its contract.

If the transition requires privileged node-local work, kOA Node Agent performs only the narrow authorized host operation. The Node Agent does not become the owner of Kristal epistemic semantics or release authority.

## Koali Space rollback

Koali Space rollback restores presentation/Space configuration and is a separate lifecycle. It must not be represented as a Runtime Pack rollback.
