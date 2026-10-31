<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Conformance-v8 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 5a9768969d5e2792fc136c89f1cf3c6d61a9ea0253d55183813ab777fc3f511f -->

# v8 Conformance

> **v9 note:** V8 conformance remains an inherited capability surface. Inherited v9 profiles are documented in [[Conformance-v9]], and hosted-network qualification in [[Conformance-v10]].


v8 defines additive profiles. A deployment claims only the profiles it actually implements.

## V8-Reader

Reads valid v6, v7 and v8 companion artifacts without redefining inherited semantics. Preserves unresolved identities and compatibility boundaries.

## V8-Language

Validates lexical Kristals/stacks, interprets BCP 47 locale tags, resolves deterministic precedence, exposes missing/conflicting lexicalization and never fabricates a lexical value as canonical output.

## V8-Query

Distinguishes read models/results from canonical state, supports exact identity-based query for declared modes, validates typed traversal, exposes normalized plans and reports `complete|partial|error` plus continuation/truncation metadata.

## V8-Federation

Preserves shard/source provenance, enforces parent budgets across subqueries and exposes unavailable/unknown shard outcomes. Continuations bind to stable normalized query/source state.

## V8-AI-Context

Emits bounded context bundles with source fingerprints, provenance/trust metadata, completeness, omissions, unresolved items and declared byte/token budget semantics.

## V8-Integrity

Preserves inherited byte/content identity. Semantic fingerprints, when supported, use declared versioned profiles and cannot masquerade as inherited byte identity.

## V8-Full

Satisfies all profiles above. Claiming a v8 profile does not remove any v6/v7 conformance obligation already claimed.
