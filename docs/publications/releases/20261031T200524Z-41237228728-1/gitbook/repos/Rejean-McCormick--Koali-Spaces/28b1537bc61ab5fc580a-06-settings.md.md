<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/07-global-surfaces/06-settings.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 87e30d5ab17c5b67464aa3428cabde3addbbcde513d64ae463cafe1f6798f40f -->

# Settings

**Classe : Normatif**

Settings possède uniquement les préférences de présentation admises par le Space : langue, appearance mode, accent, density, surface style, accessibilité, motion et restauration de vue.

Les choix `mode`, `accent`, `density` et `surface_style` sont des préférences personnelles locales. Ils sont persistés séparément de `active-state.json` et ne doivent jamais modifier un activation digest, un receipt, une capability ou un owner manifest. Le bouton de réinitialisation supprime uniquement la préférence locale et revient aux defaults du Space / thème actif.

L'application applique un bootstrap de présentation avant hydratation afin d'éviter un flash light/dark inutile. Ce bootstrap n'accorde aucune autorité : le resolver React revalide ensuite les valeurs contre `appearance_policy` et l'`InterfaceTheme` actif.

N’y pas déplacer : roles, capabilities, governance, network admin, service lifecycle, credentials ou réglages internes des applications.

Les liens vers les réglages propriétaires peuvent ouvrir une surface owner sans en transférer la propriété.
