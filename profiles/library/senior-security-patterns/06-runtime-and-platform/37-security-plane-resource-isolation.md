# SEC-37 — Security Plane Resource Isolation

## Core principle

Security controls can fail open indirectly when telemetry, analytics or untrusted workloads exhaust the CPU, DB pool, queues or threads needed for authorization, revocation and incident response.

## Security invariant

Critical authorization/revocation/audit paths MUST have protected capacity and independent failure domains from high-volume telemetry, analytics and optional detectors. Load shedding prioritizes security-critical control traffic.

## Senior architecture

Separate worker pools/queues, DB pools and autoscaling signals for control-plane vs analytics paths. Define per-tenant and per-source quotas. Reserve resources for revocation and break-glass operations. Test backpressure so overload does not starve deny/revoke processing.

## Application to the supplied ecosystem

Konfid's threat model already calls out isolating Overwatch capacity from authorization/revocation. Make the same distinction across the ecosystem: observability/knowledge ingestion should not starve trust, policy, release or recovery control paths.

## Failure modes / anti-patterns

- One queue for telemetry and revocations.
- HPA scales on average CPU while DB saturates.
- Detector flood consumes all worker leases.
- Audit outage blocks every low-risk read unnecessarily.
- Rate limiter itself depends on overloaded shared DB.

## Evidence that proves the control

Load tests flood telemetry/one tenant and prove authorization/revocation SLOs remain within bounds. Resource dashboards separate control-plane pools. Load shedding decisions are observable and policy-defined.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- Kubernetes Security and Application Security Checklist: https://kubernetes.io/docs/concepts/security/application-security-checklist/
