# SEC-36 — Network Policy Is Not Identity

## Core principle

IP/namespace segmentation limits reachability but does not prove who a peer is. In dynamic clusters, identity-aware authorization must sit above network placement.

## Security invariant

Network reachability is a necessary constraint, never sufficient authorization. Sensitive service calls authenticate workload identity and authorize application-level actions even when NetworkPolicy permits the connection.

## Senior architecture

Use default-deny network policy for blast radius, plus workload mTLS/JWT identity for peer authentication and local authorization. Treat namespace labels that grant connectivity as privileged configuration and protect them with admission/RBAC.

## Application to the supplied ecosystem

Konfid's network model intentionally uses namespace labels for allowed ingress/egress. Preserve that as coarse segmentation, then rely on workload identity + Konfid/kOA policy for actual authority. Do not create an “internal = trusted” bypass.

## Failure modes / anti-patterns

- Service allows any caller from namespace X.
- Mesh identity accepted as business authorization.
- Namespace label grants access and is editable by app team.
- NetworkPolicy absent in one CNI/cluster variant.
- mTLS authenticates a workload but no audience/resource authorization follows.

## Evidence that proves the control

Connectivity and authorization are tested independently. A permitted network peer with wrong workload identity is rejected. A valid workload identity from a blocked network path cannot connect. Label mutation is policy-controlled.


## Reference anchors

- Kubernetes Security and Application Security Checklist: https://kubernetes.io/docs/concepts/security/application-security-checklist/
- NIST SP 800-207A Cloud-Native Zero Trust: https://csrc.nist.gov/pubs/sp/800/207/a/final
- SPIFFE Workload Identity / SVID: https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/
