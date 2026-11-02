<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/wiki/Knowledge-Projection | commit: dd52671208ae86295bfcc5f896d236a20182faba | SHA-256: fd0707a4346db0aff6883adc60f1480a9f35e77497106b2238dbe0b6a7daeb33 -->

# Knowledge acquisition and projection

kOA separates **acquisition**, **epistemic authority**, **transport** and **consumer projection** so that no application silently becomes the source of truth for another system.

## Authority flow

```text
source/provider discovery
        ↓
EncyKlopedia
  acquisition evidence + referent candidates
        ↓  encyklopedia.corpus-harvest-handoff/1.0.0
Da’at
  mapping / ACL / contract adaptation
        ↓
Kristal
  Referent Registry + epistemic artifacts
        ↓  kristal.artifact.ready/1.1.0
UCKK / Univers-Cité and other consumers
  rebuildable scoped projections
```

## Frozen contract baseline

```text
Kristal                    5.0.0-rc.3 contract baseline
Referent Registry          kristal.referent-registry/1.0.0
knowledge-model bundle     sha256:07fe0527ab29a4b40870efdd0c9e0c67c91de919e5428047245b2a2c04f8ea98
EncyKlopedia handoff        encyklopedia.corpus-harvest-handoff/1.0.0
IK build request            kristal.build.request/1.1.0
IK artifact-ready event     kristal.artifact.ready/1.1.0
UCKK projection             uckk.univers-cite-projection/1.0.0
```

The supplied Kristal rc.3 metadata identifies tag `v5.0.0-rc.3` but does not resolve a final immutable commit SHA. kOA therefore treats it as a frozen **contract baseline**, not proof of a completed immutable release.

## Ownership

### EncyKlopedia

Owns source discovery/acquisition, provider resolution, immutable evidence, provenance and referent candidates. Wikidata, Project Gutenberg, VIAF and similar systems are external sources/identifiers; their presence does not confer Kristal authority.

### Da’at

Owns the integration mapping/ACL boundary into Kristal-native contracts. It preserves source identity and provenance without becoming the owner of source state or Kristal semantics.

### Kristal

Owns domain-neutral referent semantics, Structured Epistemic State, assertions, evidence/provenance, certainty, validation, authority recognition and related epistemic artifacts.

### UCKK / Univers-Cité

Owns consumer projection choices such as scope membership, primary navigation view, Moodle materialization, media presentation and derived indexes such as a glossary or chronology. The projection is rebuildable from a pinned Kristal state and does not become the Kristal source of truth.

## Consumer lens is not ontology

A consumer may choose a domain-appropriate primary lens:

```text
Christian intellectual corpus → people / works
industrial corpus             → installations / processes
art corpus                    → artists / works
historical corpus             → actors / events / places
```

These are **consumer projection choices**. kOA does not impose a universal people-first, concept-first, process-first or place-first ontology.

## Glossary and other derived indexes

A concept may be a first-class referent without becoming a mandatory navigation axis parallel to people or processes. A consumer glossary normally acts as a derived transversal index over concepts linked to assertions, actors, works and sources.

```text
consumer glossary / chronology / media view
    = rebuildable projection
    ≠ epistemic canon
```

## Non-confusions

```text
external identifier       ≠ internal authority
acquisition evidence      ≠ validated knowledge
consumer primary view     ≠ Kristal ontology
consumer glossary         ≠ parallel epistemic canon
Moodle/application record ≠ Kristal artifact
projection membership     ≠ source authority
```
