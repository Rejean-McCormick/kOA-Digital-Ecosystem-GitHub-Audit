# SEC-04 — Explicit Delegation and Actor Chains

## Core principle

Delegation is not impersonation by convention. A system needs to know both the subject whose authority is being exercised and the actor actually exercising it; otherwise delegated workflows become invisible privilege escalation.

## Security invariant

Delegated authority MUST be explicit, narrower than or equal to the delegator's effective authority, time-bounded, target-bounded, and attributable to an actor chain. Re-delegation is denied unless explicitly permitted.

## Senior architecture

Represent delegation as a first-class artifact or token semantics, not an overloaded role string. Bind it to subject, actor, tenant, allowed operations/resources, constraints, validity and delegation source. Preserve the actor chain across service boundaries and audit it at the enforcement point.

## Application to the supplied ecosystem

This fits Konfid's Delegation model and IK authority envelopes. A Konnaxion or Orgo workflow should never erase the difference between “P123 is allowed” and “svc:orgo-prod acted for P123 under delegation D42”. Node Agent receipts should capture the requesting authority chain, not only the node-local service identity.

## Failure modes / anti-patterns

- "Run as user" without an auditable delegation object.
- Delegation that copies all current and future permissions.
- Nested delegation with no depth or scope limits.
- Losing actor information during token exchange.
- Treating approval as delegation to execute anything.

## Evidence that proves the control

A verifier can reconstruct the delegation chain from immutable references. Revoking the delegation blocks new actions. Tests prove no privilege amplification through delegation. Audit queries can answer “who actually initiated this effect?” even across service hops.


## Reference anchors

- RFC 8693 — OAuth 2.0 Token Exchange: https://www.rfc-editor.org/info/rfc8693/
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
