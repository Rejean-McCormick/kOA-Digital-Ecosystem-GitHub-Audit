<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/1-Overview/Components-Kristal-and-Daat.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 53297d38c4b69899e5a71f52c85c0f2f0a9478d19b633cde172f08cd104a3714 -->

# Kristal, Da’at and the knowledge boundary

Kristal is the ecosystem's portable structured knowledge/state layer. Da’at is the anti-corruption/mapping boundary used to enter Kristal-native contracts. EncyKlopedia and UCKK sit on opposite sides of this boundary with different responsibilities.

## Current authority flow

```text
source/provider discovery
    ↓
EncyKlopedia
    acquisition evidence + referent candidates
    ↓ encyklopedia.corpus-harvest-handoff/1.0.0
Da’at
    mapping / ACL / contract adaptation
    ↓ kristal.build.request/2.0.0
Kristal v6
    referents + Kristal State
    valuations / coordinates / applicability
    provenance / validation / recognition
    record_role / actionability
    ↓ kristal.artifact.ready/2.0.0
UCKK / Univers-Cité or another authorized consumer
    rebuildable projection / presentation / authorized downstream flow
```

## Kristal v6 lifecycle

```text
Kristal State (draft/working)
    ↓ evidence / review / validation / recognition
Kristal State (recognized/reference when applicable)
    ↓ deterministic derivation
Runtime/query projection or consumer projection
```

Validation, recognition and `artifact_status` remain separate. A reference status is scoped recognition, not universal truth.

## Actionability boundary

Kristal v6 can state that an action is eligible for automation or requires a human review/decision. This does not make Kristal or Da’at an execution owner. Cross-system effects still require the explicit receiving contract and authority. This preserves the ecosystem rule that automation reduces friction without bypassing human or institutional responsibility.

## Referent identity

Referent Registry `1.0.0` remains the ecosystem's current domain-neutral identity surface. External identifiers such as Wikidata, Gutenberg or VIAF support matching/provenance; they do not become authority for a Kristal assertion.

## EncyKlopedia responsibilities

EncyKlopedia owns source discovery/acquisition, provider resolution, lossless evidence/provenance, source snapshots/exports, referent candidates and the immutable corpus-harvest handoff. Acquisition alone does not validate knowledge.

## Da’at responsibilities

Da’at maps source/IK-facing payloads into Kristal-native v6 contracts, preserves source identity/provenance/roles, enforces mapping/ACL boundaries and does not acquire source or Kristal authority. It must not infer `automatic` from a high valuation: actionability is a separate policy statement.

## UCKK / Univers-Cité responsibilities

UCKK owns consumer projection choices such as applicability/view configuration, primary view, derived glossary, Moodle materialization and media-library presentation. The projection is rebuildable from a pinned Kristal State and does not become Kristal canon.

## Current baseline

```text
Kristal Standard          6.0.0
canonicalization          kristal.v6:jcs-rfc8785
Referent Registry         1.0.0
IK build/artifact         2.0.0 / 2.0.0
```

See [knowledge-projection.md](../2-Technical-Reference/40-integration/knowledge-projection.md).
