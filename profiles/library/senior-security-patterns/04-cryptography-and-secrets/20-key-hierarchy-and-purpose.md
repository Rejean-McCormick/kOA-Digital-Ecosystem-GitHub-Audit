# SEC-20 — Key Hierarchy with Purpose Separation

## Core principle

A flat set of “signing keys” becomes unmanageable during compromise. Senior key management separates offline trust anchors, online intermediates, workload/service identities and purpose-specific signing keys with explicit constraints.

## Security invariant

No key may silently gain a new purpose. Root keys remain offline or hardware-protected; online keys are bounded by purpose, environment, issuer/audience or artifact class. Trust stores encode status, validity and permitted usage.

## Senior architecture

Use hierarchical trust where operationally justified: offline root → intermediate/distribution trust → short-lived workload or release credentials. Keep artifact signing, user identity signing and transport TLS keys separate. Record `key_id`, algorithm, purpose, validity and revocation state.

## Application to the supplied ecosystem

Your ecosystem key-management document already sketches root/distribution/service/test roles. Mature it by ensuring production verifiers enforce key purpose/domain, non-production keys cannot chain into production, and release/knowledge/runtime signing identities are not interchangeable.

## Failure modes / anti-patterns

- Same key signs user tokens and releases.
- Production trusts “any key in JWKS”.
- Test root imported into production for convenience.
- Root key used online for every release.
- Rotation changes key ID but not trust constraints.

## Evidence that proves the control

Automated verification rejects wrong-purpose signatures and non-production roots. HSM/KMS access policies match key purpose. Key inventory can answer which artifacts/identities depend on each key before revocation.


## Reference anchors

- NIST SP 800-63-4 Digital Identity Guidelines: https://csrc.nist.gov/pubs/sp/800/63/4/final
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- Sigstore / Cosign keyless signing: https://docs.sigstore.dev/cosign/signing/overview/
