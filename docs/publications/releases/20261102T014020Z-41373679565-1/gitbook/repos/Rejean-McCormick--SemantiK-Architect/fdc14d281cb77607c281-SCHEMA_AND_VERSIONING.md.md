<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/blob/74b07c42811dae0c68549d8554c00bc44a04298d/docs/reference/SCHEMA_AND_VERSIONING.md | commit: 74b07c42811dae0c68549d8554c00bc44a04298d | SHA-256: 2a40d521ccb042e4eafc8ccebe85f9483ae18a2980cb55580a9433daabe28b86 -->

# Schema and Contract Versioning

Status: **normative reference**

## Independent versions

SA maintains separate versions for:

- application/package version;
- public request/result schema version;
- SA↔GF contract version;
- capability profile version;
- runtime manifest schema version;
- lexical/locale artifact identities.

These versions MUST NOT be collapsed into one global number.

## Compatibility

Readers MUST reject incompatible major versions. Unknown optional fields are accepted only where the schema explicitly allows extension; locked objects with `additionalProperties: false` are intentionally strict.

## Canonical hashing

Deterministic identities SHOULD be computed from canonical serialized semantic content plus explicit version/runtime identifiers, excluding operational metadata such as request time, trace ID and latency.
