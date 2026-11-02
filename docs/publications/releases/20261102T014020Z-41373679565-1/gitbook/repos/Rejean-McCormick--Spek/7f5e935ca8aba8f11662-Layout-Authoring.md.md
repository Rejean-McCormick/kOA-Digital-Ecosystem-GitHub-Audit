<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Layout-Authoring | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 168fa8ede056626cbe85564cfcb451df283a39be31ad10f5325634421194255c -->

# Layout Authoring

A Spek layout is a versioned contract for **what typed information can be represented**, not a generic request to write prose. Layouts may arrange content, but may not select Kristal assertions or fill missing evidence or uncertainty.

## Contract example

```json
{
  "format": "kristal.editorial-layout/0.1",
  "id": "result-card",
  "version": "1.0.0",
  "slots": {"claim": {"allowed_kinds": ["claim"], "min": 1, "max": 1}}
}
```

This is a shortened illustration, not a full layout. Use the eight complete definitions in `layouts/*.json` as the authoritative contracts.

## Safe authoring process

1. Define the reader question and the intended semantic structure.
2. Declare typed slots, minimum/maximum cardinalities and ordering.
3. Keep evidence, limitations, applicability, objections and provenance visible.
4. Implement each admitted renderer in `spek/render.py` and translations in `spek/locale.py`.
5. Supply fixture data and negative tests for missing/extra/wrong-kind slots.
6. Compare the trace and reading order across HTML, PDF, XeLaTeX and `document.json`.
7. When supporting the optional Wiki extension, extend `spek/wiki.py` and register the layout under an explicit Arketype profile only when applicable.

## Archetypes are not layouts

An **Arketype** identifies a content-structure profile; a **Spek layout** defines typed reader presentation slots. The optional Wiki profile registry only maps compatibility (`preferred_layout`, `allowed_layouts`). It does not copy, weaken or replace Spek's contracts. A layout is never allowed to manufacture an assertion in order to satisfy a slot.

See [[Wiki Templates by Archetype]] and [[Epistemic and Security Boundaries]].

## Versioning and current implementation

Breaking semantic/cardinality changes require a new layout version. Spek 0.5.0 has eight explicit implemented layouts; an arbitrary JSON layout does **not** become automatically renderable. The Wiki Markdown renderer is available only after installing the separate integration overlay.
