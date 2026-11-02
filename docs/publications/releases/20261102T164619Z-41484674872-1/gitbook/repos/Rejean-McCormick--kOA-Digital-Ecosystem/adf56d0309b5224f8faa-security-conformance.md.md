<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/40-integration/identity-oidc/security-conformance.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 02cf8dff8355dd44f8cfb282c3898e052cbe7e70ca37d9ad60ea857368933955 -->

# Identity Security & Conformance

**Status:** Normative (kOA)

## 1) Security invariants

Implementations MUST protect against identity mis-linking, token theft/replay, issuer confusion, audience confusion, privilege escalation, stale memberships, shared service credentials, and PII leakage.

## 2) Secret handling

Passwords, access tokens, refresh tokens, client secrets, and recovery credentials MUST NOT be stored in Git, demo scenarios, or ordinary logs.

## 3) Minimum conformance tests

- same `(issuer, subject)` resolves the same local account;
- changed email does not create a second identity;
- same email with a different subject does not silently merge;
- wrong issuer does not match;
- wrong audience is rejected;
- revoked local role remains revoked after successful SSO;
- each application authorizes locally;
- IdP outage leaves documented local recovery available;
- changing one application's local password does not alter another application's password;
- synthetic personas do not get login credentials by default;
- service credentials are distinct from human sessions.

## 4) Privacy

Federation is not permission to join all user data across applications. Cross-system data sharing remains subject to purpose limitation, local ownership, minimization, and explicit integration contracts.
