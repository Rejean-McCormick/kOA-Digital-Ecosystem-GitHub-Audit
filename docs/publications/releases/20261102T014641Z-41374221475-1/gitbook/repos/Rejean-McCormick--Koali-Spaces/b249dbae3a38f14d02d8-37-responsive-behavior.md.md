<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/02-host-experience/37-responsive-behavior.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: d3e8e6fe378aa2a2011fef5a231366ffe6bb6e5fdb8fecf522470768280e27f7 -->

# 37. Responsive behavior

Mode framed :

- desktop : sidebar fixe selon le shell existant ;
- mobile : drawer selon le shell existant ;
- application host prend l'espace restant ;
- aucune largeur fixe dépendante de Konnaxion ne doit être codée dans le host.

Mode immersive :

- surface prend `100dvw x 100dvh` conceptuellement ;
- utiliser les unités dynamiques viewport lorsque supportées pour réduire les problèmes de browser chrome mobile ;
- respecter safe areas si nécessaire ;
- le contrôle Retour à Koali doit rester accessible.

`LOCK-KS-SURF-118` — **Pas de dimensions codées pour une seule application.**

---
