<!-- Frozen source: https://github.com/Rejean-McCormick/Interaction-Kernel/blob/1d0598456fe8203625f9831ec00c32225422631d/docs/conformance.md | commit: 1d0598456fe8203625f9831ec00c32225422631d | SHA-256: 2408ee0c1d89b6ba2399f862bdc343f6710e76ff41846c460866d70e5027c775 -->

# Conformance

Claims:

- `IK-Core/1.1`
- `IK-Reliable/1`
- `IK-HTTP/1` (optional binding)
- `IK-Artifact/1`
- `IK-Kristal/1`
- `IK-KX-ORGO/1`

The TCK contains the 9 pinned Kristal RFC 8785 JCS vectors and IK request-fingerprint vectors shared by Python and TypeScript runtimes.

Scenario fixtures such as UCKK-A014 are end-to-end conformance tests, not definitions of Core.

## Tandem Konnaxion–Orgo

The active versions of the three Konnaxion–Orgo Profiles are pinned with file digests and checked across Python and TypeScript. See [Tandem contract gate](tandem-konnaxion-orgo-conformance.md). This is a repository gate, not a live qualification.
