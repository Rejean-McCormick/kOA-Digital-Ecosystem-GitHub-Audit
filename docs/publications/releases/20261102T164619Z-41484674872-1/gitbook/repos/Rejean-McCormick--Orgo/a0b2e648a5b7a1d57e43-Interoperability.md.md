<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo/wiki/Interoperability | commit: b89ca31f268c521cbd70ab1c736338a8c5039df7 | SHA-256: 644b9efb9b0d88fc9ed5d862711c83b1ae4ac663575b0ec1a3af4ac560e7d0da -->

# Interoperability

Orgo is designed to coordinate work **with** other systems rather than absorb them.

This matters in the wider kOA Digital Ecosystem, where different systems have different responsibilities.

## The basic rule

```text
Orgo owns workflow state.
The other system owns its own domain state.
```

An Orgo Task can request an operation, track its progress and record a receipt without becoming the source of truth for the external object.

## Konnaxion

Konnaxion owns its civic/public domain.

Orgo has a generic provider-bridge pattern for coordinating external operations and retaining references/receipts. A native Interaction Kernel Konnaxion adapter is not claimed by the current implementation snapshot. When Orgo coordinates work related to a consultation, deliberation or civic process, the ownership boundary remains:

```text
Orgo Case ≠ Konnaxion Topic
Orgo Task ≠ Konnaxion Consultation
```

## Kristal

Kristal owns epistemic artifacts and their semantics.

Orgo's generic provider bridge can coordinate external operations while retaining opaque references and receipts, but a native Interaction Kernel / Da’at Kristal adapter is not claimed by the current implementation snapshot. Completing an Orgo Task does not automatically mean a Kristal assertion has been validated or recognized.

## SemantiK Architect

SemantiK Architect owns language-generation planning and realization.

Orgo can request generated output as part of a workflow, but generated language is not the same thing as Orgo workflow state.

## kOA-Linux

When Orgo runs within kOA-Linux, Orgo keeps ownership of its Cases, Tasks and workflows. kOA-Linux owns the local platform boundary: host resources, service lifecycle, privilege mediation, recovery and other operating-system responsibilities.

## Why this separation matters

It prevents one integration from turning into a shared database where nobody knows which system is authoritative.

A healthy integration looks more like:

```text
Orgo requests
→ external system validates and acts
→ result / event / receipt returns
→ Orgo reconciles its own workflow
```

The same principle applies to other external tools and services.
