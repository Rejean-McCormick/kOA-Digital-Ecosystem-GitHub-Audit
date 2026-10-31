<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Automation-and-Organizational-Memory | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 236f848267fe429d0b0bed424728ed16260086a946350b6a5058acebda6f028c -->

# Automation & Organizational Memory

> **v9 compatibility note:** This page documents the retained v6 portable-state semantics. V9 preserves the contract as a frozen substrate and may wrap/project it through Logical Artifacts without redefining it. See [[Version-Stack-v6-v7-v8-v9]].

Kristal is designed to capitalize work done by both people and AI.

## Without persistent structured memory

```text
AI researches
  ↓
answer is produced
  ↓
next task starts again
```

## With Kristal

```text
AI or human work
  ↓
assertions + evidence + applicability + valuations
  ↓
Kristal State
  ↓
validation / corrections / new observations
  ↓
updated state
  ↓
next agent inherits previous work
```

## Progressive reduction of friction

The first occurrence of an unusual case may require a human decision. If the organization later decides that the same decision should apply whenever explicit conditions X/Y/Z hold, that judgment can be represented as an organizational rule.

Future cases matching X/Y/Z may then become automatically actionable.

This is not “the AI silently learned what to do”. It is **explicit institutional learning** with provenance, scope and authority.

## Knowledge / policy / state / decision / action

A healthy architecture keeps these separate:

```text
KNOWLEDGE    what is represented
POLICY       how the organization wants to act
STATE        what is currently observed
DECISION     application of knowledge + policy to state
ACTION       execution by an authorized owner
```

Kristal can preserve all five as traceable records without turning them into one undifferentiated workflow state.

The same principle applies to **external constraints, observed state and organizational rules**: they can contribute to one decision while retaining different authority and change boundaries. See [[Information-Layers-and-Operational-Boundaries]].

Because Kristal semantics are portable across storage forms, this accumulated memory does not need to live in one monolithic database. Graph, relational, document and analytical projections may coexist when they preserve the canonical semantic boundaries. See [[Universal-Structure-and-Transposition]].
