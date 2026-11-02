<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Security-and-Confidentiality-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 2a11690bd9d2e13f471a56b87fa806430738e60a89342374aba26cb0acab2704 -->

# Security, Confidentiality & Host Trust — v10

The hosted-network layer introduces disclosure and execution risks without redefining epistemic trust.

## Required separation

- **No reusable secrets in Host Bindings.** Use least-privilege credentials for the actual host operation.
- **No private-node leakage** through a public directory, README, profile, receipt or attestation by default.
- **Visibility is not cryptographic confidentiality.** A public mirror of private knowledge requires an explicit policy decision.
- **Host attestations are not epistemic authority** and automation is not authorization.
- **Fail closed** when a required protection is unavailable; do not market a best-effort feature as required protection.
- **Constrain untrusted workflow inputs**: resolve paths within the workspace, reject traversals/symlink escapes for privileged publication paths, avoid interpolating paths as shell code.
- **Pin managed workflow dependencies** (third-party Actions and the Framework) to immutable SHAs; update through reviewed changes.

## Operator checklist

1. Decide node/collection visibility and directory disclosure separately.
2. Keep the all-node registry private where both public and confidential nodes exist.
3. Verify exact State Commitments and publication resource digests, not just host status flags.
4. Audit which files enter GitHub read surfaces; do not assume a private directory protects a public repository's contents.

See [[GitHub-Reference-Profile-v10]], [[Publication-and-Discovery-v10]] and [[Authority-Provenance-and-Trust-v9]].

*Normative source: Framework `spec/v10/Security-and-Confidentiality.md`.*
