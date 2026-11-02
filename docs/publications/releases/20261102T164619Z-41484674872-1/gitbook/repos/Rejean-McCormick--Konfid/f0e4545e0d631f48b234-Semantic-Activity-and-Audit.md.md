<!-- Frozen source: https://github.com/Rejean-McCormick/Konfid/wiki/Semantic-Activity-and-Audit | commit: e707adff40a4b9a660647bec302236caf6d6edf6 | SHA-256: ac9ca9cc128f946a9243cc1607ebb474fa40da4ce247ff5ea0f0cf86514d3129 -->

# Semantic Activity, Minimization, and Audit

Konfid tracks **security-relevant actions** rather than systematically copying application content.

## Semantic event

```text
actor=P123
service=konnaxion
action=employee.export
resource_class=HR_RECORD_SET
scope=organisation-ABC
decision=DENY
policy=POL-17
correlation=C-8821
```

This event explains what happened without including the HR record itself.

## Why this matters for privacy

Traditional technical logs may accidentally contain:

- full payloads;
- sensitive query strings;
- tokens;
- serialized objects;
- messages;
- form data.

Konfid prefers an explicit schema that permits only the fields required for security.

This reduces the likelihood that the audit system becomes a second copy of sensitive data.

## What must be auditable

Examples:

- identity binding or revocation;
- role/grant change;
- delegation;
- decision on a protected operation;
- export;
- privileged action;
- policy change;
- detector change;
- break-glass;
- approval;
- containment;
- final receipt.

## What must not be copied by default

- full document content;
- email body;
- medical record;
- password;
- bearer token;
- secrets;
- keystrokes;
- data with no security purpose.

## Claim Check for sensitive evidence

When content is required for an investigation, it can remain in a protected store:

```text
Evidence Store
  evidence/9282
       │
       ├─ access policy
       ├─ retention
       └─ digest
             │
             ▼
Audit Event
  evidence_ref=...
  digest=...
```

The log can therefore establish provenance and integrity without copying the evidence.

## Correlation without centralizing content

```text
Login              C-8821
Access request      C-8821
Policy decision     C-8821
Approval            C-8821
Response command    C-8821
Receipt             C-8821
```

The same `correlation_id` makes it possible to reconstruct the history of an action without moving the same sensitive content from one system to another.

## Audit ≠ surveillance

The objective is:

> **to explain and prove sensitive decisions using the minimum collection necessary.**

It is not:

> recording all user behavior simply because it is technically possible.

## Audit ≠ telemetry

Detection telemetry may be high-volume, aggregated, and retained for a short period.

Audit evidence is smaller, controlled, and designed for accountability.

This separation protects both performance and privacy.
