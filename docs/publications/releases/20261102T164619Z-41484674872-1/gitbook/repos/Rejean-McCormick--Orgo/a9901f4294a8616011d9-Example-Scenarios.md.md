<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Example-Scenarios | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: e1a3361e5ebaafed535afb3fd5c6b4a148f3b47717956740856e0dd2f984577e -->

# Example Scenarios

These examples illustrate the Orgo model without defining new domain contracts.

## 1. Facilities issue

A staff member reports water leaking near an entrance.

```text
report arrives
→ Signal
→ workflow evaluates severity and routing
→ Case: recurring/continuing facilities situation when needed
→ Task: inspect the leak
→ maintenance context links the relevant asset/location
→ Task is assigned and tracked
→ later incidents can appear in Insights as a pattern
```

The maintenance information is specialized, but the work still uses the common Orgo Task lifecycle.

## 2. Sensitive HR report

A report concerns a person and requires restricted handling.

```text
report
→ Signal
→ HR workflow
→ Case for durable confidential context
→ primary Task for the next required action
→ HR participants/context attached
→ visibility and authorization rules apply
```

The Person concerned by the Case does not need to be an Orgo User.

## 3. Education support

A student-support concern is submitted.

```text
support signal
→ workflow
→ Task
→ education context links the relevant person/group
→ assignment and follow-up
```

Education-specific context stays in the domain layer while work progression remains canonical Orgo Task state.

## 4. Repeated incident becomes organizational work

Several similar incidents occur over time.

```text
individual Tasks/Cases
→ Insights detects a recurring pattern
→ pattern is reviewed
→ explicit follow-up Case/Task is created
→ normal routing and accountability
```

Insights does not silently rewrite operational state.

## 5. Coordinating an external system

An Orgo workflow needs an operation performed by another system.

```text
Orgo Task
→ explicit request to external system
→ external system validates and acts in its own domain
→ result / receipt returns
→ Orgo reconciles the Task
```

Orgo coordinates the work without taking ownership of the external system's internal data.
