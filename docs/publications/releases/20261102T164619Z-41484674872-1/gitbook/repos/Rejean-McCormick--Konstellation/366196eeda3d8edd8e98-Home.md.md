<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Home | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: c3b53cc06a46c9d38895347e31b56093c7e62edc91b300d56499b9bee4a367e8 -->

# Konstellation — Working Wiki

> **Navigate knowledge in Kristals without changing its meaning.**

Konstellation is an **adaptive, domain-independent knowledge explorer**. It reads surfaces it is authorized to access, applies reader policies, proposes relevant perspectives, and turns results into visual navigation paths. A view displayed in Konstellation **does not add canonical truth** to a Kristal.

## Start here

- **[[Quick Start|Quick-Start]]** — install and launch Konstellation on Windows.
- **[[Select a Kristal|Selecting-a-Kristal]]** — understand the neutral **My Kristals** landing page.
- **[[Explore Knowledge|Exploring-Knowledge]]** — perspectives, Astrolabe, facets, relationships, and projections.
- **[[Semantic Labels and Localization|Semantic-Labels-and-Localization]]** — read technical properties, Wikidata IDs, statuses, and provenance in the user-facing French display.
- **[[Astrolabe and Search|Astrolabe-and-Search]]** — orientation matching, ranking, and search limitations.
- **[[Example: Kristal Catho|Kristal-Catho]]** — open Catho without moving it.
- **[[Troubleshooting|Troubleshooting]]** — common startup and integration errors.

## How it works

```text
Konstellation.cmd
  → config/local-catalog.json
  → My Kristals (explicit selection)
  → compatible reader and read-time checks
  → Reader Policy / QuerySpec / Lens
  → NavigationPlan → projection → renderer
  → exploration, relationships, and provenance
```

Kristal directories **are not moved**. The local catalog discovers immediate subdirectories containing `kristal.workspace.json`. Opening a Kristal is **not** the same as qualifying or publishing it.

## Project status — October 17, 2026

| Item | Documented status |
| --- | --- |
| Application | `1.0.0-rc.2` in the examined snapshot |
| Neutral landing page and local catalog | Functional prototype in the neutral-selector archive |
| Local Kristal v10 reader | **Experimental**: reads v9 semantic states; optionally supports derived projections |
| Reference Framework | `10.0.0-draft.3.2`, a **proposed standard**, not finalized |
| Manager | Advisory alpha.14 integration / candidate contracts |
| Daat and Interaction Kernel | No changes needed for the local selector |
| French semantic display | **Experimental patch (October 17)**: explicit predicate labels, readable status text, filtered technical facets, and reduced search false positives |
| Search and visual presentation | Word-aware Astrolabe and less-prominent `v9:node_kind` metadata; not a universal translator or ontology reasoner |
| Release 1.0 qualification | **Not achieved**: full Windows build and E2E still need qualification |

This wiki describes the **October 16 neutral-selector baseline plus the October 17 semantic-display patch** (`Konstellation_lecteur_v10_presentation_FR_2026-10-17.zip`). It does not claim the GitHub repository or the user's Windows installation has been updated. The UI improvements are currently **French-specific display mappings**, although this wiki is in English.

## Browse the guides

| Use | Understand | Develop / operate |
| --- | --- | --- |
| [[Quick Start|Quick-Start]] | [[Architecture|Architecture]] | [[Configuration|Configuration]] |
| [[Select a Kristal|Selecting-a-Kristal]] | [[Contracts and Versions|Contracts-and-Versions]] | [[API|API]] |
| [[Explore|Exploring-Knowledge]] | [[Manager and Discovery|Manager-and-Discovery]] | [[Develop a Reader|Developing-a-Reader]] |
| [[Semantic Labels|Semantic-Labels-and-Localization]] | [[Astrolabe and Search|Astrolabe-and-Search]] | [[Testing|Testing-and-Qualification]] |
| [[Catho|Kristal-Catho]] | [[Ecosystem and Responsibilities|Ecosystem-and-Responsibilities]] | [[Testing and Qualification|Testing-and-Qualification]] |
| [[FAQ|FAQ]] | [[Security|Security-and-Privacy]] | [[History|History-and-Migration]] |

Detailed decisions and contracts remain in the repository's `docs/`, `contracts/`, and `server/` folders. This wiki is a **navigation guide**, not a replacement for the authoritative standards or source schemas.
