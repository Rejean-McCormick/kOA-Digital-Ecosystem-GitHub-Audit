# kOA — Evidence-based certification and continuous improvement

This document describes the **intended review model**, not an external certificate, legal compliance attestation or independent security audit.

## Governance source and scope

The model follows the supplied **kOA Digital Ecosystem** repository snapshot (2026-10-29) and local wiki archive. The repository's `docs/status/current.md` explicitly distinguishes:

> specified / architected ≠ implemented ≠ tested / qualified ≠ integrated with another owner ≠ production-proven.

Its **authority map** states which owner can make each decision. An audit repository does **not** replace the owner, release authority, security specialist or product qualification evidence.

Input provenance:
- `znapshot_kOA_Digital_Ecosystem_10291320.zip` — SHA-256 `feb7df99db37c106a920e04fdea7ac2ddd896ee6c48a2199c022946f9b0d0ec7`
- `kOA_Digital_Ecosystem.wiki (2).zip` — SHA-256 `912da74c3cdbde360aa460a9a7d7e8cedc02a2a530caae5adf096386e6715a43`

The owner repository and its current authoritative status remain the final reference; local archives are snapshots only.

## What belongs on the certification board

| Layer | Legitimate claim | Never infer from |
| --- | --- | --- |
| Repository inventory | In-scope project, measured engineering profile availability | Folder naming, duplicate checkout, inferred deployment |
| Engineering footprint | Number of active files, production/test files, code line method and language distribution | Code quality, defect rate, completeness, deployment readiness |
| Architecture & security practice | Manual disposition: `Non évalué`, `Pas applicable`, `À améliorer`, `Appliqué` with evidence | Presence of a README, file name, workflow or keyword |
| Qualification milestones | Manually reviewed proof for a declared stage and scope | A positive result at a lower stage, project size or latest status of a different revision |
| Technical observations | Unqualified diagnostic leads and scan limitations, tracked separately | Confirmed vulnerability or automatic maturity downgrade |
| Continuous improvement | Named next action, owner, supporting evidence, review date | Counting every false-positive heuristic as backlog work |

## Five independent milestones

Every project has five independently assessed stages:

1. **Specified / architected** — architecture, contracts and boundaries are documented by the appropriate owner.
2. **Implemented** — implementation exists for the declared feature and scope.
3. **Tested / qualified** — qualifying evidence exists for the exact revision and declared test scope.
4. **Integrated** — owner-to-owner integration evidence exists for the relevant boundary.
5. **Production-proven** — real production or operational evidence exists; synthetic tests do not qualify.

Each stage begins as **Not assessed** and can be manually set to **Not applicable**, **Needs documentation**, or **Supported by evidence**. Supporting a stage requires an explicit **scope** plus an **evidence reference**. One stage never automatically promotes another. For instance, Konnaxion↔Orgo's qualified local IK boundary is **not** a blanket Konnaxion or Orgo production claim.

Local records are saved to `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\qualification.json` and **never uploaded to GitHub Pages by the Publish button**.

## Pattern checklist: deliberate review only

The 86 imported architecture and security practices remain **source patterns**, not mandates that every one of the 49 repositories must implement. `Pas applicable` is a documented normal outcome, **not a penalty**. `À améliorer` means a human reviewer identified a relevant improvement. `Appliqué` means the reviewer has evidence. All three explicit states require a justification or evidence reference; `Non évalué` is the safe default.

## Diagnostic noise management

- **Similar names, duplicate folders or alternate local clones** are inventory questions. They do not downgrade certification.
- **`.env`-style file names** alone do not prove an exposed secret. Check Git tracking and content securely through targeted triage when warranted.
- **Action references by tag**, when observed, are policy-hardening candidates, not confirmed vulnerabilities.
- **Large files excluded by scanner budget** affect only measurement coverage, not project quality.
- **Static test declarations** do not prove test success. Similarly, a workflow file does not prove that CI passed.
- **`verify=False` in capsule handling** is not necessarily an HTTPS TLS bypass. The historical false positives were identified separately.
- A real, context-supported security issue may still require a prioritized review, remediation and evidence of closure. This is kept distinct from certification levels.

## Using the application

In the private **Registre des 49** tab, review the official inventory and double-click a repository to open its detailed record. The **Axes suivis** count includes only practices that a human reviewer explicitly marked `À améliorer`; it is never calculated from scanner findings.

In the **Certification & profils** tab, select a repository. The upper panel records a milestone status with scope and evidence reference; the lower panel contains engineering/security profiles and the 86 manually-reviewed source patterns.

The public-safe dashboard shows **coverage and engineering measurements** first. Technical pattern counts are available in a collapsed secondary diagnostics section, never treated as negative certification points. All stages and pattern assessment records remain local by default.

This app does not rescan automatically when the user changes a manual assessment; no GitHub write is implied.
