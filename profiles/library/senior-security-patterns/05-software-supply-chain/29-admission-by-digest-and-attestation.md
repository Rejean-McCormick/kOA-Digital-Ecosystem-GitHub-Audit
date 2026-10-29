# SEC-29 — Admission by Digest and Attestation

## Core principle

Scanning in CI is advisory if the runtime can deploy something else. The decisive control is admission: only immutable artifacts satisfying provenance/signature/policy are allowed to become active.

## Security invariant

Production activation MUST resolve to immutable digests and verify required attestations at the trust boundary where activation occurs. Missing/invalid evidence fails closed for the specific activation transition.

## Senior architecture

Admission policy can require signer/workflow identity, source repository/ref, vulnerability policy, SBOM/provenance, build level and environment constraints. Separate “published” from “eligible” from “active”. Keep last-known-good state intact on verification failure.

## Application to the supplied ecosystem

This maps naturally to kOA-Linux release channels and `kristal_runtime` activation: a Release Set or Runtime Pack can be present but not activatable until digest, provenance, trust and compatibility gates pass. Node Agent should execute only an already-admitted immutable candidate.

## Failure modes / anti-patterns

- Deploying `:latest` or mutable tags.
- Verifying signature in CI, not at cluster/activation boundary.
- Admission policy can be bypassed by privileged manual kubectl.
- Publication success interpreted as activation permission.
- Rollback artifact no longer satisfies current trust policy with no defined exception process.

## Evidence that proves the control

Runtime inventory reports exact digest and attestation identities. Attempted deployment of unsigned/wrong-builder artifact is rejected by admission. Break-glass bypass, if allowed, is explicit, time-bound and audited.


## Reference anchors

- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
- Sigstore / Cosign keyless signing: https://docs.sigstore.dev/cosign/signing/overview/
- Kubernetes Security and Application Security Checklist: https://kubernetes.io/docs/concepts/security/application-security-checklist/
