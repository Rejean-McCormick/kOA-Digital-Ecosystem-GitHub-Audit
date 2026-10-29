# SEC-33 — Release Set as a Security Object

## Core principle

In a multi-repository ecosystem, secure components can combine into an insecure release. Compatibility, policy, schema, key and protocol versions form a security-relevant configuration that should be promoted atomically as a tested set.

## Security invariant

Production promotion SHOULD reference an immutable release set describing exact component/artifact digests and security-relevant compatibility. “Latest compatible” resolution is not performed during activation.

## Senior architecture

Create a signed/attested manifest containing component versions/digests, policy bundle, schema/contract set, trust config version, migrations, Runtime Pack/knowledge artifacts and rollback set. Qualify the set in staging/canary, then promote the manifest identity.

## Application to the supplied ecosystem

kOA-Linux already models Release Sets across channels. Treat that Release Set as a high-value security artifact: verify not only component compatibility but security contract compatibility—issuer/audience changes, policy schema, trust roots, receipt formats, migration head and revocation expectations.

## Failure modes / anti-patterns

- Independent services auto-upgrade to latest.
- Rollback only one component into incompatible auth/policy protocol.
- Trust-store update not tied to release set.
- Database migration cannot be reconciled with previous policy semantics.
- “Compatible” means starts successfully, not security-contract compatible.

## Evidence that proves the control

A running environment can emit its release-set digest and constituent digests. Rollback rehearsal uses a defined compatible set. Contract tests include identity/policy/audit compatibility, not only API shape.


## Reference anchors

- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
- NIST SP 800-218 SSDF 1.1 (final): https://csrc.nist.gov/pubs/sp/800/218/final
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
