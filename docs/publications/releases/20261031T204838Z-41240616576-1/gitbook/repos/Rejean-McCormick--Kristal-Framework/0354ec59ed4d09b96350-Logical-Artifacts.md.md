<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Logical-Artifacts | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: c701fe4e916ca92982d04fd198d2048c9c7677f0df0efb574484247c7423b973 -->

# Logical Artifacts

A **Logical Artifact** is the fundamental polymorphic boundary in Kristal v9.

It associates a stable logical identity and contract with a domain-native payload without forcing the payload into a universal structure.

Conceptually:

```json
{
  "artifact_id": "urn:recipe:variant:carbonara:42",
  "logical_contract": {
    "id": "recipes.procedure-graph",
    "version": "3.0"
  },
  "payload": {},
  "logical_commitment": {
    "profile": "kristal.logical/jcs-sha256-v1",
    "digest": "sha256:..."
  }
}
```

## Native shapes

A Logical Artifact may naturally be:

- a relation;
- a graph or cyclic graph;
- a DAG;
- an AST;
- a hierarchy;
- a matrix;
- an event ledger;
- a document/research corpus;
- a domain-specific composite object.

The v9 core does **not** define universal fields such as `nodes`, `edges`, `rows`, `events` or `assertions`.

## Logical contract responsibility

The named `logical_contract` defines:

- schema/shape;
- validation rules;
- internal stable identities;
- collection semantics;
- logical normalization;
- projection behavior;
- allowed commitment profiles.

## Assertions remain valid

V6 assertions are not deprecated. They remain the right logical unit when independently addressable claims are the natural model. V9 only removes the assumption that every domain-native canon must be an expanded assertion list.

## Epistemic overlay

A domain-native artifact may receive provenance, valuation or applicability through an explicit epistemic overlay instead of embedding v6-shaped envelopes at every internal node.

```text
DOMAIN ARTIFACT + EPISTEMIC OVERLAY
```

This preserves both native structure and Kristal's epistemic distinctions.
