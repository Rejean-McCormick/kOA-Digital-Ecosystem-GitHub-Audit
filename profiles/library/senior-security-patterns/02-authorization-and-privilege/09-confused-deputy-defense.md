# SEC-09 — Confused Deputy Defense

## Core principle

A powerful service can be tricked into spending its own authority for a weaker caller. This is especially dangerous in orchestration, export, webhook, storage and agent-tool systems where the deputy has access the requester does not.

## Security invariant

Whenever a service uses its own privilege on behalf of another principal, authorization MUST bind caller, actor, target resource, intended audience and requested operation. User-controlled locators or target identifiers never implicitly select a privileged resource.

## Senior architecture

Use audience-bound tokens, actor/caller binding, resource ownership checks and destination allowlists. Prefer opaque owner-issued artifact references over caller-provided URLs. In cloud APIs, pass explicit tenant/account/project context and verify it against authenticated identity before any lookup or side effect.

## Application to the supplied ecosystem

IK `ArtifactRef` and source-owned locators should stay opaque and credential-free. Da’at, Runtime Pack fetchers and Koali integrations must not become generic URL fetchers with privileged network access. Konfid's actor `azp/client_id` binding is a good confused-deputy countermeasure.

## Failure modes / anti-patterns

- Backend fetches any URL supplied in an artifact field.
- Service chooses tenant from request body instead of caller context.
- “Act on behalf of” without audience binding.
- Signed URL accepted outside its intended service/resource.
- Internal service grants because caller came through a trusted proxy.

## Evidence that proves the control

SSRF tests cannot reach metadata/control-plane endpoints. Cross-tenant object IDs fail even when valid. Token for service A cannot be replayed to service B. Artifact locators resolve only through an owner-defined retrieval policy.


## Reference anchors

- OWASP API Security Top 10 2023: https://owasp.org/www-project-api-security/
- RFC 9700 — OAuth 2.0 Security Best Current Practice: https://www.rfc-editor.org/rfc/rfc9700.html
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
