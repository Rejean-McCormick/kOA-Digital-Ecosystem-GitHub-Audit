<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Safety-and-Provenance | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: adda866682fa286253fed12c7776210454bf917ae26188507dd149e3af78a82d -->

# Safety model, provenance and trust boundaries

Skope's design reduces several classes of accidental mutation and evidence confusion. It is **not** a third-party security audit, and the code is primarily intended to be run by a trusted local operator.

## Input integrity

- `db.connect(..., readonly=True)` opens the compact index using SQLite `mode=ro`, rejects incompatible/incomplete schemas, and forbids a writable connection through this adapter.
- Scope profile imports are validated JSON, **never** Python imports or shell commands. The catalog rejects symlinks, duplicate keys, unsafe toggles, oversized files and invalid campaign structure.
- The HTTP service binds only to local addresses and checks Host and browser Origin on POST. It is not an authenticated, Internet-facing service.
- Full-record extraction checks job/source identity, existing locator/reader support and output zones; it rejects unexpected changes on resume.

## Controlled writes

The source SQLite index, original dumps, existing fast access files, selected Kristal workspace and canonical material are read-only **from Skope workflows**. Explicit user actions can create files under Skope-owned `30_working/skope-large-scopes`, `30_working/skope-extractions`, `30_working/skope-reconciliation`, `20_evidence/scope-snapshots`, plus a small local workspace-selector settings file.

Therefore, **"read-only" applies to the external source and canon, not to all of Skope**. Skope *does* deliberately write its own job state, local settings, evidence snapshots and review decisions.

## Provenance strength by stage

| Stage | Evidence strength | Do not infer |
| --- | --- | --- |
| Name/edge lookup | Aggregated index attributes | Original statement ID or verified factual claim |
| Scope preview | Selection and reasons tied to index metadata | Complete inventory if truncated |
| QID job | Persisted within-policy inventory and recipe | Full Wikidata records or geographic completeness |
| Full-record extraction | Source JSON bytes, record/part hashes, prior verified-manifest identifier | Independent source correctness or new 96 GiB rehash |
| Batch ranking | Offline heuristic reasons and candidate order | Probability, identity certainty or approval |
| Documented review | Human attestation, URL, note, audit/revision | Website content was read or checked by Skope |
| Portfolio lexical lookup | Cached bounded matches against read-only index | Verified KQ↔Q or KP↔P identity |
| Portfolio full claim | Source-checked complete raw entity and statement | Independent correctness of Wikidata claims or approval to publish |
| Proposal ZIP | Working handoff and source fingerprint | Permission to publish, activate or change a canon |

## Portfolio source and identity boundaries (0.15.0-alpha.1)

- Portfolio inventory reads source v11 ZIP/folders without changing them; its operational state is `portfolio.sqlite` in a separate `--work` directory.
- A bounded exact-label index match (`lexical_only_unverified`) is **not** an identity verification. Auto-suggestions skip `A-Kristal` and same-namespace collisions, but index results are bounded and never exhaustively prove uniqueness.
- `approve-review` records independent reviewer/evidence/reason **attestation** for a listed candidate inside Skope only. It neither promotes diK crosswalks nor verifies third-party URLs online.
- Verified full-entity acquisition reuses Skope dump/source checks and chunk checksums. A development JSONL fixture accepted by `propose` is labeled **unverified**, not production evidence.
- Every full claim proposal remains noncanonical; raw `mainsnak`, qualifiers, references, statement ID, rank and source identity are preserved. Unknown KP remains unspecified, linked QIDs remain separate seeds, and no automatic Authoring Kit publication exists.

See [Portfolio Enrichment](Portfolio-Enrichment) for the stage-by-stage guarantees.

## Three distinct identity protections

**Human type check:** `P31=Q5` helps avoid matching an entity that is not indexed as a human, but does not establish that it is the correct person. **Collision checks:** prevent silent reuse of a QID already associated with another source roster entry. **Documentary review:** explicit source URL, reason, reviewer attestation, current revision, SHA-256 of exact reviewed CSV, and an atomic transaction for grouped confirmations. The external webpage's contents remain outside the software's verification boundary.

## Operational safeguards

Run on a trusted machine only. Back up Skope-owned working data according to your retention policy; never delete historical evidence directories as a routine upgrade. Examine license, source code and profiles before deployment. Do not put tokens, secrets, personally sensitive reviewer notes or confidential roster material in a **public GitHub wiki**.

See [Architecture](Architecture), [Known Limitations](Known-Limitations), [Batch Identity Review](Batch-Identity-Review).
