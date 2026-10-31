<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Compatibility-v6-v7-v8-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 545988cd479a65ebc1533d8f8c1b8d444a8ade32a82538636636bc6ae24b80cb -->

# Compatibility: v6, v7, v8 and v9

V9 is additive.

```text
v6 portable state ─┐
v7 semantic core ──┼─> preserved/frozen substrate
v8 capabilities ───┘
                     ↓
                v9 state architecture
```

## Required behavior

A v9 implementation must not silently redefine inherited semantics merely to make the new architecture easier to implement.

Stable surfaces include:

- v6 portable-state semantics and canonical identity rules;
- v7 KQ/KP/KA/KS identity semantics;
- v8 language/query/completeness boundaries;
- epistemic provenance/valuation/applicability distinctions;
- unresolved disagreement and scope.

## Adoption without rewrite

An unchanged `kristal_state/6.0` can participate as one Logical Artifact under its inherited contract.

A domain-native v9 model may also produce a v6 projection for interoperability without declaring that projection to be its richer native canon.

## Projection versus materialization

These must be distinguished:

```text
same logical contract + different physical representation
    = materialization

different logical contract/view
    = projection
```

A lossy/partial projection must not be mislabeled as a lossless materialization.

## Downgrade

A downgrade may lose v9 lifecycle/materialization capabilities, but must not rewrite semantic claims to simulate unavailable features.

Historical pages remain available: [[Compatibility-v6-v7-v8]], [[Migration-v7-to-v8]] and [[Adapters-v6-v7]].
