<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/20-nodes/daat-kristal-bridge.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: e9a64dfc997a1f8ffa09cf70327eb4a9132065aa2318563b2c45bdc83576b251 -->

# Da’at — ecosystem/IK to Kristal v6 boundary

Da’at is the anti-corruption/mapping layer between ecosystem/IK-facing interactions and Kristal-native contracts. Kristal does not parse arbitrary external envelopes directly.

## Current knowledge baseline

```text
Kristal Standard         6.0.0
Referent Registry        1.0.0
knowledge-model bundle   sha256:07fe0527ab29a4b40870efdd0c9e0c67c91de919e5428047245b2a2c04f8ea98
```

The supplied rc.3 release metadata has an unresolved commit SHA. Da’at must therefore distinguish a frozen contract baseline from an immutable published release claim. Existing downstream locks remain scope-specific until explicitly updated.

## Responsibilities

- validate the declared external/IK profile and exact contract version;
- map immutable source-owned exports/evidence into Kristal-native inputs;
- preserve source identity, provenance, referent-candidate status and epistemic labels;
- invoke Kristal-native contracts/tools;
- validate produced artifacts against the applicable contract set;
- return receipts/events with Kristal-owned ArtifactRefs;
- preserve Working/Reference status, validation/recognition metadata and Reader Policy references.

## Non-responsibilities

Da’at does not:

- make acquisition evidence epistemically valid merely by mapping it;
- add ecosystem-only fields to Kristal core schemas;
- collapse compilation, validation and recognition into one gate;
- interpret a signature as epistemic recognition;
- own physical Runtime Pack activation;
- read/write another product's live operational database as part of Kristal compilation;
- maintain bidirectional authority synchronization;
- treat derived query/projection stores as authoritative state.

See [`../40-integration/knowledge-projection.md`](../40-integration/knowledge-projection.md).

Kristal v6 actionability may guide routing, but Da’at does not execute source-owner mutations or infer authorization from `automatic`.
