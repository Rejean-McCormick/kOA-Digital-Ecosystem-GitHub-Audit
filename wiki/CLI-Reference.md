# CLI Reference

Run commands from the extracted project root. Python **3.11+** is required.

## Local only (no GitHub API)

```powershell
# Discover local Git repositories
python -m koa_audit local-plan --root "C:\mycode" --max-depth 4

# Scan local repositories into a new report set
python -m koa_audit local-audit --root "C:\mycode" --max-depth 4 --out reports

# Restrict scanning to the bundled inventory
python -m koa_audit local-audit --root "C:\mycode" --only-inventory --out reports

# Recheck existing findings, generate sanitized ZIP
python -m koa_audit local-triage --root "C:\mycode" --audit-json reports/audit.json --out reports/triage.zip

# Generate safe public-dashboard aggregate locally, without pushing
python -m koa_audit dashboard-publish --audit-json reports/audit.json --out docs
```

### Useful arguments

| Argument | Applies to | Meaning |
| --- | --- | --- |
| `--root` | `local-plan`, `local-audit`, `local-triage` | Local directory containing the relevant Git trees |
| `--max-depth` | Local commands | Bounded search depth; default 4 |
| `--limit` | `local-plan`, `local-audit` | Limit the number of repositories for a pilot |
| `--max-files` | `local-audit` | Per-repository inspection file budget; default 6000 |
| `--only-inventory` | `local-audit` | Exclude discovered repositories outside the 49-name reference |
| `--audit-json` | Triage/dashboard | Existing report to process; avoid rescanning |

## Publication (explicit remote write)

```powershell
# Uses existing Git for Windows credentials
python -m koa_audit dashboard-sync
```

This command should only update aggregate dashboard data and the Pages deployment workflow in the audit repository. It does not force-push or change source repositories. Git permissions and initial Pages configuration can block publication.

## Historical imports

```powershell
python -m koa_audit import-legacy --tool <catalog-tool> --repo "owner/repository" --input path/to/summary.json --out reports/historical.json
```

The family identifier must be one supported by the actual CLI catalog. Use `python -m koa_audit import-legacy -h` to list values.

## Optional remote GitHub observations

The older `plan` and `audit` subcommands read remote API data. They are **optional** and unrelated to local auditing. Rate limits and missing permissions can produce `unknown` rather than an answer. Do not interpret unavailable alert counts as zero.

## Tests

```powershell
python -m unittest discover -s tests -v
```
