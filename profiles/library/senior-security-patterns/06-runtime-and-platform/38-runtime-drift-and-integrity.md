# SEC-38 — Runtime Drift Is a Security Signal

## Core principle

Even with immutable deployments, emergency edits, compromised nodes or side-loaded files can make runtime differ from the admitted artifact. Security needs a way to detect “what is running” versus “what was approved”.

## Security invariant

Runtime identity SHOULD be continuously reconcilable to admitted artifact digest, release-set identity and expected configuration. Drift in executable/config/security policy is treated as security-significant.

## Senior architecture

Expose workload image digests and release metadata, inventory active Runtime Packs/policy bundles, and compare against desired signed manifests. Prefer immutable filesystems and declarative reconciliation. Detect unexpected binaries/processes/config writes at high-risk nodes.

## Application to the supplied ecosystem

`kristal_runtime` already owns active Runtime Pack state and receipts; kOA Release Sets own release compatibility. Use those as authoritative runtime identities and make direct node mutation impossible except through the narrow Node Agent with receipts.

## Failure modes / anti-patterns

- SSH hotfix with no release record.
- Runtime downloads executable plugin from internet.
- ConfigMap changed manually outside promotion flow.
- Health says “up” but active digest is unknown.
- Rollback restores image but not policy/trust configuration.

## Evidence that proves the control

Runtime inventory can prove exact image/config/policy/Runtime Pack identities. Drift alert links to an unauthorized mutation or reconciler event. Recovery can restore a complete last-known-good set, not only a container image.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
- Kubernetes Security and Application Security Checklist: https://kubernetes.io/docs/concepts/security/application-security-checklist/
