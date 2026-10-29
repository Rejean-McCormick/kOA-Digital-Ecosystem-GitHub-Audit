# Offline Auditing

The default mode is **`LOCAL_OBSERVE`**. It reads directories you explicitly select; it does not clone repositories, access GitHub, execute project code, install dependencies, run CodeQL, test CI, or fetch CVE information.

## Discovery and binding

1. Search the selected root folder for Git working trees using bounded traversal; do not follow directory symlinks.
2. Attempt to map each repository to the **49-name bundled inventory** using its Git remote when available, and unambiguous fallback information where appropriate.
3. Report ambiguous duplicate local copies separately, rather than selecting or deleting a copy automatically.
4. If you choose the option to scan all discovered repositories, include locally discovered repositories outside the 49-name reference; otherwise use `--only-inventory`.

## Inspection scope

- GitHub Actions workflow file presence and potentially unpinned `uses:` references.
- Local CodeQL declarations and Dependabot configuration **presence**.
- Dependency manifests and lockfile presence, not vulnerable-version determinations.
- Bounded scans for certain potential credentials, Python coding risks, and TLS bypass APIs.
- File counts, files inspected, bytes inspected, and partial-inspection indicators.

The scanner records filenames, paths, line numbers, rule IDs, and limited metadata in the local report. It intentionally does **not** include sensitive string values or full source files.

## Read statuses correctly

| Status | Interpretation |
| --- | --- |
| `INSPECTED_NO_PATTERN_MATCH` | Nothing matched the configured heuristic checks within inspected scope |
| `REVIEW` | An observation warrants contextual review |
| `PARTIAL` | Parts of the working tree could not be fully inspected |
| `NOT_DETERMINED` / `NOT_PERFORMED_OFFLINE` | This audit did not establish the answer |

These are **observation statuses**, never release/security approval. For a real finding, use [Triage and Evidence](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Triage-and-Evidence).

## Outputs

- `audit.json`: structured local observation, including per-repository entries and local paths.
- `audit.csv`: spreadsheet-friendly summary (with CSV formula safety handling).
- `SUMMARY.md`: human-readable aggregated report and limitations.

Keep raw outputs local unless you have reviewed their metadata for sensitivity. The public dashboard uses a separate allowlisted aggregate format.
