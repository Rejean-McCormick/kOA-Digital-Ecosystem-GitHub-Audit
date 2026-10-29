# SEC-19 — Unknown Outcome Is a First-Class State

## Core principle

Distributed side effects have an uncomfortable state: the caller timed out after sending, so the effect may or may not have happened. Treating timeout as failure and blindly retrying creates duplicate destructive effects.

## Security invariant

When an external effect cannot be proven, record `UNKNOWN`/`RECONCILING` rather than success or failure. Retry only through the same idempotent action identity or reconcile against authoritative target state.

## Senior architecture

Persist intent before delivery, use leases and idempotency keys, validate receipts, and maintain a reconciliation protocol that can query target state. Distinguish delivery status from domain effect. Operators must not edit payloads in place to “fix” uncertain actions.

## Application to the supplied ecosystem

Konfid's outbox/response model and runbook already embody this pattern. Generalize it to Runtime Pack activation, release promotion, artifact publication and any Node Agent operation that can succeed after the requester's connection disappears.

## Failure modes / anti-patterns

- HTTP timeout → immediately issue a new command.
- Mark failed because receipt was lost.
- Requeue dead-letter after manually editing payload.
- No authoritative query to discover target state.
- Restoration resumes workers before reconciling old intents.

## Evidence that proves the control

Fault injection kills workers before/after external effect and validates convergence. Reconciliation produces an audited closure. Duplicate delivery returns the same or equivalent authoritative receipt without repeating unsafe effect.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
