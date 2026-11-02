<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Canonical-Semantic-Model | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: c52d28dc4fb8aa5c54ce716813c85f9f5981cc924b7f24150fce6d5540ba1294 -->

# Canonical Semantic Model

The canonical model is designed to remain stable across many products and hundreds of languages without becoming a universal ontology.

It locks the **structure** of meaning while keeping semantic vocabularies extensible.

## SemanticGraph

A `SemanticGraph` contains:

- typed nodes;
- predicate-role statements;
- optional qualifiers;
- source references.

### Structural node kinds

- `EntityRef` — entity identity plus optional labels;
- `ConceptRef` — concept/lexicalizable identity;
- `LiteralValue` — string, boolean or identifier-like value;
- `QuantityValue` — number plus optional unit;
- `TemporalValue` — instant, date, time, interval or duration;
- `CollectionValue` — explicit collection with ordering semantics.

Domain-specific classes such as `TaskDeadline` do not belong in the SA core. They are mapped at the ACL boundary into generic semantic statements.

## SemanticStatement

A statement has the conceptual shape:

```text
SemanticStatement
  id
  predicate_ref
  arguments[]
    role_ref
    value_id
  polarity
  qualifiers[]
  source_refs[]
```

Predicate and role identifiers are namespace-qualified and extensible.

Example:

```text
statement: repair_event
  agent   → Marcel
  patient → machine_4356
  event_type → repair
```

## CommunicationObligation

A `CommunicationObligation` means **this content must be communicated**.

Baseline communicative forces:

- `ASSERT`
- `ASK`
- `DIRECT`
- `PRESENT`

A successful result must discharge every obligation.

There is no `required=false` escape hatch. If content should not be communicated, the caller does not submit it as an obligation.

## SupportingSemanticContext

Some information is needed to realize meaning correctly without itself becoming a claim. Examples:

- lexical sense hints;
- grammatical gender/class;
- valency/government data;
- terminology profile information;
- planning hints for extensible predicates.

Supporting context must never be silently promoted to a new factual claim.

## Semantic identity

SA accepts namespace-qualified identities such as:

```text
wikidata:Q123
wikidata-lexeme:L456
kristal:claim/abc
orgo:task/123
local-concept:repair
```

Wikidata is important, but it is not the only identity namespace.
