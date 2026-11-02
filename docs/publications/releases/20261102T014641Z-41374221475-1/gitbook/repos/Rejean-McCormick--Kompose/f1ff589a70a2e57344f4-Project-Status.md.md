<!-- Frozen source: https://github.com/Rejean-McCormick/Kompose/wiki/Project-Status | commit: ec94ee500739b0078a14ee9cf67d34d46d2087e4 | SHA-256: 4f867b7b94fc8318af72fc2c856bdf58c735f2fd3bb11439e04efad6a16d5102 -->

# Project Status — Source Snapshot Review (2026-10-27)

**Package version: `0.2.0`.** This is a documentation review of the supplied source snapshot, **not** a newly published release or confirmation that external services are deployed.

| Capability | Confirmed in source | NOT established |
|---|---|---|
| OpenAPI / JSON Schema contracts | Local specifications in `contracts/` | No hosted API or verified compatibility of external services |
| Rivers example, deterministic reader and prompt selection | Local Python and fictional fixtures | No approved historical corpus or real Kristal permissions |
| Entry and session lifecycle | Pure local rules, pause/resume and tests | No operational Tandem Case/Task transitions, IAM or transactional storage |
| Mission dependencies and phases | Local graph/model checks | No Orgo dispatch or durable event outbox |
| Kontexte B6 bakery example | **3 roles**, **3 human-review steps**, **2 fragment references**; safe preview and fictional receipt replay | No live Case/Task, learner assignment, real fragment release or curriculum approval |
| Ekole Tandem P1 | Strict local `ekole.tandem-teacher-preview/1.0` file verifier; **11 synthetic tasks** in example | No teacher authentication, permission checks, verified release, or runtime admission |
| KOR integration | Optional sample adapter manifest | No live connection |
| School UI, SSO, allocation optimizer | Design only | Not implemented |

### Preview verdict is deliberately limited

For the accepted Ekole fixture, `verify-ekole-preview` returns `runtime_admitted: false`, `permissions_verified: false`, and `world_release_verified: false`. These flags **do not change to true** as a result of local verification.

### Tests

The supplied source tests cover reference rules, B6 mock replay, P1 JSON validation, security rejections and optional wiki navigation. Wiki tests are **skipped** if the sibling wiki checkout is missing; a skipped test is not a passing wiki review. See [[Testing-and-Validation]].

### Work still required before school use

Live authoritative Orgo integration, real tenant/World and permission checks, school SSO, secure data storage, verified educational material, global assignment solver, adaptive assessment validation, accessible teacher and student interfaces, audited delivery, and institutional approval.

[[Home|← Home]] · [[Tandem-Orgo-Boundary|Who owns execution?]] · [[Roadmap|Roadmap →]]
