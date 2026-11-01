<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Global-Communications-and-Distribution | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: d30c5f56dd73c4deb39fbd768272a20251233578a01aedd0e620ffc691d5052a -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Global Communications and Distribution

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## Communication is part of coordination

The kOA model does not treat communication as an isolated chat feature. A communication may be public knowledge, an announcement, a request, an incident report, a decision, a task-generating signal, a distribution package or a synchronization event.

## Two complementary paths

### Konnaxion: public and community distribution

Konnaxion supports the publication and distribution of learning resources, knowledge, projects, deliberation, decisions and shared memory. Content may be delivered online, mirrored locally or packaged for offline use.

### Orgo: communications that require accountable action

Orgo can ingest email, forms, APIs, field notes, call logs, imported archives and other signals. Role inboxes map communication channels to functions. Workflow rules decide whether a signal opens a case, creates tasks, routes work, starts a timer or triggers escalation.

## A governed communication path

```text
message, report or event
    ↓
identity, consent and disclosure checks
    ↓
classification: information / request / update / decision / report / distribution
    ↓
public distribution or private organizational routing
    ↓
receipt, ownership, task or queued delivery
    ↓
response, escalation and closure when action is required
```

## Global does not mean centralized

Distribution can cross organizations and regions while each node preserves its own authority, storage and policy. Portable artifacts, local mirrors, asynchronous queues and explicit gateways reduce dependence on one global service.

## Automation boundaries

Automated messages must identify their source, applicable policy, target scope and whether action is expected. High-volume automation must be rate-limited and cannot bypass consent, visibility or role permissions.

## Sources

- [Konnaxion](https://initkoa.org/platforms/konnaxion)
- [What Orgo does](https://initkoa.org/platforms/orgo/what-it-does)
- [Routing and escalation](https://initkoa.org/platforms/orgo/routing-escalation)
- [docs/02-system/07-cross-component-communication.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/02-system/07-cross-component-communication.md)
- [docs/07-security/17-cross-domain-publication.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/07-security/17-cross-domain-publication.md)
