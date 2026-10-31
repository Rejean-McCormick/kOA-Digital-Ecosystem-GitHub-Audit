<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/What-is-Orgo | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 1398dcfbe5504f72984d6c9364ec0cf83bccc96838f120ec5062a732214dc3f6 -->

# What is Orgo?

Orgo is a **multi-tenant workflow and coordination system**.

Its purpose is simple to state: take the many things that happen around an organization and turn the ones that require attention into structured, traceable work.

## The problem Orgo addresses

Organizations receive signals from many places:

- email;
- forms and APIs;
- staff or community reports;
- operational systems;
- periodic reviews;
- offline synchronization;
- timers and recurring checks.

Without a common structure, the result is usually fragmentation: different teams invent different status labels, important context is lost between tools, and recurring problems are hard to see.

Orgo standardizes the operational layer without forcing every domain to become identical.

## One backbone, many domains

Orgo uses the same shared work backbone across domains:

```text
Organization
   ├── Cases
   │    └── Tasks
   ├── Workflows
   ├── Labels
   ├── Profile
   └── Insights
```

A maintenance task and an education-support task can therefore share the same basic operational lifecycle while keeping very different domain-specific details.

## Orgo owns workflow state

This is an important boundary.

Orgo is authoritative for things such as:

- whether an Orgo Task is pending, in progress or completed;
- who is assigned to that Task;
- which Case groups related work;
- the routing label attached to the work;
- escalation and reactivity state;
- Orgo workflow execution and audit information.

Orgo does **not** become the owner of another system's internal state simply because a Task refers to it.

For example, if Orgo coordinates work related to a Konnaxion consultation or a Kristal artifact, the Task can reference that external object while the external system remains authoritative for its own domain.

## A coordination system, not a department-specific app

Orgo is designed to remain useful across different organizational settings. Specialized domain modules can add context for Maintenance, HR, Education and other areas, but they reuse the same core work model.

That is the central design idea:

> **Different domains, shared operational grammar.**
