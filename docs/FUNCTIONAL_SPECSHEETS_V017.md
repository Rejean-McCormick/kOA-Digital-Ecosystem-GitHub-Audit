# Functional specification sheets — v0.17.0

The first dashboard workspace now starts with **what each application does** rather than with a single ambiguous "Security 0/53" score. It has two primary levels:

1. **Fonctionnalités** (audience-facing capabilities): manage universes/worlds, import/verify capsules, authenticate the local agent, perform release admission, run diagnostics, etc. Related evidence is grouped by user-facing purpose.
2. **Technologies** (developer-facing subsystems): languages/frameworks, API/contracts, data/storage, identity/access, security enforcement, real-time exchange, and tests. Each entry has its source file path and SHA-256 fingerprint.

The existing **Tests, Sécurité, Architecture, Implémentation, Intégration, Production, Composants Kristal** sections remain available. The 53 security and 33 architecture patterns are review **criteria**, not a score or automatic result.

## Audited source snapshots

The functional analysis was curated from three owner-supplied snapshots dated 2026-10-30 (the SHA-256 of each source ZIP and every referenced member is in `private_evidence/KOA-SPECSHEETS-2026-10-30.json`):

| Application | Source-supported features | Technology/subsystem entries | Actual targeted test results |
|---|---:|---:|---|
| KonnaxionDiag | 4 | 5 | **3 / 3 passed** (`tests/test_core.py`, `tests/test_signing.py`) |
| Konnaxion-Capsule-Manager | 6 | 6 | **42 / 42 passed** (`tests/test_security_gate.py`) |
| Konnaxion-Worlds | 6 | 6 | No tests executed for this snapshot (Django/PostgreSQL dependencies not provided in the execution environment) |

Test results were produced on **temporary copies of the supplied ZIPs**, not on the owner's live worktrees or on GitHub's current branch. The suite was `pytest` in a Linux/Python 3.13 environment. The sanitized JUnit XML files are under `private_evidence/test_reports` with their exact SHA-256 values in `KOA-TEST-EXECUTIONS-2026-10-30.json`. They are opened from **local-only** routes `/local/spec-tests/<repo>`. No secret, original source files, arbitrary executable or network call is needed for dashboard browsing.

The **42 Capsule Manager tests** cover a selected unit-test suite around Security Gate contracts, and do **not** confer PASS on all 53 security practices. The **3 KonnaxionDiag tests** cover command-subprocess behavior/timeouts and detached Ed25519 signature verification, not the entire diagnostic or deployment product. A definition of a test, a service, or a protocol is not a passed execution.

## Example distinctions that must never collapse

- **Secure account creation:** The Capsule Manager snapshot contains local Agent authentication through bearer token and constant-time verification. This does **not** establish a public sign-up workflow, password policy, OAuth/OIDC implementation or MFA.
- **Messaging:** Konnaxion-Worlds contains a WebSocket session/world resolver and tests defined for scoping, not an established end-to-end user messaging feature.
- **Voting:** A `smart-vote` scenario manifest exists in Konnaxion-Worlds. A scenario configuration does **not** establish a running vote engine, a cast ballot or a verified tally.
- **CI status:** A historical green GitHub workflow only describes that workflow on the observed SHA; it does not prove every functional feature or all security practices.

## Status semantics

- **Code observed**: source file and relevant implementation inspected; deployment, integration and runtime result **not validated**.
- **Scenario/specification observed**: configuration or specification is present; implementation and runtime **not validated**.
- **Targeted test PASS**: the exact named tests executed successfully on the archived ZIP source, tied to that snapshot's hash and sanitized JUnit report. **Not a whole-feature or application certification**.
- **Source not yet reviewed**: a per-repository functional spec has not been curated. It says nothing about whether a feature is present or about its quality.
- **Documentary qualification backed by the historical evidence review**: this is independent of the targeted test result and applies only to its recorded scope.

The source snapshots do not establish a matching Git commit SHA. Their metadata is intentionally not repinned to today's HEAD. For preservation, **new private dated campaigns** archive the reviewed functional-spec index, test manifest and JUnit XML, marked `linked_to_current_commit=false`. Existing campaigns remain immutable and backward compatible.

## Privacy and extension

`private_evidence/` must never be copied to the GitHub Pages publication directory. The standard page contains only an empty placeholder in public mode; the local loopback handler serves the reviewed specs and test logs. To add more applications, supply a dated snapshot of source and relevant test logs, or collect targeted JUnit/coverage results with an explicit provenance record. Do not guess capability or success from a name or filename.
