<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Home | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 49e2bea3d9ce97790b9a5ea9ca4f66789c7b7af31dd1814ae3f71833d5009b94 -->

# Orgo

**Orgo is a coordination system for turning messy signals into clear, accountable work.**

Organizations rarely receive work in a neat format. A request may begin as an email, a form, a conversation, a report, a recurring issue or a system event. Orgo gives these signals a common operational language so they can be understood, routed, acted on and reviewed without forcing every organization into the same workflow.

A useful way to think about Orgo is as an **operational nervous system**:

```text
something happens
      ↓
Orgo receives the signal
      ↓
context is organized into a Case when needed
      ↓
action becomes one or more Tasks
      ↓
work is routed, tracked and escalated
      ↓
patterns become visible through Insights
      ↓
new work can be created when action is needed
```

Orgo is multi-tenant: each **Organization** has its own work, people, policies and behavioral profile.

## What makes Orgo different

Orgo is built around a few shared ideas rather than a separate workflow engine for every department:

- **Task** is the common unit of work.
- **Case** keeps durable context around related work.
- **Signals** are inputs, not automatically work items.
- **Workflows** evaluate what should happen.
- **Labels** help route and classify work.
- **Profiles** adapt Orgo to different organizations without changing the core model.
- **Insights** help organizations notice recurring patterns and review how work is actually flowing.
- **Domain modules** add specialized context while reusing the same Task/Case backbone.

This lets a maintenance team, a school, a care organization, an association or an internal operations team use the same underlying coordination model while keeping their own vocabulary and rules.

## Start here

- [[What is Orgo|What-is-Orgo]]
- [[How Orgo Works|How-Orgo-Works]]
- [[Cases and Tasks|Cases-and-Tasks]]
- [[Signals and Workflows|Signals-and-Workflows]]
- [[Routing and Labels|Routing-and-Labels]]
- [[Profiles and Adaptability|Profiles-and-Adaptability]]
- [[Reactivity and Escalation|Reactivity-and-Escalation]]
- [[Domains and Use Cases|Domains-and-Use-Cases]]
- [[Cyclic Overview and Insights|Cyclic-Overview-and-Insights]]
- [[Organizations, People and Privacy|Organizations-People-and-Privacy]]
- [[Interoperability]]
- [[Semantic Charters|Semantic-Charters]]
- [[Glossary]]
- [[Example Scenarios|Example-Scenarios]]
- [[FAQ]]
- [[Validation and Release Status|Validation-and-Release-Status]]

## Current validation snapshot

As of **2026-09-17**, the current development tree has passed Orgo's complete local automated validation chain: database, deep validation, browser validation and production-like acceptance. The acceptance path includes backup/restore, an isolated Docker deployment and 24/24 Chromium journeys.

See [[Validation and Release Status|Validation-and-Release-Status]] for the exact scope and the distinction between local production-like evidence and a real production deployment.

## What Orgo is not

Orgo is not meant to replace every business system around it.

It is not, by itself:

- a payroll system;
- an accounting ERP;
- a casual chat application;
- a domain database for every external system;
- a knowledge-truth engine;
- a civic decision system.

Orgo coordinates work and keeps operational state. When another system owns the underlying domain, Orgo tracks and orchestrates the work around it rather than silently taking ownership of that system's data.

---

**Technical implementation details live in the Orgo documentation.** This wiki focuses on the public-facing concepts and how Orgo is meant to be understood and used.
