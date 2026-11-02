<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/20-nodes/malkuth-runtime.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: e18a7b924a574f6c4fe168d2e5a14f0a534493b78489aec9e8a8ad1ee2eb8cfe -->

# Malkuth — runtime query and serving role

Malkuth is a conceptual runtime-consumption role, not an ownership grant.

## Responsibilities

- query/serve the active Runtime Pack through its Query Contract;
- apply Reader Policy;
- preserve source/validation/recognition/valuation labels;
- expose deterministic query errors and bounded behavior.

## kOA-Linux mapping

On kOA-Linux, `kristal_runtime` owns the active Runtime Pack record and runtime health. If a privileged host transition is needed, kOA Node Agent performs that narrow operation. Malkuth-like consumers observe/use the active selection; they do not create another activation authority.
