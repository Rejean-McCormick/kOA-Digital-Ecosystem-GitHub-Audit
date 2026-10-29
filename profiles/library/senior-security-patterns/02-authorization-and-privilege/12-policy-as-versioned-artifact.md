# SEC-12 — Policy as a Versioned Security Artifact

## Core principle

Policy changes are production code changes with potentially larger blast radius than application code. Treating policy as mutable configuration invites silent authorization drift.

## Security invariant

Every policy decision MUST be attributable to an immutable policy version/digest. Policy rollout must be staged, observable and reversible; policy state changes require the same provenance and review discipline as privileged code.

## Senior architecture

Package policy bundles immutably, sign/attest them, run differential tests against captured decisions, deploy in shadow mode, then canary. Record policy digest in decision receipts. Support rollback to last-known-good without editing the old bundle.

## Application to the supplied ecosystem

Konfid's release checklist already calls for a policy bundle digest. Extend that into a full policy supply chain: source review, tests, provenance, admission, shadow decisions, canary tenant/scope and rollback. kOA Governance Policy Runtime should expose active bundle identity to every decision.

## Failure modes / anti-patterns

- Editing production policy in a dashboard with no source review.
- "Hotfix" rules that are not versioned.
- Rollback means manually recreating old state.
- Canary based only on availability, not decision deltas.
- Decision logs omit policy version.

## Evidence that proves the control

A decision can be deterministically attributed to a bundle digest. CI produces authorization regression diffs. Canary monitors ALLOW/DENY/STEP_UP delta by action/tenant without leaking sensitive identities. Rollback restores a previously attested artifact.


## Reference anchors

- NIST SP 800-218 SSDF 1.1 (final): https://csrc.nist.gov/pubs/sp/800/218/final
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
