# Contracts and confidence boundaries

- `koa_audit.local_observation.v1`: offline file/workflow heuristic observation, with exact working-folder locations and coverage caveats. Schema: `schemas/local-observation.schema.json`. Does not attest to CI success, to CVE absence, or to CodeQL execution.
- `koa_audit.legacy_record.v1`: historical specialist diagnostic summaries, bound explicitly to a repository. Schema: `schemas/legacy-record.schema.json`.
- `koa_audit.observation.v1`: **legacy optional remote API** observations; no longer used by the Windows launcher or scheduled automation. Schema: `schemas/observation.schema.json`.

These are observation formats only, never release or authorization contracts. An `INSPECTED_NO_PATTERN_MATCH` value is not a security PASS, and an `UNKNOWN`/`PARTIAL` cannot be converted to zero vulnerabilities.
