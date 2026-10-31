<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Integration-Kristal-v5 | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: a1cd72c83534bdaba49a99ec670a213ef08293db4b1d1b8e90c40faaf78ec718 -->

# Integration — Kristal v5

kOA integrates against the frozen Kristal v5 contract baseline. Kristal remains the sole normative authority for its schemas, referent semantics and epistemic lifecycle.

## Current baseline

```text
version                  5.0.0-rc.3
status                   release-candidate contract baseline
tag                      v5.0.0-rc.3
commit                   unresolved in supplied release metadata
referent registry        kristal.referent-registry/1.0.0
knowledge-model bundle   sha256:07fe0527ab29a4b40870efdd0c9e0c67c91de919e5428047245b2a2c04f8ea98
canonicalization         kristal.v5:jcs-rfc8785 / 1
```

The supplied rc.3 metadata does not resolve an immutable commit SHA. kOA therefore treats rc.3 as a frozen contract baseline, not as proof of a completed immutable published release.

## Core model

Kristal v5 separates:

```text
artifact existence
integrity
referent identity
assertion status
certainty
validation
recognition
reader visibility
publication
activation
```

The normative structured input is **Structured Epistemic State**. Claim-IR remains an optional extractor proposal profile rather than a mandatory universal stage.

A Structured Epistemic State may compile to a **Working Exchange** before final validation/recognition. A **Reference Exchange** is a recognized reference artifact under declared authority/scope.

## Referent and domain neutrality

Referent Registry `1.0.0` provides a domain-neutral identity layer. kOA does not define a competing universal taxonomy or prescribe one primary navigation axis.

External identifiers such as Wikidata, Gutenberg or VIAF may assist matching, discovery and provenance. They do not become internal epistemic authority merely by being referenced.

## Runtime Packs

A Runtime Pack declares at minimum its source Exchange reference and `source_artifact_status`. Packs derived from working and reference artifacts are not equivalent.

Reader Policy and Query Contract determine how eligible content is exposed; they do not rewrite the underlying epistemic status. Query-oriented tables/indexes/read-only stores embedded for performance are derived and rebuildable from the referenced source artifact.

## Operational ownership rule

Orgo, Konnaxion and other products keep mutable operational state in their own stores. Knowledge compilation begins from immutable source-owned exports/snapshots and produces separate Kristal artifacts with provenance. kOA does not use bidirectional operational-DB↔Kristal synchronization as the authority boundary.

## Consumer projection rule

UCKK / Univers-Cité and other consumers may materialize scoped views over pinned Kristal artifacts. Their primary navigation lens, glossaries, media views, chronology and application/Moodle records remain derived consumer state.

See [Knowledge acquisition and projection](Knowledge-Projection).
