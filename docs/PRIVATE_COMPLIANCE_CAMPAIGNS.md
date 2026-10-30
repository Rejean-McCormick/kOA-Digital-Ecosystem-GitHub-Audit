# Private, dated compliance campaigns (v0.12.0)

A **campaign** is an explicitly created, dated snapshot of available evidence and manually reviewed decisions. It is **not** a certification, a Git tag, a release, a backup of every source file, or a live link to the head of a repository.

## Why this exists

Software changes. A qualification statement should always say **what was observed, at what date, for which scope and using which source**. This feature preserves the selected evidence as it was when the campaign was created, instead of allowing a later `git push` or an edited local document to silently change past reports.

## Capture workflow (Windows, no GitHub token)

1. Extract and launch `kOA_GitHub_Audit_Launcher.pyw`.
2. Review the five independent qualification milestones and the 86 manual architecture/security practices. Unassessed is the default; a static finding or a missing tool cannot mark a stage failed.
3. Open **Campagnes datées**. Name the campaign, for example `Bilan de référence — octobre 2026`.
4. Select an **existing** local `audit.json` to import the historical Git SHA and statistical observations. You can leave the report blank, but then historical SHA links may be unavailable. **Do not run the entire audit again merely to create a campaign.**
5. Optionally use **Joindre une preuve…** for an existing JUnit XML, coverage XML/JSON, SARIF or supporting report. Review the document before attaching it; the original file content is copied into the private campaign ZIP. Nothing is auto-uploaded.
6. Click **Créer une campagne figée** and confirm. The tool reads existing local documents and, where paths from the audit report remain available, checks only local Git metadata (`HEAD`, `origin` and tracked working-tree status). It never checks out a revision, downloads code, runs project tests or accesses GitHub.
7. Double-click the campaign to open the private history in the browser. Click a repository for its **dated detail page** (five manual milestones, reviewed practices, Kristal associations and sources), its frozen Engineering Profile, or the pinned commit/download ZIP links.

## Stored independently of the application

Windows: `%LOCALAPPDATA%\kOA-GitHub-Audit\campaigns\`

Each creation produces two files:

```text
20261030T120000Z-0123456789ab.zip
20261030T120000Z-0123456789ab.zip.sha256
```

The ZIP contains `campaign.json`, a manifest of SHA-256 hashes, copies of the available Engineering/Security Profiles for the 49 official repositories, a timestamped semantic Kristal projection (not raw catalogs), manual assessment states, and **only explicitly attached proof files**. The existing audit JSON is **not** copied into the ZIP: only allowlisted counters and Git version identifiers are frozen. The ZIP and its `.sha256` sidecar are stored outside the application's extracted installation directory.

The integrity checker validates the external SHA-256 and each internal file. This detects accidental changes, but **SHA-256 alone is not a digital signature and does not prove the original author**. For stronger long-term assurance, keep an independent offline backup and consider signing a copy of the manifest.

## Source-version links, with precise limitations

For a Git SHA documented in the historical local audit, the campaign records:

- `https://github.com/OWNER/REPO/commit/FULL_SHA`
- `https://github.com/OWNER/REPO/archive/FULL_SHA.zip`

Historical SHA references are labeled **reported during the audit**, not automatically verified as clean source trees. If an accessible local clone has a matching, unambiguous GitHub `origin`, a *separate* current local HEAD and tracked working-tree status is recorded. If there are tracked changes, the working tree cannot be treated as identical to HEAD. Untracked/ignored files and submodules are not asserted identical even when tracked files are clean.

GitHub generates commit ZIPs on demand. If the SHA is deleted or becomes unreachable after a force push or repository deletion, the URL may stop working. GitHub may also regenerate ZIP archives with a different binary layout although the extracted source contents are the same. For mission-critical history, retain an independent source ZIP or a protected release asset, under your own access and retention policy. The campaign feature deliberately does not archive full source repositories automatically.

