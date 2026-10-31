<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Layout-Catalog | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 3b16aa62ba778f33c74ea4f530cf760fa5b9b0260e40765d8a789e4992290378 -->

# Layout Catalog

Spek 0.5.0 ships **eight reusable editorial layouts**. The authoritative versioned, typed contracts live in `layouts/*.json` in the main Spek repository; cardinalities and allowed kinds are checked by the compiler. These contracts are shared by HTML, PDF and XeLaTeX rendering.

| Layout ID | Purpose | Typical structure |
| --- | --- | --- |
| `result-card` | Finding with boundaries | Claim, conditions, evidence, uncertainty, optional implications |
| `argument-map` | Explicit reasoning | Thesis, premises, inference, conclusion, objections |
| `comparison` | Two approaches against criteria | Topic, criteria, approaches A/B, synthesis, limitations |
| `concept-card` | Explain a concept | Definition, examples/counterexamples, context, limits |
| `learning-path` | Guided learning or procedure | Objective, prerequisites, ordered steps, reflection, limits |
| `evidence-comparison` | Compare distinct source perspectives | Question, sources A/B, perspectives, synthesis, limits |
| `observation-inference` | Separate observation from explanation | Observations, interpretation, verification, limits |
| `chronology` | Document ordered events | Context, events, optional interpretation, limits |

The precise required/optional slots and per-slot cardinalities **must be read from each layout contract**; this overview is not a substitute for the JSON schemas. For example, a `result-card` requires explicit evidence links, while a `chronology` must not invent causality between adjacent events.

## Which layout for a Kristal Wiki page?

The optional Arketype Wiki overlay records 19 Arketype profiles with preferred and admitted layouts in `wiki-templates/archetype-profiles.json`. It **does not add new slot rules** or derive scientific facts from a page template. A single article can contain several compatible sections.

See [[Wiki Templates by Archetype]] and [[Wiki Draft Workflow]]. Specialized graph, taxonomy, mathematical and topological representations may need a new versioned Spek layout rather than an artificial conversion to an existing one.

## Implementing new layouts

A JSON contract alone is not an executable layout. Its rendering, localization, negative tests, semantic traceability and cross-format consistency must be implemented and reviewed. See [[Layout Authoring]].
