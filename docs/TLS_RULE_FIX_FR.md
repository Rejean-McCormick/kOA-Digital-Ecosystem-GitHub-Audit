# Correction ciblée des faux positifs TLS — v0.4.1

## Limite corrigée

Dans v0.4.0, l’expression régulière `\bverify\s*=\s*False\b` signalait à tort toute option Python `verify=False` comme « TLS verification may be disabled ».

Les six alertes relevées dans le snapshot `Konnaxion-Capsule-Manager` du 28 octobre 2026 concernaient des paramètres de **vérification des capsules** ou des commentaires/chaînes, pas HTTPS. Elles n’autorisaient aucune conclusion sur la sécurité TLS.

## Nouvelle détection

L’analyse des fichiers Python utilise maintenant `ast.parse`, sans exécuter le code :

- Appels reconnaissables à `requests` ou `httpx` avec `verify=False`, y compris les alias d’import et sessions simples.
- Indicateurs explicites `verify_tls=False`, `verify_ssl=False`, `ssl_verify=False` dans les appels de fonction.
- Appel `ssl._create_unverified_context()`.

Aucun extrait de source ni secret n’est exporté dans les rapports. Une correspondance implique une **revue humaine**, pas une vulnérabilité prouvée. Le détecteur n’est pas une analyse complète de flux de données ; des contournements plus indirects peuvent ne pas être détectés.

## Requalification sans audit complet

Avec `audit.json` issu de v0.4.0, l’onglet **Vérification + ZIP** peut retourner :

- `NOT_A_TLS_BYPASS_API` : la ligne historique contient un motif `verify=False` qui ne correspond pas à un contournement TLS reconnaissable.
- `TLS_BYPASS_API_STILL_PRESENT` : une construction de contournement TLS identifiable par AST est encore présente.

Le snapshot a par ailleurs révélé un problème distinct : `kx_agent/runtime/healthchecks.py` crée un contexte SSL non vérifié lorsque `verify_tls=False`; les valeurs par défaut et deux appels dans `kx_agent/actions.py` désactivent cette vérification, notamment pour les profils HTTPS publics. Il faut examiner et tester le contrat de certificats avant de modifier le projet source. Les versions copiées dans `tools/` ne doivent pas être considérées comme du code actuellement exécuté sans preuve.

La présente correction modifie uniquement l’application d’audit centrale, **pas** `Konnaxion-Capsule-Manager`.
