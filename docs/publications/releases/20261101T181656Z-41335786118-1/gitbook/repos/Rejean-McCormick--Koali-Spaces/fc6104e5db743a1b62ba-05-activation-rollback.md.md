<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/03-space-model/05-activation-rollback.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 1e66b4b5993f2c9a15ed01b6cd4ce925425a1d0bc7c4ac3de77f1312e9ce9e0d -->

# Activation, rollback et deactivation

**Classe : Normatif**

L’activation suit : validate -> resolve refs -> vérifier capabilities -> vérifier assets/offline -> produire état candidat -> bascule atomique -> receipt.

Le control server actuel implémente :

- `POST /space/activate` ;
- `POST /space/rollback` ;
- `POST /space/deactivate`.

Le state conserve une seule previous state pour rollback immédiat. Une stratégie plus riche peut être ajoutée côté owner sans transformer le shell en historique métier.

L’activation d’un Space ne démarre pas automatiquement les applications propriétaires sauf décision explicite via le lifecycle owner/broker.
