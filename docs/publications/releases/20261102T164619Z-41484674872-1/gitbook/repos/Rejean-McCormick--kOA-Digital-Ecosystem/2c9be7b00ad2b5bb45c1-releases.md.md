<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/2-Technical-Reference/50-operations/releases.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: e10f0c00e3f98fc162030f6dbd52043a15dbebbd01732f7278e68e64637000c2 -->

# Operations — release and activation

## Platform release model

kOA-Linux separates `system`, `services`, `governance` and `knowledge` release channels and binds compatible versions through Release Sets.

A Release Set is authoritative for platform release compatibility, not for Kristal epistemic validation or Runtime Pack active state.

## Tandem Konnaxion + Orgo — VPS-specific deployment track

The first tandem candidate is **VPS Linux + Docker + Konnaxion Capsule Agent**, not a default kOA-Linux Runtime Pack deployment. [C0 coordination profile and blocking gates](../40-integration/tandem-vps-capsule-agent/README.md) records the user's selected target and exact-owner handoffs. **Capsule Agent owns its own protected host operations and admission PEP for this profile**, while KonnaxionDiag independently verifies exact signed release authorization. This profile does not transfer the `kristal_runtime`/kOA-Linux active-state or release-channel authority described below. No VPS activation or approval is claimed.

## Runtime Pack activation

For a kOA-Linux Runtime Pack:

1. artifact arrives through the `knowledge` release channel;
2. Release Set compatibility is checked where required;
3. `kristal_runtime` validates schema/identity/digest/provenance/trust/compatibility/channel/downgrade/substitution policy;
4. `kristal_runtime` owns activation eligibility and active Runtime Pack state;
5. kOA Node Agent executes the narrow privileged transition when required;
6. owner receipts/evidence are emitted.

Digital Ecosystem defines no parallel release or Runtime Pack active-state authority.
