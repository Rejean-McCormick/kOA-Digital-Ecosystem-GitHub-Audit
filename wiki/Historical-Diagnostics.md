# Historical Diagnostics

The application can import metadata summaries from older kOA diagnostic families, including:

- KonnaxionDiag
- KorDiag
- KristalDiag
- LevelUpDiag-Orgo
- LevelUpDiag-Skope
- LevelUpDiag SemantiK Architect

The exact family options are provided in `config/legacy-source-catalog.json` and the `import-legacy` CLI choices.

## Import workflow

1. Open **Import historique**.
2. Select the diagnostic family and the explicit `owner/repository` binding.
3. Choose a metadata summary JSON, or specify an exact JSON member in an archive.
4. Select an output location and import.

CLI example (replace the tool choice with a valid catalog entry):

```powershell
python -m koa_audit import-legacy --tool <catalog-tool> --repo "owner/repository" --input path/to/summary.json --out reports/historical.json
```

Import is **metadata-only** and preserves provenance. It does not rerun old diagnostics or verify past cryptographic evidence. An old `PASS` must never be treated as today's GitHub security status or as release authorization.

Use local audit and triage for current observations, and keep historical qualifications in their original context.
