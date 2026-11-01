<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/API-Reference | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: 55786e5855a6a5c13361d820ee96a68154b63fec1534b4969813802c8ce0819c -->

# Local HTTP API reference (0.15.0-alpha.1)

Base address: `http://127.0.0.1:8767`. The server uses Python `ThreadingHTTPServer`; it is **not** intended to be exposed publicly. All POST requests expect JSON (maximum request body **65,536 bytes**). Calls with a nonlocal Host, or a mismatched browser `Origin`, are rejected.

**Note:** There are **no portfolio-specific HTTP endpoints** in alpha.1. `skope portfolio` is a CLI workflow; existing browser routes remain dedicated to scopes, extraction and identity campaigns. See [Portfolio CLI Reference](Portfolio-CLI-Reference).

**Examples below are for a trusted local user**, not for public internet services. The exact response shape can contain more fields than listed here.

## Read / discovery routes (GET)

| Endpoint | Required query fields | Purpose |
| --- | --- | --- |
| `/api/meta` | — | Index metadata and source identity status |
| `/api/config` | — | Startup recipe, release, active target, scope folder |
| `/api/diagnostics/reader` | — | Real server Python, reader imports, locator diagnostics |
| `/api/kristals` | — | Available workspace catalog and active target |
| `/api/scope-profiles` | — | Available scope profiles |
| `/api/scope-profiles/catalog` | — | Fully validated rescan, including errors |
| `/api/search` | `q` | Bounded item/name search (server uses a 15-result limit) |
| `/api/node` | `qid` | Indexed entity label, description, aliases |
| `/api/branches` | `root`; optional `direction`, repeated `pid` | First-hop graph branch summary |
| `/api/large/latest` | — | Latest QID job |
| `/api/large/status` | `job` | Persistent QID job state |
| `/api/large/result.zip` | `job` | ZIP for **completed** QID inventory |
| `/api/extract/profiles` | — | Installed extraction profiles |
| `/api/extract/latest` | — | Latest full-record extraction |
| `/api/extract/status` | `job` | Extraction state and evidence path |
| `/api/author-campaign/preview` | `profile` | Catho roster preview for active workspace |
| `/api/author-campaign/latest` | — | Latest author campaign |
| `/api/author-campaign/status` | `job` | Specialized campaign state |
| `/api/reconciliation/people` | optional `job`, `q`, `filter`, `offset`, `limit` | Filter/paginate unresolved roster |
| `/api/reconciliation/detail` | `job`, `person`; optional `qid` | Candidate evidence details |
| `/api/reconciliation/export.zip` | optional `job` | Individual review decision/audit ZIP |
| `/api/reconciliation/batch/status` | optional `job` | Batch analysis status |
| `/api/reconciliation/batch/results` | optional `job`, `bucket`, `offset`, `limit` | Ranked result page |
| `/api/reconciliation/batch/export.zip` | optional `job` | Triage, staged proposals, human-review CSV |

## Actions (POST JSON)

| Endpoint | Main input fields | Effect |
| --- | --- | --- |
| `/api/preview` | Recipe fields at **JSON top level** | Bounded preview, no persistent collection |
| `/api/export` | Recipe fields at **JSON top level** | Proposal/large-plan ZIP, non-canonical |
| `/api/kristals/select` | `id` (or `null`) | Activate/clear local target |
| `/api/kristals/add` | `path` | Add validated local workspace and activate |
| `/api/scopes/open-folder` | `{}` | Open local scopes directory (Windows only) |
| `/api/large/start` | `recipe`; optional `resume` | Start/resume disk-backed QID job |
| `/api/large/pause` | `job` | Request pause |
| `/api/large/open` | `job` | Open results folder (Windows only) |
| `/api/large/copy` | `job` | Put results ZIP file on Windows clipboard |
| `/api/extract/preflight` | `profile`, `source_job` | Validate source and data prerequisites without extracting |
| `/api/extract/start` | `profile`, `source_job`, `confirmed: true`; optional `resume` | Explicit full JSON extraction |
| `/api/extract/pause` | `job` | Request pause |
| `/api/extract/open` | `job` | Open evidence folder (Windows only) |
| `/api/author-campaign/start` | `profile`, `confirmed` | Start explicit Catho orchestration |
| `/api/author-campaign/pause` | `job` | Request pause |
| `/api/author-campaign/resume` | `job`, `confirmed` | Explicitly resume with active workspace checks |
| `/api/reconciliation/decision` | `job`, `person_id`, `decision`, `qid`, `note`, `evidence_url`, `confirmed`, `expected_revision` | One reviewed decision |
| `/api/reconciliation/batch/start` | `job`; optional `force` | Start/recompute offline ranking |
| `/api/reconciliation/batch/stage` | `job`, `selections`, `roster_digest`, `confirmed` | Stage unverified proposals |
| `/api/reconciliation/batch/validate-reviewed` | `job`, `csv` | **Dry run** documented CSV |
| `/api/reconciliation/batch/confirm-reviewed` | `job`, `csv`, `csv_sha256`, `confirmed: true` | Atomic reviewer-attested confirmations |

## Small example: inspect metadata

```bash
curl http://127.0.0.1:8767/api/meta
```

## Small example: preview (no new job)

```bash
curl -X POST http://127.0.0.1:8767/api/preview \
  -H 'Content-Type: application/json' \
  --data-binary @fixtures/demo.recipe.json
```

The sample works only if the root of `fixtures/demo.recipe.json` is represented in your connected finalized index. A supplied JSON profile is not an executable instruction; the backend validates traversal options and rejects unsupported combinations.

## Error and security semantics

Unsupported routes return 404; wrong local Host or disallowed browser Origin return 403. Several validation errors return 400 with `{"error":"..."}`; unexpected internal errors return a 500 with the exception *type*, not full traceback. Download routes return a ZIP content type. A successful HTTP response to a **start** action generally means queued/running, **not** completed.

Do not build remote-facing automation on this unauthenticated loopback API. See [Safety and Provenance](Safety-and-Provenance) and [CLI Reference](CLI-Reference).
