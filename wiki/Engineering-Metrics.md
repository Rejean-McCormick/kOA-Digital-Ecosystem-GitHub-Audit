# Engineering Metrics: What They Mean

The dashboard shows useful **descriptive** metrics, not a synthetic maturity or security grade.

## Size and structure

- **Discovered files**: files enumerated in the bounded local inspection. This is not the complete authoritative size of every repository.
- **Inspected files and bytes**: files and content the local scanner actually checked. Files excluded by limits remain unverified.
- **Size buckets**: rough groups by enumerated file count; they do not measure complexity or project value.
- **Configured controls**: presence of workflows, dependency manifests, Dependabot configuration, or CodeQL configuration. Presence does not mean the control ran successfully.
- **Structuring bands**: a dashboard heuristic based on a few visible controls. These are **not** manually assessed checklist statuses or official completion scores.

## RepoSurveyor engineering profile

The supplied RepoSurveyor profile is designed for **engineering surface characterization**. It may report:

- active files, source files, tests, documentation, migrations, schemas;
- production/test nonblank physical source lines, not necessarily logical code lines;
- languages and structural areas;
- static probable routes and test declarations (not executed tests);
- optional `scc`, Universal Ctags, and Lizard measures;
- optional Lizard cyclomatic-complexity distribution and evidence limitations.

An active engineering surface excludes common noise such as archives, snapshots, caches, dependency directories, and private local configuration. An absent optional analyzer does not justify a guessed value.

### Actual measurement source (v0.8.0)

The 13 bundled engineering profiles are derived directly from the supplied **October 29, 2026 snapshot batch (`EP.zip`)**, using the RepoSurveyor 1.0 engine with documented backup/index exclusions. Twelve repositories are included in the official inventory; one supplemental profile is listed separately.

Each profile includes source snapshot SHA-256, static test declarations, structural footprint, active languages and configured controls. This does **not** verify current Git state or successful test runs. Optional Lizard, `scc` and Ctags analyzers were unavailable, so their statistics are omitted rather than estimated.

The previous Konnaxion measurements from September remain separate as historical evidence and are not treated as a comparable controlled trend.

## Quality is not a single number

A heuristic signal count can help prioritize review, but **0 signals ≠ 0 vulnerabilities** and **many signals ≠ poor code**. An application may be large and well tested yet have more potential matches due to its code volume. Treat security, architecture, complexity, testing, and feature completion as **different dimensions**.

For a decision about an individual practice, use [Repository Profiles and Checklist](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Repository-Profiles-and-Checklist).
