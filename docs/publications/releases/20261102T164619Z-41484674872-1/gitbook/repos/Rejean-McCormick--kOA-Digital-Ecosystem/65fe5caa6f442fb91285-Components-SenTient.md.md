<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/1-Overview/Components-SenTient.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: ba789170881c6fb6b15c92809ade4fd7a9f6bbaeca15c2bf9cbda7084b6603ee -->

# SenTient

SenTient is an optional **extraction/resolution capability**, not the universal proposal boundary of the ecosystem.

Depending on the Profile it may consume source material, Claim-IR, Kristal State, Exchange fragments or dataset records and may produce Resolved Claim-IR, Kristal State updates, resolution bundles or candidate mappings.

## Constraints

SenTient:

- must preserve provenance and unvaluation;
- must not silently upgrade valuation, validation or recognition;
- must not assign authority recognition;
- must not mutate a Reference Exchange by side effect;
- is optional when a source already emits a supported Kristal-native structured input.

Claim-IR / Resolved Claim-IR remain valid compatibility and extractor profiles under Kristal v6, but kOA documentation must not present them as mandatory for every knowledge flow.
