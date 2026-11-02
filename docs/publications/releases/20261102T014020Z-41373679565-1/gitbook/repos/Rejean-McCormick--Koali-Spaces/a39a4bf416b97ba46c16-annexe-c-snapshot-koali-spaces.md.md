<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/08-reference/annexe-c-snapshot-koali-spaces.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 22c3980b1ddf8daebc0cc0836391e321294af4303befc1a60fa1a07c2180aed9 -->

# Annexe C — Snapshot Koali Spaces utilisé

Snapshot de référence fourni : généré `2026-09-05T16:03:46.899520`.

Stack documentée :

```text
Next.js 15.5.24
React 18.2.0
Ant Design 5.26.2
@ant-design/pro-components 2.8.10
TypeScript 5.9.x
pnpm 10.20.0
```

Le snapshot indique que Koali Spaces est déjà conçu comme couche d'expérience indépendante, avec shell partagé, module selector, sidebar responsive, top bar, PageShell générique, assets locaux et absence de copie du business Konnaxion.

Ce document étend cette direction en fixant la couche de rendu manquante : **SurfaceRenderer + ApplicationHost + framed/immersive + local surface registration + règles anti-dérive**.
