<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Contract-Evolution-v9 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: cfdfdd837fe0b1dc3403115cd0784e690953871c2a9f9925b6cf7306c43ff6e4 -->

# Contract Evolution — v9

V9 uses additive evolution and compatibility locks.

```text
v6 portable substrate      frozen
v7 semantic identity       frozen
v8 language/query layer    frozen
v9 state architecture      additive
```

## Independent contract versioning

A domain Logical Contract versions independently from the Kristal Standard.

```text
recipes.procedure-graph/3.0
→ recipes.procedure-graph/3.1
```

does not automatically require Kristal v10.

## Change classes

Contracts should distinguish:

- compatible addition;
- presentation-only change;
- rename;
- semantic replacement;
- split;
- merge;
- identity migration;
- commitment-profile migration.

## Identity migration

Changing what defines “the same logical object” is not a normal schema rename. It must be explicit and traceable from old IDs to new IDs.

## Commitment-profile migration

Changing projection fields, exclusions, collection ordering, domain separator or hash algorithm requires a new profile identifier.

## Compatibility lock

A v9 release can pin inherited normative files and TCK vectors by digest. Compatibility means keeping those surfaces unchanged, not merely keeping similar filenames.
