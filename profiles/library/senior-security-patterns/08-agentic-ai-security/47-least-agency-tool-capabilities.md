# SEC-47 — Least Agency and Tool Capability Firebreak

## Core principle

Least privilege for agents must include least agency: even a correctly authorized agent should not have more autonomous action latitude than the task requires.

## Security invariant

Each agent/tool session receives a narrowly scoped capability set: allowed tools, operations, resources, tenants, quotas, time window and maximum side-effect class. Destructive capability is absent by default, not merely discouraged in prompt text.

## Senior architecture

Issue ephemeral tool capabilities from policy after user/task context is known. Expose domain verbs (`propose_release`, `request_suspend_grant`) rather than generic shell/HTTP/SQL. Separate read, propose and execute capabilities. Require approval for irreversible/high-blast-radius transitions.

## Application to the supplied ecosystem

Map agent tools onto your existing narrow authorities: IK request construction, Orgo workflow proposals, Konfid response proposals, artifact queries. Do not expose Node Agent or release KMS directly to an AI model; route through typed, policy-gated operations.

## Failure modes / anti-patterns

- One MCP server exposes filesystem, shell and cloud admin to every agent.
- Tool descriptions are the only access control.
- Agent inherits user's entire session token.
- Read tool can smuggle side effects.
- Tool capability persists after task ends.

## Evidence that proves the control

Tool inventory is machine-readable with risk class and required policy. Captured agent credential cannot call a non-granted tool/resource. Destructive tools require separate approval evidence. Session capability expires automatically.


## Reference anchors

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI 600-1 — Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
