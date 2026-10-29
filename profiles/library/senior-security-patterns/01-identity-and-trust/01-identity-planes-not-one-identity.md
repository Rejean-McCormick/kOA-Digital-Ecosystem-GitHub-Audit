# SEC-01 — Separate Identity Planes

## Core principle

A principal is not a single string. Senior systems separate at least: human identity, authenticated session, calling workload, delegated actor, tenant, device/workload attestation, and effective authorization context. Collapsing these planes creates implicit privilege transfer.

## Security invariant

Every security-sensitive decision MUST be able to answer independently: who is the human actor, which workload made the call, for which tenant, under which delegation, with what assurance, and which local policy produced the effective authority. Missing planes are not inferred from another plane.

## Senior architecture

Use independent credentials or cryptographically bound claims for workload and human actor. Keep application sessions local. Carry explicit `actor`, `caller_service`, `tenant`, `delegation`, `auth_time`, and assurance metadata only where needed; do not let application JSON self-assert assurance. Authorization consumes these identities but does not redefine them.

## Application to the supplied ecosystem

This matches Konfid's split between workload JWT and actor assertion, the ecosystem's rule that IdP identity does not imply application roles, and IK's receiver-side admission. Extend the same distinction to Node Agent and release automation: CI identity, release approver identity, signer identity and runtime activator identity should remain separately attributable.

## Failure modes / anti-patterns

- Treating email as canonical identity.
- Passing a human access token as a service credential.
- Assuming a service account implies the human who triggered it.
- Copying roles across products because SSO is shared.
- Letting `tenant` or `assurance` arrive as unsigned business fields.

## Evidence that proves the control

Tests prove cross-tenant mismatch rejection and actor/caller mismatch rejection. Audit records preserve both actor and caller. Tokens show bounded audiences. Policy decisions can be replayed from captured identity inputs without consulting mutable UI session state.


## Reference anchors

- NIST SP 800-63-4 Digital Identity Guidelines: https://csrc.nist.gov/pubs/sp/800/63/4/final
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
- RFC 8693 — OAuth 2.0 Token Exchange: https://www.rfc-editor.org/info/rfc8693/
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
