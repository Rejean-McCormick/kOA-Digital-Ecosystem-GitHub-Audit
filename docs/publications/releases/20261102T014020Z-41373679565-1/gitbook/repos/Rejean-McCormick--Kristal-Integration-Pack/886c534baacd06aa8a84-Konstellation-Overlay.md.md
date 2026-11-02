<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Integration-Pack/wiki/Konstellation-Overlay | commit: 949de422daed28c0b84684b509e675807ac9c48b | SHA-256: 5907d968fd30c3f2d4b0a5b200de7abb3a35c36909047a72a4bc6cd00a61f269 -->

# Historical Konstellation Overlay

The Integration Pack includes **candidate source overlays** for an older Konstellation + Kompiler integration:

- `overlay/server/integrations/kompiler-bridge.mjs` — local HTTP bridge.
- `overlay/src/components/KompilerPanel.svelte` — optional UI component.
- `overlay/server/integrations/kristal-v11-read-view.mjs` — defensive v11 derived-view consumer, **not installed automatically**.

The legacy bridge provides these Konstellation routes where intentionally installed in a compatible host:

| Method | Route | Role |
| --- | --- | --- |
| GET | `/api/kompiler/capabilities` | Query local backend capabilities |
| POST | `/api/kompiler/validate` | Validate a Kompiler request |
| POST | `/api/kompiler/run` | Execute an authorized query |
| POST | `/api/kompiler/projection` | Request a derived projection |

## Before even considering installation

The provided 2026-10-12 Konstellation snapshot **already had an integration** with different bridge/panel bytes. Its status check returned **`DO_NOT_REINSTALL_EXISTING_INTEGRATION`**. **Do not run `--apply` to replace that existing owner integration.** Coordinate any changes in the Konstellation-owned repository.

On a separately verified **unmodified historical** Konstellation `1.0.0-rc.2` checkout only, the installer can preview, apply and roll back the original overlay. See [[Installer-and-Rollback]].

## Application qualification not included

- No complete Astro/Svelte application build or browser end-to-end test was performed against the supplied host.
- Shared/multiuser integration is **blocked** until reader-specific upstream Kompiler authorization is enforced for every request.
- This Pack neither deploys Konstellation nor creates an alternative fleet or concept navigator.
- The v11 read-view module is not a new public HTTP service.

See [[Legacy-Kompiler-Bridge]] and [[Security-and-Trust-Boundaries]].
