<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Configuration | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: ee1841f485d5e06b938c3a3088c8af82411bf73649a75d5029ee7f74ed6650e4 -->

# Reader and Server Configuration

## Neutral selector: `config/local-catalog.json`

Minimal example, without a Kristal-specific recipe:

```json
{
  "adapter": "kristal-local-catalog-v10",
  "directory": "C:/mycode/Kristal/locals",
  "readModels": {}
}
```

- `directory` is a **parent directory**, not the path to one Kristal.
- `readModels` is an optional dictionary of read recipes keyed by **subdirectory name**.
- `presentation.kindLabels`, `predicateLabels`, `preferredKind`, and `featuredKinds` are **noncanonical UI preferences**. They do not establish identity, membership, or validation.
- The current French relation-name fallback comes from `src/lib/semantic-display.mjs`. An explicit, independently meaningful configured label can take precedence. Neither mechanism changes original relation IDs or source commitments.
- **No general locale selector or automatic translation pipeline is implied** by the October 17 patch. Names of works in the source language may remain untranslated.
- `node-edge-json/1` model paths are relative to the selected workspace.

The legacy `config/active-reader.json` configures Catho **directly**. It is **not** the configuration used by the neutral `Konstellation.cmd` launcher.

## Main environment variables

| Name | Role |
| --- | --- |
| `KONSTELLATION_BACKEND_CONFIG` | Explicitly select a reader configuration |
| `KONSTELLATION_DEPLOYMENT_PROFILE` | `local`, `lan`, `shared`, or `public` |
| `HOST` | Network interface; `127.0.0.1` recommended for local use |
| `PORT` | HTTP port (`4321` in the provided launcher) |
| `KONSTELLATION_ENABLE_MY_KRISTALS` | Enable the local Manager preview when applicable |
| `KONSTELLATION_FLEET_EXPORT` | Optional Manager inventory export file |
| `KONSTELLATION_FLEET_POLICY` | Explicit access policy for that export |
| `KONSTELLATION_DISCOVERY_CATALOG` | Optional small, projected and filtered Discovery catalog |
| `KONSTELLATION_LOCAL_PRINCIPAL` | Local principal identity |
| `KONSTELLATION_AUTH_TOKENS` | Tokens and scopes for nonlocal profiles |

**Important:** the neutral local selector works **without** a Manager export, which is a separate integration. Local-file readers are restricted to a private local profile and loopback interface.

## Legacy configurations

Examples under `examples/integrations/` include v6, v10 GitHub, SemantiK, local v10, and historical collection adapters. They demonstrate different interfaces: **do not enable all of them at once**, and do not assume a GitHub catalog automatically opens a Kristal's semantic content.

See [[Windows Installation|Windows-Installation]] and [[Security|Security-and-Privacy]].
