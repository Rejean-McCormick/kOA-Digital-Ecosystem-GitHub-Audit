<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Realizations-and-Languages | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 0a313a524b57f3bb9c25a479295324692d6ee41d247bc94fbe06c6a89240a1bb -->

# Realizations and Languages

Each used realization key must have **one non-empty entry for every requested language**. A source can use the same unit IDs for all languages, but must not assume that a short expression is automatically accurate in another language.

## Realization shape

```json
{
  "format": "kristal.layout-realizations/0.1",
  "entries": {
    "unit.claim": {
      "en": {"text": "A short expression.", "status": "fixture", "provider": "manual_demo"},
      "fr": {"text": "Un énoncé bref.", "status": "fixture", "provider": "manual_demo"},
      "it": {"text": "Un enunciato breve.", "status": "fixture", "provider": "manual_demo"}
    }
  }
}
```

Entries can declare `fixture`, `reviewed`, or `qualified`. **These are input declarations, not independently authenticated facts.** Qualified entries must include a nonempty `runtime_set_id`; production workflows also require independent language and disclosure approvals.

## Strict no-fallback behavior

- Missing English, French, or Italian entries block the build when that language is requested.
- Unrecognized languages block compilation (0.1 supports only `en`, `fr`, `it`).
- The imported historical SemantiK fixture never invents missing translations.
- Translating label text does **not** change the unit IDs or evidence references.

## SemantiK-based Wiki realizations (optional overlay)

For a real Wiki draft, the extension requires each used key to carry a declared SemantiK channel and a qualified realization with `request_id` and `runtime_set_id`. These are **input consistency checks** only; a separate trusted workflow must authenticate the actual RuntimeSet, review provenance, and grant disclosure permission. A missing FR/EN/IT rendering is not created by another language or by the template.

## Future qualification

An independently verified SemantiK integration should pin the RuntimeSet, preserve request identity, validate terminology, and record signed or otherwise authenticated review outcomes. Spek cannot perform that verification today.
