<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Domains-and-Use-Cases | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: af81b62c49840b7466ce2efe9655741e9bf6ae0a4e3eb5fa805cca5e93488c90 -->

# Domains and Use Cases

Orgo is not limited to one industry or department. Domain modules add specialized context while keeping the shared Task/Case backbone.

The current Orgo model includes examples for **Maintenance, HR and Education**, and the charter system also defines reusable semantic families for care, programs, operations, groups and incidents.

## Maintenance

A maintenance request can add context such as:

- asset;
- location;
- repair information;
- calendar or maintenance slot.

But the actual work remains a canonical Orgo Task.

```text
maintenance request
→ Orgo Task
→ maintenance-specific context
→ normal Task lifecycle
```

## HR

A sensitive HR situation can use a Case for durable context and Tasks for the actions that follow.

```text
report
→ Case
→ primary Task
→ HR-specific participants and context
```

This is useful because confidentiality and subject participation can remain domain-specific while assignment and work progression continue to use the shared Orgo engine.

## Education

Education-support or incident work can be linked to learning groups, people and education-specific context while remaining a canonical Task.

## Why domain modules are not separate workflow engines

The goal is not to make every domain identical. It is to avoid rebuilding basic operational concepts every time.

A domain can have rich business rules and additional data without redefining:

- what a Task is;
- the Task lifecycle;
- how Cases contain work;
- how core routing and events operate.

## Beyond the built-in examples

The same pattern can support other organizational settings when their specialized data and rules can be layered around the common work backbone.

Orgo's semantic charters help describe these domains without turning every vocabulary difference into a new core schema.
