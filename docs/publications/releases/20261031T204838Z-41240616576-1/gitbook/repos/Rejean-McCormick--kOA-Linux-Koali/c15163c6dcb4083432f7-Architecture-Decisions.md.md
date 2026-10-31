<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Architecture-Decisions | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: ab3c79a1862a98c45eb762759d6469b0c60471e49dd13e682813bb95cc376b32 -->

<!-- Navigational projection. Normative authority remains in the repository docs/ corpus. -->

# Architecture Decision Records

> **Authority notice:** This wiki is a readable navigation layer. Source contracts, accepted ADRs, normative documents, and executable validators in the repository remain authoritative.

ADRs preserve context, considered options, rationale, consequences, and impact. Active system facts remain in the applicable source contracts and normative documents.

## Accepted ADR set

| ADR | Decision | Source |
| --- | --- | --- |
| ADR-001 | — Use a Standard Maintained Linux Kernel | [record](../blob/main/docs/10-adrs/ADR-001-standard-maintained-linux-kernel.md) |
| ADR-002 | — Immutable Signed OS Image | [record](../blob/main/docs/10-adrs/ADR-002-immutable-signed-os-image.md) |
| ADR-003 | — Appliance Shell Without GNOME | [record](../blob/main/docs/10-adrs/ADR-003-appliance-shell-without-gnome.md) |
| ADR-004 | — Minimal Wayland and Embedded Web Engine | [record](../blob/main/docs/10-adrs/ADR-004-minimal-wayland-and-embedded-web-engine.md) |
| ADR-005 | Rootless Podman and Quadlet | [record](../blob/main/docs/10-adrs/ADR-005-rootless-podman-and-quadlet.md) |
| ADR-006 | — Expanded First-Class Component Boundaries | [record](../blob/main/docs/10-adrs/ADR-006-expanded-first-class-component-boundaries.md) |
| ADR-007 | — Kristal as a Transversal Knowledge Layer | [record](../blob/main/docs/10-adrs/ADR-007-kristal-as-transversal-foundation.md) |
| ADR-008 | Four Independent Release Channels | [record](../blob/main/docs/10-adrs/ADR-008-four-independent-release-channels.md) |
| ADR-009 | — Governance Policy Runtime | [record](../blob/main/docs/10-adrs/ADR-009-governance-policy-runtime.md) |
| ADR-010 | — Selective Audit | [record](../blob/main/docs/10-adrs/ADR-010-selective-audit.md) |
| ADR-011 | — No Kubernetes Requirement on Endpoints | [record](../blob/main/docs/10-adrs/ADR-011-no-kubernetes-requirement-on-endpoints.md) |
| ADR-012 | — Single Narrow Privileged Broker | [record](../blob/main/docs/10-adrs/ADR-012-single-narrow-privileged-broker.md) |
| ADR-013 | — System Baseline and Profile Separation | [record](../blob/main/docs/10-adrs/ADR-013-system-baseline-and-profile-separation.md) |
| ADR-014 | — Strict External AI Boundary | [record](../blob/main/docs/10-adrs/ADR-014-strict-external-ai-boundary.md) |
| ADR-015 | Development Workspace Isolation with UV | [record](../blob/main/docs/10-adrs/ADR-015-development-workspace-isolation-with-uv.md) |
| ADR-016 | — Generated Markdown Projections | [record](../blob/main/docs/10-adrs/ADR-016-generated-markdown-projections.md) |
| ADR-017 | — User Lightweight Hardware Profile | [record](../blob/main/docs/10-adrs/ADR-017-user-lightweight-hardware-profile.md) |
| ADR-018 | SenTient as an Isolated Optional Workbench | [record](../blob/main/docs/10-adrs/ADR-018-sentient-as-isolated-optional-workbench.md) |
| ADR-019 | Resource Governor and Policy Runtime Separation | [record](../blob/main/docs/10-adrs/ADR-019-resource-governor-and-policy-runtime-separation.md) |
| ADR-021 | Ariane Local Navigation with Optional External Voice | [record](../blob/main/docs/10-adrs/ADR-021-ariane-local-navigation-with-optional-external-voice.md) |
| ADR-023 | — Explicit Profile Overlays | [record](../blob/main/docs/10-adrs/ADR-023-explicit-profile-overlays.md) |
| ADR-024 | — Logical Data Ownership with Profile-Dependent Physical Isolation | [record](../blob/main/docs/10-adrs/ADR-024-logical-data-ownership-with-profile-dependent-physical-isolation.md) |
| ADR-025 | — English-Only Active Documentation | [record](../blob/main/docs/10-adrs/ADR-025-english-only-active-documentation.md) |
| ADR-026 | — No Unresolved Active Authority | [record](../blob/main/docs/10-adrs/ADR-026-no-unresolved-active-authority.md) |
| ADR-027 | Contract-First Documentation and Generated Navigation | [record](../blob/main/docs/10-adrs/ADR-027-contract-first-documentation-and-generated-navigation.md) |
| ADR-028 | Subsystem Documentation Remains Authoritative | [record](../blob/main/docs/10-adrs/ADR-028-subsystem-documentation-remains-authoritative.md) |

## Decision workflow

A significant architectural change should identify the affected authority, record the decision, update the owning contracts and documents, rebuild generated projections, and pass validation before activation.

## Sources

- [`docs/10-adrs/README.md`](../blob/main/docs/10-adrs/README.md)
- [`docs/generated/decision-index.md`](../blob/main/docs/generated/decision-index.md)
