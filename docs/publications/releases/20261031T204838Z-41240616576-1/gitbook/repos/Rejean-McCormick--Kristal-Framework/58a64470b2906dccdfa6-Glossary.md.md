<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Glossary | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: c31f522f4d5e2b5f51409ee3b541b49a12200b8d2fb6c23dbd7224e6c105a690 -->

**v11 identity/dictionary quick terminology:** **KQ** = Kristal namespaced semantic referent ID, **KP** = property ID, **KA** = assertion ID, **KS** = source ID. **Wikidata QID/PID** are external IDs, not internal KQ/KP aliases without a typed, reviewed crosswalk. **Lexical dictionary** = words/aliases by language; **diK coverage** counts direct, fallback, missing and conflicts for KQ and KP separately. See [[Semantic-Identity-v11]], [[Dictionary-Management-v11]] and [[diK-Integration-v11]].

---

# Glossary

## V10 hosted-network terms

### Node Manifest
`kristal_node_manifest` describes an operational node with stable `node_id` and roles; it is not a v9 State Snapshot.

### Collection node
A node hosting one or many independently committed states; a repository is an operational boundary, not semantic identity.

### Host Binding
`kristal_host_binding` links a node to one host and profile, without changing v9 commitments.

### Publication Record
`kristal_publication` binds exact v9 state and verified resource bytes to a hosted publication location, independently of activation.

### Directory
`kristal_directory` advertises mutable node discovery locations. It does not confer authority or exact federation membership.

### GitHub read surface
Derived projection (`kristal.github-read-surface/1.0`) listing exact readable files; it is not canonical state.

### Sync Manifest
`kristal.github-sync-manifest/1.0` records the Manager-owned hosted reader subtree and integrity metadata.

### Collection Index
`kristal.github-collection-index/1.0` is derived reader discovery under `kristals/index.json`, not a semantic directory.

### Sync
Mutable reader-surface transport, distinct from immutable Publication and optional Activation.

See [[Kristal-v10]] and [[Core-Invariants-v10]].

---

## V9 semantic-state terms (preserved)

## Activation
Selection of a published immutable State Snapshot for a mutable operational channel such as `production` or `HEAD`.

## Artifact Descriptor
V9 metadata identifying a Logical Artifact contract/commitment and related representation information.

## Blob
Exact stored bytes.

## Blob Digest
Digest over exact physical bytes. Distinct from a Logical Commitment.

## Build
Computation that produces candidate logical artifacts/materializations. Does not imply publication or activation.

## Build provenance
Declared computational lineage: inputs, transform, parameters, toolchain and policies.

## Canon / canonical state
The authoritative logical content under a declared authority/domain contract. A runtime index is not canon merely because an application uses it.

## Commitment profile
Versioned rules for logical projection, normalization, ordering, domain separation and digest generation.

## Coverage
Metadata describing which part of a logical state/artifact is available in a materialization/runtime.

## Derivation
Machine-readable transformation relationship from exact inputs to outputs.

## Derived artifact
Rebuildable artifact produced from declared source state. It is not automatically semantic authority.

## Epistemic overlay
Epistemic metadata/claims attached to domain-native identities without forcing the native payload into a universal assertion shape.

## Epistemic provenance
Evidence/source/authority lineage relevant to why knowledge is supported or how it should be interpreted.

## Exchange
Portable/verifiable packaging of a State Snapshot and its physical materializations.

## Factorization
Non-destructive sharing of repeated structure/metadata while preserving effective logical reconstruction.

## HEAD
Mutable operational pointer to an immutable state. `HEAD` is not the State Snapshot itself.

## Identity migration
Explicit change in the rules defining semantic identity, including split/merge/remapping.

## Logical Artifact
Domain-native logical unit governed by a named Logical Contract.

## Logical Commitment
Digest over normalized logical content under a named commitment profile.

## Logical Contract
Versioned domain contract defining artifact structure, semantics, normalization and validation rules.

## Materialization
Physical representation of one Logical Artifact.

## Materialization Manifest
Binding from a source Logical Artifact commitment to physical segments/blobs under a materialization profile.

## Materialization Profile
Versioned rules defining how logical content is encoded and reconstructed physically.

## Owned member
Logical Artifact that participates directly in a State Snapshot's owned membership.

## Pinned reference
Reference to an exact immutable external artifact/state commitment.

## Projection
Explicit transformation from one logical contract/view to another. May be partial or lossy and must declare that fact.

## Publish
Creation/admission of an immutable State Snapshot according to release policy.

## Repack
Physical reorganization that preserves logical content: resegmentation, recompression, dictionary rebuild, etc.

## Runtime Pack
Derived optimized representation for lookup/query/computation. It must not silently become canonical authority.

## Segment
Immutable physical storage unit. Not a semantic shard by default.

## Semantic ID
Stable identity answering which logical object is referenced.

## Shard
Semantic/governance/lifecycle partition that may be independently curated/versioned.

## State Snapshot
Immutable composition of owned Logical Artifacts and pinned external references.

---

## Preserved v6/v7/v8 terms

### Applicability
Envelope in which an assertion applies: domain, jurisdiction, time, environment or other context.

### Assertion
Independently addressable statement, commonly subject → predicate → object plus epistemic metadata.

### Actionability
Human/automation policy boundary. Does not itself grant execution authority.

### Authority recognition
Scoped recognition by an authority channel. Distinct from validation and signature authenticity.

### BCP 47 locale
Language tag such as `fr`, `fr-CA` or `sr-Cyrl` used by v8 lexical resolution.

### Completeness
Declared extent to which a query/result satisfied requested semantic/evidence/source scope.

### Continuation
Opaque state used to resume a stable paginated query.

### Coordinates
Domain-specific position/context of an assertion.

### Evidence
Material directly supporting a claim. Distinct from provenance, validation and build lineage.

### KQP
Kristal Query Protocol `kristal-query/1.0` from v8.

### Kristal
A structured knowledge artifact/state. In v6, `kristal_state/6.0` is the central portable artifact; in v9, a broader state may compose multiple domain-native Logical Artifacts.

### Kristall
v7 encyclopedic knowledge space/meta-orchestrator over registries, Mesh/KOS mappings, projections and many Kristals.

### Lexical Kristal
External v8 companion mapping semantic references to language-specific forms.

### Partial result
Useful result that did not cover all requested scope. Not evidence that omitted facts do not exist.

### Query index
Rebuildable read-side structure used to accelerate query. Not canonical truth.

### Record role
Functional role such as authoritative constraint, observed state, organizational rule, reference knowledge, derived state, decision, action or structural record.

### Referent
Stable identity for what v6 assertions are about.

### Semantic fingerprint
V8 versioned digest over a declared semantic projection. It remains distinct from v9 artifact/state Logical Commitments.

### Symbol table
Local compact mapping used by an AI/context bundle. Never a persistent semantic identity.

### Validation
Policy evaluation of an artifact/claim. Distinct from authority recognition and truth.

### Valuation
Typed measurement/state attached to an assertion.

### Value state
Explicit status such as `unknown` or `not_applicable`; not interchangeable with numeric zero/false.
