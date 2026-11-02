<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Semantic-Fingerprints-and-Integrity | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 12f2cde61b231e260652441a2e8932834a46b74d3a674a1072fb83cc2d9737e0 -->

# Semantic Fingerprints and Integrity

> **v9 note:** V8 semantic fingerprints remain valid under their profiles. They are not retroactively replaced by v9 Logical Commitments; see [[Identity-and-Commitments-v9]].


v8 separates **byte/content identity** from **semantic fingerprinting**.

```text
SEMANTIC FINGERPRINT != BYTE HASH
```

## Byte identity

Inherited v6/v7 content hashes continue to identify canonical bytes under their declared canonicalization boundaries. v8 does not change those rules.

## Semantic fingerprint

A semantic fingerprint is an optional derived digest over a versioned semantic projection. It is useful for caching, deduplication and query continuation when irrelevant presentation differences should not change the semantic key.

A fingerprint must declare a profile, for example:

```text
kristal.semantic-fingerprint/v1
```

The profile defines included semantic fields, excluded presentation/derived fields, canonical ordering, scalar encoding, hash algorithm and domain separator.

Processors cannot invent local exclusion lists while claiming the same profile.

## Language exclusion

Canonical semantic fingerprint profiles should normally exclude external lexical labels when those labels do not alter meaning. Lexical Kristals have their own content/fingerprint identities.

## Tamper evidence

A local hash chain or Merkle root is not independent proof if the same attacker can rewrite both data and chain head. High-assurance deployments should anchor release/snapshot roots in an independently governed system and define restore/fork reconciliation.

## Authority

A valid digest proves identity/integrity under its profile. It does not prove factual correctness or epistemic authority.
