# SEC-28 — Keyless Signing and Transparency

## Core principle

Long-lived CI signing keys become high-value secrets exposed to workflow compromise. Identity-based ephemeral signing can reduce key custody risk and add an auditable transparency record.

## Security invariant

Release signatures must bind artifact digest to an authenticated workload/workflow identity and a trusted issuance context. Verification policy names the expected identity and issuer; “valid Sigstore signature” alone is too broad.

## Senior architecture

Use Sigstore/Cosign keyless signing or an equivalent internal system: CI obtains short-lived OIDC identity, ephemeral signing certificate, signs immutable digest, and records/verifies transparency evidence. For private ecosystems, use a governed private root/transparency design if public disclosure is unsuitable.

## Application to the supplied ecosystem

For container images, release metadata and selected bundles, this can complement your offline root model: the root governs which CI/workflow identities are legitimate while the release job avoids a reusable private signing key.

## Failure modes / anti-patterns

- Verification trusts any identity from the public issuer.
- Signing a mutable tag instead of digest.
- Keyless means no trust policy is needed.
- Transparency log inclusion never verified.
- Workflow identity not bound to protected branch/environment.

## Evidence that proves the control

Verification policy asserts exact issuer + workflow/repository identity + artifact digest. Signing leaves no reusable private key in CI. Release record includes signature bundle/transparency proof and can be independently verified offline where required.


## Reference anchors

- Sigstore / Cosign keyless signing: https://docs.sigstore.dev/cosign/signing/overview/
- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
- GitHub Actions — OIDC for short-lived deployment credentials: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers
