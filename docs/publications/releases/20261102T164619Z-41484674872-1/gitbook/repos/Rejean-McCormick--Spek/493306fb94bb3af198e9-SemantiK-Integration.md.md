<!-- Frozen source: https://github.com/Rejean-McCormick/Spek/wiki/SemantiK-Integration | commit: 4eb78305f912b1e78e9caa5a9afd83b6a9e03253 | SHA-256: 38ea1bf9a1038615c33d1aaddbbf5a1705825ddd76a0775efccda067e644f400 -->

# SemantiK Architect Integration

**SemantiK Architect articulates explicitly selected meaning. Spek composes the supplied results.** SemantiK is not a fact selector or a page-layout engine; Spek is not a natural-language generator.

## Existing Spek importer (shipped 0.5)

The historical prototype fixture is imported using:

```bash
python -m spek import-semantik \
  --input examples/semantik-prototype-minimal.json \
  --mapping examples/semantik-case-mapping.json \
  --out semantik-import.json
```

The importer accepts a documented `cases` shape plus an explicit mapping from case ID to phrase key/language. It preserves supplied request/runtime metadata and marks historical prototype entries **`fixture`**; the importer is not a live SemantiK invocation or a GF/PGF certification.

## Kristal Wiki pipeline (optional integration overlay)

1. Kristal-Manager selects public-eligible assertions; the selection authority remains upstream.
2. An upstream adapter makes an explicit `semantik.kristal-v6.communication-projection/1.0` for SemantiK. The `KristalV6Acl` validates source-reference traceability; it does **not** infer communicative obligations from raw Kristal states.
3. SemantiK's released, pinned runtime realizes short, bounded `CommunicationRequest` obligations. Its `CommunicationResult` includes coverage, source references, deterministic result ID and RuntimeSet identity.
4. The upstream integrator binds reviewed outputs to exact Spek `realization_key` values in `kristal.layout-realizations/0.1`, using `channel: semantik_architect`, `request_id` and `runtime_set_id` where applicable.
5. Spek validates `kristal.layout-article-source/0.1` and composes its chosen typed slots into a **private Wiki Markdown draft**. It does not call SemantiK automatically in the current overlay.

The Kristal adapter described in step 2 consumes a **portable v6 communication projection**, not arbitrary state v9 JSON. A deliberate upstream mapping is required. See [[Kristal Wiki Architecture]] and [[Wiki Draft Workflow]].

## Release boundary

Input labels such as `qualified` and `reviewed` are declarations; Spek does not authenticate SemantiK release evidence, linguistic equivalence, signatures, C1/C2/C3 gates or disclosure rights. Unsupported language/RuntimeSet, missing obligations, incomplete realization keys or absent source references must **block**, never trigger a template or AI prose fallback.

See [SemantiK Architect](https://github.com/Rejean-McCormick/SemantiK-Architect), [[Realizations and Languages]] and [[Epistemic and Security Boundaries]].
