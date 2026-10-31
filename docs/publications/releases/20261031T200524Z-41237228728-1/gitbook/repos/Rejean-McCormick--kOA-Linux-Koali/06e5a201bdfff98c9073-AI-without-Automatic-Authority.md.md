<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/AI-without-Automatic-Authority | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: 67056ff33490ecef7a0304cdedfb2235661d8a589cea141d76d83b9eb67b278c -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# AI Assistance and Automation

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## AI is optional capability, not hidden authority

kOA-Linux Operating System may expose local or external AI services for search assistance, summarization, classification, drafting, reconciliation, translation support or interface guidance. Those services do not automatically become authoritative sources of facts, policy, permissions or system state.

## Allowed roles

Depending on policy, an AI system may:

- propose classifications or candidate entities;
- summarize selected material with source links;
- draft text for human review;
- recommend a navigation path;
- suggest tasks or routing;
- assist multilingual work where deterministic resources are unavailable;
- identify patterns for review.

## Prohibited shortcuts

An AI service must not silently:

- invent missing architectural authority;
- convert a candidate claim into a validated fact;
- approve its own output;
- bypass consent or disclosure limits;
- gain unrestricted filesystem, database or host access;
- replace a missing subsystem with an undeclared provider;
- execute a sensitive action without the required task, policy and authorization chain.

## Automation as accountable work

Automated activity should be represented as tasks or declared operations with an actor identity, input references, capability restrictions, resource limits, expected output, status, evidence and failure code.

## External services

When data leaves the local environment, the user and policy layer need to know what is sent, to whom, for which purpose, under which retention assumptions, and whether a local alternative exists.

## Sources

- [docs/02-system/09-ai-boundary.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/02-system/09-ai-boundary.md)
- [docs/02-system/10-external-ai-surfaces.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/02-system/10-external-ai-surfaces.md)
- [docs/07-security/11-ai-boundaries.md](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/07-security/11-ai-boundaries.md)
- [SenTient status and scope](https://initkoa.org/technology/sentient)
