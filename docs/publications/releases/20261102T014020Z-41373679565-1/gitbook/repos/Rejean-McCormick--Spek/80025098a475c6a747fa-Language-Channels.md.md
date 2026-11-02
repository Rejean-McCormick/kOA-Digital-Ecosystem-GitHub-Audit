<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/Language-Channels | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: a0e0009d7c05b5b11d4333fd2f22c49054ff4875838144e1c02805c124ef60be -->

# Language Channels

Each Spek phrase is supplied by **either SemantiK Architect or preconstructed AI text**, independently of which connector supplied the knowledge. Spek itself does not invent the sentence.

- **SemantiK Architect:** short expressions can carry `request_id` and `runtime_set_id`; `qualified` is reserved for claimed SemantiK runtime qualification. Spek does not authenticate that runtime attestation.
- **Preconstructed AI:** sentences are generated elsewhere, imported locally with `model_id`, `generation_ref`, `prompt_sha256` and `human_review`. They are `fixture` while unreviewed or `reviewed` with an explicit human review reference, never GF-qualified. No SemantiK fields are added.
- **Legacy:** existing manual fixtures and old imported phrase prototype files remain classified `legacy`; no silent provenance upgrade.

```powershell
python -m spek import-ai --input examples/bridge/ai-preconstructed-example.json --base examples/bridge/realizations-without-example-claim.json --out ai-realizations.json
python -m spek build --realizations ai-realizations.json --out dist-ai
```

The sample is **illustrative**, and does not represent a real AI model invocation. It demonstrates the format and the isolation rule only. Review provenance is not independently authenticated by Spek.

See `docs/LANGUAGE_CHANNELS.md` and [Source Explorer](Source-Explorer).

## Policy for Arketype-driven Kristal Wiki

The optional Wiki integration requires **SemantiK-supplied qualified realizations** in its real (non-demonstration) path. Existing AI/manual fixture channels remain useful for other Spek use cases, but must not silently impersonate SemantiK or be promoted to a real Wiki release. Spek checks declared provenance for consistency; a trusted upstream process still verifies that the supplied SemantiK RuntimeSet is genuinely released. See [[SemantiK Integration]] and [[Wiki Draft Workflow]].
