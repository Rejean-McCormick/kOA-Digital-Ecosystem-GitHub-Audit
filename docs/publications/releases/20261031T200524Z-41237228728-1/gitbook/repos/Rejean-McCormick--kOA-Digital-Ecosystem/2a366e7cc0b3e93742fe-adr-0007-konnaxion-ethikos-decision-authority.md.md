<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/90-reference/adr/adr-0007-konnaxion-ethikos-decision-authority.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 2c2daf53bda86a8106856cf4d5ffa58ab5192610e1635fcb898bb92bcd2fab6d -->

# ADR-0007 — Konnaxion/eThikos owns civic decision finalization and direct Orgo handoff

**Status:** Accepted

## Decision

For Konnaxion-owned civic/public decisions:

```text
Konnaxion / eThikos deliberation
→ readings (Smart Vote / EkoH / other lenses)
→ eThikos decision stage
→ finalized DecisionRecord
→ direct Konnaxion → Orgo machine handoff
→ Orgo Signal / Workflow / Case / Tasks
```

The finalized eThikos DecisionRecord is the authoritative source event for the Orgo handoff.

UCKK may independently consume the decision for publication, learning or presentation, but it is not the mandatory relay or decision authority for this path. Smart Vote/EkoH outputs remain readings unless an explicit decision contract says otherwise.

## Boundary rules

- Konnaxion/eThikos owns civic decision state and finalized DecisionRecords.
- Orgo owns Signal/WorkflowVersion/Case/Task operational state.
- the handoff is authenticated, versioned and idempotent.
- Konnaxion does not write Orgo tables directly.
- Orgo does not become owner of the civic decision.
- Orgo→Konnaxion durable impact publication uses IntegrationOperation + outbox + terminal receipt semantics.
- UCKK publication is optional and independent.

## Related documents

- `../../40-integration/orgo-konnaxion/index.md`
- `../../../3-Layer-Model/layers/07_decision_legitimacy.md`
- `../../../3-Layer-Model/layers/08_execution.md`
