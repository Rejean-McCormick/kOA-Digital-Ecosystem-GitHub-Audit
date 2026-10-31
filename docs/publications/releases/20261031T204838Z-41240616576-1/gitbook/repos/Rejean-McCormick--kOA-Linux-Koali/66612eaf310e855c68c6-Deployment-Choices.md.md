<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Deployment-Choices | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 4a58227996feb6a127bac9ad009f6d54a85f21ab66adf1b8d7576e30a98008c4 -->

<!-- Navigational projection. Normative authority remains in the repository docs/ corpus. -->

# Deployment Choices

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## One architecture, different capability sets

kOA-Linux Operating System uses profiles to state what a deployment includes, how much resource it may consume, which network assumptions apply, and how it behaves when a capability is unavailable.

## Main choices

| Profile or overlay | What it is for |
| --- | --- |
| User Lightweight | Daily local use on commodity hardware with bounded resources |
| Developer Linux Workstation | Isolated local development and testing on Linux |
| Developer Windows WSL | Isolated development from a Windows workstation using WSL |
| Sovereign Linux Node | Hardened production operation on one Linux node |
| Sovereign Hub | Locally autonomous shared services and coordination |
| Build Farm | Heavy compilation, validation, indexing, and artifact production |
| Control Plane | Release coordination, policy distribution, fleet metadata, and controlled oversight |
| Appliance Shell overlay | A focused appliance-style user surface |
| High Assurance overlay | Stronger trust, key custody, separation of duties, audit, and recovery requirements |
| Sovereign Offline overlay | Stricter offline and disconnected-operation conditions |

Profiles can compose with overlays, but an overlay may not silently weaken the primary profile's baseline.

## Sources

- [Profile model](../blob/main/docs/03-profiles/00-profile-model.md)
- [Profile composition](../blob/main/docs/03-profiles/01-profile-composition-and-overlays.md)
- [Generated profile catalog](../blob/main/docs/generated/profile-catalog.md)
- [Profile contracts](../tree/main/docs/contracts/profiles/)
