<!-- Frozen source: https://github.com/Rejean-McCormick/Kompiler/blob/cf4836ccf2741b609c562254d09ba47d7e9a6187/docs/06-operations/failure-recovery.md | commit: cf4836ccf2741b609c562254d09ba47d7e9a6187 | SHA-256: 1bba1db90eaa0c3d45e4e43d7ca15913fecf40255888d7b60dd4d7d2da35027e -->

# Failure Paths and Recovery

## Failure classes

### Admission failure

No operation runs. Return `kompiler.error`.

### Single operation failure

Apply the node/request error policy. Record a deterministic receipt.

### Source integrity failure

Fail the affected operation. Do not fall back to an unverified source copy unless an explicit adapter policy defines such a fallback and exposes it in provenance.

### Timeout/resource cap

Terminate the operation, mark `truncated` or failed according to capability semantics, and never silently present incomplete results as complete.

### Compilation failure

Raw operation results MAY be retained for diagnostics under the retention policy, but no misleading successful Context Pack is emitted.

## Partial packs

A partial pack is allowed when:

- at least one requested branch succeeded;
- failed branches are explicitly listed;
- gaps include the missing branches;
- `status=partial`.

## Retry

Retries are disabled by default for deterministic local adapter failures. Transient adapters MAY advertise retryable error classes. Retry count/backoff is configured in trusted runtime policy, not supplied as arbitrary executable logic by the Query Plan.

## Crash recovery

Run state transitions SHOULD be transactional in SQLite. On restart, any `running` operation without a completion receipt becomes `abandoned`. The user may rerun the original Query Plan; cacheable completed nodes can be reused if their cache keys still validate.
