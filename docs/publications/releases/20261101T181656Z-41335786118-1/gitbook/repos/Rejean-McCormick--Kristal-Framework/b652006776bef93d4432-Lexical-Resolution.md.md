<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Lexical-Resolution | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 380297e2ac25d4ae7acc2ebd6e9999da264652682686b0aeb050401d2a206e67 -->

# Lexical Resolution

A `kristall_lexicon_stack` declares deterministic lexical precedence.

## Resolution algorithm

For a semantic reference and requested locale:

1. validate locale and stack policy;
2. select compatible lexicons and explicitly allowed fallbacks;
3. discard entries not marked `resolved`;
4. select the matching entry with highest declared precedence;
5. if equal-precedence entries disagree, return a conflict;
6. if none resolve, return the semantic reference with `lexical_status: missing`.

Locale fallback such as `fr-CA → fr` is allowed only when declared by policy. Fallback does not create semantic equivalence.

## Recommended precedence

```text
base language
  < general domain
  < specialist domain
  < education / region
  < project delta
```

Precedence is a **rendering rule**, not semantic authority. A project may prefer another display term without changing the concept.

## AI-generated translations

A language model may propose lexical candidates during curation, but generated translations must not become canonical lexical output without an explicit curation/admission step.

## Conflict visibility

Lexical disagreement is data. Resolvers expose conflicting candidates and lexicon provenance instead of silently choosing one.
