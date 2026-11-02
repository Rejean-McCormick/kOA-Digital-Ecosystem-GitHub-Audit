<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/40-integration/kristal-v10-alignment/contracts-and-versions.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: fb914edd5195e1f0e3bf0dfe38cdeb0256726b065a68e195a4f8ff50a3bb48e5 -->

# v9/v10 interface contracts and exact-version gates

| Contract / identifier | Producer | Consumer | Status from supplied evidence |
|---|---|---|---|
| `kristal.state/9.0` | Authoring Kit / Framework | C1, Manager readers, Konstellation | Logical commitments retained under v10 |
| `kristal.hosting/10.0` | Framework v10 | Bootstrap / host adapters | Specified; draft.3.1 baseline in the snapshot |
| `kristal.host/github/1.0` | Framework GitHub profile | Bootstrap / collection | Owner commit must be pinned |
| `kristal.github-read-surface/1.0` | Authoring Kit 3.2.4 | Manager | Contract/command documented, not live end-to-end qualified |
| `kristal.github-sync-manifest/1.0` | Manager | C3 / Konstellation | Manager runtime incomplete in snapshot; not E2E verified |
| `kristal.github-collection-index/1.0` | Manager/collection | C3 / Konstellation / Kompiler | `kristal-public` index absent from supplied snapshot |
| `kristal.c2-public-authorization/0.1-candidate` | C2 owner-approved issuer | Manager / Bootstrap / C3 | Candidate; exact grant/trust/signature gates pending |
| `kristal.c2-prepublic-qualification/0.1-candidate` | Independent C1 qualification | C2 / C3 | Candidate; not an issued Zoology approval |
| `konstellation.light-catalog/1.0` | Derived public/static importer | Light UI | Demo/local until release input authorized |
| `encyk.source-evidence-handoff/2.0.0` | EncyKlopedia | Médiathèque | Producer defined, real bilateral receiver not qualified here |
| `encyklopedia.corpus-harvest-handoff/1.0.0` | Historical EncyK lane | v6 knowledge/IK | **Frozen historical lane; never silently replace with v2** |

## Baseline and SHA ambiguity

Framework `10.0.0-draft.3.1` is described as *draft*, not a final ratified `v10.0.0` release. The sources mention differing Framework repository/commit pins in Bootstrap examples and public C3 workflows. They may refer to different histories or artifacts. C0 records them as **unresolved** pending read-only confirmation of the actual contract set and full SHA of each remote commit. **Never replace a pinned value with a guessed or mutable branch name.**

## Gates for claiming interoperability

1. **Producer → schema:** exact contract revision and hash validated.
2. **Kit → Manager:** file list, SHA/size, state_ref and readiness agree on a real fixture.
3. **Manager → C3:** derived index/manifest match state, commit, source coverage and actual bytes.
4. **C1/C2/C3:** independent qualification and scope-limited owner authorization checked *before* any public repository write.
5. **C3 → readers:** policy-first traversal, exact revision, provenance and coverage; refusal for an unavailable/incorrect source.
6. **Konstellation → Arketype:** only explicit, noncanonical archetype labels; never infer source truth from a UI shape.

**Source of truth:** files in each owning repository at an approved commit. This C0 page is a coordination view, not a normative schema.
