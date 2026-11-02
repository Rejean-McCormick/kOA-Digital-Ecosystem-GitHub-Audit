<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/09-security/00-security-model.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 79855bbb4720faacc2a5be334394c80cba7a243defc6d4e4f0e1ce5fd73bfc8e -->

# Modèle de sécurité

**Classe : Normatif**

Koali Spaces applique least exposure et fail closed.

Principes : loopback presentation, control socket local, paths confinés, CSP, no remote runtime assets pour le shell offline, capability projection non autoritative, absence de secrets dans artifacts de présentation.

L’hébergement d’applications ajoute une frontière browser qui doit suivre le threat model Surface Layer v1.1.
