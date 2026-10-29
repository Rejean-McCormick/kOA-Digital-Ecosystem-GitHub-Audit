# SEC-11 — Quorum and Separation of Duties

## Core principle

For high-impact actions, least privilege is insufficient if one compromised identity can both request, approve and execute. Senior systems separate duties across identities and, ideally, across independent control planes.

## Security invariant

Critical actions MUST define incompatible roles (requester, approver, operator, auditor) and quorum rules based on risk. The system validates distinct principals, eligible roles, approval scope, expiry and exact proposal digest at execution time.

## Senior architecture

Model approval as immutable evidence over a canonical proposal. Enforce `requester != approver` where required and optionally multi-party quorum. Keep executor credentials separate. Emergency paths may reduce quorum only under a separately governed break-glass policy and enhanced evidence requirements.

## Application to the supplied ecosystem

Konfid already references requester/approver/operator separation and quorum. Promote this to ecosystem-wide rules for root key operations, release promotion, trust-store changes, emergency shutdown, tenant freeze and destructive data recovery.

## Failure modes / anti-patterns

- Two clicks by the same account counted as two approvals.
- Approval of a mutable object without digest binding.
- Approver may edit proposal while approving.
- CI bot both signs and approves promotion.
- Emergency mode silently disables audit.

## Evidence that proves the control

Tests prove same-principal quorum rejection and proposal mutation rejection. Audit evidence lists distinct identities and roles. Root/trust changes require independently authenticated participants. Emergency override is separately detectable and reviewable.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
- CISA et partenaires — Secure by Design / Secure by Default: https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf
