<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion/wiki/Glossary | commit: 62c3bb451bacb4cfbbeb68181c1edfc7ba47a8f9 | SHA-256: 266fd861e546aa6ad81d7021d7355a03e5adbe438dd09882fe29facf16ed2968 -->

# Konnaxion Glossary

## Konnaxion

An **ecosystem system** in the kOA Digital Ecosystem and a **platform** in its own scope.

When hosted by kOA-Linux, it can be described as an **integrated subsystem from the kOA-Linux scope**. That host-relative term does not transfer Konnaxion domain authority.

## Module

`module` is a convenient product/UI word, not a precise architecture category.

When the category matters, use:

```text
module
→ domain
→ application
→ service
→ component
→ gateway
→ interface surface
```

Examples:

- Konnaxion — ecosystem system/platform.
- EkoH — Konnaxion domain/service boundary.
- Smart Vote — Konnaxion reading/aggregation boundary.
- K-Port — EkoH evidence application/gateway, not a peer of Konnaxion.
- kOA Spaces — subsystem of kOA-Linux, not a Konnaxion owner.

## Source fact

Authoritative state owned by the domain that captured it.

Examples:

- an `EthikosStance`;
- a formal consultation ballot.

## Baseline

A direct declared aggregation/view of source facts without a contextual Smart Vote lens silently replacing it.

## Reading

A derived interpretation of source facts under an explicit lens.

```text
Reading = f(SourceFacts, LensDeclaration, SnapshotContext?)
```

## Lens

A declared method and contextual policy used to compute a reading. A lens is not truth and does not own source facts.

## EkoH snapshot

The identifiable EkoH contextual inputs used by a reading. A durable/replayable published reading requires those inputs to be recoverable, not merely hashed.

## Korum

Logical structured-deliberation sub-domain inside ethiKos. It is implemented primarily in `konnaxion.ethikos`, not as a separate Django app.

## Konsultations

Logical consultation/intake/formal-decision source boundary. It is not identical to an Orgo Task or to a Smart Vote reading.

## EkoH

Konnaxion domain for expertise taxonomy/scores, ethics/reliability context, privacy and rating access.

## ISCED-F 2013 / CITE-F 2013

UNESCO classification of fields of education and training used by EkoH as its expertise-domain backbone. The full classification contains 11 broad / 29 narrow / about 80 detailed fields; EkoH uses a default **10 / 26 / 77 = 113-category** domain-bearing profile. A code classifies a domain; it is not an expertise score or voting weight. See [[EkoH Expertise Taxonomy|EkoH-Expertise-Taxonomy]].

## Smart Vote

Konnaxion domain for declared derived readings and related aggregation/lens semantics.

## Kollective Intelligence

A product/navigation umbrella and compatibility area. It is **not the canonical backend owner** of EkoH or Smart Vote state.

## Gateway

A controlled boundary that validates, normalizes, qualifies or routes data. A gateway does not become owner of the destination domain merely by controlling passage.
