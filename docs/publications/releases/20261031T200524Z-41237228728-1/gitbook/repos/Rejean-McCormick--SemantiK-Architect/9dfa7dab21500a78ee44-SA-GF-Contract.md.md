<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/SA-GF-Contract | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: da67457737e84a966867264cc195657ba22aa4772b1459d6dbfff611be7aa364 -->

# SA ↔ GF Contract

GF/RGL is the grammatical realization authority. SemantiK Architect targets a **thin, versioned bridge contract** instead of manipulating arbitrary grammar internals.

## Why a bridge contract exists

Without a stable bridge, every language could require bespoke SA code. The bridge turns SA's planned grammatical intent into expressions accepted by the exact PGF artifact.

```text
LanguagePlan
   │
   ▼
RealizationUnit
   │ operation_id + slots + features
   ▼
SA↔GF bridge spec
   │
   ▼
GF expression
   │
   ▼
PGF concrete language
   │
   ▼
surface text
```

## v1 operation families

The initial registry includes:

- `discourse.greeting`
- `discourse.closing`
- `clause.intransitive_event`
- `clause.transitive_event`
- `clause.ditransitive_event`
- `clause.copular_classification`
- `clause.copular_attribute`
- `clause.existential`
- `clause.locative`
- `clause.possession`
- `clause.passive_event`
- `question.polar`
- `question.content`
- `directive.action`
- `coordination.clause`
- `relative.subject`
- `relative.object`
- `nominal.apposition`
- `comparison.comparative`
- `comparison.superlative`

A capability profile defines the exact subset a language must support.

## Strict consumption rule

A bridge variant succeeds only if it faithfully consumes all required semantic material in the `RealizationUnit`.

The adapter verifies that:

1. required slots are available;
2. every bridge placeholder is bound;
3. every lexical slot is consumed;
4. every communicatively relevant feature is consumed or explicitly acknowledged;
5. variant conditions match.

If, for example, an obligation contains action + machine + deadline and the bridge would realize only action + machine, realization fails instead of returning partial text.

## Versioning

- patch — clarification/tests only;
- minor — additive operation/features with old behavior preserved;
- major — incompatible operation semantics or role/feature changes.

Runtime artifacts declare their exact compatible contract version.
