# SEC-02 — Workload Identity by Trust Domain

## Core principle

Long-lived service secrets are an implementation shortcut, not an identity architecture. Mature service-to-service security uses short-lived workload identities rooted in a defined trust domain and issued from attested workload state.

## Security invariant

A workload MUST obtain authority because it is an admitted workload in a trust domain, not because a static secret exists on disk. Identity must be rotatable without rebuilding the application and scoped to the workload instance or role.

## Senior architecture

Prefer workload federation, SPIFFE/SVID-like identities, or cloud workload identity. Establish explicit trust domains and federation edges. Keep issuance separate from authorization: possession of an SVID proves workload identity; the receiving service still decides whether that identity may perform the requested operation.

## Application to the supplied ecosystem

Konfid already models service identity independently from actor identity. The next maturity step is replacing bearer integration secrets where feasible with workload identity or mTLS-bound credentials for Policy Runtime, Audit Broker, IK and privileged agents. Trust-domain boundaries should align with kOA platform authority rather than repository names.

## Failure modes / anti-patterns

- Shared API keys between replicas or services.
- One cluster-wide service identity.
- Treating mTLS as authorization.
- Automatically federating every trust domain.
- Reusing the same identity across production and non-production.

## Evidence that proves the control

Identity issuance logs show workload selectors/attestation and TTL. Receiver policy names exact workload identities or classes. Rotation can happen without application rebuild. A stolen old credential expires quickly and cannot authenticate from an untrusted trust domain.


## Reference anchors

- SPIFFE Workload Identity / SVID: https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/
- NIST SP 800-207A Cloud-Native Zero Trust: https://csrc.nist.gov/pubs/sp/800/207/a/final
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
