# Historical diagnostic consolidation

These prior tools already collect targeted and useful information. The observer **does not replace or execute them**; it imports narrowly selected summary metadata with explicit provenance.

| Tool family | Accepted summary schema | Interpretation boundary |
|---|---|---|
| KonnaxionDiag | `konnaxiondiag.campaign-summary.v4` | Functional/security qualification; signed authorizations and PEP decisions are **not** audited or trusted by this importer |
| KorDiag | `kordiag.summary.v1` | Subject/evidence digests are *declared*, not independently recalculated |
| KristalDiag | `kristaldiag.summary.v1` | External semantic/contract qualification, not a GitHub security pass |
| LevelUpDiag-Orgo | `levelupdiag.campaign-summary.v2` | Orgo acceptance, ecosystem and browser diagnostic results |
| LevelUpDiag-SemantiK | `levelupdiag.campaign-summary.v2` | Semantic architecture/runtime/adversarial checks, not generic SAST |
| LevelUpDiag-Skope | `levelupdiag.campaign-summary.v2` | Catalog/reader/server checks, often local-only and environment-dependent |

These schema names and responsibilities were derived from user-supplied 2026-10-28 snapshots. The code does **not** assert that the snapshots represent current live branches or qualified production versions.

## Import, without executing an old tool

```bash
# Orgo embedded historical summary from the supplied ZIP:
python -m koa_audit import-legacy \
  --tool LevelUpDiag-Orgo \
  --repo Rejean-McCormick/Orgo \
  --input 'LevelUpDiag-Orgo_Code_snapshot(1).zip' \
  --member verification/embedded/summary.json \
  --out .legacy/orgo.json

# KorDiag archive demonstrates the need for explicit target binding.
# Its target Kor is NOT in the 49-repo source inventory; it will be
# out of scope unless the canonical owner inventory includes it.
python -m koa_audit import-legacy \
  --tool KorDiag \
  --repo Rejean-McCormick/Kor \
  --input 'KorDiag_Code_snapshot(1).zip' \
  --member .kordiag/logs/2026-10-03_15-49-49_standard_7861f1ed/summary.json \
  --out .legacy/kor-old.json
```

For KonnaxionDiag, KristalDiag, SemantiK Architect and Skope, point to a genuine generated campaign summary; source code snapshots containing only schema definitions cannot establish completed historical campaigns.

The importer does **not** scan all ZIP entries, follow code executables, make target GitHub writes, validate evidence signatures or call external runtime processes. It reads exactly one explicit JSON member or JSON path and exports a reduced record. It refuses unknown schema/verdicts. Run `local-audit --root C:\mycode --legacy-dir .legacy` to include in the distinct historical section. Do not commit `.legacy/` and do not publish original ZIPs.

## Migration from previous batch-security kit

The earlier `koa-security-batch` kit read current alert counts, and offered **write-capable** `enable --apply` paths. This repository supersedes its **read-only audit** purpose and deliberately drops every write path. Historic batch counts are not imported as current results because they are time-bound; use `local-audit` for fresh local file inspections; it cannot confirm GitHub alert metadata or online advisories.

## Future evidence verification (not in v0.1)

If future independent verifier integration is authorized, implement it **per native evidence contract** (KorDiag subject hashes, LevelUpDiag integrity files, Konnaxion signed authorization, Kristal manifests). Record verification outcome separately from the original native verdict. Never infer cryptographic validity from a digest string alone.
