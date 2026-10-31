<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/kristal-v6/index.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 1564453be479e3b9c34132c5d3cd18e856a7f8bbd9ee7bd281b2581a05f974aa -->

# Kristal v6 integration

**External normative authority:** Kristal Standard 6.0.0

The active knowledge boundary uses `kristal_state` as the canonical structured artifact. Kristal v6 generalizes historically epistemic field names into typed valuations, coordinates, applicability, data roles and actionability while retaining atomic assertions, provenance/evidence, validation/recognition, conflicts, supersession, lineage and deterministic content identity.

## Ecosystem-specific invariants

- product-owned mutable state enters Kristal only through explicit immutable snapshots/artifacts;
- `record_role` describes the data's role, not ownership;
- `actionability` describes the human/automation boundary, not execution authority;
- `automatic` actions cross the same explicit contract/admission path as any other owner mutation;
- measurements/valuations and policy thresholds remain separate;
- projections remain rebuildable and non-authoritative.

See [`pinned-dependency.md`](./pinned-dependency.md), [`conformance.md`](./conformance.md), [`koa-profile.md`](./koa-profile.md), and [`../knowledge-projection.md`](../knowledge-projection.md).
