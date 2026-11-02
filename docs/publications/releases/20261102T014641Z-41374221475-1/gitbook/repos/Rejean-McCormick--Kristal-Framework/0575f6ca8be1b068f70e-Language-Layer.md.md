<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Language-Layer | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 3b132a4d2d3024436060f1ea33aec1dce213ee464919f5490ae577061e4cf3bf -->

# Language Layer

The v8 Language Layer separates **stable semantic identity** from **human language**.

It supports many languages, specialist vocabularies, education levels, regional terminology and project-specific lexical choices without embedding every translation in every semantic Kristal.

## Lexical Kristal

A `kristall_lexicon` is an external companion artifact. Each lexical entry points to a semantic reference and provides language-specific lexical material.

Default identity spaces are:

- `kristall` — v7/v8 `KQ`, `KP`, `KA`, `KS` identities;
- `kristal_v6` — stable v6 namespaced referents where no v7 mapping is required;
- `external` — an explicitly declared external identity space.

A lexicon may be incomplete. `lexical_status: missing` records a known gap and must never be replaced by an invented translation.

## Locale and script

Language and requested locale use BCP 47 syntax, for example:

```text
fr
fr-CA
sr-Cyrl
```

Lexicons may also declare default script, writing direction and optional morphology. These assist rendering but do not change semantic assertions.

## Composition

Lexicons should be small and composable:

```text
fr-core
+ fr-science
+ fr-chemistry
+ fr-science-college
+ fr-CA
+ project lexical delta
```

Domain, education and geographic scopes should use semantic identities where stable IDs exist.

## Non-authority

Definitions, glosses, synonyms and usage notes in lexical artifacts are explanatory lexical material. They cannot override semantic assertions, ontology constraints, provenance or authority rules.

See [[Lexical-Resolution]] and [[Semantic-Universe-and-Lexical-Kristals]].
