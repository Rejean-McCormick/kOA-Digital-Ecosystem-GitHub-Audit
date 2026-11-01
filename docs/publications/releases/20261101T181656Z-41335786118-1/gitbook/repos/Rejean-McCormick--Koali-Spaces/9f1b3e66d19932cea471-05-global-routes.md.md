<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/04-shell/05-global-routes.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 753d506bfb9fb57715ae205a04628d382747353c5ed136909f33ee470b7eed87 -->

# Routes globales Koali Spaces

**Classe : Normatif**

Routes globales de base :

| Route | Owner | Rôle |
|---|---|---|
| `/` | Koali Spaces | accueil/context overview |
| `/search` | Koali Spaces | agrégation Search providers |
| `/tasks` | Koali Spaces | agrégation Task providers |
| `/offline` | Koali Spaces | état local/offline |
| `/health` | Koali Spaces | health de présentation |
| `/settings` | Koali Spaces | préférences de présentation |
| `/apps/[moduleId]/...` | route host | surface d’un module/app |

Ces pages globales ne doivent pas devenir des copies des interfaces administratives des owners.
