<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal/wiki/Medical-Source-Orchestration | commit: 93fba2ff54b0d2066bc5f3ba8afecf16ec10590c | SHA-256: d6797d3de14d4b1d7bfd2728d4da8759fbd5f65ee44c1c36e8e451d2bb29a594 -->

# Medical Source Orchestration

MediKristal begins from a simple premise: **there is no single “medical database.”** Medicine is already distributed across terminologies, classifications, drug databases, guideline publishers, local protocols, and clinical standards.

MediKristal does not replace those authorities. It creates a traceable semantic layer between them.

## Core source stack

| Source | Primary role in MediKristal | Official link |
|---|---|---|
| **SNOMED CT / SNOMED CT CA** | symptoms, findings, procedures, clinical concepts | [SNOMED International](https://www.snomed.org/) · [Canada Health Infoway](https://infocentral.infoway-inforoute.ca/en/standards/canadian/snomed-ct) |
| **ICD-11** | disease classification and diagnosis grouping | [WHO ICD-11](https://icd.who.int/) |
| **LOINC** | laboratory tests, measurements, observations, panels | [LOINC](https://loinc.org/) |
| **pCLOCD** | Canadian laboratory/observation terminology and mappings | [Canada Health Infoway terminology](https://infocentral.infoway-inforoute.ca/en/standards/canadian/terminology) |
| **CCDD** | normalized Canadian clinical drug terminology | [Canada Health Infoway terminology](https://infocentral.infoway-inforoute.ca/en/standards/canadian/terminology) |
| **Health Canada DPD** | authorized Canadian drug products, DINs, market status, monographs | [Drug Product Database](https://health-products.canada.ca/dpd-bdpp/index-eng.jsp) |
| **RxNorm** | normalized drug concepts and cross-system interoperability | [U.S. NLM RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/) |
| **WHO Guidelines** | global clinical/public-health recommendations | [WHO Guidelines](https://www.who.int/publications/who-guidelines) |
| **NICE / NICE CKS** | evidence-based recommendations and primary-care guidance | [NICE Guidance](https://www.nice.org.uk/guidance) |
| **CDC guidance** | public-health and clinical guidance | [CDC](https://www.cdc.gov/) |
| **Canadian / provincial / institutional guidelines** | jurisdiction-specific clinical practice | source-specific |
| **CQL** | machine-readable clinical quality/decision logic | [Clinical Quality Language](https://cql.hl7.org/) |
| **FHIR Clinical Reasoning** | computable clinical knowledge artifacts | [HL7 FHIR Clinical Reasoning](https://hl7.org/fhir/clinicalreasoning-module.html) |

## Orchestration is not anonymous merging

A normalized MediKristal concept can point to several source identities while keeping them distinct.

```json
{
  "concept_id": "medikristal:condition/example",
  "external_ids": [
    {"system": "SNOMED_CT_CA", "code": "..."},
    {"system": "ICD_11", "code": "..."}
  ]
}
```

The mapping itself is a medical knowledge claim. It therefore needs provenance, versioning, and review.

## Terminology is not protocol

```text
SNOMED / ICD / LOINC / CCDD / DPD / RxNorm
                    ↓
      names, codes, products, classifications

Guidelines / protocols / validated rules
                    ↓
          what should be considered or done
```

A disease code does not establish a diagnostic rule. A drug record does not establish an indication. A test identifier does not establish when the test should be ordered.

MediKristal keeps these layers separate and then links them explicitly.

## Canadian medication orchestration

```text
CCDD
  → normalized Canadian clinical drug concept

Health Canada DPD
  → authorized product / DIN / market status / monograph

RxNorm
  → international or cross-system mapping

Guideline / formulary / protocol
  → indication / contraindication / dose / monitoring
```

No single source replaces the others.

## Diagnostic investigation orchestration

```text
SNOMED CT CA
  → symptom / sign / finding concepts

ICD-11 + SNOMED CT CA
  → disease identity and classification

LOINC + pCLOCD
  → test and observation identities

Guideline / protocol
  → when a test is relevant and how it changes the pathway
```

## Required source metadata

Every imported source should retain at least:

```text
source identifier
publisher / authority
source type
version / release
retrieval date
jurisdiction
language(s)
license / terms
intended MediKristal use
original record/document reference
```

## Trust is purpose-specific

“Official” does not mean “sufficient for every purpose.”

- SNOMED CT may be authoritative for a concept identifier but not for a treatment rule.
- DPD may be authoritative for Canadian product authorization but not for a full therapeutic recommendation.
- a guideline may support a recommendation but only for a defined population and jurisdiction.
- an institutional protocol may be authoritative locally but not globally.

The relevant question is always:

> **Trusted for what, by whom, for which scope, and under which version?**

## Canadian-first reference stack

```text
Clinical concepts      SNOMED CT CA
Diseases               ICD-11 + SNOMED CT CA
Tests / observations   LOINC + pCLOCD
Medications            CCDD + Health Canada DPD
Cross-system mapping   RxNorm
Protocols              Canadian/provincial + WHO/NICE/CDC where applicable
Logic                   JSON initially → CQL/FHIR-compatible artifacts
```

The objective is not maximum database volume. It is a coherent, traceable medical surface.
