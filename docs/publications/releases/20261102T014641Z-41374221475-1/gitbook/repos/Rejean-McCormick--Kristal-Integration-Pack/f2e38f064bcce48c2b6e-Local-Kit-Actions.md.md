<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Local-Kit-Actions | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: bbdc851a0105a64fc3f8b9836aa98d08acfd840d2a2d88899155249ba499adff -->

# Guarded Local Kit Actions

The Node CLI's historical `author` command delegates a **small allowlist** of actions to an existing Python Local Kit tool. It does not bundle or replace the Authoring Kit runtime.

## Actions

| Action | Default behavior |
| --- | --- |
| `inspect` | Read-only |
| `status` | Read-only |
| `check` | Read-only |
| `read-surface` | Read-only; forwarded with `--require-ready` |
| `build-v9` | Write-capable; explicitly gated |
| `publish-v9` | Write-capable; explicitly gated |

```bash
node tools/kristal-bridge.mjs author \
  --action inspect --tool /kit/tools/tool.py --workspace /kit/workspace
```

For `build-v9` and `publish-v9`, **both** are required: environment variable `KRISTAL_ALLOW_WRITE=1` **and** `--confirm` equal to the specific action. These flags prevent accidental writes; they do **not** establish owner authorization, domain correctness or full rollback qualification.

The new v11 Authoring Kit actions (`import-dik-catalog`, `select-v11-catalog`, `recover-v11`) are **not** part of the Pack's historical `author` allowlist. Execute them separately in the **Authoring Kit** under the project's review procedure.

See [[diK-to-Authoring-Kit-Handoff]] and [[Architecture-and-Ownership]].
