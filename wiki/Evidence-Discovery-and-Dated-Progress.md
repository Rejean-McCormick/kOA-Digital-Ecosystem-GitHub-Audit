# Evidence Discovery and Dated Progress

**v0.12.0** adds bounded, read-only discovery of **existing** JUnit, coverage and SARIF reports inside selected local Git clones. A matching GitHub `origin` is required. Only recognized report names in a small set of fixed directories are considered; there is no recursive source scan or test execution.

In the Windows app, open **Campagnes datées**, select a clone or an existing local audit report, and use **Trouver rapports de ce clone** or **Trouver rapports des clones de l'audit**. The UI shows report names and asks before copying their original bytes into the next private snapshot. Files may contain sensitive content; review them before sharing any ZIP. A document changed after discovery must be reviewed again before capture.

The **local** atlas now shows the most recent dated campaign, five independent manual-evidence bars, and a previous-campaign comparison. Each application can link directly to its immutable private historical page, Engineering Profile, individual evidence files and the archived GitHub commit ZIP. The comparison records attached documents added or removed by content hash and report type, as well as changes in manually evidenced milestones and practice reviews.

**Provenance:** a matching collector-reported Git HEAD is only a matching Git reference, never proof that tests executed on that source. Imported reports generally remain unbound to a commit, and historical snapshots do not become certified automatically. Public GitHub Pages cannot read private campaigns or their evidence.

See [`docs/EVIDENCE_AUTOMATION_AND_PROGRESS_V012.md`](../blob/main/docs/EVIDENCE_AUTOMATION_AND_PROGRESS_V012.md) and [Dated Compliance Snapshots](Dated-Compliance-Snapshots) for more detail.
