# kOA-Digital-Ecosystem-GitHub-Audit

> **Local, read-only repository auditor for the kOA Digital Ecosystem. No GitHub token or internet connection required.**

## Getting started (Windows)

1. Extract the **entire** ZIP to a normal folder (never launch directly inside the ZIP).
2. Install Python 3.11+ with Tkinter (normally included in the official Windows installer).
3. Double-click **`kOA_GitHub_Audit_Launcher.pyw`**.
4. In **Audit local**, choose the folder containing your local Git repositories, e.g. `C:\mycode`.
5. Click **Découvrir les dépôts locaux**, then **Scanner localement**.
6. Open **Rapports** to read `SUMMARY.md`, `audit.csv` and `audit.json`.
7. Open **Vérification + ZIP**, select the newly generated `audit.json`, and click **Contre-vérifier et créer le ZIP** to produce a sanitized evidence bundle.

No GitHub credentials are requested, loaded or transmitted by the local mode. The launcher deliberately defaults to local analysis. If it does not open, run `DIAGNOSTIC_LAUNCHER.cmd` for a visible Windows error and an external diagnostic log.

## CLI (also fully offline)

```powershell
python -m koa_audit local-plan --root "C:\mycode" --max-depth 4
python -m koa_audit local-audit --root "C:\mycode" --max-depth 4 --out reports
python -m koa_audit local-triage --root "C:\mycode" --audit-json reports/audit.json --out reports/triage.zip
```

Options: `--root` may be repeated; `--limit 5` limits inspections for a pilot; `--max-files 6000` controls per-repo inspection budget; `--only-inventory` excludes local repositories not in the 49-name snapshot. By default **all discovered Git repositories** are inspected, including previously unlisted projects. Reports are saved **only on your computer** under `reports/` (gitignored). The local scanner reads files and local Git metadata; it neither clones nor fetches repositories, runs target code, installs packages or modifies code.

## What the offline scanner actually checks

- Finds working trees under selected local roots (`.git` directory or worktree marker), with a bounded directory search and no symlink traversal.
- Matches them against a **snapshot inventory of 49 kOA repositories** (scope reference, not permission to modify). Reports missing and ambiguous matches separately.
- Inventories GitHub Actions configuration files, indicators of CodeQL declarations and Dependabot configuration. **Does not run CI or CodeQL and does not know if GitHub runs succeeded.**
- Inventories dependency manifests/lockfiles, counts files inspected and records a local Git commit when available. **Does not determine whether dependency versions have known CVEs.**
- Runs **bounded heuristic pattern checks** for suspected private keys, GitHub/AWS key patterns, some risky Python calls and select GitHub Actions misconfigurations. Reports file paths, line numbers and rule names, **never secret contents**. These are leads requiring review, not definitive vulnerabilities.
- Preserves support for importing historical KonnaxionDiag, KorDiag, KristalDiag, Orgo, Skope and SemantiK diagnostic summaries separately from current local findings. A historical `PASS` cannot turn a new scan into `PASS`.

For the 2026-10-28 Konnaxion-Capsule-Manager snapshot, the six original generic `verify=False` alerts were false positives. The corrected rule also surfaced a separate genuine TLS verification bypass in runtime HTTPS healthchecks, which requires a targeted code review; **the audit app does not modify the source repository**.

A clean local scan does **not** mean the code is vulnerability-free. It cannot replace a real CodeQL/Semgrep analysis, a dependency advisory database, the GitHub platform's secret-scanning engine or tests against an actual deployed environment. Unscanned, over-limit and missing content must never be treated as successful inspection.

## Report files and privacy

- `reports/audit.json` — full bounded metadata and heuristic findings, local locations and local HEAD hashes.
- `reports/audit.csv` — Excel-safe one-row-per-repository summary.
- `reports/SUMMARY.md` — coverage and caveats.

Source code is never copied to the report. Do not share reports publicly before checking local paths and operational information. The `.gitignore` excludes generated reports, evidence ZIPs, `.legacy/`, and the Windows helpers `ZmartZnap*.pyw` / `GitSink*.bat`.

## Offline triage evidence ZIP (v0.4.1)

The **Vérification + ZIP** tab rechecks the previously reported finding locations without re-running target applications. It uses the current local Git index to determine whether flagged files are tracked, identifies duplicate Git remote mappings, records GitHub Actions `uses:` references and SHA pinning, and inventories Git-tracked source files above the original 256 KiB scan limit. All checks are offline and read-only.

**v0.4.1 correction (TLS false positives):** A bare `verify=False` is **not** evidence of disabled HTTPS certificate verification. The local scanner now uses AST syntax inspection to identify direct HTTP client calls with `verify=False`, explicit `verify_tls=False`/similar flags, and `ssl._create_unverified_context()`; it ignores capsule verification options, comments, and strings. Historical `PYTHON_SSL_VERIFY_DISABLED` findings are requalified by the **Vérification + ZIP** flow as `NOT_A_TLS_BYPASS_API` or `TLS_BYPASS_API_STILL_PRESENT` without requiring another full audit. This remains a limited heuristic, not full security dataflow analysis.

The ZIP includes `TRIAGE.json`, a human-readable `SUMMARY.md`, `workflows.json`, `duplicates.json`, `sensitive_tracked_names.json`, and `large_files.json`. **No raw source code, environment file contents, secret values or whole workflows are ever packaged.** Local paths and repository metadata are present, so treat the bundle as confidential. Run the audit first; the local triage accepts only a `koa_audit.local_observation.v1` report and never overwrites an existing ZIP. A rule still matching a line is not a confirmed exploit, and a missing match does not prove a vulnerability was fixed.

## Historic diagnostic import

Select **Import historique** in the interface. Provide the diagnostic family, an explicit `owner/repo` target, a JSON summary (or exact member of a ZIP archive), and a local output folder. The import is metadata-only and preserves original schema/verdict provenance without re-verifying cryptographic evidence.

## Architecture and boundaries

- `kOA-Digital-Ecosystem` owns the architectural and repository scope reference.
- Individual diagnostics own their own level meanings and authoritative qualification logic.
- This repository owns only local, non-authoritative observation and aggregation (`LOCAL_OBSERVE`).
- No source repository is changed, no GitHub permissions are requested, no remote workflows are triggered, and the reports do not authorize releases.

The older optional CLI `audit` subcommand for remote GitHub API reads is retained for backward compatibility, but **is not used by the launcher or by scheduled automation**. The `local-audit` and `local-plan` subcommands never instantiate a GitHub client.

## Verification

```powershell
python -m unittest discover -s tests -v
```

Detailed instructions: [guide Windows](docs/LAUNCHER_FR.md), [local architecture](docs/ARCHITECTURE.md), [historical imports](docs/LEGACY_DIAGNOSTICS.md).

No open-source license has been selected.
