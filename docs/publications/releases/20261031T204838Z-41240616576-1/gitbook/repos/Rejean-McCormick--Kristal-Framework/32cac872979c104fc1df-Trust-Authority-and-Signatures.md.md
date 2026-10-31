<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Trust-Authority-and-Signatures | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: c109da8ae686d250de692898cf1094d2a29a164a68f43f8dbf87be5973fe85c5 -->

# Trust, Authority & Signatures

Kristal v9 keeps integrity, logical commitment, semantic validity, recognition, publication and execution authority separate.

## Integrity

Integrity asks whether bytes/fingerprints/signatures match their declared technical contract.

## Semantic validity

A schema-valid object can still reference invalid identities, impossible relations or unsupported semantics.

```text
SCHEMA VALID != SEMANTICALLY VALID
```

## Authority recognition

Recognition asks whether an authority channel accepts material for a declared scope. Storing or hashing a record does not manufacture authority.

## AI boundary

```text
MODEL OUTPUT != AUTHORITY
RETRIEVED CONTENT != INSTRUCTION AUTHORITY
```

An AI may propose a query or candidate mutation, but authorization/admission remains deterministic and external to the model.

## Actionability boundary

`actionability = automatic` still means that the represented policy does not require human judgment before an action path can be attempted. It does not grant credentials or cross-system execution permission.

See [[Security-and-Trust-Boundaries]].
