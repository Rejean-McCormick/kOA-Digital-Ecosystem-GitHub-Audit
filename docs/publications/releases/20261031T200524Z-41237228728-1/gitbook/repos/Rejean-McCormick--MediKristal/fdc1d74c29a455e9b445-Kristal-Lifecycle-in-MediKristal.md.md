<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/Kristal-Lifecycle-in-MediKristal | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: 8dc7e2b952a407fd405be7e01b36e25f0736210004730c74f649566d69e72d52 -->

# Kristal Lifecycle in MediKristal

MediKristal uses the **Kristal** model to turn a medical claim into a portable, inspectable artifact rather than an anonymous row in a database.

- [Kristal Framework repository](https://github.com/Rejean-McCormick/kristal-framework)
- [Kristal in the kOA-Linux Wiki](https://github.com/Rejean-McCormick/kOA-Linux/wiki/Kristal)
- [Portable Knowledge with Kristal](https://github.com/Rejean-McCormick/kOA-Linux/wiki/Portable-Knowledge-with-Kristal)

## What a medical Kristal can carry

Conceptually, a MediKristal artifact can preserve:

```text
assertion identity
subject / predicate / object
source references
source versions
jurisdiction
population / applicability
certainty / uncertainty
status
review history
semantic relations
language representations
reader / disclosure policy
supersession / revocation links
```

## Working knowledge and promoted knowledge

A central design principle is that compiling something does not make it medically authoritative.

```text
working Kristal
    ↓ validate
reviewable Kristal
    ↓ expert review
reviewed Kristal
    ↓ governance decision
promoted Kristal
    ↓ compile
Runtime Pack
```

A working artifact can be useful for research, comparison, testing, or review without being approved for a clinical trust surface.

## Example lifecycle

A new guideline changes the recommended threshold for a test.

1. The new guideline release is imported with source/version metadata.
2. The affected medical assertion is identified.
3. A working Kristal is modified.
4. Automated validation checks structure, provenance, identifiers, and required metadata.
5. Qualified experts review the proposed change.
6. Smart Vote produces one or more reproducible expert readings.
7. A governance authority promotes, rejects, or returns the change for revision.
8. A new knowledge release is compiled.
9. kOA-Linux verifies and activates the Runtime Pack.
10. The previous release remains historically referenceable.

## Runtime Packs

A Runtime Pack is a read-optimized, locally verifiable projection of promoted knowledge.

A MediKristal Runtime Pack may include:

```text
medical graph subset
terminology mappings
protocols
guideline/source metadata
jurisdiction
language artifacts
integrity metadata
release identity
```

The Runtime Pack is not the same thing as the working authoring corpus. This separation allows local systems to consume a stable release while authors and reviewers continue working on the next one.

## Portable knowledge, not central-server dependence

A hospital, clinic, school, research group, or field deployment should be able to carry a verified knowledge package locally rather than depend on a live central server for every query.

This supports:

- offline reference;
- controlled institutional deployment;
- reproducible historical behavior;
- explicit release management;
- local policy overlays;
- safe degradation when networks fail.
