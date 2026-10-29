# SEC-52 — Agentic Supply Chain and Tool Trust

## Core principle

Agents dynamically combine models, prompts, MCP/tool servers, plugins, retrieval sources and code packages. Any one can redirect behavior or exfiltrate data, so the agent's supply chain is broader than its container image.

## Security invariant

Every executable/privileged agent component MUST have an explicit trust identity and admission policy. Tool discovery does not imply tool trust. Tool schemas/manifests, connectors and model/prompt versions are versioned and provenance-aware.

## Senior architecture

Maintain an allowlisted tool registry with owner, version/digest, endpoint identity, permissions, data classes and risk class. Verify signed/attested tool packages where feasible. Pin model/prompt/tool versions for high-stakes workflows and evaluate updates in shadow/canary before broad use.

## Application to the supplied ecosystem

For a future ecosystem MCP layer, model tools as IK-like profiles: explicit contract, target, authority, artifact refs, version and receipt. Do not let arbitrary third-party MCP discovery attach tools to SenTient production agents.

## Failure modes / anti-patterns

- Automatically install tool suggested by model.
- MCP server authenticated only by DNS/URL.
- Tool schema changes without version/admission.
- Model provider change silently changes behavior.
- Prompt template fetched from mutable branch at runtime.

## Evidence that proves the control

Inventory can answer exactly which model/prompt/tool versions participated in an action. Unknown tool identity is rejected. Tool update produces security regression evidence before promotion. Runtime can emit the active agent release-set identity.


## Reference anchors

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- SLSA Specification v1.2: https://slsa.dev/spec/v1.2/
- NIST AI 600-1 — Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
