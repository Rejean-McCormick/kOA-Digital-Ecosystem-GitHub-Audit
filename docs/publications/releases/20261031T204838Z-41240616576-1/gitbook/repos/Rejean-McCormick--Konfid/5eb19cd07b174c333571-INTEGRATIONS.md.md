<!-- Frozen source: https://github.com/Rejean-McCormick/Konfid/blob/e3d96da8e880815dc6e6d75e8662f2ab6e871bfc/docs/INTEGRATIONS.md | commit: e3d96da8e880815dc6e6d75e8662f2ab6e871bfc | SHA-256: dd6a45fd215a38f7239dfc91761b2f987670f4d9e27f84672c3bcd11c3303c0d -->

# Integrations

## Konnaxion

Konnaxion authenticates its workload, supplies a stable signed actor assertion, requests `EvaluateAccess`, applies returned obligations and enforces the decision on its own data. It may be more restrictive than Konfid.

## Orgo

High-impact proposals generate durable `konfid.approval.request.v1` outbox events. Orgo is the human coordination surface only. Konfid independently validates approver identity, eligible role, scope, request digest, authentication freshness, distinctness and current policy version, then re-evaluates immediately before execution.

Orgo failure cannot disable automatic revoke/deny operations that policy allows without human approval.

## kOA Governance Policy Runtime

Production requires `KONFID_POLICY_MODE=koa`. Konfid submits canonical access/response context and consumes structured decisions. Policy service failure does not fall back to the local development engine. **An access `ALLOW` from kOA must have a nonempty decision/policy reference and an explicit timezone-aware `valid_until` strictly in the future and no more than 60 seconds away**. Missing, stale, naive or excessive positive-decision lifetimes are treated as `BLOCKED`, not as unbounded permissions. A `DENY` does not require an expiry.

## kOA Audit Broker

Konfid commits a chained local audit record with its local state, then exports asynchronously and idempotently to the authoritative Audit Broker. Export backlog is an operational security signal.

## Interaction Kernel / privileged agent

Privileged effects are sent as typed, scoped, expiring, idempotent commands. The outbox worker reconstructs each command from canonical state and verifies the stored digest before transmission. Receipts are validated and minimized before storage/audit. Unknown upstream fields are discarded.

## SecurityDiag

SecurityDiag is the independent qualification boundary for policy/detector/release evidence. It diagnoses and gates; it does not receive enforcement credentials.

## Transport

Outbound HTTP integrations use bounded connect/read/write/pool timeouts, connection pooling, strict TLS validation, optional mTLS, bounded responses, retry only for idempotent requests and a circuit breaker. Upstream response bodies are not copied into errors.
