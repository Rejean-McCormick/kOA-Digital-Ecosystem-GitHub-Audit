<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Troubleshooting | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: af6f9ade2bbed3ec02de5c0f9e6de76bac87bbddbbec45a96d035a6d6eb53669 -->

# Troubleshooting

| Symptom | Likely cause | Safe next step |
| --- | --- | --- |
| Framework version or SHA-256 pin mismatch | Checkout differs from reviewed draft.4 | Obtain the exact source; do not change the hash just to bypass the check |
| `v11-handoff` refusal | Wrong namespace, catalog layer, receipt, or pinned preflight result | Inspect the report/input hashes and use the correct project files |
| Candidate catalog contains a `curated` layer | Incoming Kit candidate mode accepts Wikidata layers only | Review source layers; keep curated layers separate; do not relabel silently |
| `--dik-job` rejected | Candidate flag absent, bad receipt profile/key, or mismatch with the catalog | Use `--kit-import-candidate` in Python or `--kit-candidate yes` in Node, with the original content-addressed directory |
| `--locales` rejected | Handoff requires a graph; reader `check` forbids locale selection | Add `--graph` where required and follow the operation-specific CLI rules |
| `--out` already exists | Deliberate no-clobber behavior | Choose a new report file; do not overwrite old evidence |
| `project` fails | No compatible v7 Surface for the requested projection | Inspect `doctor` target IDs and Context Pack; do not infer missing assertions |
| Local Kompiler URL refused | Not loopback HTTP or includes URL credentials/path | Use a local authorized service such as `http://127.0.0.1:7788` |
| `DO_NOT_REINSTALL_EXISTING_INTEGRATION` | Host checkout already has different owner bridge/panel | Stop; review in Konstellation's repository |
| Rollback refused | Patched files changed after installation | Coordinate manual review with owner; do not erase drift or backup metadata |
| `C3_BLOCKED` / `NOT_EVALUATED` | Collection missing required owner index or checker | Ask the collection owner to supply qualified materials and rerun diagnostic |
| Tests run with missing Framework fixtures | Exact dependency checkout not supplied | Distinguish unit-only tests from integrated tests; do not claim full cross-repo PASS |

See [[CLI-Reference]], [[Prerequisites-and-Pinning]], and [[Qualification-and-Testing]].
