<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/AI-Query-Layer | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: f51cca34c616bcd129593b4be7b158b05aa73a6fbdd8dddbfce0b5af3f0fbf2c -->

# AI Query Layer

The AI Query Layer lets an AI retrieve compact, exact semantic context without loading an entire Kristal or relying only on prose/chunk retrieval.

## Preferred flow

```text
natural-language request
    ↓ approximate discovery (optional)
candidate semantic IDs
    ↓ deterministic identity resolution
exact graph / assertion / evidence query
    ↓ typed KQP plan
semantic result / continuation
    ↓ context compiler
bounded AI context bundle
```

Approximate discovery can use lexical search, embeddings or ranking. Discovery remains distinguishable from exact semantic query.

## Standard query families

- `identity_lookup`
- `neighborhood`
- `semantic_traversal`
- `evidence_closure`
- `authority_resolution`
- `temporal`
- `diff`
- `capability`
- `constraints`
- `cross_kristal`
- `lexical`
- `unknowns`
- `semantic_slice`

Implementations may add namespaced custom modes but must expose their normalized plan and capability support.

## Progressive disclosure

Large evidence/source payloads should use a claim-check style: return semantic/evidence references, digests and compact metadata first, then expand only when needed.

## Exactness boundary

After identity resolution, traversal uses declared semantic IDs and canonical source references. Similarity scores, embedding distance and model confidence are never factual assertions.

## Planner boundary

An AI model may propose a KQP request. The query engine validates and normalizes it deterministically. The model does not gain authority by requesting a wider scope, more budget, privileged shards or mutation rights.

See [[Query-Algebra-and-Planning]], [[AI-Context-Compiler]] and [[Security-and-Trust-Boundaries]].
