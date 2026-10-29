# SEC-08 — Capability-Shaped Privileged Execution

## Core principle

The safest privileged executor is deliberately weak: it exposes a small vocabulary of typed, allowlisted operations instead of shell, SQL, Kubernetes-admin, or arbitrary HTTP. This converts compromise from “root with creativity” to bounded misuse.

## Security invariant

Privileged agents MUST NOT accept arbitrary commands when a finite operation set can express the legitimate lifecycle. Each operation has typed parameters, explicit scope, preconditions, expiry, idempotency identity and a receipt.

## Senior architecture

Put broad credentials behind a narrow broker/agent. Define operations such as `activate_pack`, `revoke_grant`, `isolate_service`, not `exec(cmd)`. Validate target allowlists and state transitions locally. For destructive operations, support dry-run/proposal then governed execution.

## Application to the supplied ecosystem

Your Node Agent boundary and Konfid enforcement model are natural homes for this. Keep host mutation and emergency response as narrow command vocabularies; do not let Orgo, Koali or an AI agent gain generic shell simply because they can request an approved operation.

## Failure modes / anti-patterns

- “Internal admin” endpoint that accepts arbitrary command strings.
- Generic webhook to privileged automation.
- Tooling that expands a narrow request into arbitrary Terraform/Kubectl without policy binding.
- Receipts that only say success, not what effect occurred.
- Hidden side effects in a supposedly read-only operation.

## Evidence that proves the control

Fuzz tests prove unknown operation/field rejection. Runtime credentials cannot perform actions outside the broker. Receipts contain operation, target, pre-state/post-state references and execution identity. Static analysis shows no shell interpolation path from external input.


## Reference anchors

- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
- CISA et partenaires — Secure by Design / Secure by Default: https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf
