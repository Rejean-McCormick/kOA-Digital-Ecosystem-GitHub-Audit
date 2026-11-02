<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Conformance-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 33c89f03a39938351b775b784b2f806df55877e10cc695e05534b0b88bf3b305 -->

# Conformance — v11 draft.3

**Draft profile; not final cross-repository certification.** The authoritative sources are Framework `schemas/v11`, `spec/v11`, `tck/v11` and compatibility locks.

| Reference profile | Minimum behavior |
|---|---|
| Reader | Validate strict graph/register semantics and historic formats under their declared versions |
| Lexical | Separate KQ/KP identities from words, preserve missing/ambiguous translations |
| Crosswalk | Differentiate local and Wikidata namespaces, exact/near match, evidence and active conflicts |
| Dictionary Manager | Versioned source/import/curation layers, hashes, fallback and locale isolation |
| diK Coverage | KQ/KP counts separately by locale; distinguish direct/fallback/missing/conflicted |
| diK Plan | Verify JSON Pointer/source hash/target roles/review evidence, **no silent execution** |
| External source | Source system, snapshot, licensing and evidence-backed alignment |
| Full | All inherited version contracts **plus** full relevant producer and consumer qualification |

## Negative test examples

- Using raw `wikidata:Q8018` instead of a KQ entity in the graph;
- using a French or English word instead of a KP predicate;
- an unresolved object reference or wrong KQ↔P / KP↔Q pairing;
- an `accepted exactMatch` without review/KS evidence;
- multiple contradictory active exact mappings;
- a candidate-only external mapping treated as a verified label;
- interpreting a text quotation as a subject or predicate ID;
- claiming a fallback (fr-CA → fr) is a direct fr-CA translation;
- applying a proposed plan to a source whose SHA-256 changed.

## Commands in Framework root

```bash
python tools/v11/validate_v11.py
python -m unittest discover -s tools/tests -p 'test_v11_*.py'
python tools/v11/dictionaries.py audit \
  --catalog examples/v11/dictionaries/catalog.json \
  --crosswalk examples/v11/external-crosswalk.example.json \
  --registry examples/v11/identity-registry.example.json
```

The checks demonstrate the local reference implementation only. They do not prove that every historical Kristal is migrated, that all Wikidata data is correct, or that independently supplied Authoring Kit/diK/Arketype code is production-qualified. See [[Status-v11]].


**Draft.4 scope:** new Framework read-only diK/Authoring Kit preflight and wiki update; semantic v11 schema/TCK bytes are unchanged from draft.3. See [[diK-Authoring-Exchange-v11]] and [[Conformance-and-Ecosystem-v11]].

**Draft.4 local preflight:** `tools/v11/interop_preflight.py` validates catalog/registry/crosswalk and can compare per-graph locale coverage, refusing unapproved sources. This does **not** independently qualify every diK alpha.7 or Authoring Kit draft.3 release. See [[Conformance-and-Ecosystem-v11]].
