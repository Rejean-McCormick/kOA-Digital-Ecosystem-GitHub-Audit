<!-- Frozen source: https://github.com/Rejean-McCormick/Skope/wiki/Enrichissement-Kristals-FR | commit: 3b1bfff4bd6a0f7956f5aacd45ef525bb5f39125 | SHA-256: c4c17a70d7e12192827fe24637b57e4ce55839591ba7e89985ad95053506091b -->

# Enrichissement des Kristals — Skope 0.15.0-alpha.1

**Skope peut désormais préparer nativement un portefeuille de Kristals v11** pour rechercher des concepts dans la base Wikidata locale, récupérer leurs fiches complètes et générer des propositions de faits. Ce n'est plus un pont logiciel séparé. Le parcours est **en ligne de commande** dans cette version alpha ; le tableau de bord spécialisé n'existe pas encore.

> **Attention :** une correspondance trouvée par nom n'est pas une identité approuvée ; une fiche Wikidata, même complète, n'est pas une preuve indépendante de la véracité des faits ; une proposition Skope n'est pas une assertion canonique Kristal.

## Qui fait quoi ?

| Composant | Responsabilité |
| --- | --- |
| **Skope** | Inventorier les KQ/KP, découvrir les candidats Q/P, extraire les faits Wikidata complets et préparer des propositions |
| **diK** | Qualifier les identités `(namespace, KQ/KP)`, les dictionnaires et les correspondances externes |
| **Authoring Kit** | Valider et publier un nouveau Kristal canonique v11 |

Skope **ne modifie pas** les canons des Kristals et ne crée pas automatiquement de KA. Un QID de Wikidata n'est jamais substitué à une identité KQ.

## Première recherche automatique sur Windows

Depuis le dossier Skope mis à jour, il est possible de glisser un ZIP de Kristals v11 sur `Run_Portfolio_Prepare.cmd`. Le lanceur utilise Python 3.12 et l'index `D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite` préconfiguré. Il écrit les fichiers de travail sous `portfolio-work/`, notamment le CSV des candidats à examiner. Il ne télécharge **pas** de dump et n'intègre aucun fait au canon.

En PowerShell :

```powershell
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
$zip = "C:\Kristals\Kristals-v11-normalized-batch104-candidate.2.zip"
$db = "D:\EncyKlopedia\30_working\wikidata\wikidata.compact.sqlite"
$work = "D:\EncyKlopedia\30_working\skope-portfolios\batch104"

& $py -m skope portfolio prepare --input $zip --work $work --db $db `
  --review-out "$work\candidats.csv" --max-queries 10000 --suggest-draft
& $py -m skope portfolio status --work $work
```

`--suggest-draft` propose seulement des appariements de libellés uniques parmi les **résultats limités** de recherche. Ils restent **non vérifiés**, ne créent pas de `exactMatch` et excluent automatiquement les `A-Kristal`. On peut réexaminer les candidats documentés dans le CSV, puis enregistrer des décisions de travail avec `approve-review`.

## Enrichir réellement avec des faits Wikidata

La recherche par index ne suffit pas : elle ne contient pas les déclarations d'origine avec leurs références et qualificatifs. Pour obtenir cela, il faut utiliser `skope portfolio acquire` avec un profil d'extraction dont le dump original a déjà été vérifié et dont l'index d'accès rapide existe. Ensuite `skope portfolio propose` génère les propositions.

Les déclarations conservent leurs `mainsnak`, `qualifiers`, `references`, `rank`, identifiant de déclaration et provenance. Les propriétés P sans KP approuvé restent externes et les QID connexes sont placés dans une liste de découverte séparée. **Aucun nouvel identifiant KQ/KP n'est inventé par Skope.**

Le fichier d'aide anglais [Portfolio Enrichment](Portfolio-Enrichment) contient les commandes complètes de collecte et la distinction entre les candidats de brouillon (`--include-draft`) et les décisions documentées. Voir aussi [CLI du portefeuille](Portfolio-CLI-Reference).

## Résultat sur le lot de 104 Kristals fourni

L'inventaire testé par Skope 0.15.0-alpha.1 a trouvé **104 projets**, dont **23 avec vocabulaire métier exploitable** : 6 945 libellés français (6 566 KQ, 379 KP). Les **81 autres** ont besoin de nouvelles racines de domaine, de profils ou d'autres sources pour obtenir des amorces de recherche pertinentes. **L'enrichissement sur le dump réel du PC Windows n'a pas encore été exécuté.**

## Limites actuelles

1. Pas de publication automatique par diK ou l'Authoring Kit ; la transaction de transfert reste à développer.
2. Pas de tableau de bord Web pour le portefeuille en alpha.1.
3. Pas de téléchargement automatique de la base Wikidata ni de création d'un nouvel index/locator.
4. Pas encore de benchmark sur le dump Wikidata de production du poste Windows.
5. Les appariements de brouillon ne doivent **jamais** être employés comme équivalences sûres, surtout pour les `A-Kristal`.

Pour commencer : [Démarrage rapide](Demarrage-Rapide-FR), [Commandes du portefeuille](Portfolio-CLI-Reference), [Limites](Known-Limitations).
