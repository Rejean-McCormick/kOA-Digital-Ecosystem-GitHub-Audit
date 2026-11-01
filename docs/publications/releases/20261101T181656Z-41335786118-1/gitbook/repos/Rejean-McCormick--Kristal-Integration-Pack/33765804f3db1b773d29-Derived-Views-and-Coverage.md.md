<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Derived-Views-and-Coverage | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 44187be8abe64b32a0e2165f9603dfca7dd1ab5264452ad8b89a5d3b4e22f0b3 -->

# Derived Views and Lexical Coverage

## Read-view envelope

`view` produces `profile: kristal.integration.read-view/v11.0-draft.1`, with `derived_only: true`. The output contains:

- `source`: namespace and graph IDs plus SHA-256 of graph, registry, crosswalk and catalog; the Framework version producing this output is draft.4.
- `requested_locale` and `coverage_counts`.
- `presentation`: individual semantic references (`semantic_id`, `kind`, `lexical`) for the graph's KQ/KP, with only **approved `exactMatch`** external references when available.
- `assertions`: the original graph's assertions copied into the derived output, retaining canonical identity endpoints and typed values.

`presentation[].lexical.status` is one of `direct`, `fallback`, or `missing`. Direct means the requested locale supplies the label; fallback means a declared fallback locale did; missing means no eligible term was resolved. These categories must not be combined as if they were all verified native translations.

## Lexical precedence

The reader uses declared layer priorities and language fallbacks from the Framework catalog. Equal-priority conflicting terms are rejected rather than choosing one arbitrarily. The full Framework dictionary audit runs before producing a view.

The optional Node consumer `overlay/server/integrations/kristal-v11-read-view.mjs` applies defensive **structural** checks to the derived envelope; it does not replay Framework validation or check underlying canonical inputs.

## Important limits

- A localized word is **never** a new semantic ID.
- A read view is a presentation artifact, not the authority for a new KQ or KP.
- Coverage describes dictionary presence, not scientific correctness, social authority, policy access, or translation quality.
- The read-only Node consumer is **not** automatically installed as an HTTP route.

See [[Framework-v11-Reader]], [[Architecture-and-Ownership]], and [[Security-and-Trust-Boundaries]].
