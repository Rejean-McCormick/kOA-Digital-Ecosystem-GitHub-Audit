# SEC-26 — Source Change Path Is Part of the TCB

## Core principle

Artifact signing cannot rescue a malicious source change that legitimately passed through the build. The trusted computing base includes repository ownership, branch policy, review, workflow definitions and the identities allowed to change them.

## Security invariant

Protected source and build configuration changes require independently authenticated, reviewable, immutable history. Security-sensitive workflow/policy files deserve stricter ownership than ordinary code.

## Senior architecture

Use branch protections/rulesets, required review, CODEOWNERS for security-critical paths, protected environments and explicit bot permissions. Treat workflow changes as privileged because they can exfiltrate CI credentials or forge releases. Prefer immutable repository identity claims in CI federation where available.

## Application to the supplied ecosystem

For your multi-repository ecosystem, define which repositories are release-authoritative for each artifact and which files control signing/admission. The ecosystem inventory is discovery metadata, not an authority map; release authority must be explicit per repository/channel.

## Failure modes / anti-patterns

- “Signed by CI” while anyone can edit the CI workflow.
- One maintainer can change workflow and approve it.
- Repository rename/transfer silently changes cloud trust.
- Generated lock/provenance files accepted without reviewer understanding.
- Bot can approve its own PR.

## Evidence that proves the control

Repository rules show protected critical paths. CI federation trust binds immutable repo/org identifiers where supported. Change logs can prove who reviewed a workflow or policy change before the corresponding release.


## Reference anchors

- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
- GitHub Actions — Secure use reference: https://docs.github.com/en/actions/reference/security/secure-use
- GitHub Actions — OIDC for short-lived deployment credentials: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers
- NIST SP 800-218 SSDF 1.1 (final): https://csrc.nist.gov/pubs/sp/800/218/final
