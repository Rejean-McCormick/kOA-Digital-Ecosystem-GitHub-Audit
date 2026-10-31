<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/50-operations/rollback.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 30a7c0b55d17bad512ec36262f6604df561509e6f509e93075d5f7788b26c696 -->

# Operations — Runtime Pack rollback

For kOA-Linux, `kristal_runtime` owns the last-valid/current Runtime Pack state and rollback result.

Rollback verifies that the target is valid/compatible/allowed and atomically restores the declared last valid runtime state. If a privileged host mutation is necessary, kOA Node Agent executes that narrow authorized transition.

Record the rollback through the owner component's receipt/evidence paths. Do not create a parallel Digital Ecosystem Runtime Activation State.
