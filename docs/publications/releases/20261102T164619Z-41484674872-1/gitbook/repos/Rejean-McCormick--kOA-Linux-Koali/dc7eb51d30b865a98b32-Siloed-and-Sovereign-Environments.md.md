<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Siloed-and-Sovereign-Environments | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 18b0671ee807ad7cc1d6a774d4c0fc4337f9e6ef9f55b80ad691af6b7fd72305 -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Siloed and Sovereign Environments

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## What “silo” means here

A silo is not automatically a defect. A community, organization, institution, field team, municipality, or high-assurance unit may need its own data, identities, rules, storage, availability and authority. The problem is not separation itself; the problem is separation without safe interoperability, portability or exit.

kOA-Linux Operating System is designed to support **bounded environments that can cooperate without becoming one shared database or one central authority**.

## Isolation dimensions

A deployment can separate:

- identities and role assignments;
- databases and authoritative stores;
- files, media and encryption keys;
- service accounts and host privileges;
- network segments and outbound access;
- policy bundles and trust roots;
- release channels and activation schedules;
- audit visibility and evidence access;
- synchronization and publication gateways.

## Interoperability between silos

Cooperation happens through declared objects and transitions:

- Kristals and other portable artifacts;
- signed or verified bundles;
- publication gateways;
- Orgo signals, cases, tasks and receipts;
- explicit synchronization sessions;
- scoped identity and trust assertions;
- controlled exports and imports.

Direct writes into another subsystem's authoritative database are prohibited by the architecture.

## Deployment patterns

### Independent organization

One organization runs a local node with private Orgo services, local files, selected knowledge packs and controlled external publication.

### Community hub

A hub serves local users, distributes knowledge and civic surfaces, and synchronizes when connectivity is available.

### Federated institutions

Several institutions maintain separate authorities but exchange verified artifacts and accountable requests.

### Air-gapped environment

Updates and exports travel through removable media or controlled transfer, with local verification before activation.

## Safe failure behavior

A missing remote system does not justify broadening access or substituting a different provider. The system preserves queued work, visible version state and explicit unavailable/degraded labels.

## Sources

- [docs/01-constitution/07-component-separation.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/01-constitution/07-component-separation.md)
- [docs/02-system/04-component-boundaries.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/02-system/04-component-boundaries.md)
- [docs/07-security/02-security-domains.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/07-security/02-security-domains.md)
- [docs/07-security/08-network-boundaries.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/07-security/08-network-boundaries.md)
- [Kristal portability and offline use](https://initkoa.org/technology/kristal/portability-and-offline)
