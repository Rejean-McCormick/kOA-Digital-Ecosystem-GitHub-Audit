<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Batch-Identity-Review | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: ca9aefe228117c58c85e112676ab444471c00508000be78785426f86abd44dfc -->

# Batch identity triage and reviewed CSV confirmation (0.14.4)

**Goal:** inspect many unresolved Catho identities quickly while keeping the line between **suggestion**, **unverified proposal**, and **reviewer-attested confirmation** explicit.

## Stage 1 — offline analysis

Choose an existing Catho campaign and click **Analyze unresolved identities**. Skope reads its `unresolved-people.jsonl` and the compact SQLite index; it does **not** fetch web pages or re-extract original Wikidata.

Candidates are drawn from the campaign's existing QID suggestions, or — when empty — a bounded name lookup (up to six search matches). Each person has at most **45** ranked candidates. Rules consider exact/partial names, listed aliases, selected description/occupation hints and collisions with previously matched entries; non-human QIDs are ineligible.

- `suggested`: top eligible candidate with score ≥ **52** and ≥ **20** points lead over the next candidate (if any).
- `needs_review`: eligible candidate(s), but no such clear suggestion.
- `no_viable_candidate`: no eligible human, collision-free candidate.

**A score is a heuristic points total, not a calibrated probability, external endorsement or verified identity.** The religious vocabulary/context signals are classification aids, not a person's beliefs or doctrinal status.

## Stage 2 — optional proposal staging

Select ranked suggestions and choose **Stage selected as unverified proposals**. This records an isolated research shortlist and a staging audit entry. It does **not** confirm identity or start source acquisition. Job/roster digest checks prevent carrying forward a stale context.

## Stage 3 — evidence export and human review

Click **Export batch CSV + evidence ZIP**. The ZIP includes:

```text
manifest.json
triage.json
staged-proposals.jsonl
human-review-template.csv
```

The CSV includes `person_id`, `suggested_qid`, `review_decision`, `documentary_identity_url`, `reason_for_confirmation`, `expected_revision` and contextual columns. To confirm, the human reviewer must inspect independent identity evidence, set `review_decision=confirm`, insert a real HTTP(S) identity source URL and a substantive reason (15–3000 characters), leaving non-confirmations blank. Do **not** mark every ranked suggestion `confirm` blindly.

## Stage 4 — dry run, then atomic commit

1. Import reviewed CSV (maximum **55 KB**, no more than **200** confirmations per batch).
2. Click **Validate CSV — dry run**. This validates format, candidate QID, P31=Q5, duplicate/collision rules, documentary field lengths and current revisions **without writing decisions**.
3. The API returns a `csv_sha256`; any CSV change after validation requires a new dry run.
4. Read and affirm the attestation that **you** verified the documentary sources. Skope cannot read/verify those pages.
5. Click **Confirm documented identities in batch**. Skope checks revisions and conflicting QIDs again, then inserts all valid decisions and audit entries in **one SQLite transaction** (all or nothing).

## Persistent outputs and limitations

```text
30_working/skope-reconciliation/<job>/
  batch-analysis.json
  batch-progress.json
  decisions.sqlite
```

Analysis progress can be restarted after server interruption. The report is considered current only while its roster SHA-256 matches the original unresolved roster.

**No source roster mutation, no canonical Kristal write, no automatic work acquisition and no online source inspection** occurs in these actions. See [Identity Reconciliation](Identity-Reconciliation), [Data Formats](Data-Formats) and [Safety and Provenance](Safety-and-Provenance).
