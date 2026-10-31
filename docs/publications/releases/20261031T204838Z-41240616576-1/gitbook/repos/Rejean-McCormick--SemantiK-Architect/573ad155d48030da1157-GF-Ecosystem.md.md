<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/GF-Ecosystem | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 8823ca94c1d7ecad458c993782e0047506d4e7fa40d8c148e0b41d60df8e218a -->

# GF Ecosystem

SemantiK Architect consumes released grammatical artifacts; it does not replace the GF language-development ecosystem.

## Responsibility map

```text
GF/RGL language repository
        │
        │ language source, morphology, syntax
        ▼
GF Wordbench
        │ build, diagnostics, validation, release workflow
        ▼
immutable grammar artifact / PGF
        │
        ├──────────────→ GF Observatory
        │                 read-only observation / evidence / maturity views
        │
        └──────────────→ SemantiK Architect conformance
                          │
                          ▼
                    RuntimeSet RELEASED
                          │
                          ▼
                    production rendering
```

The **GF RGL AI Compendium** is a development/reference knowledge source for RGL engineering patterns and language-specific reasoning. It is not a production realizer dependency.

## Language repositories

A language repository owns the actual linguistic implementation. For example, an Albanian RGL repository can contain morphology, paradigms, syntax, constructions, dictionaries and tests.

If a required Albanian construction fails in SA conformance, the fix belongs in the Albanian/GF development source (or its admitted bridge/lexical artifact), followed by rebuild and reconformance. SA core does not patch Albanian at runtime.

## GF Wordbench

Wordbench belongs on the development side of the boundary. It can support:

- language source discovery;
- GF compilation/PGF build;
- diagnostics;
- test/golden workflows;
- release artifact production.

SA consumes the resulting immutable artifacts; it does not embed the language-development workbench into its runtime path.

## GF Observatory

Observatory is an evidence/observation system, not the grammar authority used by a render request.

Its views can help answer questions such as readiness, maturity, diagnostics and evidence history. The production authority inside SA remains the exact immutable RuntimeSet and its pinned conformance evidence.

## GF RGL AI Compendium

The Compendium captures engineering knowledge such as reusable morphology/morphosyntax patterns, diagnostics and language-family evidence.

It can guide human/AI language development, but it does not replace:

- the source language implementation;
- GF compilation;
- SA profile conformance;
- immutable release evidence.

## SA boundary

SA expects a finished, validated grammatical capability:

```text
PGF + bridge + lexicon + profile + evidence
```

Once those artifacts are released, the runtime does not need Wordbench, Observatory or the Compendium to generate text.

See [[Add a Language|Add-a-Language]], [[RuntimeSets]], and [[Language Profiles & Conformance|Language-Profiles-and-Conformance]].
