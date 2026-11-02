<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Information-Layers-and-Operational-Boundaries | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: de9a333312d8002b8fe6501fa61edf11b0489822f15ca1e721987894f666651a -->

# Information Layers & Operational Boundaries

> **v9 compatibility note:** This page documents the retained v6 portable-state semantics. V9 preserves the contract as a frozen substrate and may wrap/project it through Logical Artifacts without redefining it. See [[Version-Stack-v6-v7-v8-v9]].

A useful Kristal often combines information with very different relationships to authority and change.

The most important distinction is not “structured vs unstructured”. It is **what kind of thing the record represents and who is allowed to change its meaning**.

## 1. Authoritative external constraints

Examples:

- laws and regulations;
- official government procedures;
- standards;
- manufacturer requirements;
- contractual constraints;
- regulated schedules or thresholds.

Kristal does not improve or rewrite these. It records:

- the authoritative source;
- the exact represented rule;
- its applicability;
- effective period;
- succession / supersession;
- recognition context.

Typical `record_role`: `authoritative_constraint`.

## 2. Neutral observed state

Examples:

- document received;
- payment posted;
- temperature measured;
- symptom observed;
- product label captured;
- inventory count recorded;
- workflow event occurred.

These records primarily **capture what happened**. They should not silently become policy or conclusions.

Typical `record_role`: `observed_state`.

## 3. Organizational interpretation and policy

Examples:

- escalation thresholds;
- preferred diagnostic sequence;
- internal definition of “ready”;
- review policy;
- risk tolerance;
- exception handling;
- operational prioritization.

These records reflect how an organization chooses to operate. They may be highly important without being universal facts.

Typical `record_role`: `organizational_rule`.

## 4. Derived knowledge and decisions

AI, rules or humans may derive conclusions from the three layers above.

Examples:

- this permit is applicable;
- this case is missing one required document;
- this automotive cause is strongly supported;
- this product formulation conflicts with a dietary requirement;
- this task can proceed automatically.

Typical roles include `derived_state`, `decision`, or `action`.

## Why the separation matters

```text
EXTERNAL CONSTRAINTS
        +
OBSERVED STATE
        +
ORGANIZATIONAL POLICY
        ↓
DERIVED DECISION / ACTIONABILITY
```

If these layers are collapsed, automation becomes dangerous because the system can no longer tell the difference between:

- what the law requires;
- what was observed;
- what the organization prefers;
- what a model inferred.

## Do not redesign the process by accident

Kristal's goal is not to replace an organization's existing process with a new abstract workflow.

The goal is to make the existing process **explicit enough to become action-ready**:

- deterministic checks can run automatically;
- missing information can be detected automatically;
- routing can happen automatically;
- humans receive only the ambiguity, authority, exception or judgment that actually needs them.

## Human expertise as a deliberate boundary

A healthy system asks humans for work where human expertise creates value:

- interpretation;
- ambiguity resolution;
- policy choice;
- novel cases;
- legal or organizational authority;
- negotiation;
- safety-sensitive judgment;
- exception approval.

Everything else can be progressively reduced to lower-friction machine work when policy explicitly allows it.

## Institutional learning

When a human resolves a novel case, the decision can remain a one-off decision or be promoted — through an explicit governance step — into a reusable organizational rule.

```text
novel case
   ↓
human decision
   ↓
traceable decision record
   ↓
optional policy generalization
   ↓
future matching cases may become deterministic
```

This is how Kristal improves over time without silently inventing new organizational policy.
