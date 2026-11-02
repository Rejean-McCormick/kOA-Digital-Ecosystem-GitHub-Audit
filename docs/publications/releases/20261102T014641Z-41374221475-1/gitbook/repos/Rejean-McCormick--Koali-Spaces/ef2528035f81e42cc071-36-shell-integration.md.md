<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/02-host-experience/36-shell-integration.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 132b9548413d88b27e3b24e9b3e3af99792b7f4f4c4e9236f1f40a14fcb32c34 -->

# 36. Shell integration

`GlobalShell` doit devenir sensible au `SurfaceDisplayMode` sans transférer cette logique aux applications hostées.

Pseudo-structure :

```tsx
<SurfaceModeProvider>
  <GlobalShell>
    <SurfaceRenderer />
  </GlobalShell>
</SurfaceModeProvider>
```

En `framed` :

```text
GlobalShell = normal
TopBar = visible
Sidebar = visible selon responsive
MainSurface = normal constraints
```

En `immersive` :

```text
GlobalShell = immersive modifier
TopBar = not rendered/hidden accessibly
Sidebar = not rendered/hidden accessibly
MainSurface = viewport fill
ImmersiveSurfaceControls = visible
```

`LOCK-KS-SURF-116` — **Le shell ne doit pas déléguer à l'iframe la responsabilité de masquer le shell Koali.**

`LOCK-KS-SURF-117` — **Le layout mobile doit obéir aux mêmes modes conceptuels que desktop.**

---
