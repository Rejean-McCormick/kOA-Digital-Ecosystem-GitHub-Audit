<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/konstellation/index.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 6d651db8bb6552810a8d528423f4030cddf74cb72ee85e1f5d22460fc9a32f48 -->

# Konstellation — versioned integration

Konstellation v0.4 is documented as a **reading and exploration application** in this contract view. Kristal retains authority over knowledge, provenance and epistemic metadata. SemantiK Architect (SA) fulfills an explicit communication request; the runtime orchestrator controls qualification and runtime activation. This page describes the recorded integration candidate, not a guarantee that every listed product is currently installed or integrated.

| Producer / owner | Contract or artifact | Responsibility |
|---|---|---|
| Kristal | Runtime Pack derived from Kristal v6 artifacts with `konstellation:reader-json-v1`, or Parquet with an explicit mapping | Identity, sources, policy and integrity; read projections remain derived |
| Konstellation | QuerySpec/ExplorationState 0.2, CommunicationRequest 1.0 | Selection, query and communication scope |
| SemantiK Architect | `konstellation-explorer-1`, bridge 1.0, CommunicationResult 1.0 | Faithful structured realization, French labels and coverage |
| Runtime Orchestrator | pipeline.lock 1.0, conformance CLI, activation 1.0 | Verification, qualification, promotion and activation |
| EncyKlopedia | Explicit handoff to the Kristal producer | Source preparation, **not** epistemic validation |

The realization feature remains disabled until SA publishes the requested runtime/profile/language combination. The supplied profile is a **candidate** pending GF compilation and conformance against the actual PGF. A candidate conformance command does not publish content; it is reserved for the offline pipeline.

Konstellation's tests cover criteria, pages, entities and negative filters. Metadata is not reduced to a yes/no validation flag. Incompatible capabilities must be rejected rather than silently converted to an empty result or fallback text.

Local reading does not require a new Interaction Kernel bus. HTTP connections are explicitly operator-configured; service URIs and credentials are not part of end-user queries.

## Publisher — local preparation only

[`Konstellation-Publisher`](publisher.md) is a separate tool from Konstellation Reader. Its public GitHub repository was confirmed as an identifier as of 2026-10-27, but the local checkout remote and publication of the reviewed code were not verified. Candidate `0.2.0-alpha.1` prepares and preflights packages **locally**; it blocks remote deployment pending independent permission, rollout and rollback qualification. This page grants no publication authority.

## Later C0 / v10 coordination

The v6 reader-profile mapping above is a preserved **versioned integration view**. The later [v10 harmonization](../kristal-v10-alignment/README.md) separately describes Konstellation as a navigator of Kristal fleets and concepts, while Manager owns the real instance registry and publication/read-surface synchronization. Neither this view nor the v10 proposal verifies a live fleet integration.
