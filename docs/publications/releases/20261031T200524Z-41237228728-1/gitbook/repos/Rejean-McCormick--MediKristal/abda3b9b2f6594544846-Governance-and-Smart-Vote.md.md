<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/Governance-and-Smart-Vote | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: f73a1ffd7565dd1a67287a208b37c5e8d442905e9381b9a121bad7220d9be7c1 -->

# Governance and Smart Vote

> **Status:** intended MediKristal governance architecture. Exact credential rules, thresholds, conflict policies, and promotion authorities still require formal specification and testing.

MediKristal is intended to evolve through **qualified expert participation**, not unrestricted public voting and not autonomous AI authority.

## Basic principle

```text
proposed medical change
        ↓
source evidence + explicit assertion
        ↓
verified relevant professional eligibility
        ↓
review / objections / alternatives
        ↓
reproducible Smart Vote reading(s)
        ↓
explicit governance decision
        ↓
promotion for a defined trust surface
```

## Smart Vote is domain-specific

The people eligible to review a change depend on what is being changed.

| Domain | Examples of relevant expertise |
|---|---|
| diagnosis / clinical reasoning | physicians in the relevant specialty or practice domain |
| medications | physicians, pharmacists, pharmacologists where appropriate |
| laboratory tests | laboratory medicine specialists, relevant clinicians, technologists where appropriate |
| nursing protocols | nurses and relevant clinical experts |
| epidemiology / screening | epidemiologists, public-health physicians, relevant specialists |
| terminology mappings | terminology specialists plus domain clinicians |
| multilingual clinical wording | language specialists plus domain professionals where safety requires it |

A medical license is not universal expertise over every medical question.

## Verified professional eligibility

The system may use evidence such as:

- professional license;
- specialty certification;
- recognized scope of practice;
- institutional role;
- documented domain competence;
- current professional standing.

Credentials establish eligibility evidence; they do not magically make every opinion correct.

## Facts and readings remain separate

MediKristal should preserve individual review events separately from aggregate Smart Vote outputs.

```text
review record ≠ aggregate reading ≠ promotion decision
```

A reproducible Smart Vote reading can expose:

- exact-domain specialists;
- front-line practitioners;
- pharmacists;
- Quebec-certified professionals;
- reviewers with declared conflicts removed;
- other explicit competence lenses.

Divergence between these readings is information and should remain visible to the governance process.

## Reproducibility

A Smart Vote result used in MediKristal should identify:

```text
lens definition + version
eligibility rules
credential / competence snapshot
assertion version
review population
participation rate
calculation method
timestamp
```

Same inputs + same lens should reproduce the same reading.

## Promotion is distinct

```text
Smart Vote output ≠ automatic medical truth
```

A promotion event should record:

- the exact artifact/version promoted;
- jurisdiction/population/trust surface;
- sources considered;
- Smart Vote readings considered;
- unresolved dissent;
- promotion authority/process;
- effective date/version.

## What experts vote on

Smart Vote belongs to the **knowledge-governance lifecycle**. It is not intended to vote on the treatment of an individual patient.

Examples of reviewable objects:

- terminology mappings;
- evidence-backed medical assertions;
- applicability conditions;
- protocol rules;
- guideline transformations;
- language realizations where clinical meaning is at stake;
- supersession/revocation proposals.

## No public condemnation architecture

Professional accountability does not require public spectacle. Review identity, audit evidence, access policy, privacy, and legal duties can be managed within the governed system.

The objective is to improve the corpus and the quality of care, not to create a public reputation game.

## Related ecosystem

Smart Vote belongs to the wider kOA/Konnaxion collective-intelligence architecture. MediKristal narrows that idea to **competence-aware medical knowledge governance**.

- [kOA-Linux Wiki](https://github.com/Rejean-McCormick/kOA-Linux/wiki)
- [Konnaxion Wiki](https://github.com/Rejean-McCormick/Konnaxion/wiki)
- [Collective Intelligence to Governance](https://github.com/Rejean-McCormick/kOA-Linux/wiki/Collective-Intelligence-to-Governance)
