# Triage and Evidence

Use **Vérification + ZIP** when you already know which findings need attention. You can recheck existing reports **without running another global audit**.

## Process

1. Select your existing `audit.json` from the local audit run.
2. Select the local root folder that still contains the relevant Git working trees.
3. Run the targeted triage action in the launcher (or `local-triage` CLI).
4. Review the generated evidence ZIP; share it only with people who should see repository and local-path metadata.

```powershell
python -m koa_audit local-triage --root "C:\mycode" --audit-json reports/audit.json --out reports/triage.zip
```

## Included evidence (metadata only)

The ZIP includes `TRIAGE.json`, `SUMMARY.md`, `workflows.json`, `duplicates.json`, `sensitive_tracked_names.json`, and `large_files.json`.

It does **not** copy the raw `.env`, credential values, source files, or complete workflow files. However, the ZIP can still reveal local paths and repository metadata, so it is not automatically public-safe.

The triage rechecks whether a reported line still matches, checks Git tracking/ignore state for sensitive filenames, identifies duplicate remotes, and collects GitHub Actions reference/pinning metadata. It does not automatically repair code or prove a vulnerability.

## False positives and newer rules

A broad detection such as `verify=False` is not itself evidence of disabled TLS. The v0.4.1 improved local scanner uses Python syntax inspection to identify particular real TLS/HTTP bypass contexts and avoids comments, strings and unrelated verification flags. Older findings can be reclassified by targeted triage without rescan of all repositories.

Keep separate the following concepts:

- **Pattern still present**: the same syntax appears.
- **Risk established**: code context shows an exploitable or harmful behavior.
- **Issue fixed**: a relevant change was confirmed, not merely an ignored/missing file.
- **History retained**: a retired secret might still be in Git history even when tracking has stopped.

For credential exposure, treat rotation/revocation of affected credentials as a separate decision; this tool does not manage secrets.
