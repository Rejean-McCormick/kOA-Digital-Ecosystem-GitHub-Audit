<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Artifacts-Kristal | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: bc1cd0746a6a2052028cf021f4712a3fbfe960079ae31a4d7fbec0a0684c3364 -->

# Kristal v5 artifacts

The kOA ecosystem consumes Kristal v5 artifacts without collapsing their epistemic distinctions.

| Artifact | Purpose |
|---|---|
| Referent Registry | domain-neutral stable identity layer for referents and external-ID anchors |
| Structured Epistemic State | structured epistemic state with assertions, provenance and labels |
| Claim-IR / Resolved Claim-IR | optional extractor/resolution profiles |
| Working Exchange | deterministic compiled Exchange; not necessarily validated/recognized |
| Validation Report | scoped validation decision/findings |
| Authority Recognition | scoped authority recognition decision |
| Reference Exchange | authority-recognized reference artifact for declared scope |
| Reader Policy | controls which labeled material a consumer may read |
| Runtime Pack | offline/runtime projection with explicit source artifact status |

Validation, recognition, publication and activation are separate transitions. A failed or incomplete validation does not universally mean that no Working Exchange may exist.

## Referent rule

External identifiers such as Wikidata QIDs may be associated with a referent for matching/provenance. They do not by themselves become Kristal authority.

## Projection rule

A consumer may build a scoped application projection, glossary, chronology or media view from pinned Kristal artifacts. These are derived consumer artifacts and do not become a second epistemic canon.

For production deployment, the kOA Profile may impose stricter eligibility rules (for example recognized/reference material only). Those rules must be declared as kOA deployment policy rather than attributed to Kristal's universal compile semantics.
