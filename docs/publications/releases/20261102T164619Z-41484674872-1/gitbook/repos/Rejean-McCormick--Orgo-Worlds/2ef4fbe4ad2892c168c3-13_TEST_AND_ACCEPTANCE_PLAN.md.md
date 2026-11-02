<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/Technical-Reference/Worlds/13_TEST_AND_ACCEPTANCE_PLAN.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: d6f7bcd006a399a0d1c50dfde60efee9fae92b7aea4aa08e293fc8fb7c2e30d9 -->

# Test and acceptance plan

Post-separation acceptance for `Orgo_Worlds` is intentionally narrower than main Orgo acceptance.

1. `npm run check:worlds` passes.
2. `npm run validate` passes and contains no IK/main-product test dependency.
3. The standalone API starts and reads/writes `runtime/orgo-worlds-state.json`.
4. World A → B → A selection/control operations preserve independent World metadata.
5. Create r2, promote r2, and verify `current_release_id`/release metadata change without rewriting other Worlds.
6. Membership read/manage rules are exercised with deliberately colliding World-local names.
7. Static anti-drift checks fail if Interaction Kernel, intake, work, Prisma operational schema or provider adapters are copied back into this repository.

End-to-end `DecisionRecord → Signal → Case/Tasks → Impact` qualification is **not** an Orgo_Worlds acceptance test. It belongs to the Konnaxion↔Orgo integration qualification at ecosystem level.


### Tandem P1 local qualification

- `npm run validate` checks the standalone architecture and the 9 Node
  boundary tests without opening a socket or requiring PostgreSQL.
- `npm run test:tandem-runtime` runs service-level tests when repository
  dependencies (`tsx`, NestJS) are installed; isolated temporary JSON stores.
- Public bind, production NODE_ENV, external origins and remote TCP peers
  must all be refused. Never expose the standalone header-based API on VPS.
- Cross-tenant matching World keys, revoked private access, archived World
  writes and mismatched current releases must be refused by service tests.
- Real main-Orgo tenant mapping, JWKS/SSO, World RBAC in a live service and
  independent database evidence remain outside this local qualification.
