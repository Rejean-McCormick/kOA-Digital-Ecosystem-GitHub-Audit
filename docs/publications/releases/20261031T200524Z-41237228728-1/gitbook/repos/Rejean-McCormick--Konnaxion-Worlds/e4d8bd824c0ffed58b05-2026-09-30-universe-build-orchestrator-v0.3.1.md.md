<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion-Worlds/blob/0e8d47c147d13a5721c5ae8e4b1dd7968def51fb/docs/status/2026-09-30-universe-build-orchestrator-v0.3.1.md | commit: 0e8d47c147d13a5721c5ae8e4b1dd7968def51fb | SHA-256: 897a20a9278cd66878fde7ec266319c61506bc297efbdde4e98d3fae67145da8 -->

# Universe build orchestrator v0.3.1

Follow-up hardening from real Lévis multi-process build testing.

## Fixes

- Migration search-path isolation is transaction-local and transaction-pooler safe.
- One migration group is atomic, preventing committed partial DDL when a migration fails.
- Build failure persistence reconnects after broken PostgreSQL transactions.
- Local orchestrator fails fast on provider disk/project limits and DDL collisions instead of cascading through all pending jobs.
- Pending never-started local jobs remain queued for resume.
- Storage preflight estimates atomic-upgrade headroom when `neon.max_cluster_size` is exposed.
- New `worlds_storage` and `worlds_gc` management commands.
- World Manager exposes Storage and failed-release garbage collection actions.

## Operational constraint

Schema-per-release atomic Universe promotion temporarily requires old and new releases to coexist. Provider storage quotas are therefore a real build constraint; the orchestrator now exposes and checks this instead of discovering it late in migration DDL.
