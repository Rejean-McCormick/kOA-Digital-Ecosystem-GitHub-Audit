<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Semantic-Universe-and-Lexical-Kristals | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 3053f7b16954e3bccc3733ea71f2f5471e2d3996b9567040ad37c0af8e373bfc -->

# Semantic Universe and Lexical Kristals

## Language-neutral semantic universe

v8 does not create a second semantic identity system. The semantic universe is built from the existing v7 identity model (`KQ`, `KP`, `KA`, `KS`), v6-compatible referent mappings and declared external KOS crosswalks.

A large deployment may federate and shard the universe by subject:

```text
semantic universe
├── core
├── mathematics
├── physics
├── chemistry
├── biology
│   ├── botany
│   └── zoology
├── medicine
├── law
└── engineering
```

External systems such as Wikidata, UNESCO vocabularies, MeSH, GBIF or GeoNames may supply mappings, labels and evidence. Their IDs remain external mappings unless explicitly represented as Kristall semantic identities.

## Domain ownership with global contracts

Specialist communities may steward domain shards while shared contracts preserve identity syntax, provenance, compatibility, fingerprint profiles and query semantics.

## Orthogonal lexical universe

Language partitioning is independent from semantic partitioning:

```text
fr
├── core
├── science
├── chemistry
├── science-college
├── botany
└── botany-north-america

en
├── core
└── ...
```

A chemistry semantic shard can therefore be rendered in French, English or another language without modifying the chemistry Kristal.

## Companion pattern

A project can publish a small lexical delta next to its semantic Kristal:

```text
chemistry-course.kristal
chemistry-course.fr.lexicon.kristal
chemistry-course.es.lexicon.kristal
```

The project companion should contain only what is not already covered by the user's base/domain lexical stacks.

## Coverage generation

A lexical-delta generator should:

1. enumerate semantic references used by a target Kristal;
2. resolve them through the selected lexicon stack;
3. emit unresolved references as `lexical_status: missing`;
4. never invent a lexical value.
