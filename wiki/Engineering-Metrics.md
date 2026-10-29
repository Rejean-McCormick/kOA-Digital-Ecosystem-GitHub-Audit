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

### Sample attribution warning

The bundled Konnaxion profile is **provisionally attributed** to that repository and measured on a September 2026 snapshot. Orgo and kOA-Linux-Koali currently have preliminary documentation rather than complete RepoSurveyor complexity profiles.

## Quality is not a single number

A heuristic signal count can help prioritize review, but **0 signals ≠ 0 vulnerabilities** and **many signals ≠ poor code**. An application may be large and well tested yet have more potential matches due to its code volume. Treat security, architecture, complexity, testing, and feature completion as **different dimensions**.

For a decision about an individual practice, use [Repository Profiles and Checklist](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Repository-Profiles-and-Checklist).
