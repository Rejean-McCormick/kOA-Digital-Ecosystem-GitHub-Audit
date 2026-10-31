<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/API-and-Contracts | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: cccf01810fd5658830e09342512643903bfa4f40fada90e4357477a4d976c5b8 -->

# Contracts and Illustrative API — Not Hosted

The source repository includes `contracts/openapi.yaml`, versioned JSON Schemas and the event catalog. These describe **proposed** operations; the `.invalid` example server address is intentionally non-functional. **No network service is implemented** by KOMPOSE.

## Proposed session API (not operational Tandem routes)

| Method | Route from OpenAPI | Conceptual purpose |
|---|---|---|
| POST | `/sessions/join` | Join with externally authenticated school identity |
| GET | `/sessions/{sessionId}/snapshot` | Filtered session view |
| GET | `/sessions/{sessionId}/roles` | Role view |
| POST | `/sessions/{sessionId}/role-choices` | Eligible supervised choice |
| POST | `/sessions/{sessionId}/kristals/{kristalId}/access-requests` | Request access through future authorization |
| POST | `/teacher/sessions/{sessionId}/commands` | Teacher-led simulated session controls in the design |
| POST | `/teacher/sessions/{sessionId}/phases/advance` | Shared phase transition in the design |
| POST | `/teacher/sessions/{sessionId}/kristals/{kristalId}/guardians/transfer` | Proposed supervised transfer |

These are **not Orgo Case/Task/Signal endpoints**, nor do they grant KOMPOSE authority to advance operational Tandem workflows. Future integrations must use the canonical Orgo contracts, explicit permissions and release checks.

## Existing local data contracts

- `contracts/schemas/` contains capsule, mission, phase, role, Kristal and other model definitions, plus `kontexte-preview` and `orgo-mock-replay` definitions.
- `src/kompose/tandem_handoff.py` enforces an exact allowed key set for the **synthetic** Ekole P1 teacher preview; this is not a deployed API.
- `contracts/events.md` describes reference event names. Their existence does **not** imply a production broker or durable outbox.
- Versioned knowledge stays under editorial control; event and user-facing projections must not expose private data.

## Validation is not authorization

- B6 receipts tagged `orgo_mock_fixture` are fictional data; `human_reviewed` does not authenticate a teacher.
- A valid Ekole preview always yields `runtime_admitted: false`, `permissions_verified: false`, and `world_release_verified: false`.
- Tenant/World/WorldRelease UUID parsing checks syntax, not ownership, signature or release existence.

**Primary references:** `contracts/openapi.yaml`, `contracts/events.md`, `docs/adr/0008-tandem-orgo-operational-authority.md`, `docs/TANDEM_P1_ORGO_EKOLE_ALIGNMENT.md`, and source tests.

[[Home|← Home]] · [[Ekole-P1-Preview|P1 strict verifier]] · [[Architecture|Architecture →]]
