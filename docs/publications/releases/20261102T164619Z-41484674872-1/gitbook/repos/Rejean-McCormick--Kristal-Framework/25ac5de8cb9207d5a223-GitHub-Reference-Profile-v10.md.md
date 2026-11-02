<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/GitHub-Reference-Profile-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 09aed634dc1dac825bbd06dae20d678fd5a255261c4e5d005a3cc357d7085bc5 -->

# GitHub Reference Host Profile — v10

**Optional profile:** `kristal.host/github/1.0`. The Framework's v10 semantic commitments do **not** depend on GitHub.

| Kristal concept | Reference GitHub surface |
| --- | --- |
| account integration | public `.github` integration repo |
| node host / collection | repository |
| proposed change | pull request |
| qualification | GitHub Actions / checks with bound receipt |
| immutable publication | verified Release and assets |
| materialization distribution | GitHub Release assets and/or GHCR (host policy) |
| activation surface | deployment / environment or equivalent pointer |
| discovery | dedicated directory node/repo |

## Recommended network topology

```text
account
├── .github                 (public integration)
├── private root directory (authoritative all-node discovery)
├── collection-public      (one or more public Kristals)
└── collection-private     (confidential Kristals)
```

A collection repo can hold **many** Kristals; use repository boundaries for lifecycle, permissions, cost and ownership, not as a forced 1:1 mapping to semantic artifacts.

## Bootstrap-managed node

```text
.kristal/node.json
.kristal/bindings/github.json
.kristal/capabilities.json
.kristal/bootstrap-state.json   # managed operational fingerprints
.github/workflows/...           # qualify, publication, collection ingest
```

Bootstrap's managed workflows pin their Framework checkout and external Actions to full commit SHAs. Qualification is read-only and bound to a candidate commit. Publication verifies local and downloaded bytes before finalizing an immutable Release. A required Environment is enforced only if explicitly configured as `required`; best-effort is not the same guarantee.

GitHub's plan-dependent features must degrade explicitly and must not alter v9 semantics. Public-node workflows need a readable Framework reference without embedding reusable secrets.

See [[Workflow-GitHub-v10]], [[GitHub-Read-Surfaces-v10]], [[Security-and-Confidentiality-v10]].

*Normative profile source: Framework `spec/v10/GitHub-Reference-Profile.md` and `profiles/github/schemas/`.*
