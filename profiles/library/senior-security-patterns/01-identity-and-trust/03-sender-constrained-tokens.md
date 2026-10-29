# SEC-03 — Sender-Constrained Credentials

## Core principle

Bearer tokens convert theft into authority: whoever possesses the token can use it until expiry. For high-value service calls, bind credentials to a cryptographic key held by the caller so exfiltration alone is insufficient.

## Security invariant

Tokens authorizing privileged or high-value operations SHOULD be sender-constrained where practical. The resource server must verify the proof-of-possession binding, not merely trust that the issuer created the claim.

## Senior architecture

Use mTLS certificate-bound access tokens or DPoP depending client/runtime constraints. Keep token TTL short, audience exact and key rotation automated. At proxies, preserve proof-of-possession semantics end-to-end; a TLS terminator must not turn a certificate-bound identity into an unauthenticated header.

## Application to the supplied ecosystem

For Konfid-to-Policy/Audit/IK or privileged enforcement, sender-constrained credentials reduce the consequence of a leaked bearer integration token. For browser-facing human flows, use modern OAuth/OIDC code flow with PKCE and follow RFC 9700 rather than inventing token transport.

## Failure modes / anti-patterns

- "TLS already encrypts the bearer token" as replay protection.
- Forwarding client-certificate identity via spoofable headers.
- DPoP without nonce/replay handling where required.
- One proof key reused across unrelated clients.
- Long-lived refresh credentials without binding.

## Evidence that proves the control

Red-team test: exfiltrated access token used from a different key fails. Gateway and application agree on the authenticated key binding. Token audience and issuer mismatches fail closed. Telemetry can distinguish token failure from proof-of-possession failure.


## Reference anchors

- RFC 9700 — OAuth 2.0 Security Best Current Practice: https://www.rfc-editor.org/rfc/rfc9700.html
- RFC 9449 — OAuth 2.0 DPoP: https://www.rfc-editor.org/info/rfc9449/
- RFC 8705 — OAuth 2.0 mTLS and certificate-bound tokens: https://www.rfc-editor.org/info/rfc8705/
