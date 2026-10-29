# SEC-35 — Restricted Runtime Profile as Admission Policy

## Core principle

Container hardening in YAML is brittle unless the platform rejects workloads that violate it. Secure runtime attributes should be enforced centrally, not copied from examples.

## Security invariant

Production namespaces for normal workloads SHOULD enforce a restricted pod baseline: non-root, no privilege escalation, dropped capabilities, read-only root filesystem where possible, seccomp, controlled volumes and explicit exceptions.

## Senior architecture

Use Kubernetes Pod Security Admission or policy engine equivalents. Enforce immutable image digests and allowed registries alongside runtime context. Higher-risk security-plane or agentic-code workloads may use stronger isolation via dedicated nodes/runtime classes/sandboxing.

## Application to the supplied ecosystem

Konfid documentation already targets non-root, read-only root filesystem and dropped capabilities. Turn those expectations into admission controls so a later manifest change cannot silently weaken them.

## Failure modes / anti-patterns

- SecurityContext present in one Deployment but not worker/job.
- Rootless image but `allowPrivilegeEscalation` left open.
- Privileged init container undermines main container policy.
- HostPath mounted to solve operational problem.
- Exceptions become permanent without owner/expiry.

## Evidence that proves the control

Policy tests reject deliberately weakened manifests. Cluster inventory shows no drift from restricted baseline except documented exceptions. Runtime class and node placement for higher isolation are visible in release evidence.


## Reference anchors

- Kubernetes Security and Application Security Checklist: https://kubernetes.io/docs/concepts/security/application-security-checklist/
- CISA et partenaires — Secure by Design / Secure by Default: https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf
