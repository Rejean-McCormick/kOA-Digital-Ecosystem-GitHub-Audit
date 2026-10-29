# SEC-50 — Agent Memory Is Security State

## Core principle

Persistent memory can carry attacker instructions or corrupted facts across sessions, turning one injection into durable behavior change. Treat memory writes like mutations to a security-relevant knowledge store.

## Security invariant

Persistent agent memory MUST have provenance, author/source, tenant, sensitivity, write policy, expiry/retention and reviewability. Untrusted content cannot silently promote itself into trusted instruction or durable preference.

## Senior architecture

Separate episodic/user memory, operational facts, retrieved documents and policy/system instructions. Gate memory writes with deterministic rules; summarize into structured fields rather than storing arbitrary instruction text where possible. Support quarantine, versioning and rollback of poisoned memory.

## Application to the supplied ecosystem

Kristal's distinction between epistemic artifacts, validation/recognition and runtime projections provides a strong conceptual model: an agent observation can be stored as evidence/working knowledge without becoming recognized truth or executable policy.

## Failure modes / anti-patterns

- Agent writes every conversation into a global vector store.
- Retrieved memory can override system policy.
- No provenance/tenant on embeddings.
- “User preference” memory contains hidden tool instructions.
- Deleted/invalidated source remains in derived memory indefinitely.

## Evidence that proves the control

Poisoning tests show malicious memory cannot change tool policy. Memory records expose provenance/version. Revocation or source invalidation propagates to derived memory/materializations within a defined SLO.


## Reference anchors

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI 600-1 — Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
