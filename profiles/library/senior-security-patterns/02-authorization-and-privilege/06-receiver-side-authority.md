# SEC-06 — Receiver-Side Authority Is Final

## Core principle

A sender may carry claims, evidence and requested authority, but the receiving trust domain owns the final decision. Cross-system protocols that treat a sender's role claim as executable authority create transitive trust and confused-deputy failures.

## Security invariant

Every receiver MUST authenticate the caller, validate the request, authorize locally against its own resource semantics, and admit the operation. Upstream `allowed=true`, role names or approval statements are evidence, not local authority.

## Senior architecture

Separate transport authentication, contract validation, policy evaluation and execution admission. Allow an upstream system to provide signed evidence or approval receipts, then revalidate issuer, scope, freshness, digest, quorum and local policy at the receiver.

## Application to the supplied ecosystem

This is already a strong ecosystem principle: IK admission is local, Orgo coordinates workflows but Konfid revalidates approval semantics, and Node Agent does not inherit release authority. Codify it as a universal invariant across every new integration.

## Failure modes / anti-patterns

- Trusting upstream HTTP 200 as authorization.
- Shared global role table across products.
- “Internal network” bypass routes.
- Admin UI calling an undocumented privileged endpoint.
- Downstream executor unable to explain why it accepted authority.

## Evidence that proves the control

Contract tests send forged upstream approval/role claims and observe local rejection. Every privileged receipt points to a local decision/policy version. No endpoint can execute privileged state transitions solely because an upstream component is trusted.


## Reference anchors

- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
- NIST SP 800-207A Cloud-Native Zero Trust: https://csrc.nist.gov/pubs/sp/800/207/a/final
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
- OWASP API Security Top 10 2023: https://owasp.org/www-project-api-security/
