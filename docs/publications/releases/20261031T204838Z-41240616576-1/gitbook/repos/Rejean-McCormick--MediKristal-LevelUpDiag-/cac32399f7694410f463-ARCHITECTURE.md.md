<!-- Frozen source: https://github.com/Rejean-McCormick/MediKristal-LevelUpDiag-/blob/ce1c0dead57361ef21f9e3fcd8043711124ba41d/docs/ARCHITECTURE.md | commit: ce1c0dead57361ef21f9e3fcd8043711124ba41d | SHA-256: fe67e5fb44f57024634585a64154e58a5a1459760b3caf78065dd4a4e82181dc -->

# Architecture

LevelUpDiag-MediKristal is a standalone adaptation of the LevelUpDiag process-isolated diagnostics frame.

```text
CLI / ZIP launcher
      ↓
manifest + MediKristal profile config
      ↓
campaign scheduler
      ↓  fresh process per level
N* universal levels + MK* target levels
      ↓
read-only target observation / explicit validators / disposable-copy generators
```

The target is normally selected explicitly with `--target`, or extracted temporarily by `run_medikristal_zip.py`. Evidence is written under the target `.levelupdiag/` directory for an extracted repository; ZIP runs copy the finished run outside the temporary extraction.

`N05` executes only declared read-oriented validators. Target-mutating canonical generators are not run in-place: `MK60` copies the repository and regenerates contracts, validation evidence, runtime assets, SBOM and manifest in that disposable copy.

`parallel_safe: false` levels run exclusively. Synthetic blocked results are persisted to `result.json`, including fail-fast paths, so campaign summaries and `latest/` remain complete.
