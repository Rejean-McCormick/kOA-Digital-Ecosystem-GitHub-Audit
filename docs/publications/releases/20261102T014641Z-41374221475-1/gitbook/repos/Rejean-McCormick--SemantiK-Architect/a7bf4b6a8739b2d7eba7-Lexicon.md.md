<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Lexicon | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 09a6d204205054eb72135e220acc3fcc7b621a84057656e4e54c647d7f6ca2ff -->

# Lexicon

Lexical resolution is split into two phases because construction choice may depend on lexical properties, while morphology remains GF's responsibility.

## Phase A — lexical knowledge preflight

Before final language planning, SA may resolve:

- candidate lexical sense IDs;
- lexical category;
- valency/argument structure;
- grammatical gender/class;
- governed complement/adposition information;
- countability/classifier metadata;
- register/domain terminology tags;
- lexical availability.

This information informs planning. It does not inflect words.

## Phase B — exact lexical binding

After the `LanguagePlan` selects operations, the binder maps every lexical slot to an exact runtime lexical reference.

```text
(unit_id, slot_id) → lexical_ref
```

Bindings are immutable and tied to the lexical artifact identity.

## Sources

Adapters may use local copies of:

- Wikidata/Wikidata Lexeme data;
- Kristal-derived lexical projections;
- GF dictionaries;
- project-owned lexicons;
- terminology packs;
- domain dictionaries.

No live service is required by the canonical runtime.

## Precedence

Lexical precedence must be explicit and versioned. A typical policy is:

```text
request terminology override
  > active domain terminology pack
  > admitted project lexicon
  > admitted Wikidata/Lexeme projection
  > admitted generic GF lexicon
```

## Fail closed

If a required semantic concept has no admitted lexicalization for the released language/profile, generation fails. SA does not guess a synonym or silently switch languages.
