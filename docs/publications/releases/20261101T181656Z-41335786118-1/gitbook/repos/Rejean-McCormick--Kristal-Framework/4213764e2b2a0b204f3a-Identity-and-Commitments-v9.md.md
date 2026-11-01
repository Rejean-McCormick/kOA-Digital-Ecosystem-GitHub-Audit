<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Identity-and-Commitments-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 4867ef276e05d9f2e47ae001ed3bfab46715c281d419683387f6e2250fafee4f -->

# Identity and Commitments

V9 separates three questions.

## Semantic identity

**Which logical object is this?**

Inherited KQ/KP/KA/KS identifiers remain stable. Domain Logical Artifacts may use stable artifact URIs or another declared identity profile.

## Logical Commitment

**What is the exact normalized logical content of this revision?**

Two different physical encodings may have the same Logical Commitment.

## Blob digest

**What exact bytes were stored or transported?**

Compression, encryption envelope or physical packing normally changes this digest.

```text
SEMANTIC ID
    !=
LOGICAL COMMITMENT
    !=
BLOB DIGEST
```

## Baseline artifact profile

The baseline profile is:

```text
kristal.logical/jcs-sha256-v1
```

Its pipeline is conceptually:

```text
domain normalization
      ↓
collection normalization
      ↓
logical projection
      ↓
RFC 8785 JCS
      ↓
domain-separated SHA-256
```

The domain contract must define whether arrays are ordered sequences, sets, multisets or other deterministic structures. JCS alone cannot infer semantic collection meaning.

## Baseline state profile

State commitments bind the normalized membership/reference composition, not physical manifests, blob digests, activation status or runtime indexes.

## Revision continuity

When content changes while the conceptual object remains the same:

```text
same semantic ID
new logical commitment
```

When identity-bearing semantics change, that is an explicit **identity migration**, not a hidden schema edit.

## Profile immutability

Once a commitment-profile identifier is published, its projection, exclusions, ordering, domain separator and digest algorithm must not silently change.
