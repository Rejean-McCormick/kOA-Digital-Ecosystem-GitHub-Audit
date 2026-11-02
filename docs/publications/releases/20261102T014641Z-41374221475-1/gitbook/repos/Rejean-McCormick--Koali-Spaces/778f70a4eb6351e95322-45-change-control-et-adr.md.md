<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/06-surface-layer/00-governance/45-change-control-et-adr.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 57b9b65502928ffa29d5292f5664b9b40ba54d5a57d3473dbb21d6f2be2c6a4d -->

# 45. Change control et ADR obligatoires

Un ADR est obligatoire pour :

- ajouter un SurfaceKind ;
- modifier la séparation authority/presentation ;
- choisir une stratégie de transport uniforme ;
- introduire un BFF d'expérience ;
- introduire un postMessage bridge métier ;
- introduire Browser Fullscreen comme comportement produit ;
- introduire un SSO global ;
- autoriser une origine réseau non locale dans le renderer de base ;
- permettre des extensions exécutables distantes ;
- modifier la politique de capability ;
- modifier l'externalité UCKK ;
- modifier les exclusions Ame-Artificielle / VotingMachine ;
- faire de Koali le propriétaire d'un nouvel état métier cross-module.

Template minimal :

```markdown
# ADR-KS-SURF-XXXX — Decision
Status: proposed|accepted|rejected|superseded

## Context
## Source contracts
## Lock IDs affected
## Decision
## Security consequences
## Authority consequences
## Compatibility consequences
## Migration
## Tests required
## Rollback
```

---
