# SEC-53 — Agentic Budgets and Circuit Breakers

## Core principle

Autonomous loops turn small mistakes into cascading failures: repeated tool calls, recursive delegation, repeated purchases/deletes, token burn or fan-out across services. Safety needs hard budgets outside the model.

## Security invariant

Agent execution MUST have deterministic budgets for time, steps, tool calls, cost, data volume, concurrency and side-effect count/scope. Exceeding a budget stops or requires explicit reauthorization.

## Senior architecture

Enforce budgets in the orchestration/control layer, not prompt text. Use per-task idempotency, rate limits, fan-out limits, circuit breakers and a kill switch that actually revokes capabilities. For destructive classes, cap cumulative scope and require new approval beyond threshold.

## Application to the supplied ecosystem

Integrate budgets with Konfid policy/response and Orgo workflows: an agent may propose many tasks, but its effective capabilities and execution quotas remain bounded. Overwatch can detect anomalous behavior but must not be the only stop mechanism.

## Failure modes / anti-patterns

- Prompt says “do at most 10 calls”.
- Agent can spawn child agents with fresh budgets.
- Stop button only sends another natural-language instruction.
- Retry loop creates new idempotency IDs.
- Cost budget exists but destructive-action budget does not.

## Evidence that proves the control

Forced runaway scenarios stop at deterministic limits. Child agents share or consume parent budget. Emergency stop revokes tool capability at control plane. Metrics expose budget consumption and circuit-breaker trips without relying on model self-report.


## Reference anchors

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI 600-1 — Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