Profiles previously measured from `EP.zip` retain their **separate snapshot SHA-256 provenance**, not a fabricated Git SHA. A profile and a Git audit can refer to **different snapshots**.

## Evidence levels — what is automated and what is not

| Source or tool | What the campaign automatically preserves | What it does **not** claim |
| --- | --- | --- |
| Existing local audit JSON | Scoped counts, historical recorded SHA | Confirmed vulnerabilities, complete CVE coverage, passing CI |
| Engineering Profile / RepoSurveyor | Measured counts and original dated profile | Quality grade, functional completion, production readiness |
| Local Git | HEAD, matching `origin`, tracked changes | Clean untracked files, reproducible build, remote availability |
| Local Kristal catalogs | Frozen canonical counts, repository/component associations, labeled candidates, selected semantic relationships, source-catalog SHA-256 | Tested integration or certification; absence of association is not a defect |
| Manual five-stage qualification | Explicit status, scope, evidence reference, review timestamp | An inferred maturity score |
| Manual 86-practice checklist | Explicit states and notes | Universal applicability or automated scoring |
| Explicitly added JUnit XML | Declared test/failure/error/skipped counts | Tests were executed by the campaign or correspond to stored SHA |
| Explicitly added coverage XML/JSON | Reported line coverage | Report is fresh or coverage was rerun |
| Explicitly added SARIF | Observed static-analysis result counts | All results are real vulnerabilities |
| `scc`, Lizard, Ctags (optional local tools) | Outputs can be attached after a separate intentional measurement | Tools are installed, executed or verified by the campaign |
| Integration tests / E2E / deployment checks | Existing results may be attached explicitly | Automatic test execution or production qualification |

**Execution is an explicit, separate decision.** Tests, containers, migrations, installations and runtime/security probes can alter a working tree or external environment. This tool does not execute them automatically. Run appropriate tools on an isolated checkout or CI environment and import their results as evidence with the source revision and execution context documented.

## Privacy and publication

Campaigns are **private local files**. The GitHub Pages publication flow uses a fixed allowlist of `docs/` assets and aggregate data; it does not include `%LOCALAPPDATA%`, `campaigns/`, the private assessment registry or attached evidence. The localhost browser uses loopback-only private routes; opening it does not publish evidence. Review documents before sharing a ZIP yourself.

## Long-term operational guidance

A useful cadence is to create a campaign at a meaningful milestone: architecture baseline, first complete implementation, integration qualification, release candidate or pre-production validation. Keep snapshots comparable through stable claim IDs, dates, scope and the same measurement methods. If you correct a past interpretation, record a **new dated campaign** explaining it; don't silently overwrite the old capture.

## v0.11.0 — Guided local measurement (optional, read-only)

Open **Campagnes datées** in the Windows launcher. There are now two independent measurement buttons:

1. **Mesurer ce clone**: choose an exact folder for the selected canonical repository. The collector verifies that its Git `origin` matches `OWNER/REPO` before reading tracked-file metadata.
2. **Mesurer clones de l’audit**: select an existing *local* `audit.json` referencing folder locations. The collector will attempt only those folders which still exist and match the expected Git origin; missing and ambiguous folders are skipped without affecting any repository score.

The default is **metadata only** (Git HEAD, tracked worktree state, tracked file count and bytes, language extension counts, documentation markers and number of GitHub Actions workflow definitions). This has low impact and does not copy raw files. If you explicitly enable the checkbox, the collector may additionally run installed `scc`, Lizard and Universal Ctags in read-only scanning mode, recording line/complexity/symbol summaries. Each tool has a 75-second timeout and an 8-MB maximum collected output; a timeout or unsupported output is shown as *unavailable*, never *non-compliant*. A **Cancel after current repository** control interrupts bulk processing between repositories; a currently running optional tool may continue until its timeout.

The resulting private JSON files are stored separately in:

```text
%LOCALAPPDATA%\kOA-GitHub-Audit\evidence_runs\
```

