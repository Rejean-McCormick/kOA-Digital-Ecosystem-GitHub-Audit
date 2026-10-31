<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Exploring-Knowledge | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 8d9c28b23f70d2ffdd861e7216f8645a8ac1122dd96e8d5afea35bfb44fffc1b -->

# Exploring Knowledge

## Inside Explorer

Once a Kristal is opened, Konstellation displays a **perspective** (entity type), facets, a list or another suitable representation, and available relationships. The same Kristal may support multiple ways of viewing a selection.

### Suggested workflow

1. **Perspective:** choose a family of objects (e.g., people, works, themes).
2. **Search:** look up visible labels and identifiers.
3. **Refine:** use facets and filters. The French display patch hides empty facets and routine technical node-kind metadata by default, unless a corresponding filter is already active. Hidden UI controls do **not** imply deleted assertions.
4. **Open an item:** inspect the context, links, and exposed sources. Readable French relation labels and statuses are presentation aids; open **Provenance et détails techniques** to inspect raw references when available.
5. **Adaptive navigation:** review suggested views and their explanations.
6. **Share / Save:** save a navigation exploration, **not** a new canonical state.

## Astrolabe and orientation search

Astrolabe provides orientation based on a word, category, or label. In the October 17 patch, the French UI ranks exact terms and whole-word matches ahead of weaker partial matches. Searching for **`aquin`** can match **Thomas d’Aquin** without accidentally matching the end of **Joaquín**. Results with the same visible title are diversified while **their underlying entity identities remain separate**.

A suggestion is a **navigation candidate**, not proof of semantic equivalence or historical evidence. Results are bounded and depend on visible labels, aliases, and available descriptions. Names of works in other languages are not translated by this patch. See [[Astrolabe and Search|Astrolabe-and-Search]].

## Plans and renderers

After Reader Policy, the engine inspects the **visible** structure, identifies *navigation affordances*, proposes a `NavigationPlan`, and passes a bounded projection to an authorized renderer. Depending on the data, available views may include lists, tables, constellations, timelines, trees, dependency graphs, flows, causal loops, matrices, state diagrams, traceability, multiscale, and spatial views.

A graph, timeline, or evidence view must never turn a candidate relationship into truth, a dependency into causation, or a cited source into scientific validation. The October 17 patch prevents the technical `v9:node_kind` relation from dominating the initial constellation suggestions, **without removing it from the underlying assertions**.

User-facing translations are currently implemented as an **explicit, bounded French dictionary** rather than an automatic multilingual translation engine. See [[Semantic Labels and Localization|Semantic-Labels-and-Localization]].

## Catho example

The local reader can offer **People, Works (Wikidata), Historical Themes, Historical Sources, Historical Assertions, and Open Hypotheses** at the entry point. Technical `V9 state` and artifact objects remain accessible; they should not dominate the initial view when a valid derived graph is present.

Learn more: [[Kristal Catho|Kristal-Catho]], [[Perspectives and Renderers|Perspectives-and-Renderers]], [[Security|Security-and-Privacy]].
