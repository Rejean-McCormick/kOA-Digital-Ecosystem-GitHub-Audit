<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/orgo-konnaxion/index.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 4b2458f7a45bfce57e8a3d721c353942ccc62b06632db54c98b2ed1afe95802e -->

# Konnaxion/eThikos ↔ Orgo — decision execution and durable impact publication

**Current state:** qualified in integrated local runtime for two explicit Interaction Kernel profiles.

## Ownership

```text
Konnaxion / eThikos
    owns deliberation + finalized DecisionRecord

Orgo
    owns Signal + WorkflowVersion + Case + Task + IntegrationOperation + outbox

Konnaxion
    owns accepted civic/accountability impact state
```

No shared mutable database is required or permitted by this mapping.

## Profile 1 — decision execution

```text
governance.decision.execute/1.0.0
```

Flow:

```text
Konnaxion finalized DecisionRecord
    → authenticated/versioned IK envelope
    → Orgo validates scope + replay identity
    → Signal persisted/deduplicated
    → WorkflowVersion evaluation
    → Case / Tasks
```

Konnaxion does not write Orgo tables. Orgo does not query Konnaxion tables as a substitute for the handoff.

## Profile 2 — durable impact publication

```text
accountability.impact.publish/1.0.0
```

Flow:

```text
Orgo work / operational observation
    → IntegrationOperation
    → transactional outbox
    → provider delivery
    → terminal receipt
    → Konnaxion-owned impact/accountability state
```

## Receipt semantics

```text
accepted  = durable non-terminal acceptance
succeeded = terminal success
```

Orgo must not mark the business operation succeeded until a terminal success state is established.

## Replay semantics

- same business idempotency key + same payload → idempotent replay;
- same idempotency key + divergent payload → reject/fail closed;
- retries/redrive reuse the original business identity rather than creating duplicate effects.

## UCKK relationship

UCKK may independently publish, display or teach a Konnaxion decision. It is not a mandatory relay between Konnaxion and Orgo and does not become owner of the civic decision merely by presenting it.

## Qualification scope

The integrated local qualification demonstrated:

- DecisionRecord delivery into Orgo;
- Signal → Workflow → Case → Task execution;
- durable impact publication back to Konnaxion;
- owner-local mutation only;
- idempotent replay;
- divergent replay rejection.

This establishes the boundary for the tested profiles. It is not, by itself, a claim of production-environment qualification.
