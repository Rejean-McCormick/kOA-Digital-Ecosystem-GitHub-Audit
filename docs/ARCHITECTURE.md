# Architecture, data boundaries and trust

```text
kOA-Digital-Ecosystem (owner of declared inventory)
         | pinned Git commit, inventory SHA-256
         v
kOA-Digital-Ecosystem-GitHub-Audit (observer only)
   |-- GitHub API: repo metadata / Actions / code-scanning analyses
   |-- GitHub API: open alerts by category (no secret values)
   |-- Optional historical metadata: KonnaxionDiag / KorDiag / KristalDiag
   |                                LevelUpDiag-Orgo / SemantiK / Skope
   v
Sanitized audit.json + audit.csv + SUMMARY.md (private artifacts)
```

This repository implements only **OBSERVE**. There is no `ENABLE`, `REMEDIATE`, write API, repository dispatch, cross-repo workflow execution or target-side code checkout. The `GET`-only GitHub client should remain a mechanically testable boundary.

## Provenance and non-escalation

- Source inventory in bundled JSON has `authoritative_live=false`, regardless of snapshot quality.
- Live inventory is read from the GitHub source repository by SHA-pinning `GET /contents/...?...ref=<commit>`. Capture both commit and SHA-256 for each observation run. A pinned read is not a semantic authorization.
- Target repositories remain independently owned; reading their metadata grants no Git operations or release rights.
- CodeQL alerts and CodeQL analyses are distinct. Zero open alerts without default-branch analyses means **not observed as scanned**.
- Latest 100 code-scanning analyses are a sample, not complete language/branch coverage. `unknown` may mean insufficient access, feature disabled, or incomplete pagination.
- Default-branch CI runs sample at most the newest 100 observations; do not present this as a complete CI history. Other branches, external CI and local-only diagnostics may exist.
- API permissions are not security assurance. A permission error is an observation gap.

## Historical evidence mapping

Importer discards free-text findings and environment paths. It keeps the source JSON SHA-256, original schema, run/campaign id, verdicts, level ids, number of findings and *declared* digests. The digest is a claim from the historic report, not independent verification. Reports retain `evidence_independently_verified=false` even when digest fields are populated. Crypto verification must be owned by the respective diagnostic or dedicated verifier.

The correct binding is **audit target**, not diagnostic tool repository. Human confirmation required for import; no heuristic matching. Historical records never influence the current GitHub security alert totals or present-day `coverage` fields.

## Status vocabulary

- `ok`: endpoint returned all pages inside configured caps.
- `partial`: endpoint returned bounded results, but more pages exist.
- `unknown`: API inaccessible, unsupported, network error or missing evidence.
- `recent`/`stale`: age classification for an observed CodeQL analysis on the default branch only.
- `not_observed`: no CodeQL in the consulted full first-page analysis set, not proof CodeQL is disabled.

A snapshot's status is not evidence that the live GitHub HEAD, deployments or runtime configurations match it.
