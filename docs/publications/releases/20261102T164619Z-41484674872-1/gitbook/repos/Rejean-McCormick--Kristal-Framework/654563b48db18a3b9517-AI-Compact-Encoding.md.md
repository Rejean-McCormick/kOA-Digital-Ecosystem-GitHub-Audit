<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/AI-Compact-Encoding | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: de22d6d2585adb5a96a5f8519a185b6fdff01ffa996dc9f97b23188df8f04102 -->

# AI Compact Encoding

**Profile:** `kristal-ai-compact/1.0`

Expanded JSON is interoperable but can waste AI context by repeating long IDs and field names. v8 therefore defines an optional compact projection for AI transport.

## Symbol table

A compact bundle may assign local symbols:

```text
0 → KQ847291
1 → KP31
2 → KS9021
```

Semantic atoms can then reference `0`, `1`, `2`. These local symbols exist only inside the bundle and never become persistent semantic identities.

## Determinism

Deterministic compact output should assign symbols by first canonical occurrence after stable atom ordering. Enough metadata must remain to expand losslessly to the source semantic IDs.

## No semantic compression

Compact encoding may remove syntactic repetition. It must not:

- merge distinct assertions;
- erase provenance;
- turn uncertainty into certainty;
- replace unresolved identities with guessed labels.

Processors that do not support compact encoding can request `expanded_json`.
