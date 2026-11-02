<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/1-Overview/Integration.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 3a390fd14d4a86034f55bf9108a4bafcfe74e893e07a05f7f80ed8b4de1bca30 -->

# Integration

kOA integrations preserve owner boundaries and use explicit versioned contracts.

## Current integration layers

- **Owner contracts** remain authoritative inside each product/platform.
- **Interaction Kernel** carries selected cross-system envelopes/Profiles only where explicitly adopted.
- **EncyKlopedia** hands off immutable acquisition evidence and referent candidates through `encyklopedia.corpus-harvest-handoff/1.0.0`.
- **Da’at** maps acquisition/operational inputs into Kristal-native contracts without taking source or Kristal authority.
- **Kristal** owns referent identity semantics and Kristal v6 knowledge/state artifacts; the active baseline is Standard `6.0.0` + Referent Registry `1.0.0`.
- **UCKK / Univers-Cité** consumes pinned Kristal artifacts through `uckk.univers-cite-projection/1.0.0`; Moodle/glossary/media views are rebuildable projections.
- **kOA-Linux Release Sets** coordinate compatible platform artifact versions across release channels.
- **Koali Spaces** composes presentation surfaces without taking product authority.
- **UCKK interchange with kOA-Linux** remains directional (`publish_to_uckk`, `import_from_uckk`) and does not create a shared database.
- **SemantiK / GF release integration** uses owner-preserving external contracts; sequencing does not transfer grammar, semantics or diagnostic authority.

## Key non-confusions

```text
source acquisition            ≠ knowledge validation
referent candidate            ≠ authority-recognized referent
Kristal artifact              ≠ UCKK projection state
IK Profile                    ≠ kOA-Linux internal contract unless adopted
Release Set                   ≠ Kristal validation/recognition
Space activation              ≠ Runtime Pack activation
kOA Node Agent operation      ≠ active Runtime Pack ownership
UCKK import/publication       ≠ shared database or background sync
SemantiK release sequencing   ≠ ownership of GF/SA semantics
```

See the [contract map](../2-Technical-Reference/40-integration/contract-map.md) and [knowledge projection boundary](../2-Technical-Reference/40-integration/knowledge-projection.md).

## v6 actionability rule

Kristal may describe actionability, but an `automatic` classification is not cross-system execution authority. Automation still crosses the explicit owner contract and admission boundary.

## Skope and Ékole

Skope supplies a **noncanonical** Wikidata scope/snapshot that may *eventually* enter governed acquisition/mapping before Kristal compilation. Ékole is a pedagogical **consumer/projection** over authoring workspaces, with candidate Moodle plans only. No direct Skope→Ékole link, automatic publishing, or new IK Profile is claimed. [Read the candidate handoff map](../2-Technical-Reference/40-integration/skope-ekole/index.md).
