<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Dictionary-Management-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 1d42ae6785f282f3ea646265d0def515c4c26ac5d5ee34a21e26a7a130da05e3 -->

# Dictionary management and 300+ languages — v11

v11 stores the **canonical graph as language-neutral identities**. A collection of hashed, versioned lexical files is sufficient as the portable source of truth; an index, SQLite cache or GUI is derived and rebuildable. **Support for 300+ locales is a data/format capability, not a guarantee that all 300 translations already exist.**

## Three lexical layers

| Layer | Purpose | Provenance and mutations |
|---|---|---|
| `wikidata` | Labels, aliases, descriptions linked to reviewed Q/P exact crosswalks | Frozen by source snapshot; never overwritten by curation |
| `external` | Third-party terminology | Requires source identity, snapshot, rights and reviewed KQ/KP alignment with evidence |
| `curated` | Domain-specific locally preferred terms and translations | Independent reviewed layer; new revisions instead of modifying import |

The `kristal_dictionary_catalog` declares each locale's layers, relative file path, priorities, SHA-256 digest and explicit locale fallbacks. Text is separate from the graph, and **same word ≠ same referent**. Conflicting preferred terms at equal precedence must be reported, not randomly chosen.

### Language example

```text
KQ1001 → fr: “Augustin d'Hippone”
       → en: “Augustine of Hippo”
       → fr-CA: not translated directly
```

If the catalog explicitly declares `fr-CA → fr`, the displayed term may come from French, but completeness reports **fallback**, never direct Canadian-French translation. The absence of a local entry is reported as **missing**; no fictitious label is generated.

## Downloading Wikidata

A Wikidata entity dump contains labels/aliases/descriptions for languages **actually present**, so it can be scanned once and emitted into per-language imported layers. The shipped Framework reference importer reads a **local** JSON/JSONL/bz2/gz source; it does not implement remote download, resumable bulk-sync or full-dump scale certification. The separate **diK** application manages source-oriented tasks. Wikidata lexemes (`L…`) and their senses/forms are a different data family, not Q/P aliases.

## Verify local example

From Framework repository root:

```bash
python tools/v11/dictionaries.py audit \
  --catalog examples/v11/dictionaries/catalog.json \
  --crosswalk examples/v11/external-crosswalk.example.json \
  --registry examples/v11/identity-registry.example.json

python tools/v11/dictionaries.py resolve \
  --catalog examples/v11/dictionaries/catalog.json \
  --id KQ1001 --locale fr-CA
```

See [[diK-Integration-v11]] and [[Conformance-v11]] for report and validation boundaries.


**Draft.4 scope:** new Framework read-only diK/Authoring Kit preflight and wiki update; semantic v11 schema/TCK bytes are unchanged from draft.3. See [[diK-Authoring-Exchange-v11]] and [[Conformance-and-Ecosystem-v11]].

**Application update:** diK alpha.7 adds optional local resumable imports and a reconstructible SQLite index; this is application-level tooling and not a new Framework contract. See [[diK-Synchronization-v11]] and [[diK-Authoring-Exchange-v11]].
