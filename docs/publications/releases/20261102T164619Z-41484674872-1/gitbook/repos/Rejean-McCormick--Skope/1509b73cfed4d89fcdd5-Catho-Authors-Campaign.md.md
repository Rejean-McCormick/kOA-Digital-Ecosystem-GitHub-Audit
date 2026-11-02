<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Catho-Authors-Campaign | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: f588277aa707e4c7ce03609bf91005efc20808147246ac2e63fe8fcf45a4aac5 -->

# Catho recognized persons → authored works campaign

The `catho-recognised-authors` profile is **not** a generic traversal pass. It is a specialized, explicitly initiated workflow that reads a Catho Kristal recognition roster, resolves unambiguous local Wikidata persons, collects indexed `P50` work relations, then attempts the separate **verified full-record extraction** stage.

## Source and target

- Profile format: `skope.author-works-campaign/1.0`.
- Required target: active **`kristal-catho`** workspace.
- Roster: `canon/domain/personnes-reconnaissances.json`, read **only**, beneath that workspace.
- Work relation: `P50` (Wikidata `author` relation in the index).
- Associated extraction profile: `catho-recognised-authors-full-wikidata`.

**Procedure:** activate the Catho Kristal → select `catho-recognised-authors` → **Check roster** → review categories/counts → explicitly start **Run complete author campaign**. Resume is also explicit and retains the worker's captured workspace.

## Matching policy

Names and explicitly listed variants are normalized for exact lookup in the compact name index. `P31=Q5` is required for eligible person candidates. Multiple human homonyms or overflow produce an **ambiguous** case; absent matches remain **unmatched**. Skope deliberately does not guess identities from partial resemblance in this campaign stage.

Category and recognition rosters do not themselves prove that a selected Wikidata QID is the right historical person; they identify people to research. Likewise `P50` is an indexed assertion, not independent proof of every work attribution.

## Result files

Specialized jobs under `30_working/skope-large-scopes/<job>/` can include:

| Artifact | Meaning |
| --- | --- |
| `matched-people.jsonl` | Exactly matched human roster entries and source context |
| `unresolved-people.jsonl` | Ambiguous/unmatched cases for human review |
| `author-work-links.jsonl` | Index-discovered author→work `P50` edges |
| `selected-qids.jsonl` | Persons/works selected for later full-record extraction |
| `provenance-manifest.json` | Campaign counts, source digest, limitations |
| `campaign-state.json` | State and progress for the specialized orchestration |

The full-record stage is subject to the same dump, locator, manifest and free-space blockers described in [Full-Record Extraction](Full-Record-Extraction). A campaign can produce useful partial roster/relationship artifacts without achieving complete source JSON extraction.

## After unresolved cases

Use [Identity Reconciliation](Identity-Reconciliation) for individual documentary review, or [Batch Identity Review](Batch-Identity-Review) for an entire unresolved roster. **Saving a new identity decision never silently regenerates a source campaign or fills in missing works.**
