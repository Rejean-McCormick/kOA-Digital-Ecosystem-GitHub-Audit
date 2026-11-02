<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Developing-a-Reader | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 1f22608899abca7910d0c1b5a90d109ad6f397660f84d310daede661194192d8 -->

# Developing or Extending a Kristal Reader

## When is a new reader needed?

If a workspace contains a v9 state but no known semantic representation, Konstellation can expose its technical topology. A **specialized reader** is useful when a specific logical type needs lossless interpretation (multiplex graphs, epistemic corpora, procedures, ASTs, and so on). Avoid a branch such as `if (corpus === "Catho")` for capabilities that should be generic.

## Recommended approach

1. Study the **Framework contracts** and a real example of that artifact type.
2. Define a **versioned, noncanonical reader contract**, with bounds, identities, provenance, and uncertainty states.
3. Validate paths, bytes, file sizes, hashes, and resource limits at read time.
4. Adapt data to the Konstellation pack format and validate against `contracts/` **without weakening schemas**.
5. Expose readable domain kinds plus advisory `preferredKind` and `featuredKinds`; retain access to technical views.
6. Preserve relationships and statuses without turning candidate claims into established facts. For human-readable UI output, prefer **explicitly registered localized labels**; preserve raw identifiers and show an honest unresolved label when none is available.
7. Add fixtures, access-control tests, regression tests, Kristal-switching tests, and frontend checks.
8. Document what was **actually tested** and what is not yet qualified.

## Real-world case: `domain <= 10`

Catho's graph had 13 node families. Schema `relation-registry/0.2` allows a maximum of **10 domain types per relation definition**. The chosen fix **partitions the definitions** rather than deleting assertions or silently broadening the standard. See `docs/36-correctif-registre-relations-catho.md`.

## Important files

- `server/integrations/kristal-local-v10.mjs`
- `server/integrations/local-catalog.mjs`
- `server/integrations/kristal.mjs`
- `src/lib/semantic-display.mjs`
- `tests/semantic-display.test.mjs`
- `server/pack.mjs`
- `contracts/relation-registry.schema.json`
- `tests/neutral-local-catalog.test.mjs` and local reader tests
- `docs/23-extension-guide.md`, `docs/27-behavior-by-kristal.md`

## Do not exceed the reader's mandate

A reader does not issue C1 qualification, make C2 decisions, invent State Commitments, or publish anything. A projection is **always derived** and must preserve epistemic status conservatively. Replacing `P138` by a French display label is **not** a conversion of the underlying Wikidata statement or evidence. Do not synthesize natural-language truth statements from unknown predicates.
