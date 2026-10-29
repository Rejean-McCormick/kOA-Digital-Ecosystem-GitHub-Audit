# SEC-46 — The Model Is an Untrusted Planner

## Core principle

Once an AI can call tools, the primary trust boundary is no longer “prompt vs model”; it is “probabilistic planner vs deterministic authority”. The model can propose intent but must not be the final authority for privileged effects.

## Security invariant

LLM output MUST be treated as untrusted input to deterministic validation, authorization and execution controls. A model cannot grant itself identity, scope, tool access, network access or approval by producing text that requests it.

## Senior architecture

Use a planner/executor split. The model outputs a typed proposal. A trusted control plane validates schema, resolves allowed tool, authorizes actor/workload/resource, enforces budgets and preconditions, and only then calls a narrow executor. Feed the receipt back as data, not as new authority.

## Application to the supplied ecosystem

This fits your architecture unusually well: SenTient or future agents should sit above Konfid/kOA/IK, not inside their trust core. Agent plans can create Orgo tasks or Konfid proposals, but policy, quorum, Node Agent and owner-system invariants remain deterministic and receiver-owned.

## Failure modes / anti-patterns

- Model prompt says “never do dangerous things” but tool has admin token.
- LLM chooses raw URL/command executed directly.
- Agent's confidence score changes authorization.
- Tool result contains instructions that bypass policy.
- Model can alter its own system prompt/policy store.

## Evidence that proves the control

Red-team prompt injection cannot cross the deterministic gate. Tool calls are fully reconstructible as typed proposals + policy decisions + receipts. Removing the model and submitting the same proposal produces the same authorization outcome.


## Reference anchors

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI 600-1 — Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- NIST SP 800-207 Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
