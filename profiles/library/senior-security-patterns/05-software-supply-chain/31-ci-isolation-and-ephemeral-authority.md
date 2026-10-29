# SEC-31 — CI Isolation and Ephemeral Authority

## Core principle

CI executes attacker-influenced code by design. The key architectural question is what authority that code can touch during that run and whether untrusted contributions can cross into privileged jobs.

## Security invariant

Untrusted build/test jobs MUST NOT possess production secrets, release signing authority or write-capable repository/cloud tokens. Privileged promotion jobs consume immutable outputs only after trust gates and obtain short-lived credentials just in time.

## Senior architecture

Separate PR testing from trusted release workflows. Use least `GITHUB_TOKEN` permissions, OIDC federation instead of long-lived cloud keys, protected environments for deploy, and artifact handoff with integrity verification. Pin third-party Actions to full commit SHAs.

## Application to the supplied ecosystem

In the supplied Konfid workflows, permissions are already narrow, but Actions are referenced by version tags such as `@v7`/`@v4`. GitHub's current guidance states that full-length commit SHA pinning is the immutable option. Make SHA pinning an ecosystem policy and use OIDC for deployment/signing authority.

## Failure modes / anti-patterns

- `pull_request_target` executes fork code with secrets.
- Build and deploy run in same job with same credentials.
- Third-party action pinned only to movable tag.
- Long-lived cloud key in repository secrets.
- Privileged workflow trusts artifacts from an untrusted job without digest/provenance.

## Evidence that proves the control

Organization policy enforces SHA pinning. Untrusted PR cannot obtain secrets or production OIDC claims. Deploy job credentials expire quickly and are bound to protected repo/ref/environment claims. Artifact digest is verified between build and promote jobs.


## Reference anchors

- GitHub Actions — Secure use reference: https://docs.github.com/en/actions/reference/security/secure-use
- GitHub Actions — OIDC for short-lived deployment credentials: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers
- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
