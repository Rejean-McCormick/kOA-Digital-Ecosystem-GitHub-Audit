<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/17_ADR_REGISTER.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: a432db3d31c4d1c19ce52f8a408a7491a0fdccadd1ff7d0c7bc61fbab2d01f8d -->

# ADR register

- **ADR-W01** — Orgo Worlds is a standalone sibling repository, not a copy of main Orgo.
- **ADR-W03** — WorldRelease is an immutable configuration/provenance generation, not a copy of operational history.
- **ADR-W05** — Organization identity and World membership remain additive control-plane context.
- **ADR-W07 (2026-09-19 separation cleanup)** — Main Orgo exclusively owns Signal/Workflow/Case/Task/IntegrationOperation/Outbox and provider adapters. Orgo_Worlds must not recreate them.
- **ADR-W08 (2026-09-21 IK placement)** — The Konnaxion↔Orgo Interaction Kernel boundary terminates in main Orgo. Orgo_Worlds may supply World/release routing/provenance metadata only.

ADR-W02/W04/W06 from the pre-separation phase (row-key operational isolation, `/api/v3/w/{key}` operational route rewriting, and worker/outbox release pinning) are superseded for this standalone repository. They may remain useful historical context for the main product integration, but they are not active Orgo_Worlds runtime decisions.
