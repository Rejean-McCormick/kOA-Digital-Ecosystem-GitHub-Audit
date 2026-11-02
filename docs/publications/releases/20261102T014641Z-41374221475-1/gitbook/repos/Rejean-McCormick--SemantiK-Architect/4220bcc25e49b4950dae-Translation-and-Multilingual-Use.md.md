<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Translation-and-Multilingual-Use | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 4bfe6ed95fe85baf1d5eb7bf86f52945364b0d8f4d8bf34b7a06192595cdbdc4 -->

# Translation & Multilingual Use

SemantiK Architect is not a canonical string-to-string machine translation engine.

Its multilingual strength comes from separating meaning from language.

## Canonical translation flow

```text
source human text
       │
       ▼
semantic ingestion / formalization
       │
       ▼
structured meaning
       │
       ├──────────────┐
       ▼              ▼
 target language A   target language B
       │              │
       ▼              ▼
      SA             SA
       │              │
       ▼              ▼
      GF             GF
       │              │
       ▼              ▼
   communication A  communication B
```

In the kOA ecosystem, SenTient/Kristal can perform the ingestion/formalization step. SA then realizes the same structured semantics in any released target language/profile.

## Why this matters

A semantic pivot makes it possible to:

- preserve entity identity;
- preserve polarity/modality;
- inspect exactly what was communicated;
- produce different natural structures in different languages;
- avoid an English pivot;
- validate semantic coverage across languages.

## What SA does not do

SA does not take arbitrary source prose and infer the intended semantic graph by itself. If structured meaning is missing, semantic ingestion belongs upstream.
