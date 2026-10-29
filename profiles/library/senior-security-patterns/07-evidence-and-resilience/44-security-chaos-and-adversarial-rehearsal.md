# SEC-44 — Security Chaos and Adversarial Rehearsal

## Core principle

Security architecture remains theoretical until failure modes are exercised under realistic partial failure: stale keys, duplicate delivery, policy outage, forged approvals, corrupted artifacts and overloaded control planes.

## Security invariant

Critical security invariants MUST have executable failure tests, not only documentation. Rehearsals verify safe behavior and operational competence under conditions that violate happy-path assumptions.

## Senior architecture

Build a recurring fault/adversarial matrix: IdP/JWKS outage, stale policy, compromised signer, revoked key, malicious dependency, CNI policy gap, delayed audit, worker death around side effect, forged approval, cross-tenant ID, restore replay, agent prompt injection and tool abuse.

## Application to the supplied ecosystem

Konfid's release checklist already lists several failure exercises. Expand this into an ecosystem SecurityDiag suite that can run against a candidate Release Set and produce evidence linked to promotion.

## Failure modes / anti-patterns

- Tabletop only, no system fault injection.
- Pen test finds issues but release gates never encode regressions.
- Exercises run against toy dev mode with security controls disabled.
- Success means “service stayed up” rather than “authority remained correct”.
- Findings do not become automated tests.

## Evidence that proves the control

Each critical invariant has at least one negative/fault test. Candidate release records reference SecurityDiag evidence. Past incident root causes become regression scenarios. Exercises track security outcome and evidence integrity, not merely uptime.


## Reference anchors

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST SP 800-218 SSDF 1.1 (final): https://csrc.nist.gov/pubs/sp/800/218/final
- CISA et partenaires — Secure by Design / Secure by Default: https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf
