# Dated Compliance Snapshots

The **Campagnes datées** tab freezes evidence and manual qualification decisions as local, dated ZIP archives with SHA-256 integrity manifests. It preserves history separately from changing GitHub repositories.

The workflow is entirely private and offline. Import an existing `audit.json`, add optional evidence files only after review, choose a campaign name, then select **Créer une campagne figée**. No whole-ecosystem rescan is necessary.

Open a campaign to browse all 49 repositories, read frozen Kristal relationship evidence and the Engineering Profile as it existed at capture time and follow full-SHA GitHub commit and source-download links when a revision is known. These links are references, not guarantees of retention: a force-pushed-away commit can become unavailable. Keep independent source backups for important revisions.

The campaign freezes **manual decisions without re-evaluating them**. Configured controls, source size, filenames, duplicated directories, static patterns, JUnit files and coverage reports do not automatically increase or decrease a certification level.

For the complete evidence model, limitations and privacy rules, see [`docs/PRIVATE_COMPLIANCE_CAMPAIGNS.md`](../docs/PRIVATE_COMPLIANCE_CAMPAIGNS.md) in the main repository.

## Verified historical evidence — v0.11.0

The latest launcher adds two opt-in actions: measure **one selected clone** or **all accessible, explicitly mapped clones from an existing audit report**. Only matching Git origins are measured. It collects read-only Git metadata and optional `scc`, Lizard and Universal Ctags aggregates when the checkbox is enabled; no project tests or source code are executed. Results remain in private local files and can be attached to a new campaign.

Every attached proof is now clickable from the dated application's page and has a private preview or original-file download. Campaign creation enforces archive-size and count limits, then verifies the complete ZIP before finalizing it. Each campaign has a five-stage manual-evidence chart and can be compared with a previous campaign to see new, revised or withdrawn evidence and reviewed practices. All comparisons describe documentation changes, not automatic certification or functional completion.

Historical audit SHA, current locally observed SHA and an imported Engineering Profile snapshot SHA are **separate references** unless actual source equivalence is demonstrably verified. Source downloads use the full historical GitHub SHA, not a live branch.
