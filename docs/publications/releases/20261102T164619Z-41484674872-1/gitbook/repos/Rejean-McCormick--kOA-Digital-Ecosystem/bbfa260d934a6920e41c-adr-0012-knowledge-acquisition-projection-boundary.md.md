<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/90-reference/adr/adr-0012-knowledge-acquisition-projection-boundary.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: da883244ce4e76fdabba464bf8a44a879589eb2694f0c0779bb4c354a94e8ecc -->

# ADR-0012 — Knowledge acquisition, Kristal canon and consumer projections

- **Status:** Accepted
- **Date:** 2026-09-28

## Decision

1. EncyKlopedia owns source discovery/acquisition and immutable evidence handoff.
2. Da’at owns mapping/ACL at the Kristal boundary.
3. Kristal owns referent identity semantics, assertions, evidence/provenance, validation/recognition and canonical epistemic artifacts.
4. UCKK/Univers-Cité owns consumer projection choices: scope membership, primary navigation view, derived glossary, Moodle materialization and media-library presentation.
5. A consumer projection is rebuildable and never becomes the Kristal source of truth.
6. External identifiers such as Wikidata or Gutenberg do not transfer authority.
7. Interaction Kernel carries only explicitly adopted versioned boundary profiles; it owns none of the participant states.

## Frozen contracts

- Kristal Standard `6.0.0`; Referent Registry `1.0.0`.
- EncyKlopedia `encyklopedia.corpus-harvest-handoff/1.0.0`.
- UCKK `uckk.univers-cite-projection/1.0.0`.
- IK `kristal.build.request/2.0.0`, `kristal.artifact.ready/2.0.0` and `kristal.revision.request/2.0.0` for the v6 knowledge boundary.

Amended by ADR-0013 for Kristal v6 generalized state roles and the actionability/execution-authority boundary.
