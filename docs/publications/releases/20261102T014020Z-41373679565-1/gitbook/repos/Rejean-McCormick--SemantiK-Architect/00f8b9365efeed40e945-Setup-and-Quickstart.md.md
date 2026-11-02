<!-- Frozen source: https://github.com/Rejean-McCormick/SemantiK-Architect/wiki/Setup-and-Quickstart | commit: f187a43fc9540ce7d443ff4d2ab26dfdc7a48bfe | SHA-256: 9952643dca65792926bb0fc8dad4c69485bc40da09151886e73999161f0d622b -->

# Setup & Quickstart

## Requirements

- Python 3.12+
- the SemantiK Architect package/repository
- for real rendering: a released language RuntimeSet and the GF Python binding compatible with its PGF artifact

The core can validate requests and inspect configuration without a language RuntimeSet.

## Install from source

```bash
python -m pip install -e . --no-build-isolation
```

Or install the built wheel:

```bash
python -m pip install semantik_architect-1.0.0-py3-none-any.whl
```

GF support is an optional package extra/environment dependency where available.

## Validate a request

```bash
semantik-architect validate-request examples/orgo_fr_request.json
```

This does not require a released language runtime.

## Configure runtimes

Place immutable RuntimeSets beneath a runtime root:

```text
runtime/
  activation.json                  # optional
  <runtime-set>/
    runtime.manifest.json
    capabilities.json
    bridge.json
    lexicon.json
    grammar.pgf
    profile-*.json
    conformance-*.json
```

Validate one:

```bash
semantik-architect --runtime-root runtime validate-runtime <runtime-set-id>
```

## Render

```bash
semantik-architect --runtime-root runtime render request.json
```

If the requested language/profile is not released or the RuntimeSet fails integrity/conformance checks, SA fails explicitly.
