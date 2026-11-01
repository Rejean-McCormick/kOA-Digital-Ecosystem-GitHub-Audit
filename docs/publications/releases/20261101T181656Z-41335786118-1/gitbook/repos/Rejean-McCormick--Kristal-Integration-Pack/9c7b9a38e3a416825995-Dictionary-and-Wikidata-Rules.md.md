<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Dictionary-and-Wikidata-Rules | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: adb87e7d9e296449bd67bbf88f3540984c82a89f4d8f627c4bba62747bcb8356 -->

# Dictionaries, Wikidata and Identity Rules

Kristal Framework v11 keeps semantic identities apart from language and outside references.

| Layer | Example identifier | Rule |
| --- | --- | --- |
| Canonical entity | `KQ1001` | Stable internal entity ID, interpreted with its namespace |
| Canonical property | `KP2001` | Stable internal property ID |
| Assertion / source | `KA…` / `KS…` | Explicit semantic assertion and evidence references |
| Wikidata item/property | `Q8018` / `P50` | **External identifiers only**, not interchangeable with KQ/KP |
| Human labels | A preferred term or alias | Lexical data, never an identity or automatic match |

## Approved external identity links

Only an **accepted `exactMatch`** that has passed the Framework's crosswalk checks may be surfaced as an accepted external exact reference. Suggested matches, fuzzy term similarity, `closeMatch`, unreviewed redirects, and data-import existence do not establish semantic equivalence.

## Catalog validation

The Pack delegates to Framework v11 for:

- Catalog namespace and language declarations.
- SHA-256 checks of the lexicon layers actually referenced by the catalog.
- Crosswalk and registry coherence, including required external evidence.
- Declared precedence, fallbacks and lexical record validation.

A diK alpha.7 `import-large` job may produce a valid catalog from approved mappings, but its own SHA-256 of dump bytes **does not prove their Wikidata origin**. The Integration Pack does not authenticate review signatures or inspect the complete original dump.

## Import and selection are separate

The Pack only verifies the handoff. The **Authoring Kit** must separately register a revision and explicitly select it. The Framework's canonical IDs and existing curated lexical layers must not be silently overwritten by incoming Wikidata text.

See [[diK-to-Authoring-Kit-Handoff]] and [[diK-Alpha7-Receipts]].
