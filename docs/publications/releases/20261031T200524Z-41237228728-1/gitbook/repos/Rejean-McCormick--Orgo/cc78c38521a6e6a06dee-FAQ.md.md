<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/FAQ | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 8a1d7816d54998c0bb8287131f71fd38907be402379e8b442da1dfe4af811f71 -->

# FAQ

## Is Orgo a ticketing system?

It can handle work that resembles tickets, but its model is broader. Orgo separates Signals, Cases and Tasks, adds workflow evaluation, organization profiles, routing labels and cyclic review, and supports multiple domain modules on the same core.

## Is a Case just a large Task?

No. A Case is durable context for a situation. A Task is a unit of work. A Case may contain many Tasks over time.

## Does every Signal create a Task?

No. A Signal is evaluated first. A workflow may ignore it, update existing work, create a Case, create one or more Tasks, route information or perform another declared action.

## Can each department define its own Task statuses?

Not as a separate core lifecycle. Domain modules add context while reusing the canonical Orgo Task lifecycle.

## What are Labels for?

Labels help classify and route work. They are not a replacement for authorization and should not be overloaded with every possible taxonomy concept.

## What is a broadcast label?

It is an informational routing form. Broadcasting something does not automatically create mandatory work. A workflow must explicitly create a Task when action is required.

## How does Orgo adapt to different organizations?

Through Organization Profiles and domain modules. Profiles tune behavior; domain modules add specialized context.

## What is Reactivity Time?

It is Orgo's way of expressing how quickly work is expected to receive attention or response. The actual defaults can vary by Organization Profile.

## Does Orgo use AI to decide everything?

The architecture does not depend on a heavy external LLM as its core workflow engine. Workflow rules, labels, profiles and semantic charters are designed to remain explicit and compatible with local/offline operation.

## Is Insights allowed to change Tasks automatically?

Insights is primarily analytical. When a detected pattern should create operational work, that should happen explicitly through the normal Case/Task core rather than by silently rewriting operational state.

## Is Orgo part of kOA-Linux?

Orgo is an ecosystem system in its own right. In a kOA-Linux deployment it can be integrated as a subsystem from the host's point of view, while Orgo remains authoritative for its own workflow state.

## Does Orgo own Konnaxion or Kristal data when it coordinates them?

No. Orgo may track work, external references and results, but the external system remains authoritative for its own domain.

## Is Orgo an ERP?

No. It may coordinate work around ERP-like processes, but it is not intended to become the authoritative accounting, payroll or inventory system simply because those processes create Tasks.
