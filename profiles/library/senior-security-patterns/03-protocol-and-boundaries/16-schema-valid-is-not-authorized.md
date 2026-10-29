# SEC-16 — Schema Validity Is Not Semantic Safety

## Core principle

A perfectly schema-valid request can still be malicious, unauthorized, stale, contradictory or dangerous. Mature protocols keep syntactic validity, semantic validity, authority, and state transition admissibility as separate judgments.

## Security invariant

Schema validation MUST run early but MUST NOT be used as evidence of trust, ownership, authorization or business-state validity. Sensitive enumerations and invariants are additionally checked against receiver-owned state and policy.

## Senior architecture

Use strict schemas (`additionalProperties: false` where appropriate), bounded collections/strings and versioned contracts, then run semantic validators and authorization. For extensibility fields, define namespacing and size/shape limits instead of accepting arbitrary JSON blobs into privileged flows.

## Application to the supplied ecosystem

IK already distinguishes contract validation from authority and idempotency. Apply the same to Kristal artifact roles, Release Set activation and Konfid response proposals: “conforms to schema” must not be confused with “may become active”.

## Failure modes / anti-patterns

- Pydantic/JSON Schema success treated as security approval.
- Unknown fields persisted for forward compatibility in privileged models.
- Enum/string values forwarded directly into shell/cloud operations.
- Oversized nested JSON causing parser or policy DoS.
- Schema version accepted but semantic profile unsupported.

## Evidence that proves the control

Fuzzing proves bounded parsing. Unknown/extension fields cannot influence privileged behavior unless explicitly recognized. Security tests distinguish schema-reject, semantic-reject, auth-reject and state-transition-reject paths.


## Reference anchors

- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
- OWASP API Security Top 10 2023: https://owasp.org/www-project-api-security/
