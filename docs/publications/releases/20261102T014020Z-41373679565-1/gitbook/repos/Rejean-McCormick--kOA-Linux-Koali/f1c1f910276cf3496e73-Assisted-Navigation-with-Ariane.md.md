<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Assisted-Navigation-with-Ariane | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 510fab4fa81a0fb4e5cb2d70c1e22bed45a12af07bf1419a186854c873df95a1 -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Assisted Navigation with Ariane

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## What Ariane changes

Traditional automation sees an interface as pixels, coordinates, selectors or undocumented scripts. Ariane treats the interface as data: screens, controls, actions, states and relationships form a semantic graph.

That graph allows a person, an assistive technology, or a bounded agent to ask not only “where is the button?” but “what action is available, what does it do, what state is required, and what happens next?”

## Navigation by intention

```text
user intention
    ↓
permitted capability and current context
    ↓
Ariane interface graph
    ↓
possible actions and prerequisites
    ↓
guided step, assistive action or bounded automation
    ↓
visible result and receipt when required
```

## Use cases

- guide a user through a complex administrative process;
- expose software to screen readers and other assistive systems through semantic actions;
- provide consistent navigation across profile-specific interfaces;
- help a local agent locate a permitted control without unrestricted host access;
- support multilingual labels while preserving one underlying action model;
- record which action was requested and which interface transition occurred.

## Boundaries

Ariane describes navigation and interaction possibilities. It does not automatically authorize an action. Authorization, consent, data disclosure and host privilege remain separate decisions.

External voice or AI services are optional integrations. The local navigation model remains distinct from any provider and must degrade explicitly when an optional service is unavailable.

## Offline behavior

The local graph and approved interface metadata can remain usable without network access. Remote voice recognition or remote language services may be unavailable, but their absence must not silently change the action model.

## Sources

- [Ariane public overview](https://initkoa.org/technology/ariane)
- [docs/02-system/11-ariane-system-boundary.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/02-system/11-ariane-system-boundary.md)
- [docs/10-adrs/ADR-021-ariane-local-navigation-with-optional-external-voice.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/10-adrs/ADR-021-ariane-local-navigation-with-optional-external-voice.md)
- [docs/contracts/subsystems/ariane.subsystem.json](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/contracts/subsystems/ariane.subsystem.json)
