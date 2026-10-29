# SEC-21 — Short-Lived Credentials and Secret Zero

## Core principle

Secret managers reduce sprawl but do not solve the “secret zero” problem if workloads still need a long-lived bootstrap credential to access them. Prefer federated or attested identity to obtain short-lived credentials just in time.

## Security invariant

Production workloads SHOULD avoid static long-lived credentials when an identity federation path exists. Bootstrap trust must be rooted in platform workload identity, node attestation, hardware identity or another narrowly governed mechanism.

## Senior architecture

Use workload identity to obtain short-lived DB/cloud/KMS tokens. Mount private material as files only when needed, minimize lifetime in process memory, and avoid environment variables for secrets that can be inherited/dumped broadly. Rotation should not require image rebuild.

## Application to the supplied ecosystem

Konfid docs already prefer external secret managers and mounted files. The higher-level target is to remove static bearer integration secrets for kOA Policy/Audit/IK where supported and use federated workload identity or short-lived client credentials.

## Failure modes / anti-patterns

- Vault token stored as a Kubernetes Secret forever.
- CI deploy key valid for a year.
- Rebuilding image to rotate secret.
- Secret copied into logs/crash dumps.
- One bootstrap credential shared by all replicas/environments.

## Evidence that proves the control

Credential inventory shows TTL and issuance source. Rotating/revoking one workload does not require global restart. Secret scanning finds no production credentials in repositories or images. Compromise exercise demonstrates bounded credential lifetime.


## Reference anchors

- SPIFFE Workload Identity / SVID: https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/
- Kubernetes Secrets good practices: https://kubernetes.io/docs/concepts/security/secrets-good-practices/
- GitHub Actions — OIDC for short-lived deployment credentials: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
