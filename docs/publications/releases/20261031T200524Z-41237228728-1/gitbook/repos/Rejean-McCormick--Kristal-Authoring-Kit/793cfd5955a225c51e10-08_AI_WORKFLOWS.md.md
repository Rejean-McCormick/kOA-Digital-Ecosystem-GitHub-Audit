<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Authoring-Kit/blob/2a20971ca69828a5168c7a086a14accbbb5cee6f/docs/08_AI_WORKFLOWS.md | commit: 2a20971ca69828a5168c7a086a14accbbb5cee6f | SHA-256: 305f94c29703e0be08b503ed85689041a6cf7913cce17fcdfb0486efa56adcdd -->

# 08 — Optional AI workflows

## Two uses

1. **AI-assisted authoring:** follow `AGENTS.md`; AI changes remain proposed until the relevant domain authority admits them.
2. **AI-assisted reading:** Kompiler or `pack-ai` consumes a noncanonical, derived reader model, with source references and declared coverage.

## Normal local workflow

```bash
python tools/kristal.py check PATH
python tools/kristal.py build-v9 PATH
```

No AI output is created by the second command unless `--with-ai` is given.

## When AI helps

Use `build-ai`, `check-ai`, `read-surface`, and `pack-ai` only when a reader projection is needed and when access policies permit its creation or transport. A stale AI file does not become ready merely because it exists.

## Kompiler

Kompiler is an optional read-only retrieval/context consumer. It cannot admit claims, edit canon or authorize publication.

## Hosted v10

Manager may synchronize only the verified, permitted read surface with independent owner authorization for disclosure. Publishing a network release remains a separate qualified process.
