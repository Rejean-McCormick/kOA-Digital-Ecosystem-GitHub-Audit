# SEC-40 — Logs Are Not Authoritative Evidence

## Core principle

Application logs optimize diagnosis; authoritative security evidence must survive compromise, retries, clock quirks and operator mistakes. Treating logs as audit records lets the same compromised process rewrite the story.

## Security invariant

Security decisions and privileged effects SHOULD emit structured evidence to a separately governed audit path. Logs may reference decision/action IDs but are not the sole proof of who authorized or what executed.

## Senior architecture

Record minimal canonical audit events atomically with local state where needed, then export to an authoritative broker/store controlled by a different role. Include actor/caller, tenant, operation, target, decision/policy identity, semantic digest, outcome/receipt and timestamps.

## Application to the supplied ecosystem

Konfid already distinguishes local chained journal from authoritative kOA Audit Broker and explicitly says logs are not authoritative audit. This should become the ecosystem norm for release promotion, Runtime Pack activation, key use and privileged Node Agent actions.

## Failure modes / anti-patterns

- Parsing text logs to reconstruct approvals.
- Same admin can perform action and delete audit.
- Audit emitted only after side effect, so crash loses it.
- Storing secrets/full payloads in evidence.
- Assuming centralized log platform is immutable by default.

## Evidence that proves the control

State mutation and local evidence stay consistent under crash tests. Audit Broker copy survives app/DB compromise within threat model. A privileged action can be reconstructed without relying on free-form logs.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
