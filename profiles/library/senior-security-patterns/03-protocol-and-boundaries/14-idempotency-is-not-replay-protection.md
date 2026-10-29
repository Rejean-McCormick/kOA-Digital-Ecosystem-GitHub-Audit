# SEC-14 — Idempotency Is Not Replay Protection

## Core principle

Idempotency prevents duplicate effects for a known semantic operation; replay protection prevents an attacker from reusing captured authority. They overlap but are not interchangeable.

## Security invariant

Privileged requests need both semantic idempotency and authority freshness. A repeated request with the same idempotency key can return the prior receipt; a captured credential or approval cannot create a fresh operation outside its validity/scope.

## Senior architecture

Store idempotency key + semantic fingerprint + prior result under an authority-relevant scope. Separately validate token/approval expiry, nonce/jti/replay policy where appropriate, sender binding and state preconditions. Do not generate a new effect simply because a replay uses a new idempotency key.

## Application to the supplied ecosystem

IK has strong semantic idempotency behavior. Konfid requires `jti`; remember that presence of `jti` alone is not anti-replay unless uniqueness/freshness is enforced where needed. For privileged response commands, action identity, approval digest and target receipt should define replay semantics.

## Failure modes / anti-patterns

- “JWT has jti, therefore replay is solved.”
- Client chooses unlimited new idempotency keys for same destructive intent.
- Idempotency record expires before the effect can no longer be replayed safely.
- Same key accepted with different semantics.
- Retry path skips current authorization entirely.

## Evidence that proves the control

Tests cover exact replay, divergent replay, expired authority, new-key same-intent abuse and replay after restore. The system can return a prior receipt without repeating the side effect and can prove why a replay was rejected.


## Reference anchors

- RFC 9449 — OAuth 2.0 DPoP: https://www.rfc-editor.org/info/rfc9449/
- RFC 8705 — OAuth 2.0 mTLS and certificate-bound tokens: https://www.rfc-editor.org/info/rfc8705/
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
