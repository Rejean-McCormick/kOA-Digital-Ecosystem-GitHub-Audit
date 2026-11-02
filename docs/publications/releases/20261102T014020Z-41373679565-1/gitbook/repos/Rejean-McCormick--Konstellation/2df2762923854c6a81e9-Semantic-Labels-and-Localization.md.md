<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Semantic-Labels-and-Localization | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 357d026d787dbfb7bd710d2cabd9d29864ad785f2b7155491aa30d9c5d4d85b1 -->

# Semantic Labels and Localization

> **Readably presented does not mean semantically verified.** This page documents the October 17, 2026 **French-display patch** to Konstellation; it is written in English to match this wiki.

## Why the display layer exists

Kristals, derived graph packs, and Wikidata legitimately use stable machine identifiers (`P138`, `Q…`, `academicien_sur_liste_publiee`, `not_evaluated`). These codes should remain available for provenance, but most exploration surfaces should show grounded, readable labels.

The current implementation is in **`src/lib/semantic-display.mjs`**, used by the local v10 reader and the user interface. It adds a **bounded, explicit French mapping**, not an automatic translation service or a new semantic contract. All original predicates, entity references, statuses, and underlying assertions remain unchanged.

## Examples from the patch

| Source identifier or status | Current French display | Meaning / caveat |
| --- | --- | --- |
| `P138` | **Nommé d’après** | Explicit Wikidata property mapping |
| `P50` | **Auteur** | Explicit Wikidata property mapping |
| `academicien_sur_liste_publiee` | **Source attestant une inscription sur une liste d’académiciens** | Source-oriented; not independent certification of membership |
| `saintete_reconnue` | **Source relative à la sainteté reconnue** | Does not turn a source into an authenticated fact |
| `historic_author_reference` | **Référence d’auteur historique** | Domain predicate label |
| `pontificat_recense` | **Pontificat recensé** | Domain predicate label |
| `wikidata_identity · Albert le Grand` (open research hypothesis) | **Identité Wikidata proposée · Albert le Grand** | Still **unverified**; display change only |
| `not_evaluated` | **Non évalué** | Status text; not upgraded to validated |
| `unspecified` | **Non précisé** | Missing/unspecified status |
| `read_only_local_projection` | **Projection locale en lecture seule** | Access/presentation mode |

**Unknown codes remain unresolved.** For example, an unknown `P9745` becomes **« Propriété Wikidata P9745 (libellé indisponible) »**. A bare `Q…` is not automatically converted to a person's name: its fallback is **« Élément Wikidata Q… (libellé indisponible) »**. An unfamiliar domain predicate may receive a readable formatting fallback, but **not a guessed definition**.

## Where the changes appear

- **Relationships:** labels in the derived Catho relation registry use explicit French display names while preserving their original predicates and upstream references.
- **Facets:** empty facets and the routine `v9:node_kind` facet are hidden during normal exploration; an already-active filter is kept visible.
- **Entity inspector:** human-readable status strings appear in ordinary view. Technical references remain accessible under the provenance / technical-details disclosure, subject to Reader Policy.
- **Constellation:** `v9:node_kind` metadata no longer dominates recommended conceptual relationship groups. The underlying metadata and assertions are not deleted.
- **Open-research items:** known diagnostic prefixes receive non-assertive wording, explicitly preserving their candidate nature.

## Localization boundary

**This is not full multilingual support.** The dictionary currently targets French relation and status display. Wikidata work titles, source-language names, unknown properties, and domain-specific values may remain in English, Spanish, Latin, or as unresolved codes. There is no claim of a global locale switch or automatic translation of every Kristal.

A trustworthy longer-term approach would rely on **versioned, source-backed localized labels** and clear language fallback, but that remains a **future direction**, not a feature certified in this patch. Arketype, Manager, and Discovery do not automatically authorize or validate a translation.

## Validation and boundaries

The October 17 test report records **15/15 targeted tests passing**. In Catho, 4,527 entities and 13,217 assertions were preserved, and two observed `P138` edges displayed **« Nommé d’après »**. These checks do **not** establish historical truth, completeness of translations, full Windows UI qualification, or semantic identity equivalence.

See [[Astrolabe and Search|Astrolabe-and-Search]], [[Kristal Catho|Kristal-Catho]], [[Architecture|Architecture]], and [[Testing and Qualification|Testing-and-Qualification]].
