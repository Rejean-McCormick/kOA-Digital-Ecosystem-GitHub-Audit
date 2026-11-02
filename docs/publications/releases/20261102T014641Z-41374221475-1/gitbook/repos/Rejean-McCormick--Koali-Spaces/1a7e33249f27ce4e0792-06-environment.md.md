<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/08-runtime/06-environment.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: bed26be53cf83101885bac475e9e2ff39ed1bced1a7dc02756082bbd9e6698ff -->

# Variables d’environnement runtime

**Classe : Référence**

| Variable | Default | Rôle |
|---|---|---|
| `KOALI_SPACES_BIND` | `127.0.0.1` | bind presentation |
| `KOALI_SPACES_PORT` | `4173` | port presentation |
| `KOALI_SPACES_SOCKET` | `/run/koa/sockets/koa-spaces.sock` | control socket Linux |
| `KOALI_SPACES_STATE_ROOT` | `/var/lib/koa/integrations/koa-spaces` | active state |
| `KOALI_SPACES_ARTIFACT_ROOT` | `/usr/lib/koa/integrations/koa-spaces` | admitted artifacts |
| `KOALI_SPACES_APP_ROOT` | runtime root | Next app root |
| `KOALI_SPACES_DEV_FALLBACK` | dev implicit | autorise fallback de développement |
| `KOALI_SPACES_SURFACE_REGISTRY` | `<stateRoot>/surface-runtime.json` | override du registre runtime Surface Layer Koali |
| `KOALI_SPACES_FRAME_SRC` | vide | allowlist d’origines `frame-src` additionnelles, séparées par espaces, évaluée au build Next |

`KOALI_SPACES_FRAME_SRC` n’est pas un registre d’autorisation applicatif. Une origine doit aussi être résolue par le registre runtime serveur avant qu’un descriptor public puisse la fournir au navigateur.

Toutes les nouvelles variables Koali Spaces utilisent le préfixe `KOALI_SPACES_`.
