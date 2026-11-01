<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Semantic-Identity-and-Registries | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 752ade55789886c03b7838654b5fc9acd92c849b02ee6eb7d72e286c274839ac -->

# Semantic Identity and Registries

v7 introduced opaque, namespace-scoped semantic identities that remain the semantic substrate used by v8:

```text
KQ…  entity / item
KP…  property / relation
KA…  assertion
KS…  source
```

External Wikidata, UNESCO, MeSH, GBIF, GeoNames, Orgo or other IDs are **mappings**, not Kristall master IDs unless separately represented under the Kristall identity rules.

Core identity rules include:

```text
IDENTITY != LABEL
EXTERNAL_ID != KRISTALL_ID
SIMILARITY != EQUIVALENCE
ENTITY RESOLUTION != AUTHORITY
```

A label such as `oxygen`, `oxygène` or `oxígeno` therefore does not define the semantic identity. v8 moves lexical forms into external lexical Kristals while keeping the KQ/KP/KA/KS substrate stable.

## Kristal vs Kristall

**Kristal** is a portable state/projection. **Kristall** is the encyclopedic knowledge space spanning many Kristals. Kristall preserves source boundaries and can generate oriented projections without flattening incompatible assertions into one truth document.

Large Kristall deployments should be shardable; the logical knowledge space does not require one giant file.

See [[Semantic-Universe-and-Lexical-Kristals]] and [[Version-Stack-v6-v7-v8]].
