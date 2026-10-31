<!-- Frozen source: https://github.com/Rejean-McCormick/LevelUpDiag-Orgo/blob/79d495e637838784a1e137a7cf83722354f020f2/docs/LEVEL_CONTRACT.md | commit: 79d495e637838784a1e137a7cf83722354f020f2 | SHA-256: 2eacb2740c3f5b680039bf2c8e385d64549f9596c9c455ba020d99f8b80d76f8 -->

# Level contract

A level is a focused diagnostic unit declared in `levelupdiag_manifest.json` and implemented as an importable module exposing:

```python
def run(cfg, report):
    ...
```

The module executes inside its own worker process.

A level should:

- have a stable ID and narrow purpose;
- use config instead of machine-specific constants;
- generate stable dot-separated finding IDs;
- separate message, evidence and recommendation;
- preserve bounded evidence rather than dumping unlimited output;
- distinguish target failure from blocked evidence and diagnostics errors;
- avoid destructive behavior by default;
- never turn a timeout into `PASS`;
- never make a required placeholder look complete.

Verdicts:

| Verdict | Meaning |
|---|---|
| PASS | Check completed and condition satisfied. |
| WARN | Useful evidence found a non-blocking risk. |
| FAIL | Target was checked and a required condition failed. |
| SKIP | Intentionally not executed. |
| BLOCKED | A prerequisite prevented useful execution. |
| PARTIAL | Some evidence exists but is incomplete. |
| ERROR | Diagnostic implementation failed. |
| INFRA_ERROR | Execution infrastructure failed or timed out. |
| CONFIG_ERROR | Diagnostics configuration is invalid. |

A finding ID should identify the contract, not wording or timestamps, e.g. `repository.merge_markers.absent`.
