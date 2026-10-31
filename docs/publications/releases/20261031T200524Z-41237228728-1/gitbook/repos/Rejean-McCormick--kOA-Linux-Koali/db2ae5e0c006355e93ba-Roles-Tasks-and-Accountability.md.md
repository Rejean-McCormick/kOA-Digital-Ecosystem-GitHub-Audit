<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Linux-Koali/wiki/Roles-Tasks-and-Accountability | commit: a014d6b410b475fe227e3f0153bbae6e54ef0520 | SHA-256: b385c18725ffbf6bd8a06f0ad6e071563aeadb04c3d9edb27e4b604c942e4cd9 -->

<!-- Explanatory wiki projection; not an independent normative authority. -->

# Roles, Tasks, and Accountability

> **Authority and status:** This wiki is an explanatory navigation layer. The repository contracts, accepted ADRs, normative documents, and executable validators remain authoritative for kOA-Linux Operating System. Public initkoa.org pages explain the wider kOA ecosystem and the product capabilities provided by its independently documented subsystems.

## Function-first coordination

Orgo routes work to responsibilities such as Intake, Incident Response, Procurement, Legal Review, Case Management or Maintenance. This reduces dependence on whoever happens to read a message and preserves continuity when people leave or teams reorganize.

## Roles

A role represents a durable responsibility with scoped permissions. People may be assigned to roles for an organization, team, location, unit or other declared scope. Role assignments are revocable and auditable.

## Cases

A case is the durable context for a situation: why work exists, which policy applies, who owns it, which artifacts are linked, what tasks belong to it, and how the outcome can be reviewed.

## Tasks

A task is an executable unit of work with:

- identity and parent case;
- owning role or person;
- status and allowed transitions;
- inputs and expected outputs;
- deadline and retry limits;
- approval and capability gates;
- visibility and confidentiality;
- evidence and completion criteria.

## Escalation and closure

An overdue task does not disappear silently. Policy determines when responsibility escalates and who is notified. Closure records the result, actors, changes, evidence and unresolved matters.

## Organizational learning

Recurring delays, duplicates, failures or policy friction can become new review or audit cases. The system therefore converts operational patterns into governed improvement work.

## Sources

- [What Orgo does](https://initkoa.org/platforms/orgo/what-it-does)
- [Routing and escalation](https://initkoa.org/platforms/orgo/routing-escalation)
- [Core guarantees](https://initkoa.org/platforms/orgo/guarantees)
- [docs/contracts/subsystems/orgo.subsystem.json](https://github.com/Rejean-McCormick/kOA-Linux/blob/main/docs/contracts/subsystems/orgo.subsystem.json)
