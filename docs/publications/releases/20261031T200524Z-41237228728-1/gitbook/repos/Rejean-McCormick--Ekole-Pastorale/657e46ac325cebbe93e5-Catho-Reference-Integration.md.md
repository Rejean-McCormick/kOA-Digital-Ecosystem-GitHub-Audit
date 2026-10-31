<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole-Pastorale/wiki/Catho-Reference-Integration | commit: 7c73b3852cf83a881cd83a14f345a78e163dc8c3 | SHA-256: e0e2e7fb8e9c155d7c7c06addfc91ae728bd4aaa40deadc2995320c01f147f8f -->

# Catho Reference Integration

The project is intended to use the wider Catholic intellectual and spiritual heritage without duplicating that heritage into every course.

## Current state

The provided historical **A-Kristal-Catho** artifacts have been inventoried in:

```text
federation/catho-legacy-bridge.json
```

This file records two exact artifact hashes and historical source entries. The archive analyzed for the prototype reported **38 Doctors of the Church** and **138 documentary source references**. These figures describe the material inventoried in the supplied snapshot; they are not proof that every entry has been checked against the latest external authority or migrated into v11.

The bridge's status explicitly identifies it as a **pinned historical artifact, not a v11 crosswalk**.

## What is not yet implemented

- No automatic assignment of new v11 `KQ` identities to old person records.
- No confirmed equivalence between identifiers based only on their labels.
- No claim that all historical references are publication-ready or fully licensed.
- No live semantic federation from every course to independently versioned Catho artifacts.

## Proposed staged migration

1. **Inventory:** preserve original artifacts, their SHA256 hashes, source metadata, and licenses.
2. **Set ownership:** distinguish corpus, people/works index, saints/witnesses, and teaching sequences.
3. **Create reviewed v11 identities:** establish new namespace-scoped entities from genuinely reviewed records.
4. **Maintain a crosswalk:** store historic ID, new local ID, evidence, reviewer, date, relationship type, and status (unresolved/candidate/confirmed/rejected).
5. **Validate:** run Framework v11 checks, examine lexical coverage and assertion provenance, and verify state commitments.
6. **Pin references:** only reviewed references to known committed states should be consumed by course Kristals.

**Never** treat lexical similarity or historical URN spelling as a definitive semantic equivalence.

## Saints: writings and lived witness

A saint may be significant not only for the works they wrote, but also for virtues embodied in their life. The ARK-21 prototype for Francis of Assisi therefore separates writings, historical actions, later hagiography, virtue exemplars, and miracle-attribution narratives. It does not independently authenticate miracles.

Future saint records should be built as separate source-bearing Kristals and reused by multiple lessons.

## Audit tool

`outils/auditer_catho.py` checks the current documentary bridge against local historical assets when those assets are supplied. It does **not** perform the semantic migration described above.

Related pages: [Arketypes](Arketypes-ARK-20-and-ARK-21.md) and [Editorial Principles](Editorial-Principles.md).
