<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/02-host-experience/08-etat-mode-navigation.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 94d066cf7de47b9a319a9ffe85745852b80dc66190929a39de725f7d5271661c -->

# 8. État de mode et navigation navigateur

Le mode d'affichage est un état Koali.

Recommandation normative :

```ts
interface SurfaceViewState {
  moduleId: string;
  displayMode: "framed" | "immersive";
}
```

L'état MAY être persisté par session utilisateur locale. Il MUST NOT être stocké dans le système métier du module.

La navigation Back/Forward du navigateur SHOULD préserver une expérience cohérente. La route métier du module et le display mode ne doivent pas être confondus.

`LOCK-KS-SURF-028` — **Koali ne modifie pas la route interne d'un module uniquement pour entrer/sortir du mode immersive.**

`LOCK-KS-SURF-029` — **Changer de module sort du mode immersive du module précédent.** Le nouveau module reprend son mode par défaut ou sa préférence propre, jamais un mode hérité accidentellement d'un autre module.

---
