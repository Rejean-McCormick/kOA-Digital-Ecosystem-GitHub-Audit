<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Perspectives-and-Renderers | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: edf90e4ef3328f807ff0c71ed0e42a938a87012611e0a502e96bbd5a9ddaeae1 -->

# Perspectives, Lenses, Plans, and Renderers

## What does each component do?

- **Perspective:** the kind of object to explore; the choice can be informed by the open corpus.
- **QuerySpec:** describes a selection and its filters.
- **Lens:** defines a reading angle compatible with the selected kind, without changing assertions.
- **Reader Policy:** determines which information is visible.
- **Navigation Affordances:** structural hints about useful paths and representations.
- **NavigationPlan:** recommended views with reasons and limitations.
- **Projection DTO:** bounded, derived data prepared for a renderer.
- **Renderer Registry:** controlled set of available visualizations.

## Representation families

| View | Justified use |
| --- | --- |
| List / table | General browsing, catalogs, filters |
| Constellation / graph | Relationships actually declared among entities |
| Timeline / lineage | Explicit dates, states, or transmissions |
| Tree | Hierarchical organization when present in the data |
| DAG / dependencies | Declared prerequisites or chains of evidence |
| Flow / states | Processes and conditional transitions |
| Causal loops | **Explicitly** represented causality and feedback |
| Matrix | Comparing dimensions or measurements |
| Traceability | Sources, assertions, and provenance |
| Multiscale | Connected layers and memberships |
| Spatial | Location only when coordinates/places are available |

A Kristal may support several views. There is **no requirement to produce a visually spectacular view**. Fallback lists or tables are appropriate when the data does not justify a specialized renderer.

## Readable relationships and technical facets

Konstellation's current French semantic-display patch changes **presentation**, not graph semantics. Known predicates such as `P138` receive readable French labels, unknown property codes remain visibly unresolved, and routine `v9:node_kind` information is de-emphasized in the constellation. Facets with no values are normally hidden unless the user has an active filter. The original relation identifier must remain available to readers inspecting provenance.

These are **current heuristics**, not a guarantee that every rendered edge names a domain entity instead of a metadata property. Consult [[Semantic Labels and Localization|Semantic-Labels-and-Localization]] and [[Astrolabe and Search|Astrolabe-and-Search]].

## Security and performance constraints

Renderers must be selected from the controlled registry. External `navigationHints` cannot execute JavaScript, inject an arbitrary component, or expand permissions. Projections may be truncated; respect `truncated`, `nextCursor`, and resource budgets.

Detailed sources: `docs/03-navigation.md`, `docs/15-adaptive-navigation.md`, `docs/17-renderer-registry.md`, `contracts/navigation-plan.schema.json`, `contracts/navigation-projection.schema.json`.
