# Engineering Profiles — Snapshot Batch (2026-10-29)

## Inputs

The user-supplied `EP.zip` contains 13 nested `*_Code_snapshot.zip` archives and corresponding index files. The snapshot indexes identify their capture times on October 29, 2026. Archives were analyzed as extracted read-only reference data in the processing workspace; no source repository was modified.

## Method

The supplied RepoSurveyor 1.0 `survey_project` and `render_profile` implementation was used consistently across all snapshots. It classifies source, test and documentation files, excludes recognized caches / generated files / private configuration, measures nonblank source lines, identifies likely routes and static test declarations and recognizes engineering control configuration files. To avoid counting backup copies as active production source, the processing applied two narrowly documented extra scope filters: `.koali-update-backups/**` (backup copies), and embedded `SMARTDUMP_INDEX.txt` / `snapshot_index.txt` (snapshot metadata).

Captured source snapshots are not guaranteed to include all files from the author's live filesystem or current Git revision. `EP.zip` contains **13** code snapshots, of which **12** are in the bundled 49-repository inventory and **1** is supplemental (`Konnaxion-Universe-Worlds-Manager`).

Optional analyzers (`scc`, Universal Ctags, Lizard) were absent in the measurement environment. The generated reports therefore **do not assert precision code/comment/blank line counts or cyclomatic complexity**. Production/test nonblank physical line counts include comments; static test declarations are not executed tests. CI configuration or test dependencies are evidence of setup, not a passing run. A coverage value not calculated from a fresh execution is not an assurance.

For provenance, each `PROVENANCE.md` includes the SHA-256 of its exact nested snapshot archive and the source index's capture time. Each `ENGINEERING_METRICS.json` contains only normalized fields; no raw source files or secrets are bundled with the generated profiles.

## Available profiles

See [`profiles/ENGINEERING_PROFILE_INDEX.md`](../profiles/ENGINEERING_PROFILE_INDEX.md) for the complete list and key statistics. The desktop application displays all measured profiles in its existing **Profiles & compliance** tab and keeps the 86 manual checklist criteria unassessed until the user makes an evidence-supported decision.

## Security and limitations

This is a scale and structure characterization—not a security scan, code audit, quality score, maturity score, or production readiness certification. Separate security profiles and issue reviews remain necessary. Keep snapshot archives private because they contain source files and may contain sensitive material.
