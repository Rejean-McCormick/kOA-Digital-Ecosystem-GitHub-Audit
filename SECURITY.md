# Security guidance

This repository is designed for **read-only GitHub API observation**. Do not add `POST`, `PATCH`, `PUT`, or `DELETE` requests to the client or grant write permissions without separate design review and explicit owner authorization.

- Use a private repository and a minimal-permission GitHub App installation token.
- Protect branches and restrict workflow edit permissions; consider SHA-pinning actions before production.
- Keep original snapshots, raw security alerts, private details, JWTs, credentials, signed authorization objects and raw legacy findings **out of source control and reports**.
- Reports aggregate alert counts and status only, not secret-scanning match data.
- GitHub API errors are deliberately sanitized; do not log response bodies or Authorization headers.
- The audit may be incomplete because of API permissions, feature availability, network failure or pagination. Do not treat absence of evidence as evidence of absence.
- Report vulnerabilities through a private owner-controlled channel. Do not post working exploits or tokens in public issues.

The test suite runs offline without credentials. The generated artifact was not independently audited or penetration-tested and should undergo a maintainer review before production use.
