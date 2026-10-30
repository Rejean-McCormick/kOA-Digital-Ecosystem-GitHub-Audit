# Kristal enrichment in the ecosystem command center (v0.9.2)

This feature uses local Kristal canonical catalogs to display **evidence for potential component-to-repository associations**. It never writes to Kristal, does not run a repository scan, and does not publish private mapping data to GitHub Pages.

## How to use

1. In the Windows launcher, open the **Écosystème** tab. The default source is `C:\mycode\Kristal\locals\Kristal-kOA-Ecosystem`.
2. Click **Vérifier Kristal**, then **Ouvrir le centre de pilotage (carte + profils)**.
3. Choose **Kristal canonique · 49 dépôts**. Click an application and select **Kristal (local)** in the detail pane.
4. Examine **Explicit component links**, **Candidate links**, and **Unlinked/no candidate** separately. Expand the candidate semantic-relations section for context.
5. If a suggested link is correct, review and document it in Kristal using the source project's own editorial process. Clicking a suggestion in the dashboard does **not** edit Kristal or mark a qualification stage.

## What each status means

| State | Meaning | What it does not mean |
| --- | --- | --- |
| Explicit | The `components.json` record contains a `repository_ref` that equals a registered repository identity. | A tested integration, a successful deployment or a certification. |
| Candidate | The component has no `repository_ref`, but its normalized name/canonical ID matches the repository name or it shares a rare, specific GitHub source reference. | An approved component assignment, despite any `sourced` assertion metadata. |
| No candidate | No association was found by those *limited* matching rules. | An architectural defect or absence of code. |

The dashboard presents the underlying semantic relations of candidate components as **candidate context**, not as verified links to a repository. Catalog assertions labeled `sourced` are not proof of a passed integration test.

## Scope and privacy

The optional counts for contracts, capabilities and source references describe what is **cataloged**, not what is implemented. The local dashboard projects allowed labels, counts, and statuses through an HTTP server bound to `127.0.0.1`. It does **not** export source-reference IDs, raw catalog files, evidence notes, local paths or private assessments. If Kristal is unavailable, the public-safe prebuilt atlas and existing engineering report pages remain available. The GitHub Pages publishing flow does not add these local enrichment mappings.

## 30 October 2026 diagnostic cross-check

The independent `Kristal-enrichissement-20261030-121832.zip` reported **49** registered repositories, **14** with explicit component links, **23** with candidate associations, and **12** with no candidate. The v0.9.2 local projection was cross-checked against the diagnostic for all 49 repositories and produced the same candidate component IDs. These are documentation-mapping metrics, **never grades**.
