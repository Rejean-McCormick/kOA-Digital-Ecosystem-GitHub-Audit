# SEC-22 — Rotation and Revocation Are Protocols

## Core principle

Generating a new key is easy; changing trust safely across distributed verifiers is the hard part. Rotation is a multi-phase protocol with overlap, propagation evidence, rollback and revocation semantics.

## Security invariant

A key change MUST define states such as pending/active/deprecated/revoked, accepted overlap, propagation completion and failure behavior. Revocation latency is a security SLO.

## Senior architecture

Publish new trust before first use, observe verification, then switch signers, then retire old trust. For emergency compromise, support immediate deny even if that breaks availability. Keep key status and trust bundle versions observable at every verifier.

## Application to the supplied ecosystem

This directly extends the kOA key-management model. Add automated trust-store convergence checks across Konnaxion, `kristal_runtime`, Konfid and any release/admission service so rotation is not “done” until verifiers prove the expected trust set.

## Failure modes / anti-patterns

- Rotating signer before consumers trust it.
- Keeping old key indefinitely “for rollback”.
- Revocation published but caches ignore it.
- No inventory of active artifacts signed by compromised key.
- Trust store edited manually on each node.

## Evidence that proves the control

Rotation drill succeeds without downtime under normal conditions. Emergency revocation blocks new activation within the defined SLO. Verifiers expose trust-bundle version/status. Historical artifacts remain auditable without remaining activatable if policy forbids them.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- Sigstore / Cosign keyless signing: https://docs.sigstore.dev/cosign/signing/overview/
- NIST SP 800-63-4 Digital Identity Guidelines: https://csrc.nist.gov/pubs/sp/800/63/4/final
