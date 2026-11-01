<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Legacy-Migration-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 375d14c0e1304897756ae7f75c63be252a83e7a24eec083936877004df11be45 -->

# Migration of word-based historical Kristals

A legacy semantic graph may use words, slugs or local URNs as subject/predicate IDs. **Do not globally replace all matching strings.** Only fields identified by the original *schema as semantic references* can be proposed for conversion; quotations, document paragraphs and typed string literal values remain words.

## Safe pipeline

1. **Inventory** exact legacy files and their format/version; identify semantic-reference paths by schema. Compute original SHA-256 and preserve source bytes.
2. **Resolve candidates** from old identity registry first, then accepted exact external crosswalk and contextual lexical terms. Missing/ambiguous results are not guessed away.
3. **Review** each candidate against type (KQ or KP), domain and evidence; track accepted, rejected and pending decisions. Lexical similarity alone is not approval.
4. **Export** a `kristal_dik_conversion_plan` with exact JSON Pointer paths, original values, target IDs, source hash and review metadata.
5. **Apply only by an authorized producer**, under the Authoring Kit's supported input profiles, to an entirely new revision; revalidate source hashes, paths and identities. Do not mutate an old committed Kristal.
6. **Validate** the v11 artifact and record provenance, unanswered references and previous logical commitments.

## Example — what must not change

```json
{
  "subject": "Augustin d'Hippone",
  "predicate": "parle_de",
  "citation": "Le mot grâce apparaît dans ce texte."
}
```

The `subject` and `predicate` may be proposed for KQ/KP migration **after schema and human validation**. The `citation` remains untouched, even if it contains the same word as another mapped referent.

## Limits of the current toolchain

Framework `tools/v11/resolve_legacy.py` emits *candidate reports*, not committed conversions. `tools/v11/dik_conversion_plan.py` verifies structure and source digest without executing edits. Authoring Kit `4.0.0-draft.3` has limited opt-in support for **already v11-shaped** graph sources and approved plans plus field-role reviews, not arbitrary automatic conversion of all old formats. More complex historical corpus migration is separate work.

**See also:** [[Authoring-Kit-v11]] · [[Wikidata-Crosswalk-v11]] · [[Migration-v10-to-v11]].

**Interoperability note:** [[diK-Authoring-Exchange-v11]] describes the controlled catalog handoff; migration remains a separately authorized producer activity, not a consequence of dictionary import.
