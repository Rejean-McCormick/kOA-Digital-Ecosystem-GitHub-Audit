<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Missions-and-Events | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 4e933a8e4beafec4b8c8411866c21c43df3ab738e26830302f25d559dfa24a40 -->

# Missions, Phases, and Events — Local Simulation

KOMPOSE models session states and mission dependencies using **pure local Python functions**. The project originally described this as “orchestration”; in Tandem, **Orgo alone performs operational Task/Case/Signal transitions, dispatch, permission checks, and reconciliation** (ADR 0008).

## Simulated session lifecycle

`brouillon → pret → inscriptions → diagnostic → attribution → validation → aventure → terminee`; the reference also models `suspendue` and `annulee`. These identifiers belong to `src/kompose/lifecycle.py`, **not an Orgo state contract**. Inputs such as `diagnostics_reviewed` or `content_ready` are synthetic assertions in tests, not proof of genuine school review.

## Phases, dependencies, and guardianship

`src/kompose/coordination.py` can determine ready missions from a validated, acyclic `depends_on` graph, advance example phases, and suggest a guardian transfer. A transfer is a **proposal** requiring an authorized teacher decision in any future deployment; it does not grant real document access.

## Prompts and simulated events

`src/kompose/events.py` selects prewritten prompts for a recipient and event; it does not publish messages or implement private delivery. Demo data never justify disclosure of confidential teacher/student attributes.

## B6 mock Orgo receipts

`src/kompose/mission_replay.py` checks ordering, duplicate IDs, pause/resume conditions, role matching, and fictitious review flags in **mock receipts only**. It does not call Orgo or turn a fixture into real authorization. See [[Kontexte-B6-Preview]].

## Real orchestration belongs elsewhere

A real solution needs Orgo-authenticated tenant/World scope, transactional state and outbox, idempotent delivery, version consistency, verified review and audience access, recovery, and audit. None are delivered by the local KOMPOSE engine. Do not use the session simulator as a parallel scheduler.

[[Home|← Home]] · [[Tandem-Orgo-Boundary|Orgo authority]] · [[API-and-Contracts|Contracts →]]
