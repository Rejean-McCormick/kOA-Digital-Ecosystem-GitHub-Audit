# SmartDump functional-spec review — 2026-10-30

This report describes a **source-bounded, representative** capability/technology inventory, not an exhaustive functional acceptance test or certification. The owner supplied `SmartDump_20261030_200705.zip` with **35 nested repository snapshots**; no code from these snapshots is redistributed in the application.

## Method

- Each inspected ZIP is identified by a SHA-256 digest; every cited source file also has its individual SHA-256 in the private spec index.
- Distinct status labels: `code_observed` means implementation/source observed; `specification_only` means written contract or design; **neither means PASS**.
- Test-file references, where present, are defined test cases, **not execution logs**. No new tests were run on these 35 ZIPs.
- There is **no attested Git commit** for these snapshots. Do not label their source ZIP as the current GitHub HEAD.
- Previous scope-limited E2E documentary findings and the five isolated snapshot test runs remain separate, dated evidence; they are not transferable to this batch.
- Only sanitized source paths, summaries and hashes are bundled under `private_evidence/`; no raw repository content or secret/configuration values are shipped.
- Two official repositories, **Kompose and Kontexte**, were absent. They remain unreviewed, **not failed**.

## Observed functional coverage

| Repository | Files in snapshot | Documented functions | Technical entries | Cited source files |
|---|---:|---:|---:|---:|
| Akor | 114 | 3 | 2 | 6 |
| Arketype | 814 | 3 | 3 | 7 |
| initkoa-docs | 8 | 3 | 3 | 4 |
| Ekole-Pastorale | 1627 | 3 | 3 | 6 |
| Ekole | 231 | 4 | 4 | 7 |
| HomePage-initkoa.org | 636 | 4 | 6 | 10 |
| Koali-Control-Panel | 60 | 4 | 4 | 8 |
| Koali-Scenario-Mosaic | 279 | 4 | 6 | 9 |
| kOA-Digital-Ecosystem | 215 | 4 | 4 | 9 |
| Kompiler | 222 | 4 | 6 | 13 |
| Konductor | 13 | 2 | 1 | 2 |
| Konstellation-Light | 77 | 4 | 3 | 11 |
| Konstellation-Publisher | 25 | 3 | 2 | 8 |
| Konstellation | 293 | 4 | 6 | 11 |
| Kontainer | 65 | 3 | 4 | 7 |
| Kristal-Authoring-Kit | 273 | 4 | 3 | 8 |
| Kristal-Integration-Pack | 50 | 4 | 4 | 11 |
| Kristal-Manager | 517 | 4 | 5 | 13 |
| kristal-public | 30 | 3 | 2 | 6 |
| KristalDiag | 355 | 3 | 4 | 6 |
| LevelUpDiag-kOA-Linux | 77 | 3 | 3 | 6 |
| MediKristal-LevelUpDiag- | 86 | 3 | 3 | 8 |
| LevelUpDiag-Orgo | 121 | 3 | 6 | 10 |
| LevelUpDiag_SemantiK-Architect | 75 | 3 | 5 | 10 |
| Mediatheque-blank | 42 | 3 | 4 | 5 |
| Mediatheque | 416 | 4 | 6 | 12 |
| MediKristal | 126 | 4 | 5 | 11 |
| Orgo-Worlds | 200 | 4 | 6 | 11 |
| SemantiK-Architect | 283 | 4 | 4 | 12 |
| SemantiK_Runtime_Orchestrator | 44 | 4 | 4 | 11 |
| SenTient | 565 | 3 | 6 | 10 |
| Skope | 491 | 4 | 5 | 10 |
| Spek | 131 | 4 | 3 | 10 |
| UCKK-Assets | 60 | 3 | 2 | 5 |
| UCKK-Ops-Console | 52 | 4 | 3 | 6 |

## Important examples of scope

**Konductor** contains concept and design documents, without an executable runtime in this batch. **UCKK-Assets** is principally an education and branding corpus, even if local formatting utilities are present. **Ekole-Pastorale** is a prototype and its content lacks approval for public or ecclesiastical publication. **Konstellation-Publisher** explicitly excludes live remote deployment in this revision. **kristal-public** describes a hosted-collection qualification that is BLOCKED. **MediKristal** is a synthetic software reference, not clinically validated. These distinctions must remain visible.

The local dashboard and future private campaigns can display/freeze this dated index. Prior frozen campaigns are not rewritten. The public GitHub Pages build does not receive the index or source contents.
