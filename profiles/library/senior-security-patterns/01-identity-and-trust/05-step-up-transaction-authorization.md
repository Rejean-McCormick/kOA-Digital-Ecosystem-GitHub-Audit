# SEC-05 — Step-Up and Transaction Authorization

## Core principle

Authentication strength is contextual. A phishing-resistant login from yesterday may be insufficient for a destructive action now, while re-authenticating every read operation destroys usability and encourages bypasses.

## Security invariant

High-impact actions MUST bind authorization to recent authentication assurance and to the concrete transaction parameters being approved. Step-up proves freshness/assurance; it does not automatically grant the operation.

## Senior architecture

Policy returns obligations such as required assurance, maximum auth age, quorum or confirmation. After step-up, re-evaluate the exact action with the fresh assertion. For irreversible or broad-scope changes, display and cryptographically bind material parameters (tenant, target, operation, scope, expiry) to the approval artifact.

## Application to the supplied ecosystem

Konfid already models `STEP_UP_REQUIRED`, assurance and `auth_time`. Strengthen sensitive response/approval flows by ensuring the approval digest covers the exact response proposal and scope, and that policy is re-evaluated after step-up rather than accepting “recent MFA” as a generic capability.

## Failure modes / anti-patterns

- MFA as a permanent account attribute.
- Step-up performed after the privileged action starts.
- Approval UI shows friendly text while backend executes different parameters.
- Reusing one approval for expanded scope.
- “Admin logged in” used as justification for emergency commands.

## Evidence that proves the control

Tests mutate one transaction field after approval and prove execution fails. Decision records show assurance and auth age. High-risk actions require policy obligations to be satisfied at execution time. Approval receipts reference a canonical digest of approved semantics.


## Reference anchors

- NIST SP 800-63-4 Digital Identity Guidelines: https://csrc.nist.gov/pubs/sp/800/63/4/final
- RFC 9700 — OAuth 2.0 Security Best Current Practice: https://www.rfc-editor.org/rfc/rfc9700.html
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
