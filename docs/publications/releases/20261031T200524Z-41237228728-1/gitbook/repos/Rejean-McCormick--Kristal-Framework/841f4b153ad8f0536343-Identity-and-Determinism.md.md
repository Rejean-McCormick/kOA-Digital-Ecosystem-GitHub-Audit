<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Identity-and-Determinism | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 4805f8e472e18634b5bc931f47ad320407e203ed2917683d880157bf8b4a0057 -->

# Identity & Determinism

Kristal v9 preserves inherited deterministic identity and v8 semantic fingerprints while adding separate artifact/state Logical Commitments.

## Three different identities

Do not collapse:

1. **semantic identity** — stable KQ/KP/KA/KS or v6 referent identity;
2. **byte/content identity** — inherited canonical bytes/hash under the source contract;
3. **semantic fingerprint** — optional v8 derived digest over a declared semantic projection.

```text
IDENTITY != LABEL
SEMANTIC FINGERPRINT != BYTE HASH
HASH IDENTITY != FACTUAL AUTHORITY
```

## Canonicalization

The v6 canonicalization profile and inherited v7 content/hash boundaries remain unchanged. Enabling v8 must not recalculate old identities merely because a language/query capability was added.

## Deterministic projections

Derived indexes, lexical resolutions, query plans and AI bundles should declare source state/fingerprints and their transformation/profile inputs so reproducible outputs can be rebuilt where promised.

## Semantic fingerprint

A semantic fingerprint can ignore non-semantic presentation fields under a versioned profile, but it never replaces source byte identity. See [[Semantic-Fingerprints-and-Integrity]].

## Identity is not authority

A reproducible digest proves identity/integrity under its profile. It does not prove factual correctness, validation or authority recognition.
