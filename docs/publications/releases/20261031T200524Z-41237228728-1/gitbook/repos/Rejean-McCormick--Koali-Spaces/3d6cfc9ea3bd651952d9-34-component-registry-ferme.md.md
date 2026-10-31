<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/03-routing-and-registry/34-component-registry-ferme.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 9326af302450628dd802fcf74b5903fbfd8097d240cfb987e03d8cb0e68e1142 -->

# 34. Component registry fermé

Pour `registered_component_surface` :

```ts
const REGISTERED_SURFACES = {
  // explicit imports only
} as const;
```

Interdit :

```ts
import(`/components/${manifest.componentName}`)
```

si `componentName` peut être fourni librement par un manifest non compilé/allowlisté.

`LOCK-KS-SURF-112` — **Pas d'import dynamique arbitraire à partir d'un nom fourni par une définition de Space ou un manifest.**

`LOCK-KS-SURF-113` — **Chaque composant exécutable est présent dans la build locale et enregistré explicitement.**

---
