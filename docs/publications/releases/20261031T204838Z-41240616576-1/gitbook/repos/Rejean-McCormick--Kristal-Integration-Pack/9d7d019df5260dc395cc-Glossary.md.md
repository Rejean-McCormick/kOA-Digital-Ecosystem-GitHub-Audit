<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Glossary | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 09a8e55c779cc4c82b80d74b74f9fbfb9423be1ec3369a3ca8b4d236f571cdff -->

# Glossary

| Term | Meaning in this Integration Pack |
| --- | --- |
| **Canonical semantic graph** | Framework v11 graph with stable KQ/KP/KA/KS identity references; not edited by the Pack |
| **KQ / KP** | Internal Kristal entity / property identity identifiers, distinguished from external Q/P |
| **KA / KS** | Internal Kristal assertion / source identifiers |
| **Wikidata Q/P** | External item / property IDs, usable through reviewed crosswalk relationships |
| **`accepted + exactMatch`** | An approved semantic crosswalk relationship; not inferred from matching terms |
| **Dictionary catalog** | Versioned manifest of lexical layers, language fallbacks and hashes |
| **`direct` / `fallback` / `missing`** | Distinct lexical resolution and coverage outcomes |
| **Read view** | Non-canonical derived presentation envelope generated from validated inputs |
| **diK receipt** | `dik-job.json` binding a selected alpha.7 import catalog, source pins and hash-based job key |
| **Preflight** | Reader-side compatibility check; neither authorization nor registration |
| **Authoring Kit** | Separate software responsible for authoring, catalog revision registration/selection and recovery |
| **Context Pack** | Kompiler query-derived source records and execution metadata |
| **v7 Surface → v6 projection** | Limited historical derivation available only when a compatible Surface exists |
| **C1 / C2 / C3** | Independent evidence, authorization and collection-structure/release-related gates, not supplied by the Pack |
| **Reader Policy** | Principal-specific access control to be enforced at the owning Konstellation/Kompiler boundary |
| **Framework pin** | Exact version plus SHA-256 list of reviewed schema/code bytes |

See [[Architecture-and-Ownership]] and [[Security-and-Trust-Boundaries]].
