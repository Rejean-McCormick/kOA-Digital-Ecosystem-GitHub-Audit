# SEC-17 — Egress Is a Privilege, Not Plumbing

## Core principle

A service with broad outbound network access can turn SSRF, prompt injection, dependency compromise or credential theft into lateral movement and exfiltration. Senior architectures treat egress as an explicit capability.

## Security invariant

Security-sensitive workloads SHOULD have default-deny egress and destination-specific policy. Any feature that fetches caller-influenced URLs must use an egress broker/resolver policy that blocks internal/control-plane ranges and validates redirects/DNS rebinding.

## Senior architecture

Route external destinations through controlled egress gateways or proxies with identity-aware policy, DNS controls, TLS verification and audit. Separate data-plane fetchers from control-plane workloads. Do not allow privileged pods to become generic web clients.

## Application to the supplied ecosystem

Konfid's namespace-based default-deny NetworkPolicy is a strong start, and its docs already call the namespace label a security grant. Make label mutation itself admission-controlled, verify the CNI actually enforces policy, and route JWKS/Policy/Audit/IK/DB access through narrowly approved paths.

## Failure modes / anti-patterns

- NetworkPolicy exists but CNI ignores it.
- Allowing TCP/443 to the whole internet.
- Namespace labels writable by application deployers.
- DNS allowlist with no rebinding/redirect controls.
- Artifact locator or AI tool can reach metadata service/control plane.

## Evidence that proves the control

Automated connectivity tests prove only approved destinations are reachable. Admission policy restricts labels that grant egress. SSRF test suite covers redirects, alternate IP notation, IPv6, DNS changes and cloud metadata endpoints.


## Reference anchors

- Kubernetes Security and Application Security Checklist: https://kubernetes.io/docs/concepts/security/application-security-checklist/
- NIST SP 800-207A Cloud-Native Zero Trust: https://csrc.nist.gov/pubs/sp/800/207/a/final
- OWASP API Security Top 10 2023: https://owasp.org/www-project-api-security/
