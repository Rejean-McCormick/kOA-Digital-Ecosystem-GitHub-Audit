# Dated documentary adjudication — 30 October 2026 (private)

**Scope:** 49 inventory repositories × 5 independent maturity stages = **245 documentary cases**. This review was performed on **user-supplied historical artifacts**, not on current GitHub heads. It was explicitly requested by the owner. It is a bounded technical evaluation, not a security grade, production certification, or evidence of the current commit.

## Reconciled result

- **10 source-supported stage/application cases**, all **strictly limited in scope**. They refer to **three distinct original source documents**, so ten cases do **not** mean ten independent test runs.
- **235 cases marked `À documenter`**: available artifacts do not establish their entire stage. This does not mean the applications are incomplete, defective, or non-compliant.
- **0 production-proven stages** in the supplied evidence.
- **No historic evidence is attributed to a specific owner repository SHA**. The audit SHA and RepoSurveyor snapshot remain separate observations.

### Ten stage/application conclusions backed by original documents

| Repository | Stage(s) | Exactly what is supported | Source |
| --- | --- | --- | --- |
| Konnaxion | Specified; implemented; qualified; integrated | Two specific IK contract versions: `governance.decision.execute/1.0.0` and `accountability.impact.publish/1.0.0`. Documented owner roles, successfully exercised product runtime path, idempotent replay, divergent-replay HTTP 409, and successful local integrated E2E on **21 Sep 2026**. **Not production; no individual clone SHAs.** | `orgo-konnaxion/index.md` for specification, `2026-09-21-konnaxion-orgo-ik-e2e-qualification.md` for execution, test and integration |
| Orgo | Specified; implemented; qualified; integrated | Same single bilateral run and the same strictly limited boundary. **Do not count these as a second independent E2E experiment.** | Same two source documents |
| EncyKlopedia | Specified | Frozen **historical v6** `encyklopedia.corpus-harvest-handoff/1.0.0` source-acquisition boundary. **Does not support newer EncyK v2 receiver acceptance.** | `knowledge-projection.md` |
| Daat | Specified | Historical v6 mapping/ACL boundary and owner-authorization separation for Da’at→Kristal. **No claim of implementation, E2E acceptance, or production.** | `knowledge-projection.md` |

Each positive case carries the **exact SHA-256 of the original source bytes** and its explicit scope. Open it through **Preuves 245 → application → stage → document primary** in the local preview. The original source archive itself remains private.

## Application behavior

On the first start of v0.14.0, the application:

1. Rechecks the original review ZIP SHA-256 and verifies each source backing a positive case.
2. **Adds only missing stage decisions** to the private `%LOCALAPPDATA%\kOA-GitHub-Audit\profiles\qualification.json` registry.
3. Preserves **every existing owner decision**, including an explicit `Non évalué`; no previous decision is rewritten.
4. If an existing registry needs additions, creates a **create-only local backup** (`qualification.json.before-documentary-review-20261030.bak`) before the atomic update.
5. Shows the source, limitations, date and current registry result in the application. It never executes project tests or changes source repositories.

The private dashboard shows the resulting qualification counters immediately. **Old campaign ZIPs remain unchanged**, so an older campaign can still show `0/245`. Create a **new** dated campaign to freeze the reconciled state.

## Evidence classification discipline

- A successful E2E documented at the owning product boundary **supports only that boundary, its two contract versions, and its local environment**.
- An engineering profile, `audit.json` observation, source file count or test file count **does not prove implementation or tests passing**.
- An observed CI success supports that workflow's historical outcome, not comprehensive qualification.
- A source describing a frozen historical v6 contract **does not prove a newer v2 interface**.
- A candidate Kristal association or contract map **does not prove integration succeeded**.
- No source here demonstrates production readiness with a pinned deployment version and an environment-specific attestation.

## Private files and auditability

- `private_evidence/KOA-REVUE-2026-10-30.zip`: original source archive and its per-document manifest.
- `private_evidence/KOA-ADJUDICATION-2026-10-30.json`: full **245-row** rationale, scoped status, source references and primary-source SHA-256.
- The source ZIP and adjudication JSON are **not included** in public GitHub Pages publication, which receives allowlisted summaries only.

**Integrity does not imply independent attestation.** This is a source-grounded documentary review of supplied snapshots, not a newly executed test or a claim about GitHub's live state.
