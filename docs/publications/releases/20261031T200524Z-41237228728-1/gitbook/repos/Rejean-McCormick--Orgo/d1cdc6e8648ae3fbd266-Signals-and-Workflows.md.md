<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Signals-and-Workflows | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: b8bfd927e0c739bd796ea032ec059143c50714993a0a641aa6f4bec5bc7e0ca4 -->

# Signals and Workflows

A major Orgo principle is that **an incoming signal is not automatically a task**.

## Signals

A Signal is something Orgo receives that may require interpretation or action.

Examples include:

- a message or email;
- an API request;
- a form submission;
- a system-generated event;
- a timer;
- an offline/synchronized input.

Signals can carry structured context, but they do not decide their own operational outcome.

## Workflows

A **Workflow** evaluates a signal or existing operational context and determines which actions should follow.

Conceptually:

```text
Signal + Organization context
        ↓
Workflow rules
        ↓
resolved actions
        ↓
Tasks / Cases / routing / notification / metadata changes
```

Typical actions can include creating work, updating work, routing it, escalating it, attaching metadata or notifying someone.

## Why evaluation and execution are separate

Orgo distinguishes **deciding what should happen** from **performing the side effect**.

That matters because it allows a workflow to be simulated:

```text
same input + same rules
→ same resolved actions
→ no mutation in simulation mode
```

This makes workflows easier to inspect, test and explain.

## Workflows do not own everything they touch

If a workflow eventually calls another system, that system still decides whether the requested operation is valid in its own domain.

Orgo can coordinate the process and reconcile the result, but it does not gain direct write access to another system's internal data.
