# Source-based functional specification update — nine repositories

Date: 2026-10-30. Source: nine ZIP snapshots and index files provided by the repository owner. The application does not contact GitHub or execute project code during normal viewing or campaign creation.

## Scope and meaning of the dashboard

**12 of 49 official repositories now have curated functional spec sheets**: three from the previous v0.17.0 collection and the nine below. There are 71 functional observations and 59 technical/component entries across these twelve sheets. All source references contain **relative member names and SHA-256 digests**, and every ZIP has a stored SHA-256. No source ZIP is bundled into this application.

A function labelled *code observed* means that an implementation file was reviewed. A test file labelled *defined* means the test exists, **not** that it passed. The green PASS mark only appears on separately executed test suites with corresponding local JUnit output. These were run on isolated copies of the exact ZIPs provided by the owner; the ZIP-to-Git-commit relation was **not attested**.

| Official repository | Functional observations | Technical items | Scope evidenced by source |
|---|---:|---:|---|
| Daat | 6 | 4 | Offline contract and mapping tools, security-policy injection, IK v6 bridge; **pre-production, no live transport** |
| EncyKlopedia | 5 | 4 | Local, synthetic, read-only articles/search/language and HTTP demo; **no real publications** |
| Interaction-Kernel | 5 | 5 | Versioned schemas/envelopes, validation/admission, JCS fingerprints and adapters |
| kOA-Linux-Koali | 7 | 5 | Assembly, release sets, deployment renderers, audit broker, identity and policies |
| Koali-Spaces | 6 | 4 | Next.js shell, navigation, surface host, preferences and presentation boundaries |
| Konfid | 6 | 5 | Access requests, approvals, detectors, audit export, FastAPI, rate limits, persistence |
| Konnaxion | 7 | 5 | Civic consultations, Smart Vote code, identity, learning, collaboration, culture, IK bridge |
| Kristal-Framework | 6 | 5 | v11 draft semantic identity, dictionaries, external crosswalk, conversion and reference reader |
| Orgo | 7 | 5 | Workflows/tasks, communications, OIDC, organizations/Prisma and IK bridge |

The three prior sheets (KonnaxionDiag, Konnaxion-Capsule-Manager and Konnaxion-Worlds) remain unchanged.

## Tests actually executed on the new owner ZIPs

| ZIP / repository | Isolated local command family | Native result | Scope limitation |
|---|---|---:|---|
| Daat | `python -m pytest tests -q` | **99 tests passed** | Offline Python library; no Konfid/IK live network |
| EncyKlopedia | `node --test tests/catalog.test.mjs tests/http.test.mjs` | **9 tests passed** | Local HTTP demo and synthetic articles only |
| Interaction-Kernel | `python -m pytest runtime/python/tests -q` | **19 tests passed, 14 subtests passed** | Python runtime only; not whole TypeScript transport or production |

Reports: `private_evidence/snapshot_test_reports/*.junit.xml` and `private_evidence/KOA-ISOLATED-TEST-RUNS-2026-10-30.json`. Both manifest and each sanitized JUnit XML are verified by SHA-256 before the local dashboard exposes a result. Sanitized XML retains the native test-case names/counts but excludes environment-dependent file paths and logs. Do not add the 14 subtests a second time to the 19 test cases.

These are **127 new passing test cases**. Including the earlier 45 targeted unit checks on two other snapshots, the private dashboard shows **172 passing test cases across five independent, clearly scoped runs**. It does not grant 172 security checks or certify 172 functions.

## Limitations and responsible interpretation

- The six other new repositories do include test definitions, workflows and architecture notes, but their full suites were **not executed** in this review. Some require PostgreSQL, native Linux or a prepared build environment. No success is inferred from a workflow badge, file name or `pytest` import.
- The **53 security patterns** remain individually unverified by this mechanism. Security-related tests in a local suite do not automatically establish all catalogue practices.
- Historic **10/245 documentary qualifications** remain separate, unchanged and scoped. No new global production, security or integration certification has been issued.
- Source ZIPs do not carry authenticated Git commit identifiers. The local dashboard marks them as **snapshot SHA-256 only**; it must not link them to an unrelated current HEAD.
- Private code names, raw source content, diagnostic notes and JUnit logs remain **private**. Public GitHub Pages does not expose this index. A newly created private campaign freezes the updated index and corresponding local JUnit evidence; existing campaigns remain unchanged.

## Next evidence collection

For a future verification campaign on the owner's machine, capture each repository's exact commit SHA, tool versions, test command, exit code and machine-readable results with source/worktree provenance. Use disposable databases and isolated environments for Konnaxion, Orgo and Konfid; never run a project's test suite against production databases.
