<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Deployment-Profiles | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: e3cc27551ab7ab1717051e1d2a82fcc0bb1c97d35a8f1e944901b1f601ac9fed -->

<!-- Navigational projection. Normative authority remains in the repository docs/ corpus. -->

# Deployment Profiles

> **Authority notice:** This wiki is a readable navigation layer. Source contracts, accepted ADRs, normative documents, and executable validators in the repository remain authoritative.

Profiles define deployable capability sets, resource limits, connectivity, component and subsystem membership, activation rules, degradation behavior, and conformance claims.

## Active profiles and overlays

| Profile | Type | Summary | Documentation | Contract |
| --- | --- | --- | --- | --- |
| Appliance Shell Overlay | overlay |  | [guide](../blob/main/docs/03-profiles/13-appliance-shell.md) | [contract](../blob/main/docs/contracts/profiles/appliance-shell.profile.json) |
| Build Farm |  |  | [guide](../blob/main/docs/03-profiles/09-build-farm.md) | [contract](../blob/main/docs/contracts/profiles/build-farm.profile.json) |
| Control Plane | primary_deployment_profile |  | [guide](../blob/main/docs/03-profiles/10-control-plane.md) | [contract](../blob/main/docs/contracts/profiles/control-plane.profile.json) |
| Developer Linux Workstation | deployment_profile |  | [guide](../blob/main/docs/03-profiles/05-developer-linux-workstation.md) | [contract](../blob/main/docs/contracts/profiles/developer-linux-workstation.profile.json) |
| Developer Windows WSL | primary_profile |  | [guide](../blob/main/docs/03-profiles/06-developer-windows-wsl.md) | [contract](../blob/main/docs/contracts/profiles/developer-windows-wsl.profile.json) |
| High Assurance | profile_overlay | A composable security and governance overlay that strengthens boot identity, hardware-backed trust, key custody, separation of duties, privileged operations, artifact verification, audit, recovery, and conformance evidence without changing the global product model or becoming a… | [guide](../blob/main/docs/03-profiles/11-high-assurance.md) | [contract](../blob/main/docs/contracts/profiles/high-assurance.profile.json) |
| Sovereign Hub | deployment_profile |  | [guide](../blob/main/docs/03-profiles/08-sovereign-hub.md) | [contract](../blob/main/docs/contracts/profiles/sovereign-hub.profile.json) |
| Sovereign Linux Node | primary | A hardened single-node Linux production profile with a maintained standard kernel, verified immutable signed system images, atomic activation, explicit release identity, closed-by-default networking, narrow privileged host mutation, selective audit, offline recovery, and tested… | [guide](../blob/main/docs/03-profiles/07-sovereign-linux-node.md) | [contract](../blob/main/docs/contracts/profiles/sovereign-linux-node.profile.json) |
| Sovereign Offline Overlay | deployment_profile_overlay |  | [guide](../blob/main/docs/03-profiles/12-sovereign-offline.md) | [contract](../blob/main/docs/contracts/profiles/sovereign-offline.profile.json) |
| User Lightweight | primary | A resource-bounded, general-purpose Linux deployment for daily local use on commodity hardware. | [guide](../blob/main/docs/03-profiles/04-user-lightweight.md) | [contract](../blob/main/docs/contracts/profiles/user-lightweight.profile.json) |

## Composition rules

- Primary profiles establish the deployment baseline.
- Overlays add stricter or narrower conditions without silently weakening the baseline.
- Profile membership is explicit; components do not infer deployment from their own contracts.
- Resource, connectivity, security, offline, and degradation claims remain profile-scoped.

## Model sources

- [`docs/03-profiles/00-profile-model.md`](../blob/main/docs/03-profiles/00-profile-model.md)
- [`docs/03-profiles/01-profile-composition-and-overlays.md`](../blob/main/docs/03-profiles/01-profile-composition-and-overlays.md)
- [`docs/03-profiles/02-profile-inheritance.md`](../blob/main/docs/03-profiles/02-profile-inheritance.md)
- [`docs/03-profiles/03-profile-conformance-claims.md`](../blob/main/docs/03-profiles/03-profile-conformance-claims.md)
- [`docs/generated/profile-catalog.md`](../blob/main/docs/generated/profile-catalog.md)
