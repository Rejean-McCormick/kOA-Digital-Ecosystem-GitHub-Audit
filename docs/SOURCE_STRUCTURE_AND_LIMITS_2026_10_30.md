# Source structure and corrected functional sheets — v0.20.0

This update addresses the independent review of v0.19.0 without fabricating tests or turning filename matches into qualifications.

## Source-backed corrections

- **Skope:** the formerly named knowledge-graph preview is now described as *geographic scope analysis*, based on the actual `tests/test_geographic_scope.py` source. The test **definition** is present, not a passing execution.
- **SenTient:** the Wikidata graph source is now described as dump preprocessing, adjacency-matrix building, and PageRank preparation. It does not independently demonstrate live Wikidata entity search.
- **16 descriptions** referencing only tests or documentation had their implementation-observed status downgraded to specification/test-defined. This is a **source attribution correction**, not a failed application.

## Source structure across 47 snapshots

The local validation page includes **Modules & fichiers** per repository. For all 47 supplied archives, an offline script inventories file trees by directory and extension, grouping paths under APIs, identity/security-related code, data, contracts, UI, CI, tests, and documentation. Each group displays observed file counts; representative source files have SHA-256 fingerprints. Counts are **not functional coverage percentages**. A group named security does **not** imply security controls have passed; a test file does **not** imply it ran; a commit is **not** inferred from a ZIP.

Generated data (`private_evidence/KOA-STRUCTURE-SOURCES-2026-10-30.json`) are integrity-pinned by `koa_audit/source_structure.py` and private to the local dashboard. Raw source snapshots are never republished. Newly created campaigns freeze the exact index and its SHA-256; existing campaigns are unchanged.

Excluded from the structural tree: duplicate update backups, third-party vendored dependencies, secrets, binary files, build output, and caches. These exclusions protect confidentiality and keep the view oriented to live source. For this reason the number of classified files differs from the total ZIP count.

## Evidence levels

1. Documentation or defined test: **present**, not verified PASS.
2. Implementation source: **observed code**, not proof of successful behavior.
3. Snapshot test execution: **PASS only for the exact scoped suite**, with dated JUnit and snapshot hash.
4. Historical documentary milestone: scoped, source-checked **documentary finding**, not application-wide certification.
5. Production qualification: **not established** by these ZIP snapshots.

The functional entries in the 35-repository SmartDump remain a **representative selection**, not an exhaustive application specification. The structural map improves discoverability, but full behavioral verification requires runnable system evidence and provenance for each claim. **Kompose** and **Kontexte** have no supplied functional snapshots and are not judged.
