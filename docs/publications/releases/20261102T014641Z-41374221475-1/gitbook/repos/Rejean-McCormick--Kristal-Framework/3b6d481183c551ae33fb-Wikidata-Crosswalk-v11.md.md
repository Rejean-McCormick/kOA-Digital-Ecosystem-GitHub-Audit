<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Wikidata-Crosswalk-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: c09545f14aa93da88ff0d4c4d8c70e0e613ec8e7924b2b8cb289296b82e739e3 -->

# Wikidata compatibility through a persistent crosswalk

Kristal **does not imitate Wikidata's Q-number sequence**. Internal KQ/KP identities remain stable and have their own namespace; Wikidata's Q/P identifiers are external records in `kristal_external_crosswalk`.

## Rules

- Internal **KQ↔Wikidata Q** and **KP↔Wikidata P**; wrong combinations are invalid.
- Mappings use a typed relation: `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch`.
- Statuses include `candidate`, `accepted`, `rejected`, `superseded`.
- An accepted exact match requires a review decision and `KS` evidence. A shared word or AI score is never proof of identity.
- A single active crosswalk view must not contain conflicting accepted exact matches; superseded decisions remain traceable.

## Existing KQ, later external Q

```text
Today:   KQ85001 → internal canonical graph
          no exact Wikidata mapping yet

Later:   Wikidata creates Q…
          candidate → context/evidence review → accepted exactMatch

Result:  KQ85001 remains unchanged
          a new versioned mapping is added externally
```

Likewise, Wikidata redirects, merges or splits do not silently merge local KQ identities. Reconciliation can supersede an old external decision but must preserve history and existing logical commitments.

## Import strategy

A local Wikidata mirror is a **candidate retrieval and lexical source**. Once a source Q/P is connected by `accepted + exactMatch`, an offline importer can extract its labels and aliases into language-specific imported dictionary layers. A candidate/closeMatch is not an accepted exact import route. Neither absence of an external Q nor a missing translation deletes the internal referent.

**See also:** [[Semantic-Identity-v11]] · [[Dictionary-Management-v11]] · [[diK-Integration-v11]].
