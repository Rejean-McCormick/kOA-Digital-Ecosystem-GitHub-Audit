# Operations and review checklist

## Weekly cycle

1. Verify inventory commit and count, including public new-repository discovery.
2. Inspect repositories with metadata access unknown, partial alert responses or CodeQL coverage unknown/stale/not observed.
3. Review open alert counts and severities on GitHub itself; reports intentionally omit alert details.
4. Review CI metadata and last observed default-branch run. A successful run is not proof that every workflow succeeded.
5. Track results over time externally if desired; v0.1 produces isolated per-run artifacts, not a persistent database.
6. If importing diagnostic results, confirm the target repository and exact source JSON; do not reinterpret old verdicts as current assurance.

## Decision and escalation

This repository **cannot** approve releases, activate runtime packs, accept risks or edit target repositories. Operators use findings to open owner-reviewed issues in the appropriate repositories through their existing governance processes; automated actions are not implemented.

## Important limitations

The workflow observes only what its token can read. Private owner-discovery is deliberately not supported; declared inventory is always the scope. The newest 100 default-branch runs and CodeQL analyses are bounded samples. The 1,000-alert cap per feature can render counts partial. GitHub Actions workflows might be valid but not run on the default branch. `source_status` describes snapshot provenance only. No actual security run was performed when this project ZIP was built.
