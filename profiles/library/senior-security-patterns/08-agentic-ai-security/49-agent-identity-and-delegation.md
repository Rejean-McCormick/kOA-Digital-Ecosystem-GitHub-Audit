# SEC-49 — Agent Identity Is Not Human Identity

## Core principle

An agent acting for a user is neither the user nor merely the hosting service. Without explicit agent/workload/actor semantics, audit and policy cannot distinguish autonomous behavior from direct human action.

## Security invariant

Agent execution MUST preserve at least: hosting workload identity, agent instance/type, human or system principal being assisted, delegation/task context, and effective tool capability. Human identity is never copied into the agent as impersonation.

## Senior architecture

Use an actor chain or token exchange/delegation artifact. Policy can distinguish `human-direct`, `agent-proposed`, `agent-executed-with-delegation`, and `service-automation`. Bind agent capability to task/session and resource scope, with short TTL and no ambient user refresh token.

## Application to the supplied ecosystem

Extend Konfid's caller_service + actor_principal model with agent identity/task delegation when SenTient gains tools. Audit should show that an AI proposed/executed an operation for P123 via service X, not simply “P123 did it”.

## Failure modes / anti-patterns

- Agent uses user's browser cookie.
- Audit records only end user's name.
- Agent refresh token survives indefinitely.
- Multiple agents share one service identity with indistinguishable actions.
- Agent can re-delegate user authority to another agent.

## Evidence that proves the control

Audit can filter agent-originated actions. Revoking a task/delegation stops new tool calls without disabling the user account. Agent credentials are audience/tool-scoped and short-lived. Policy can prohibit certain actions when actor is agentic.


## Reference anchors

- RFC 8693 — OAuth 2.0 Token Exchange: https://www.rfc-editor.org/info/rfc8693/
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI 600-1 — Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
