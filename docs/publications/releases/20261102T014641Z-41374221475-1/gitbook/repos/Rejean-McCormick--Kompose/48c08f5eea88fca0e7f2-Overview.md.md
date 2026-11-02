<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Overview | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 67f26c2be4f100e19c01d6c912f4564bb1356cad331d5a5381949ab8057568a8 -->

# Overview — Purpose and Limits

KOMPOSE offers **tools and design rules for collaborative educational capsules**: scenarios, roles, a fictional diagnostic, supervised casting proposals, mission dependencies, and structured Kristal knowledge. Its repository is an executable local reference; it is not a running school service.

## The two key product boundaries

1. **KOMPOSE is not KOR.** KOR may eventually render a narrative interface. That independence is documented by ADR 0006.
2. **KOMPOSE is not Orgo.** Orgo alone owns real Tandem Case/Task/Signal workflows, dispatch, operational transitions, authorization, and reconciliation. This is the adopted boundary of ADR 0008. Local `lifecycle` and `coordination` are simulations.

## Nine modeled responsibilities

Entry Door, diagnostic design, casting proposals, local coordination models, Kristals, cooperative interactions, adaptation, teacher supervision, and closure. These are functional areas, **not nine deployed services**. See [[Modules]].

## Actors and authority

| Actor | Responsibility or design intent |
|---|---|
| Teacher | Approves educational choices in an actually authorized future workflow; examples only simulate this |
| Student | Joins and participates only through future school-authenticated services |
| Content/editorial reviewer | Approves sources, rights, perspectives, and document versions |
| Kontexte | Owns mission/role/step source definitions |
| Orgo | Owns operational Case/Task/Signal execution and permissions |
| Ekole | Provides the authorized teacher/learning projection |
| KOR / other UI | May display permitted views; not required by the KOMPOSE package |

## What the present code does not provide

No school identity service, authenticated teacher console, server, transactional persistence, real operational workflow client, verified WorldRelease, globally optimized roles, compliant educational content, or deployable hosting. Consult [[Project-Status]] and [[Tandem-Orgo-Boundary]] before interpreting older design descriptions.

[[Home|← Home]] · [[Architecture|Architecture →]]
