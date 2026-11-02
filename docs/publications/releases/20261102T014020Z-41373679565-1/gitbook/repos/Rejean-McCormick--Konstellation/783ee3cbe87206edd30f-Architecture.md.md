<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Architecture | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 59f936a8578fd1030aff78c39d337064825ad3a52c09aee8d31dc0280fe332e8 -->

# Konstellation Architecture

## Functional boundaries

```text
  Local / hosted Kristal (external sources and contracts)
          |
          v
  Selector / Adapter / Reader Policy
          |
          v
  Read normalization into a consumable pack
          |
          v
  Noncanonical semantic-display labels (known French mappings)
          |
          v
  Query and facet engine
          |
          v
  Visible-structure profiler → NavigationPlan
          |
          v
  Projection DTO → Renderer Registry
          |
          v
  Astro/Svelte shell → Explorer, Astrolabe, My Kristals
```

A reader can expose **relationships and facets** without gaining authority over canonical files. A navigation plan expresses *how to view* content, not *what is true*.

## Repository layout

| Location | Responsibility |
| --- | --- |
| `src/pages/index.astro` | Astro page |
| `src/components/Explorer.svelte` | Navigation, Kristal selection, main interface |
| `src/components/MyKristals.svelte` | Listing and opening accessible entries |
| `src/components/Astrolabe.svelte` | Orientation search |
| `server/index.mjs` | Local server, endpoints, filtering, reading runtime |
| `server/integrations/` | Readers, Manager, Discovery, external integrations |
| `server/navigation/` | Profiling, planning, projection, registry |
| `server/engine.mjs` | Queries, facets, entities, visible links |
| `server/pack.mjs` | Pack validation against schemas |
| `src/lib/semantic-display.mjs` | Presentation-only French labels, status text, and Astrolabe ranking helpers |
| `contracts/` | JSON Schemas |
| `config/` | Local reader configurations |
| `tests/` | Unit, API, security, E2E tests |
| `docs/` | Project standards, ADRs, guides, validation reports |

## Invariants

1. **Never mutate a Kristal's canon** through a read operation.
2. Apply **Reader Policy before deriving** results, counts, explanations, and visualizations.
3. **Never infer authority** from a name, Arketype classification, or Manager status.
4. **Bounded checks** on inputs, file paths, graphs, results, and projections.
5. **Separate** discovery, reading, qualification, authorization, publication, and activation.
6. Use **exact revisions and commitments** when making provenance or integrity claims.
7. **Human-readable labels are not new facts:** never replace raw identifiers, epistemic status, or provenance with a translated display string.

Source documents: `docs/00-decisions.md`, `docs/01-architecture.md`, `docs/04-knowledge-semantics.md`, `docs/15-adaptive-navigation.md`, `docs/19-security.md`, and `docs/adr/`.

See [[Kristal Readers|Kristal-Readers]] and [[API|API]].
