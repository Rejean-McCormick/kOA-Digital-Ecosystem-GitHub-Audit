<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Article-Source-Format | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 82633311146dd4423802e4f158df5ee6b542fb83b1643dc177fee02c7decfcef -->

# Article Source Format

The article source is a **derived editorial adapter**, not the canonical Kristal data format. It binds already selected content into Spek slots; it is not a raw Kristal→article inference format.

## Main sections

- `format`: `kristal.layout-article-source/0.1`.
- `article`: `id`, `title_key`, `subtitle_key`, `abstract_key`.
- `source`: origin, optional pinned v9 reference, review declarations.
- `units`: stable identifiers, kinds, realization keys, epistemic statuses, evidence references.
- `evidence`: ID, realization key, locator and evidence status.
- `sections`: ordered ID, heading realization key, chosen layout, slot→unit/evidence bindings.

## Minimal binding example

```json
{
  "id": "section.finding",
  "layout": "result-card",
  "heading_key": "heading.finding",
  "slots": {
    "claim": "unit.claim",
    "conditions": "unit.scope",
    "evidence": ["evidence.one"],
    "uncertainty": "unit.limit"
  }
}
```

These IDs must refer to declared units/evidence of the right kind. All heading/text realization keys need all selected languages. Slots reject missing mandatory members and extra role names. The full working fixture is `examples/article.json`. The optional Wiki extension keeps this source format unchanged and adds an independent Arketype profile binding (for a collection: `<slug>/archetype.json`).

## Evidential obligations

A result card's evidence must also appear in its claim's evidence references. Argument maps need an evidence-linked premise. An `unknown` or unreviewed status must not be silently promoted to a proved conclusion.

## Source identity

The optional `--state-snapshot` mode compares a pinned state reference and claimed digest to supplied v9 snapshot **metadata**. This is **not** a cryptographic rehash of a Kristal JCS commitment. See [[Epistemic and Security Boundaries]].

## Wiki page composition (optional overlay)

`build-wiki` consumes the same `article.json` and `realizations.json` but requires an explicit `--archetype` and a declared section layout allowed by that profile. Arketype compatibility never bypasses required Spek slots. The output is a **new, private Markdown draft** with a SHA-256 manifest; it does not mutate canonical Kristal state. See [[Wiki Draft Workflow]].
