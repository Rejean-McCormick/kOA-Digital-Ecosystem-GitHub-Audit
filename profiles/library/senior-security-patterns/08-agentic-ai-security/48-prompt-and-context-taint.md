# SEC-48 — Prompt/Context Taint and Provenance

## Core principle

Indirect prompt injection works because untrusted content is interpreted in the same semantic channel as trusted instructions. The fix is not a better warning prompt; it is provenance-aware data handling and tool policy.

## Security invariant

Context MUST retain provenance/trust class. Untrusted documents, web pages, logs, email, retrieved memory and tool outputs cannot redefine system policy, tool authority or approval requirements.

## Senior architecture

Tag context chunks with source, trust class, tenant, sensitivity and retrieval reason. Separate instructions from data structurally where platform allows. Before a context-derived value reaches a tool, validate it under the tool's schema/policy. Restrict outbound rendering/fetching to block exfiltration channels.

## Application to the supplied ecosystem

For EncyKlopedia/SenTient/Kristal knowledge flows, preserve source provenance through retrieval and compilation. A retrieved artifact can inform reasoning without becoming executable authority. IK evidence/artifact refs are useful anchors for source identity.

## Failure modes / anti-patterns

- Concatenate web page text into system prompt.
- Tool output says “ignore previous instructions” and agent obeys.
- Retrieved URL automatically fetched by privileged backend.
- RAG chunk loses tenant/source metadata.
- Model-generated citation treated as proof of source.

## Evidence that proves the control

Prompt-injection tests with hostile retrieved content cannot change tool authorization. Every high-impact derived value can be traced to context provenance. Egress policy blocks data exfiltration via arbitrary URLs/renderers.


## Reference anchors

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI 600-1 — Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
