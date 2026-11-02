<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK_Runtime_Orchestrator/blob/4e6a4fb58af8f8dbe3acc2bdde50701b2b482b87/docs/MIGRATION_FROM_EMBEDDED.md | commit: 4e6a4fb58af8f8dbe3acc2bdde50701b2b482b87 | SHA-256: 40000154b8fc0b078c2560234f871c2d7c1e36d3b8cd03f9d8ced5f78c39158e -->

# Migration from the embedded SA prototype

If the earlier embedded runtime-pipeline prototype was copied into SemantiK Architect, remove these paths from the SA repository after this independent repository is adopted:

```text
tools/build_sa_runtime.py
src/semantik_architect/runtime_pipeline/
tests/runtime_pipeline/
docs/reference/RUNTIME_PIPELINE.md
runtime_pipeline.config.example.json
RUNTIME_PIPELINE_VALIDATION.md
RUNTIME_PIPELINE_SHA256SUMS.txt
```

Do **not** remove SA-owned runtime contracts, conformance code, RuntimeReleaseValidator, runtime adapters, schemas, or `tools/build_runtime_manifest.py`. Those remain SemantiK Architect responsibilities.
