# SEC-42 — Fail Closed by Transition, Not by Slogan

## Core principle

“Fail closed” applied indiscriminately can turn a dependency outage into a self-inflicted platform outage; “fail open” hides security bypasses. Senior systems classify transitions by security consequence and define failure behavior per transition.

## Security invariant

Each operation class MUST specify dependency failure semantics: DENY/BLOCK, continue under bounded cached capability, degrade to read-only, queue for later, or use break-glass. Defaults for privileged mutation are fail closed.

## Senior architecture

Document a failure matrix for identity, policy, audit, network, KMS and owner systems. Bound any cached authorization by expiry and resource/version context. Distinguish `DENY` (policy says no) from `BLOCKED` (decision unavailable) to preserve operational truth.

## Application to the supplied ecosystem

Konfid already uses `BLOCKED` for unavailable/invalid policy and can keep local audit when the broker is unavailable under policy limits. Extend the matrix across kOA activation, Kristal validation, Koali presentation and IK delivery so unrelated failures degrade only their owned transition.

## Failure modes / anti-patterns

- Policy outage returns ALLOW to keep service up.
- Audit outage kills all reads unnecessarily.
- Cached ALLOW has no expiry.
- Dependency 500 converted to user “forbidden”.
- Presentation outage triggers rollback of unrelated Runtime Pack.

## Evidence that proves the control

Chaos tests assert expected behavior for each dependency outage. Metrics distinguish DENY vs BLOCKED vs degraded. Cached capabilities expose expiry/source. Privileged mutation has no undocumented fail-open path.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
