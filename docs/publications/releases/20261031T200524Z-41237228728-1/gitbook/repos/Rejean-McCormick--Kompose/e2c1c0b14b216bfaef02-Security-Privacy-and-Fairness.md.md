<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Security-Privacy-and-Fairness | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 91c939627e8aa8619a021cb7df67699e73c425944d1158f27fb1c5c4bba3e3e4 -->

# Security, Privacy, Accessibility, and Fairness

This wiki states **design requirements**, not legal advice or school compliance certification. Obligations must be assessed for the relevant institution and jurisdiction.

## Safeguarding minors

- Use pseudonymous, session-scoped IDs; minimize data and control deletion.
- Require time-limited entry codes **and** verified school identity.
- Enforce resource-level permissions **server-side**.
- Never expose sensitive diagnostics or relationship constraints to other participants, including in hidden HTML or API payloads.
- Never infer medical, psychological, or “social” profiles.
- Protect audit logs and omit sensitive details from public events.

## Relationship constraints

Affinities and aversions may inform safe collaboration, never judgments about a child. Hard safety constraints take precedence over optimization. Each private constraint needs a purpose, minimum justification, restricted visibility, and expiration.

## Assessment fairness

The **top-third policy** is neither compulsory nor a measure of personal worth. It must be backed by comparable scoring if used; otherwise, fall back to a non-ranking policy. Do not publish scores or class rankings. Provide alternatives for accommodations and absences.

## Accessibility

Keyboard navigation, screen-reader compatibility, sufficient contrast, plain language, audio and captions where appropriate, flexible timing, assessment resumption, and alternatives to mandatory social interaction. These requirements must be **tested in the real interface**, not assumed from documentation.

## Kristal permissions

Permission to read is separate from the document itself and its guardianship. Grants must be scoped, revocable, and auditable; fallback access prevents social exclusion or withholding of knowledge.

## Before real-world use

School SSO, TLS, protected storage, school/session isolation, backups, incident response, deletion procedures, impact assessments, and authorization/accessibility testing. **The local Python engine delivers none of these production protections.**

[[Home|← Home]] · [[Operations-and-Incidents|Incidents →]] · [[Editorial-Governance|Content →]]
