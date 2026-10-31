<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Actionability-and-Human-Boundaries | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: a6f1a07b7d84b8c7556fba9418b6b1b5dfe9e49357b3a67ffd4e91e401064084 -->

# Actionability & Human Boundaries

> **v9 compatibility note:** This page documents the retained v6 portable-state semantics. V9 preserves the contract as a frozen substrate and may wrap/project it through Logical Artifacts without redefining it. See [[Version-Stack-v6-v7-v8-v9]].

Kristal v6 can represent **whether an action is ready for automation or requires a human**, while keeping execution authority outside the knowledge artifact.

## Typical modes

A profile may distinguish modes such as:

- `automatic`;
- `human_review`;
- `human_decision`;
- `manual`;
- `prohibited`;
- `insufficient_information`;
- `not_applicable`.

## The critical invariant

```text
actionability = automatic
≠ permission to mutate another system
```

`automatic` means that, according to the represented knowledge/policy, no human judgment is required before the action path can be attempted.

The target system still decides whether the caller is authorized and whether the request is admissible.

## Operational pattern

```text
Kristal State
   ↓ actionability
routing / orchestration
   ↓
explicit owner contract
   ↓
authority + admission check
   ↓
owner-local mutation
   ↓
receipt / observation / decision
   ↓
new Kristal evidence/state
```

## Why this matters

The goal is not to redesign an organization's processes. It is to make the existing process explicit enough that deterministic work can be automated with minimal friction.

Humans are then reserved for:

- ambiguity;
- interpretation;
- legal/organizational authority;
- exceptions;
- negotiation;
- safety-sensitive judgment;
- novel cases;
- policy changes.

A human decision can itself become a traceable decision record and, when appropriate, later be generalized into a new organizational rule. That is how the system improves over time without silently learning rules that nobody approved.
