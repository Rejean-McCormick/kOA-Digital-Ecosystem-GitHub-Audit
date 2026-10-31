<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Semantic-Identity-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: af2647f1f10b4259bbdc57eceadffd33a608af7fc7176e7d83a43a33d814584e -->

# Namespaced semantic identifiers — v11

**Generic name:** *semantic identifier*. For entities/concepts, the precise expression is *semantic referent identifier* (French: **identifiant de référent sémantique**, IRS). A bare **Q** is **not** a generic name: `Q…` is a Wikidata item ID.

| Internal family | Meaning | Typical canonical location |
|---|---|---|
| `KQ…` | Entity/concept/referent | Subject and entity-valued object |
| `KP…` | Property/relation | Predicate and qualifier |
| `KA…` | Assertion | Independently identified statement |
| `KS…` | Source/evidence anchor | Source reference |

The actual identity key is `(namespace_id, KQ123)` or `(namespace_id, KP456)`, **not** the number `123` or `456`. `KQ123` in one project and `KQ123` in a different namespace do not automatically designate the same meaning.

### Sample (illustrative, not production allocations)

```json
{
  "namespace_id": "example.org/kristal-demo",
  "entities": ["KQ1001", "KQ1002"],
  "properties": ["KP2001"],
  "sources": ["KS4001"],
  "assertions": [{
    "id": "KA3001",
    "subject": "KQ1001", "predicate": "KP2001",
    "object": {"kind": "entity", "id": "KQ1002"},
    "sources": ["KS4001"]
  }]
}
```

A real `kristal_semantic_graph` additionally includes `schema_version`, `artifact_type`, `graph_id` and is validated together with a matching `kristal_identity_registry`. The excerpt above is **illustrative, not a complete schema-valid artifact**.

**Typed literals** such as `{"kind":"literal","datatype":"string","value":"A historical quotation"}` may appear as values; the structural identity fields remain opaque IDs. The issue is never whether text exists anywhere; it is **whether a word is being used to identify semantic meaning**.

See [[Wikidata-Crosswalk-v11]] and [[Dictionary-Management-v11]].
