# SEC-15 — Transport Does Not Transfer Authority

## Core principle

Message buses, API gateways, signed envelopes and internal networks transport claims; they do not create business authority. Conflating delivery authenticity with semantic authority is a recurring distributed-system failure.

## Security invariant

Authenticated transport proves who delivered a message. The receiver still verifies schema, semantic constraints, artifact integrity, authority, replay state and local ownership before mutating state.

## Senior architecture

Layer checks explicitly: transport identity → protocol version/schema → payload/artifact validation → authorization → idempotency/replay → local state-machine admission → effect → receipt. Preserve distinct error classes so operators do not “fix” an authorization rejection as a delivery retry.

## Application to the supplied ecosystem

This aligns closely with IK's admission pipeline and the ecosystem distinction between integration, ownership and authority. Make this layering mandatory for future adapters, especially around Da’at, Kristal artifact ingestion, Koali Spaces and orchestration hooks.

## Failure modes / anti-patterns

- “Signed message = approved command.”
- Message-bus ACL replaces resource authorization.
- Gateway authentication bypasses service authorization.
- Retrying semantic rejects as transient delivery failures.
- Consumer mutates another owner's database because it received an event.

## Evidence that proves the control

Integration tests can independently trigger failures at each admission layer and produce distinct deterministic errors. Message authenticity never causes a forbidden state transition. Consumers cannot write upstream owner state.


## Reference anchors

- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
- OWASP API Security Top 10 2023: https://owasp.org/www-project-api-security/
