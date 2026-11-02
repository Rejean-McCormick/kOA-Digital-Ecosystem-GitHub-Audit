<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/Clinical-Epistemic-States | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: bf9eed65f5df72714c76884c379f14e93bb1f5aeec2f3ecb1be6fcc14cde6781 -->

# Clinical Epistemic States

A core MediKristal object is the **Clinical Epistemic State**: a representation of medical knowledge together with its provenance, scope, uncertainty, review state, and governance history.

## Three separate questions

```text
Does this claim exist in the system?

Is it usable for a defined purpose?

Has it been promoted for a defined trust surface?
```

These are not equivalent.

## Proposed lifecycle

```text
draft
  ↓
under_review
  ↓
working_accepted / disputed
  ↓
promoted for defined scope
  ↓
superseded or revoked when necessary
```

Disputed content may remain represented without being promoted.

## Scope belongs to the claim

Medical assertions often depend on:

- jurisdiction;
- population;
- age range;
- pregnancy applicability;
- care setting;
- product availability;
- guideline version;
- effective date;
- review/expiration date.

Therefore “promoted” should never silently mean “universally true forever.”

## Provenance chain

```text
MediKristal assertion
        ↓ supported_by
Guideline / terminology / government data / protocol
        ↓
source version + date + jurisdiction + original identifier
```

## Historical fidelity

When medical knowledge changes, the new version should not rewrite history.

A system must be able to reconstruct:

> **Why did this node or application produce this result on that date?**

That requires retaining the prior source versions, promoted state, protocol version, Runtime Pack identity, and relevant policy.

## Compile versus promote

```text
compile ≠ approve
```

A proposed mapping, translation, or protocol can be compiled and tested before it is accepted for a clinical trust surface.
