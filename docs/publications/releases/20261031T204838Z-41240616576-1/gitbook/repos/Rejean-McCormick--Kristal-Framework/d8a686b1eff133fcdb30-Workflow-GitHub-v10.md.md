<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Framework/wiki/Workflow-GitHub-v10 | commit: cc9ab116371b3a783dfe83ef68182575e8aca83b | SHA-256: 3606b56d02870674c1b20c85bc2627c00a47efe46375ad736250c85a71601ced -->

# Workflow — Local Kristal to GitHub v10

The recommended workflow is **two independent paths**: a mutable reader synchronization path, and an immutable qualified publication path.

## 1. Author and build locally

```bash
python tools/kristal.py check <workspace>
python tools/kristal.py build-v9 <workspace>
python tools/kristal.py build-ai <workspace>
python tools/kristal.py read-surface <workspace> --require-ready
```

The Local Kit retains canon, evidence/source boundaries, v9 state and exact read-surface file selection. A separate `pack-ai` can produce a portable AI capsule if requested; `build-v9` alone does not always generate the AI capsule.

## 2. Synchronize for AI/read access (mutable)

Kristal Manager inventories, validates and synchronizes the exact selected projection into `kristals/<slug>/` within a public or private **collection repository**. It updates the derived `kristals/index.json`; it does not publish a Release or activate a channel.

## 3. Qualify and publish (immutable)

Use GitHub Bootstrap/Setup to prepare and reconcile node infrastructure. Its workflows qualify the pinned source commit, verify the v9 State Snapshot and publication bundle, publish a draft GitHub Release, verify the downloaded assets, and finalize only after the remote check succeeds. Activation, when configured, is **another operation**.

```text
LOCAL KIT:     check → build-v9 → build-ai/read-surface
MANAGER:       Validate → Sync (derived reader projection)
GITHUB SETUP:  qualify → immutable publish → optional activate
KRISTALDIAG:   independent contract / release examination
KOMPILER:      optional read/query/context; no canonical lifecycle
```

## Critical safety checks

- Use an exact 40-character Framework SHA in managed workflows.
- Do not treat a Manager sync commit as publication.
- Do not treat GitHub visibility, a directory listing or validator PASS as epistemic authority.
- An unsupported feature or failed verification must be surfaced, not converted into success.

See [[Toolchain-v10]], [[GitHub-Read-Surfaces-v10]], [[Security-and-Confidentiality-v10]].

*Sources: Authoring Kit `docs/15_GITHUB_AUTHORING_WORKFLOW.md`, `docs/20_TOOLCHAIN_INTEROP.md`; Manager `README.md`; Bootstrap `README.md`.*
