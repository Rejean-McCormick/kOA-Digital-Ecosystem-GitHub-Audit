<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/How-Orgo-Works | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: c62d68c72889bf38b8c99331c54dca60cb3e16c17e34186c3b208f9451dfae5f -->

# How Orgo Works

Orgo follows a simple operational loop:

```text
Listen → Understand → Organize → Route → Act → Review → Learn
```

## 1. Listen

A **Signal** enters Orgo.

A signal may be a request, report, message, form submission, API call, system event, offline input or scheduled trigger.

A signal is only an input. Orgo does not assume every signal deserves a new Task.

## 2. Understand

Orgo evaluates the signal in the context of the Organization:

- What kind of situation is this?
- Does it belong to an existing Case?
- Does it require action?
- Which workflow rules apply?
- How urgent is it?
- Who or what area should receive it?

## 3. Organize

If durable context is needed, Orgo can use a **Case**.

If action is required, Orgo creates one or more **Tasks**.

```text
Case = the situation / continuing context
Task = a concrete unit of work
```

A Case may contain many Tasks over time.

## 4. Route

A Task can be classified and routed using an Orgo **Label**, organization roles and workflow rules.

Routing is deterministic enough to be understood and reviewed. It is not meant to be a mysterious recommendation layer.

## 5. Act

The Task follows the common Orgo lifecycle. It can be assigned, started, paused, escalated, completed, failed or cancelled according to the core rules.

Domain-specific information remains attached without replacing this common lifecycle.

## 6. Review

Orgo keeps the operational history needed to understand what happened:

- task events;
- assignments;
- comments;
- workflow transitions;
- audit/security information where applicable.

## 7. Learn

The **Insights** layer can detect trends, recurring issues and operational pressure.

A pattern is not automatically an instruction. When action is required, Orgo brings it back into the governed workflow:

```text
pattern
→ explicit work proposal
→ Case / Task
→ normal routing and lifecycle
```

This closes the loop between day-to-day work and organizational learning.
