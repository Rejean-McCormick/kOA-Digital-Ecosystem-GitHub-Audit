<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/AI-Context-Compiler | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 6350a78dd1906be6705edf356a66fb94e6321adba94fed23356d199893390dea -->

# AI Context Compiler

The AI Context Compiler transforms an exact KQP result into a bounded `kristall_ai_context_bundle`.

## Semantic atoms

The compiler should select **semantic atoms** instead of independently filling unrelated arrays until a budget is exhausted.

An atom can contain enough material to interpret one unit, for example:

- assertion + subject/predicate/object + provenance;
- structural edge + endpoint identities + relation identity;
- evidence reference + digest + source/trust metadata;
- entity/property card needed to resolve referenced IDs.

This reduces the risk of including a claim while dropping the identity or provenance needed to interpret it.

## Selection

Selection may consider:

- roots and required connectors;
- query intent;
- graph distance;
- property relevance;
- evidence/epistemic status;
- authority scope;
- trust class;
- byte/token budget.

Selected and omitted material remain distinguishable.

## Budget model

`max_bytes` is the portable hard payload budget. `max_tokens` is optional and meaningful only with a declared `tokenizer_id`. Heuristic token estimates must say that they are heuristic.

## Completeness

The bundle carries forward query completeness and adds compiler truncation. Semantic/evidence closure should be reported as `complete`, `partial`, `not_requested` or `unknown`.

## Provenance and trust

Retrieved content retains provenance and trust class. Text included in context can inform reasoning; it does not become system policy or execution authority merely because an AI sees it.

## Language

Compilation operates on semantic IDs first. Lexical resolution is a final representation layer. Missing lexicalization preserves the semantic ID rather than causing model-generated translation inside the canonical bundle.

## RAG boundary

Vector/text retrieval is useful for discovery and uncrystallized source material. It does not replace exact Kristal traversal once semantic identities are known.
