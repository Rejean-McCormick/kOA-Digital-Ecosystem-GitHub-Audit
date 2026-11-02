<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/08-runtime/01-presentation-server.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 4805e222179d94f09c09ca688b636693a7ebc8847b43fc1045a3e8dad003afb3 -->

# Presentation server

**Classe : Référence d’implémentation**

Defaults : bind `127.0.0.1`, port `4173`.

Production : `dist/runtime/server/main.mjs` lance `dist/runtime/server.js` avec `NODE_ENV=production`, `HOSTNAME` et `PORT`.

Le presentation server sert shell, routes globales, API shell-state et assets locaux.

Il n’est pas un backend métier général.
