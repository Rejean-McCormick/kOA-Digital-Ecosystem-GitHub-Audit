# kOA Digital Ecosystem — Audit Wiki

Welcome to the English-language documentation for **kOA-Digital-Ecosystem-GitHub-Audit** (v0.7.1).

The application provides **offline, read-only observation** of a reference inventory of 49 kOA repositories, targeted evidence review, engineering and security profiles, a manual architecture/security checklist, and a public-safe aggregate dashboard.

## Choose a workflow

| Goal | Guide |
| --- | --- |
| Open the app on Windows | [Quick Start](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Quick-Start) |
| Find and inspect local repositories | [Offline Auditing](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Offline-Auditing) |
| Interpret an audit finding | [Triage and Evidence](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Triage-and-Evidence) |
| Track engineering and security profiles | [Repository Profiles and Checklist](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Repository-Profiles-and-Checklist) |
| View and publish aggregate metrics | [Dashboard and Publishing](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Dashboard-and-Publishing) |
| Import previous kOA diagnostics | [Historical Diagnostics](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Historical-Diagnostics) |
| Understand boundaries and formats | [Architecture and Trust Boundaries](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Architecture-and-Trust-Boundaries) |
| Use command-line functions | [CLI Reference](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/CLI-Reference) |
| Fix launch or preview problems | [Troubleshooting](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Troubleshooting) |
| Publish these wiki pages | [Wiki Publishing](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki/Wiki-Publishing) |

## The central principle

**Observed ≠ verified ≠ certified.** A repository may have a workflow configured without successful runs, no heuristic matches without being secure, and an engineering profile without being feature-complete. Unavailable or unreviewed data stays explicitly **unknown / not assessed**.

**Local inspection never modifies source repositories.** GitHub Pages and GitHub Wiki publication are separate, optional user actions using existing Git permissions.

## Current scope

- Inventory reference: **49 repositories** in `data/initial_inventory.json` (bundled snapshot, not a live authoritative inventory).
- Engineering/security checklist: **33 architecture patterns + 53 security patterns = 86 practices**.
- Initial profile folders: `Konnaxion`, `Orgo`, and `kOA-Linux-Koali`.
- Windows desktop launcher: `kOA_GitHub_Audit_Launcher.pyw`.
- Browser dashboard: `docs/index.html` (logo and `#1e6864` brand color).

The [README](https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/blob/main/README.md) provides the short overview. This Wiki is the detailed user and maintainer reference.
