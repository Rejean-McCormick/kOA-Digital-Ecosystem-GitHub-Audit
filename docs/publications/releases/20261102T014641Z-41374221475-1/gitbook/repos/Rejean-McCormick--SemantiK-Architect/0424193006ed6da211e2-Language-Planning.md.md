<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Language-Planning | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 9e307d7764d3fdba31775a25da6c49ce372a650c8ea22b8ee0d077a742ddbc4b -->

# Language Planning

`LanguagePlanner` converts a language-neutral `CommunicationPlan` into a target-language `LanguagePlan`.

## No English pivot

SA does not generate English and then translate it.

```text
wrong: semantic meaning → English sentence → target language
right: semantic meaning → target-language planning → GF target language
```

## LanguagePlan

A `LanguagePlan` contains:

- target language and locale;
- output block topology;
- `RealizationUnit`s;
- SA↔GF operation IDs;
- semantic role bindings;
- lexical slots;
- grammatical/communicative features;
- source obligation IDs.

## RealizationUnit

A `RealizationUnit` is the smallest planned grammatical unit passed to the realizer boundary.

Conceptually:

```text
RealizationUnit
  unit_id
  operation_id
  role_bindings
  lexical_slots
  feature_bindings
  obligation_ids
  semantic_refs
  output_slot
```

There is no extra general-purpose construction IR between `LanguagePlan` and the realizer.

## Language-specific variation

Different languages may legitimately:

- split the same obligations into different sentence counts;
- realize possession differently;
- use different argument packaging;
- express politeness differently;
- choose different information structures.

The obligation set and semantic roles must remain faithful.

## No language branches in shared core

Shared planning logic must not become:

```python
if language == "sq": ...
elif language == "fr": ...
```

Language-specific behavior belongs in validated grammar/runtime artifacts or explicit language-planning strategies behind stable interfaces.

## Extensible predicate planning hints

For domain predicates that cannot be interpreted from generic roles alone, ACLs may provide supporting hints:

- `sa:operation`
- `sa:role-map`
- `sa:slot-map`
- `sa:feature-map`

These hints select a canonical SA operation without adding domain branches to the core. They are realization metadata, not new facts.
