<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Wiki-Templates-by-Archetype | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: ad8351291bc4a7592643c657227cfd1c758a6e639b7bd56d5d37a0051d4eaa1f -->

# Wiki Templates by Arketype

**Contract:** `spek.wiki-archetype-templates/1.0` (optional overlay; not shipped in the clean Spek 0.5.0 snapshot).

Arketype describes **what kind of structured content** a Kristal page has; Spek describes **how that content can be represented** with typed slots. A profile is a compatibility constraint, not a replacement for the actual eight Spek `layouts/*.json` contracts.

## Registry — all 19 Arketype profiles

| Arketype | Preferred Spek layout | Admitted section layouts |
| --- | --- | --- |
| `carte-jalons-preuves` | `chronology` | `chronology`, `result-card`, `argument-map` |
| `compilation-collection` | `concept-card` | `concept-card`, `evidence-comparison`, `chronology` |
| `composition-hybride` | `result-card` | `result-card`, `argument-map`, `comparison`, `concept-card`, `learning-path`, `evidence-comparison`, `observation-inference`, `chronology` |
| `deposition-temoignage` | `evidence-comparison` | `evidence-comparison`, `chronology`, `observation-inference` |
| `diagnostic-causal` | `observation-inference` | `observation-inference`, `argument-map`, `result-card` |
| `dossier-suivi` | `chronology` | `chronology`, `result-card` |
| `etat-systemes` | `observation-inference` | `observation-inference`, `result-card`, `comparison` |
| `federation-topologie` | `comparison` | `comparison`, `concept-card` |
| `interpretations-couches` | `evidence-comparison` | `evidence-comparison`, `comparison`, `argument-map` |
| `invariant-theorie` | `argument-map` | `argument-map`, `result-card`, `observation-inference` |
| `memoire-recherche` | `result-card` | `result-card`, `evidence-comparison`, `observation-inference` |
| `modele-multiplexe` | `comparison` | `comparison`, `concept-card`, `evidence-comparison` |
| `parcours-pedagogique` | `learning-path` | `learning-path`, `concept-card` |
| `procedure-protocole` | `learning-path` | `learning-path`, `observation-inference` |
| `referentiel-semantique` | `concept-card` | `concept-card`, `comparison` |
| `registre-evenementiel` | `chronology` | `chronology`, `observation-inference` |
| `simulation-transition` | `chronology` | `chronology`, `comparison`, `result-card` |
| `taxonomie-classification` | `concept-card` | `concept-card`, `comparison` |
| `univers-oeuvres-medias` | `concept-card` | `concept-card`, `chronology` |

**Important:** `preferred_layout` is a proposal, not a force-fill instruction. The source supplies the ordered sections. If a required slot is absent or the unit kind/evidence cannot satisfy the chosen layout, Spek rejects the draft instead of manufacturing facts or reclassifying evidence.

## One Kristal, several sections

An article source may contain several sections using different admitted layouts. For example, a `diagnostic-causal` page might present `observation-inference` and later `result-card` **only when both sections are supported by actual, selected input units**. Spek does not infer the article plan from a folder name.

## Specialist domains

Taxonomies, topology, mathematical notation, graph relationships and similar specialized material may not be faithfully communicated by any of the current eight general-purpose layouts. The correct remedy is a **new versioned Spek layout and tested renderer**, not squeezing the input into a misleading card.

## Where profiles live

After installing the overlay:

- `Spek/wiki-templates/archetype-profiles.json` — authoritative compatibility table.
- `Spek/wiki-templates/archetype-binding.example.json` — typed per-Kristal declaration example.
- `Spek/docs/KRISTAL_WIKI_TEMPLATES.md` — normative implementation instructions.

List what the installed CLI admits:

```powershell
python -m spek list-wiki-templates
```

See [[Layout Catalog]], [[Kristal Wiki Architecture]] and [[Wiki Draft Workflow]].
