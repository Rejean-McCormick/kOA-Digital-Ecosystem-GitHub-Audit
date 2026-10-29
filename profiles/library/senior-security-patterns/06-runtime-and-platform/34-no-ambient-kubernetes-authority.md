# SEC-34 — No Ambient Kubernetes Authority

## Core principle

Pods frequently inherit cluster authority they never use. Ambient service-account tokens turn application RCE into Kubernetes API access and broaden every compromise.

## Security invariant

Workloads MUST receive no Kubernetes API credential unless the workload function requires it. When required, use a dedicated service account with minimum verbs/resources/namespaces and short-lived projected tokens.

## Senior architecture

Set `automountServiceAccountToken: false` by default, avoid default ServiceAccounts, restrict RBAC mutation/escalation verbs and use admission policy to enforce workload baselines. Separate deployer permissions from runtime permissions.

## Application to the supplied ecosystem

The provided Konfid ServiceAccount already disables token automount, which is exactly the desired default. Keep this as an ecosystem-wide admission rule and grant exceptions only with documented API calls and threat rationale.

## Failure modes / anti-patterns

- Every pod uses default ServiceAccount.
- Runtime can patch Deployments or Roles “for convenience”.
- Wildcard RBAC on namespaced resources.
- Application needs one ConfigMap but receives secret list/watch.
- CI deployment role reused by runtime.

## Evidence that proves the control

Admission rejects unexpected token mounts. RBAC review can enumerate exact API calls per workload. Compromised app container cannot call Kubernetes API unless explicitly designed to do so.


## Reference anchors

- Kubernetes Security and Application Security Checklist: https://kubernetes.io/docs/concepts/security/application-security-checklist/
- NIST SP 800-207A Cloud-Native Zero Trust: https://csrc.nist.gov/pubs/sp/800/207/a/final
