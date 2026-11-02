<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/10-system/trust-boundaries.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 074ad9b699137d6b4b3a610c1ee9fbb9628069c08cac58bf569e0d2fbdfa6a78 -->

# Trust and authority boundaries

Identity, authentication, policy authorization, resource admission, artifact verification, epistemic validation/recognition, release compatibility, privileged host operation and presentation state are distinct.

## Cross-system protocol
Where IK is adopted, the receiver authenticates/authorizes/adopts locally. IK admission is not Kristal validation and does not replace platform admission. IK transports protocol records and artifact references; it is not an authority database or artifact store.

## Operational/epistemic ownership boundary
Operational owners commit mutable domain state locally. An immutable export/snapshot may cross to Da’at for epistemic compilation, but the live record remains owned by its source product. Kristal owns the derived epistemic artifact, not the source operational record. No boundary requires a cross-system distributed commit.

## Materialization boundary
Runtime Pack query structures are consumption materializations. They may optimize reads but cannot silently become writable operational authority or change assertion/validation/recognition state independently of their referenced Kristal source artifact.

## kOA-Linux release boundary
Release Set/channel compatibility is a platform release decision. It does not make an artifact epistemically valid or active.

## Runtime Pack boundary
`kristal_runtime` verifies/adopts the candidate and owns active Runtime Pack state. Required trust, compatibility, channel, downgrade/substitution and other checks fail closed for activation eligibility.

## Privileged host boundary
kOA Node Agent executes only narrow authorized node-local transitions. Successful authorization/resource admission does not by itself mean the active Runtime Pack record changed.

## Koali boundary
Presentation registration, rendering, readiness and Space activation do not grant product authorization, Kristal authority or host privilege.
