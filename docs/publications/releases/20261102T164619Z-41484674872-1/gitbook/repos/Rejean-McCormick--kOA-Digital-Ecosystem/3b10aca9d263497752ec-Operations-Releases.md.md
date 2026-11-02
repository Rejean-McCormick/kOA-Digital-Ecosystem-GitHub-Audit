<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/58a5fa07c18b360a1abd7a213023c6ceaa9d1533/docs/1-Overview/Operations-Releases.md | commit: 58a5fa07c18b360a1abd7a213023c6ceaa9d1533 | SHA-256: 6d83384d2bc59bfae94e3fa39e553810df2fd4de4c469a887c691e386ce45b66 -->

# Releases

kOA-Linux uses independently versioned release channels joined by **Release Sets**.

## Channels

The platform baseline distinguishes:

- `system`;
- `services`;
- `governance`;
- `knowledge`.

Kristal Runtime Packs and Kristal artifacts are admitted through the **knowledge** release channel in the current kOA-Linux contracts.

## Release Set

A Release Set binds compatible versions across channels. Digital Ecosystem references this contract instead of defining a parallel authoritative Release Record.

A release decision still does not collapse independent states:

```text
artifact produced
≠ artifact admitted
≠ channel compatible
≠ Runtime Pack verified
≠ Runtime Pack active
```

## Runtime Pack activation

For kOA-Linux:

1. the Runtime Pack enters through the knowledge channel;
2. `kristal_runtime` validates identity/digest/provenance/trust/compatibility/channel/downgrade or substitution policy;
3. `kristal_runtime` owns activation eligibility and the active Runtime Pack record;
4. kOA Node Agent executes a narrow privileged host transition when the profile requires it;
5. receipts/evidence are emitted by the owning contracts.
