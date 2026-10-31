<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/1-Overview/Components-Konnaxion-and-Malkuth.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: ad885a99c759ee6aad3e12e10d45ae670d0fd01aea4651cc59407c5d3cb6a942 -->

# Konnaxion and runtime application

Konnaxion owns civic/public state, deliberation, consultations, readings, DecisionRecords and related product state.

“Malkuth” remains a conceptual runtime/application role only; it is not an activation authority by itself.

## Konnaxion boundaries

- Konnaxion can own desired/application selection for knowledge or product experiences.
- It does not automatically own Runtime Pack verification or active Runtime Pack state.
- It does not acquire Orgo workflow state or Kristal epistemic authority through integration.

## kOA-Linux Runtime Pack state

In the current kOA-Linux contracts:

- `kristal_runtime` owns Runtime Pack verification/compatibility and active-state records;
- `kristal_runtime` emits activation/rollback receipts and owns runtime health;
- kOA Node Agent performs narrow privileged node-local transitions when required;
- Release Set/channel compatibility belongs to kOA-Linux platform contracts.

Runtime Pack active state is owned by `kristal_runtime`; Konnaxion does not own platform activation state.
