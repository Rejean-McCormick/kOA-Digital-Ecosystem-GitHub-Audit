# Frequently Asked Questions

### Do I need a GitHub API token?

**No** for local discovery, offline scanning, triage, profile reading, manual assessments, and local dashboard generation. Optional GitHub publishing uses existing Git credentials; optional remote API observations are a separate feature.

### Will the application change my 49 repositories?

No. Local scans, triage, and profile imports operate read-only on source repos. Profile imports write inside the **audit application**, and dashboard/wiki publication targets their respective audit documentation repositories only.

### Is a repository with zero findings secure?

No. It means none of the configured patterns matched in the inspected scope. Security status needs additional validation and possibly CodeQL, dependency advisories, runtime tests, or manual review.

### Does a high file count mean a repository is nearly complete?

No. File counts describe size, not functional completion. Use engineering profiles to understand scope, and the manual checklist to document evidence-based assessments.

### Does `Appliqué` mean automatically certified?

No. It is a human-selected checklist status; it should carry an evidence reference and does not authorize release.

### Why are some profiles marked preliminary?

Konnaxion has a supplied RepoSurveyor engineering profile with an attribution caveat. Orgo and kOA-Linux-Koali currently have preliminary records without invented complexity or test-execution numbers.

### Should I rerun the whole audit after fixing one issue?

Not just to confirm that issue. Use **Vérification + ZIP** to check the targeted paths and compare with the previous audit.

### Why is GitHub Pages not showing my newest scan?

The dashboard is snapshot-based. Your desktop cannot stream files to Pages. Publish an updated **aggregate** from the existing report after reviewing it; the site refreshes periodically once deployed.

### Is the GitHub Wiki the same as GitHub Pages?

No. The Wiki is a separate Git repository holding documentation, while Pages serves the `docs/` dashboard. They are published independently.
