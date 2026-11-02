<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/08-runtime/02-control-server.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 675820bc837352bc9710df816380e18b70d0632ee49ccd507582033a2fe1a778 -->

# Control server

**Classe : Référence d’implémentation**

Linux Unix socket par défaut : `/run/koa/sockets/koa-spaces.sock`.

Endpoints actuels :

- `GET /health` ;
- `GET /capabilities` ;
- `POST /capabilities/update` ;
- `GET /shell-state` ;
- `POST /manifest/read` ;
- `POST /space/activate` ;
- `POST /space/rollback` ;
- `POST /space/deactivate`.

La request body est bornée. Les refs de manifest sont confinées sous l’artifact root.

Sur Windows, le control socket est désactivé dans le launcher actuel ; Windows sert au smoke test de présentation.
