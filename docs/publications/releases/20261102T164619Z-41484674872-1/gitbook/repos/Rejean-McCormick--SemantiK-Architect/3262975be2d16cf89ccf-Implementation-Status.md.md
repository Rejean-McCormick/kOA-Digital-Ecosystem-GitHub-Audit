<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Implementation-Status | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: acc4585b9f4791b9d079113fe829810720a3dddfdca0dcf7acb72e6298813ee1 -->

# Implementation Status

## Implemented in SA v1 core

- canonical semantic graph and typed values;
- semantic statements and communication obligations;
- communication context and presentation constraints;
- request validation and stable error envelope;
- deterministic communication planning;
- target-language planning to `LanguagePlan` / `RealizationUnit`;
- extensible planning-support hints;
- lexical preflight and exact binding;
- semantic/obligation coverage validation;
- strict versioned SA↔GF bridge;
- PGF runtime boundary;
- filesystem RuntimeSet catalog;
- artifact hashing and SA-version compatibility;
- explicit activation when multiple releases coexist;
- capability profile enforcement;
- conformance harness and release validation;
- deterministic result assembly;
- SDK, CLI and minimal HTTP adapter;
- health/readiness and output projections.

## External artifacts required for production language output

SA does not bundle an arbitrary grammar and call it production-ready. A language/profile needs a released RuntimeSet containing:

- a real PGF grammar;
- a compatible bridge artifact;
- lexical/locale artifacts as required;
- capability manifest;
- profile artifact;
- passing hashed conformance evidence.

## Product ACLs

The canonical ACL boundary exists. Product-specific adapters are implemented when the owning system's structured semantic contract is explicit.

## Deliberately outside SA

- raw free-text understanding;
- task/workflow state authority;
- truth/provenance authority;
- independent morphology/syntax engines;
- best-effort language fallback;
- article-generation/editorial planning.
