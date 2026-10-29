# SEC-07 — Policy Decision / Enforcement Separation

## Core principle

Centralizing policy semantics can reduce drift, but centralizing execution authority creates a crown jewel. Senior designs separate decision (PDP), enforcement (PEP), identity, and privileged effectors so compromise of one does not automatically become universal execution.

## Security invariant

The policy authority decides; the enforcement point owns the local resource transition. A PDP response is bounded, validated, attributable and short-lived. The PEP rejects malformed, stale, unknown or policy-incompatible decisions.

## Senior architecture

Use typed decision schemas with `decision`, policy/version, obligations, validity and reason codes. PEPs enforce local invariants even after an ALLOW. For critical operations, include resource version/preconditions to prevent TOCTOU between decision and effect.

## Application to the supplied ecosystem

Konfid's production Policy Runtime and local enforcement adapters already point in this direction. Make local PEP invariants explicit for Runtime Pack activation, release promotion, account/grant changes and Node Agent operations; a global policy ALLOW must not bypass local state-machine validity.

## Failure modes / anti-patterns

- Policy engine directly owns production credentials for all targets.
- PEP treats unknown decision as allow.
- Long-lived cached ALLOW with no invalidation semantics.
- Policy says “allow delete” but does not bind target/version.
- Local code duplicates policy logic inconsistently.

## Evidence that proves the control

Policy outage and malformed-response tests fail according to action class. PEP tests prove local invariants remain enforced under ALLOW. Decision receipts include version and expiry. TOCTOU tests change target state after decision and expect safe rejection/re-evaluation.


## Reference anchors

- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
- NIST SP 800-207A Cloud-Native Zero Trust: https://csrc.nist.gov/pubs/sp/800/207/a/final
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
