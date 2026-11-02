<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Glossary | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: c896c8f2c8417fdbc4bc2889d5d36469f607bf86953bb89ff2a383258c222642 -->

# Glossary

**ACL (Anti-Corruption Layer)** — boundary adapter mapping an external domain model into SA canonical contracts.

**Communication** — one bounded SA output; may contain several sentences and presentation blocks.

**CommunicationObligation** — semantic content that must be communicated for the request to succeed.

**CommunicationContext** — audience/language/register/channel information that controls articulation without selecting facts.

**CommunicationPlan** — language-neutral grouping, sequence and discourse plan over obligations.

**CommunicationRequest** — canonical public input aggregate.

**CommunicationResult** — structured output plus coverage and exact runtime identity.

**SemanticGraph** — typed semantic nodes and predicate-role statements supplied to SA.

**SupportingSemanticContext** — metadata needed for correct planning/realization but not itself a required output claim.

**LanguagePlan** — target-language-specific, realizer-neutral plan containing blocks and realization units.

**RealizationUnit** — smallest planned grammatical unit sent across the realizer boundary.

**SA↔GF Contract** — versioned grammatical operation contract between SA planning and GF realization.

**GF (Grammatical Framework)** — grammatical formalism/toolchain used by the primary realizer adapter.

**RGL (Resource Grammar Library)** — GF resource grammar libraries implementing morphology/syntax for languages.

**PGF (Portable Grammar Format)** — compiled GF runtime artifact loaded by SA.

**Lexical preflight** — language-specific lexical knowledge resolved before final construction choice.

**Lexical binding** — exact mapping from `LanguagePlan` lexical slots to immutable runtime lexical references.

**RuntimeSet** — immutable composition of grammar, lexical, locale, bridge, capability and conformance artifacts used by a request.

**Capability profile** — versioned workload promise a language/runtime must pass before production release.

**Conformance evidence** — immutable proof that a specific language/profile/runtime composition passed its required suite.

**Coverage** — mapping proving every communication obligation was discharged in output.

**Faithfulness** — preservation of supplied meaning without invention, omission, role swap, status elevation or hidden reinterpretation.

**Kristal** — ecosystem component that owns structured epistemic state, authority/provenance/certainty and semantic artifacts.

**SenTient** — ecosystem component responsible for semantic ingestion/formalization of raw human material before SA realization.

**Orgo** — workflow/task system that owns operational state and supplies selected communication semantics to SA.

**eThikos** — structured thought/question/argument system whose semantic graphs may be verbalized by SA.

**KeenKonnect / Konnaxion** — exchange/community systems that may use SA for multilingual system communication.
