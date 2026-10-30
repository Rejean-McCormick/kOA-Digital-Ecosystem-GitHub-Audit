# Historical evidence review — 49 repositories × five distinct stages

The **Evidence Review / Revue des 245** view is a local-only review of owner-provided diagnostic artifacts dated **September 21–October 30, 2026**. It contains 49 repository records and 245 separate stage reviews, built from the provided Kristal diagnostic, local audit observations, engineering snapshots, and governance/integration documentation.

## Start here

1. Download and fully extract the application ZIP on Windows; do **not** run the `.pyw` from inside the compressed archive.
2. Run `kOA_GitHub_Audit_Launcher.pyw`.
3. Open **Revue des 245**. Search for an application and select one of its five stages.
4. Double-click an available source, or choose **Voir ce jalon et ses sources** to open the complete local evidence dossier in your browser.
5. After reading the document and checking its *scope*, choose **Préparer une qualification à examiner**. This only prefills the manual form and leaves the status at **Non évalué**.
6. In **Certification & profils**, explicitly choose a status, adjust the scope and the reference, and save. Choosing **Étayé par preuve** requires a human confirmation of scope and provenance. A new dated campaign will capture the decision; earlier campaigns will not be changed.

The **Écosystème** browser dashboard also provides the link **Voir les 5 dossiers de preuves** on each repository card, **only while running from the Windows local preview**.

## What is and is not attested

- **Source present** means a historical document was supplied and is available to inspect, with an SHA-256 checked against the review manifest. It is not an automatic approval.
- **External reference** means an older audit or archive was referenced in the analysis, but the actual source document was **not** included in the review ZIP. It cannot be opened and is not presented as if it were archived.
- **Engineering Profile** indicates a measured snapshot and declared tool limitations, not tests executed or Git-commit identity.
- **CI run** is a time-specific observation, not proof that the entire repository is qualified.
- **Konnaxion ↔ Orgo E2E** is evidence of the two selected Interaction Kernel contracts, under a **local integrated runtime**, as documented in the original September 21 report. It does not attest production readiness or all system boundaries.
- **Production** remains *not established from these historical archives* for all 49 applications. A manual **Non applicable** decision is a separate applicability assessment, not an error.

The **0 / 245** counter is the number of manually recorded stage assessments in the current local register (or a frozen campaign), not a tally of historical sources detected. The review never changes it simply by opening documents.

## Privacy, dates and persistence

- All the historical material is included in `private_evidence/KOA-REVUE-2026-10-30.zip`, shipped **only with the downloaded application package**. This directory is in `.gitignore` and is never copied into `docs/` or GitHub Pages.
- When the Windows review is first opened, the app preserves the same archive at `%LOCALAPPDATA%\kOA-GitHub-Audit\evidence_reviews\` so it survives application ZIP upgrades; an existing different archive is **not overwritten**.
- The local browser serves the source documents as inert escaped text from a loopback-only endpoint. The review API is unavailable on the public dashboard.
- Qualification decisions remain at `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\qualification.json`.
- If a manually saved claim explicitly refers to `KOA-REVUE-2026-10-30`, creation of the **next** campaign embeds a SHA-256-verified copy of the review ZIP inside the private campaign. It is downloadable from that campaign's local pages.
- These historical sources are **not reliably tied to one Git tree**. A campaign's Git SHA is the version observed by its Git/audit provenance; do not automatically use it as the version for an independent snapshot.
- Existing campaigns are never updated, and no source repositories, GitHub branches, or GitHub credentials are touched by reading this review.

## Known limits

The review contains **195 stage-source references**, of which **93 are directly available for inspection** in the bundled archive; **102 are historical references not separately bundled**. References are *not unique documents*, so these counts are not repository coverage or a compliance score. The review can be expanded in a later dated package as new evidence files become available.
