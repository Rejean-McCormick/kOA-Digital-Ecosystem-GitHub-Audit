<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Security-and-Trust-Boundaries | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 62ce5eb52ed3b0dba46d2638f046d9031b75904f7d01eac386150ba523e41254 -->

# Security and Trust Boundaries

> **v9 note:** These trust boundaries remain valid. V9 adds materialization, publication and confidentiality concerns in [[Security-and-Confidentiality-v9]].


## Model is an untrusted planner

An AI can propose a typed query, projection or mutation request. It is not the final authority for privileged effects.

```text
model proposal
   ↓
schema validation
   ↓
semantic validation
   ↓
authorization / capability / budget gate
   ↓
deterministic executor
   ↓
receipt / result
```

## Prompt/context taint

Retrieved documents, web content, logs, emails, KOS text and tool outputs are data. Context items should retain provenance, trust class, tenant/scope where applicable, sensitivity classification where applicable, and retrieval reason.

Untrusted context cannot redefine system policy, tool authority or approval requirements.

## Schema valid is not enough

A valid JSON object can still reference nonexistent identities, violate semantic constraints, exceed authority scope or request unsupported operations. Implementations distinguish at least:

```text
schema reject
semantic reject
authorization / capability reject
state / admission reject
```

## Budgets and least capability

AI/federated query limits live outside the model. Child queries consume parent budget. Components should receive only the capabilities they need: a language resolver does not need canonical write authority; a context compiler does not need mutation authority.

## Logs and evidence

Operational logs help observability but are not canonical evidence unless explicitly admitted under an evidence contract.
