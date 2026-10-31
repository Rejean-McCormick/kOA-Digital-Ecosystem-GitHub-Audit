<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Identity-Reconciliation | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: a246a8014384eafd1b0701a9ec9cfa9af435bc11ff2eca32ae8d267918c606ec -->

# Individual identity reconciliation

Skope 0.14.3 introduced an independent review workflow for unresolved persons in an **existing** Catho author campaign. It does not rerun the campaign or edit its input files.

## Start

Open **Identity Reconciliation** / **Identity batches**, load the latest eligible campaign or supply a 32-character lowercase hexadecimal job ID. A valid source job contains `unresolved-people.jsonl`.

The review UI supports search, filters, pagination, candidate drill-down, French/English labels and contextual P106/P39 information. The reviewer sees whether a proposed QID collides with another already matched roster entry and whether `P31=Q5` holds.

## Decision model

| Action | Meaning |
| --- | --- |
| `confirmed` | Human documentary reviewer attests that the selected QID represents the roster person |
| `deferred` | Needs additional investigation |
| `no_reliable_match` | No supportable identity mapping at this time |
| `clear` | Remove/reset the current decision via the supported review workflow |

For confirmation, supply an explicit QID, reviewer note and documentary evidence URL and meet the API's affirmative confirmation requirements. Check the candidate's identity through **independent sources**; Skope checks URL **structure**, not website content. `P31=Q5` only means that Wikidata classifies the QID as human.

## Audit and isolation

Decisions are kept in a separate SQLite database:

```text
30_working/skope-reconciliation/<job>/decisions.sqlite
```

There is an append-only audit trail and expected-revision checks to prevent stale, concurrent writes. A QID already confirmed for another roster person cannot be silently reused.

**Export:** `GET /api/reconciliation/export.zip?job=<id>` produces a package of review decisions, audit information and roster digest. It does not change the original roster or acquired Wikidata source data.

### Important constraints

- A name match, role similarity or recognition listing does **not** constitute identity proof.
- The reviewer must inspect the **person identity**, not merely whether a source discusses a category or award.
- Decisions are Skope-local working records. They do not create canonical Kristal identities, modify Wikidata or start new extraction.

See [Batch Identity Review](Batch-Identity-Review), [Safety and Provenance](Safety-and-Provenance).
