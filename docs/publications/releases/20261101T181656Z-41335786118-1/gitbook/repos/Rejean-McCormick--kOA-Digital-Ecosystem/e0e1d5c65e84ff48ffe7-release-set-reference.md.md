<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/90865538b0c16be08423843208f4c5e6785a7523/docs/2-Technical-Reference/30-artifacts/release-set-reference.md | commit: 90865538b0c16be08423843208f4c5e6785a7523 | SHA-256: 97f6a65eebc3d5ed181e90c9b3b1fed914d7346f7e5f4a12f6ded4d7f99b99b9 -->

# kOA-Linux Release Set reference

Digital Ecosystem references the kOA-Linux `release-set.schema.json` contract rather than re-specifying it.

## Purpose

A Release Set binds tested-compatible versions across independent platform release channels:

- `system`;
- `services`;
- `governance`;
- `knowledge`.

A Release Set is a platform compatibility/release artifact. It is not Kristal epistemic validation or authority recognition.

## Runtime Pack relationship

Runtime Packs enter the kOA-Linux `knowledge` channel. Release Set compatibility can be one prerequisite for activation, but `kristal_runtime` still owns Runtime Pack verification/compatibility/active-state behavior.

## Non-confusion

```text
Release Set compatible
≠ Runtime Pack validated by Kristal
≠ Runtime Pack active
≠ Space active in Koali
```
