<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Workflows | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 46296cf4a834718cd06535f058ce5023e81a4af27d681963940f834df5547336 -->

# End-to-end workflows

## A. Explore without collecting

```text
Open Skope → choose (optional) Kristal → select scope + pass
  → Apply scope settings → Calculate scope
  → inspect Entities / Graph / Convergence / Manifest → stop
```

**Output:** browser-only working preview. No automatic disk job or canonical changes.

## B. Collect a large scope's QIDs

```text
Review recipe (1 direction, explicit PIDs, no strict geography)
  → Start QID collection → inspect status / pause / resume if needed
  → completed → export selected-qids.jsonl and summary
```

**Output:** on-disk identifier inventory for the chosen traversal policy. No original statements.

## C. Extract complete source entities

```text
Completed QID job → choose installed extraction profile
  → Check sources / preflight
  → confirm verified dump + existing locator + reader + free space
  → explicit Start extraction → monitor/pause/resume
  → verify snapshot-manifest and compressed JSONL parts
```

**Output:** preserved original entity JSON and hashes, **not** certified domain truth.

## D. Review existing Catho author identities

```text
Select Catho Kristal → Check roster → explicit author campaign
  → matched / unresolved / P50 work artifacts
  → Identity batches → Analyze unresolved identities
  → inspect suggestions → optional unverified staging
  → Export review CSV → check independent sources
  → validate CSV dry run → reviewer attestation → atomic confirmation
```

**Output:** audit-backed Skope-local identity decisions. No canonical write, no automatic second extraction.

## E. Enrich many v11 Kristals (native CLI)

```text
v11 ZIP → portfolio inventory → bounded/resumable index discovery
  → optional UNVERIFIED draft seeds (never for A-Kristals), or reviewed CSV
  → full Wikidata source extraction with verified dump/locator
  → complete claim proposals + related QID discovery queue
  → separate diK reconciliation / Authoring Kit publication (NOT YET INTEGRATED)
```

**Output:** Skope working evidence and fact proposals. Not an approved crosswalk, new KP/KA or updated Kristal. [Portfolio Enrichment](Portfolio-Enrichment) and [Portfolio CLI Reference](Portfolio-CLI-Reference) describe the native subcommands.

## F. Handoff a reviewed small scope

```text
Non-truncated scope preview → export proposal ZIP
  → inspect selection + source fingerprint + staged/ contents
  → separate human-approved EncyK import/evidence workflow
```

Never use the large-scope **plan** ZIP as if it contained a complete list of entities.

Read the specific guide for each stage: [Scope Explorer](Scope-Explorer), [QID Collection](QID-Collection), [Full-Record Extraction](Full-Record-Extraction), [Batch Identity Review](Batch-Identity-Review), [Exports and Handoff](Exports-and-Handoff), [Portfolio Enrichment](Portfolio-Enrichment).
