<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Astrolabe-and-Search | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 9f585aab17a973cf82d60b270b1fc880d934606bdeb2cc923262b11bb31c6fdc -->

# Astrolabe and Search

## Purpose

Astrolabe is an **orientation search** for the Kristal currently opened in Explorer. It suggests navigation candidates based on visible labels, aliases, and certain descriptions. A search result does **not** assert historical truth, identity equivalence, or a new relation between entities.

## October 17 matching rules

The French-display patch improves the existing orientation helper in **`src/lib/semantic-display.mjs`** and its use in **`src/components/Astrolabe.svelte`**:

1. Normalize case, accent marks, apostrophes, and selected punctuation for matching; preserve the original display text.
2. Favor exact labels and aliases over prefix or whole-word matches, with weaker description matches considered after stronger matches.
3. Respect **word boundaries** instead of finding arbitrary fragments inside larger words. Searching **`aquin`** can match **Thomas d’Aquin** without matching the ending of **Joaquín**.
4. Diversify the initial list by **visible title** so repeated titles do not dominate. Entries retain their distinct IDs, and no entity records are merged.
5. Bound suggestions (the current orientation helper requests up to **16 results**); the returned set is a navigational subset, not an exhaustive semantic search.

## Interpreting a result

A suggested work called *Thomas d’Aquin* is not automatically the same entity as the historical person. A source-language title is preserved when no grounded translation exists. Ranking does not prove a concept is related to the query beyond the actual text it matched.

### Example

| Search | Earlier symptom | Expected behavior with this patch |
| --- | --- | --- |
| `aquin` | Irrelevant works containing **Joaquín** | Word-aware matching favors **Thomas d’Aquin** |
| `Thomas d’Aquin` | Many same-titled notices filled the top results | More varied visible titles; IDs remain separate |
| Unknown `Q…` | Opaque ID | Clearly marked unresolved identifier, not an invented name |

## What is still limited

This is **not** a cross-lingual semantic search, external Wikidata resolver, synonym engine, or historical-entity reconciliation service. The reader cannot invent links, translate all work titles, or guarantee that an exact spelling match corresponds to a particular real-world person. Results still depend on available labels, aliases, allowed scope, and selected corpus.

## If search looks unchanged

Check that the October 17 patch is installed in the active repository, stop Konstellation, restart `Konstellation.cmd` (which rebuilds the UI in the documented local workflow), and test `aquin`. Review logs for stale frontend assets. See [[Troubleshooting|Troubleshooting]] and [[Semantic Labels and Localization|Semantic-Labels-and-Localization]].