The GUI stages them as attachments for the *next* campaign after your confirmation. Review any private attachment before sharing a ZIP. The collector never calls `git fetch`, `git checkout`, `git commit`, `git push`, CI, containers, project tests or application entrypoints, and does not access GitHub. **Measuring a working tree is not equivalent to measuring the old commit SHA** when files have been changed, untracked or ignored.

## v0.11.0 — Provenance and accessible evidence

On the local historical app page, follow any attached proof's name to open a private, escaped preview. PDFs are offered as downloads. The original attached files can be downloaded from the verified ZIP through loopback-only URLs and are never served as executable HTML. The reader rejects missing, mismatched or manipulated proof entries and checks both the archive SHA and manifest.

Version provenance is deliberately **three independent claims**:

- **Historical audit commit**: a SHA reportedly observed by a prior audit; pinned GitHub link generated but not checked online.
- **Present local Git commit**: HEAD and verified origin read at campaign creation; notes whether tracked worktree files were changed. Git SHA comparison may be *same*, *different*, *only one reference* or *unknown*.
- **Profile or imported proof provenance**: the profile's independent snapshot SHA-256 or collector report's explicitly *reported* Git HEAD. A matching SHA observation cannot demonstrate that an imported report was produced from exactly those clean sources or that its tests were executed. The UI preserves that uncertainty.

The campaign shows manual qualification states and scope, plus a separate visual five-stage bar chart. These bars show **counts of manually evidenced claims among the 49 official repositories**, not development completion. Missing or not-applicable claims do not count as a negative grade.

## v0.11.0 — Reliability and growing history

Creation checks **100 MB of total uncompressed evidence**, a **100 MB ZIP limit**, **500 archive entries**, **8 MB per member** and a maximum **15 attached proofs per repository**. It refuses oversize requests *before finalization*. The temporary archive is fully verified (internal hashes and archive structure) before creating the final exclusive ZIP and SHA-256 sidecar. Existing campaigns are never replaced. An unexpected crash between the two final files can leave an incomplete pair visible as invalid, never as a verified campaign.

The campaign listing uses an in-process cache keyed by ZIP and checksum modification metadata so hundreds of stable campaigns can be listed without repeatedly verifying every member; modifications force re-verification. Opening, viewing or downloading a campaign always performs fresh full SHA-256 and internal manifest verification. The dashboard provides a comparison link to the previous dated campaign, with per-stage counts and changes in documentation, explicitly reviewed practices, frozen engineering profile availability and pinned commits. These comparisons do not silently revise or re-certify the old snapshot.

**Not automatic:** executing potentially state-changing CI/test suites; verifying that the distant commit remains downloadable; long-term secure backup or digitally signing archives; proving production deployment. For those, explicitly run tests in isolation, attach the results and preserve an independently backed-up source archive or protected release if retention is important.


## v0.11.1 — Quiet Windows progress

The Tkinter launcher shows stable, determinate progress for campaign collection and creation. Repository collection uses actual processed/selected counts; campaign creation advances for each frozen repository, explicit proof integration, archive construction, internal validation, and atomic publication. The bar reaches completion only after post-publication verification. Long operations without an evidence-based unit of work show a static in-progress state, not a fake percentage or flashing indicator.

All application-managed child processes now use Windows-specific hidden-console creation flags (`CREATE_NO_WINDOW` and `STARTF_USESHOWWINDOW` / `SW_HIDE`), while retaining explicit argument vectors, no shell, timeouts and the existing read-only boundaries. Native authentication dialogs and user-triggered file selectors are unaffected.

## v0.12.0 — Approved report discovery and private progress

See [Evidence automation and dated progress](EVIDENCE_AUTOMATION_AND_PROGRESS_V012.md) for the bounded discovery allowlist, explicit import consent, changed-file protection, per-proof Git provenance and latest-campaign atlas. Older campaign archives require no migration.
