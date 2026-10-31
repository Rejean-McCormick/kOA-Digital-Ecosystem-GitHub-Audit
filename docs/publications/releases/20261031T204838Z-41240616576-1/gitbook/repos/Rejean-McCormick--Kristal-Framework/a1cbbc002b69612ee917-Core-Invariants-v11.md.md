<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Core-Invariants-v11 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 1dfd811f9a18e91cba2da1d9ca9f8d2d95be0c5a5af433b200feab05c2fdb522 -->

# Core invariants — v11

**The following restrictions apply to an explicitly declared new v11 semantic graph; they do not invalidate historical artifacts under older contracts.**

1. **Opaque identity** — every canonical KQ/KP/KA/KS value is scoped to `(namespace_id, id)` and must match its semantic role. The `namespace_id` is not optional in comparisons or crosswalk keys.
2. **Lexical independence** — labels, translated predicates, slugs and definitions belong in dictionaries, never in canonical graph identity fields.
3. **External neutrality** — Wikidata `Q`/`P` remains external; no internal minting of Wikidata IDs. Only reviewed and evidenced `accepted + exactMatch` may bridge exact identity.
4. **Typed literal preservation** — human quotations and string facts remain *literal values*; they must not be mistaken for KQ/KP IDs or modified by global string substitution.
5. **Layer integrity** — dictionary catalog paths, priorities, locales and digests are explicit. Imported snapshots are immutable; curated terms do not overwrite them.
6. **Truthful coverage** — per-language KQ/KP coverage distinguishes direct labels, fallback, missing and conflicts. A fallback is **not** a native translation.
7. **Safe migration** — older identity strings are migration candidates, never automatically equivalent. Plans cite source paths, hash, decisions and evidence; a new revision is required.
8. **Historical continuity** — v6–v10 schemas, commitments and original state snapshots remain valid according to their versions; a stricter v11 profile is opted into by new producers.
9. **Authority boundary** — a passing validator confirms shape and implemented invariants, not metaphysical truth, source reliability or entitlement to publish.

**Related:** [[Kristal-v11]] · [[Conformance-v11]] · [[Legacy-Migration-v11]] · [[Security-and-Confidentiality-v10]].
