# Evidence-first dashboard — version 0.15.0

The **first screen** of the local Windows dashboard is now a private, source-bounded validation register. Select any of the 49 repositories and read six sections: **Tests, Security, Architecture, Implementation, Integration and Production**, plus **Kristal components**. This does not overwrite the map, the dated campaigns, or the clickable engineering reports further down the page.

## Exactly what a green tick means

- **Documentary evidence (10 bounded stage claims):** a reviewed source document included in the owner's historical archive has been SHA-256 verified, and the same documented scope and source reference occur in the local qualification register. Four stage claims concern Konnaxion, four Orgo, one EncyKlopedia, one Da’at. This is **not** ten certified products. Two of these stage claims concern the *same* historical, local Konnaxion–Orgo E2E qualification; they are not two independently executed test suites.
- **Historical GitHub Actions (3 CI success observations):** the user-supplied 2026-10-28 remote OBSERVE audit recorded `completed/success` as the last sampled run at the same 40-character SHA as the separately observed repository metadata for EncyKlopedia, Koali-Control-Panel and Koali-Scenario-Mosaic. We have neither full workflow logs nor details of the checks that ran. These are **CI outcome observations**, not proof that every test succeeded, security certification, or current HEAD status. Another older success for `initkoa-docs` used a different commit and is explicitly not marked green for the snapshot head. Original audit SHA-256 provenance is recorded in the private, sanitized CI extraction.
- **Security and architecture practices:** the supplied catalog contains 53 security and 33 architecture patterns, shown for each app. Even an owner's local `Appliqué` entry displays **an assessment, not a tested pass**. No green security tick is generated from a name, file presence, static scan observation or profile.
- **Kristal components:** explicit repository bindings are shown as catalog relationships; proposed bindings are separate. A relationship is never marked as a qualified integration.
- **Production:** none of the supplied documentary sources proves an all-scope production release. Therefore no production pass is generated.

All internal evidence remains on the local machine. GitHub Pages receives the dashboard presentation code, but does not receive the private CI snapshot, practice notes, documentary qualification claims or original source documents. On the public site the validation board clearly says that private results are unavailable.

The 49 repository entries and their categories remain visible even when no profile, test result or reviewed practice is available. Empty information is **unknown**, never a failure or a penalty.

## How to obtain additional justified green ticks

Collect **version-matched, dated** artifacts for a *specific application and control*: full commit SHA, tool name and version, command or CI workflow, execution environment, start/end date, result, original JUnit/SARIF/coverage or other machine-readable report, its SHA-256 and the exact scope. Preserve this as a new dated campaign. Existing evidence discovery in **Campagnes datées** can find JUnit, coverage and SARIF reports in known locations; it does not execute project code or perform a full security scan. Tool execution is a separate, explicit, controlled step.

A green tick for a test must identify **which check passed**. A completed CI workflow alone must never be used as a blanket claim about all tests. A production validation additionally requires deployment and runtime evidence for the relevant environment.

### Traceability of the historic CI extraction

The original user-supplied observation is `audit(2).json` (generated 2026-10-28). The application contains a sanitized, private, checksum-pinned extraction `private_evidence/KOA-CI-OBSERVATIONS-2026-10-28.json`. It is not a live GitHub feed; its historical assertions never change when repositories evolve.
