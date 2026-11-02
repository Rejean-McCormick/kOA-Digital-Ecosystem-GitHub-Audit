<!-- Frozen source: https://github.com/Rejean-McCormick/Kristal-Authoring-Kit/blob/2a20971ca69828a5168c7a086a14accbbb5cee6f/docs/25_NETTOYAGE_LOCAL.md | commit: 2a20971ca69828a5168c7a086a14accbbb5cee6f | SHA-256: 99f85f4c4aa42cfb3f0a8acccc809be67bd19f6004652aa892bc67f4fd70a011 -->

# Nettoyage local de l'ancien snapshot

Dans le snapshot `znapshot_Kristal-Authoring-Kit_10131043.zip`, deux fichiers
sont des **index générés pour l'archive**, pas des éléments nécessaires au
fonctionnement du Kit :

- `SMARTDUMP_INDEX.txt`
- `SNAPSHOT_INDEX.txt`

La version consolidée n'expédie plus ces deux index devenus périmés après les
modifications. Pour retirer leurs anciennes copies sur le **dossier local déjà
installé**, copiez la nouvelle version dans le dépôt puis double-cliquez
`Nettoyer_Anciens_Fichiers.pyw` **à la racine**. Python avec `tkinter` est
nécessaire. Une interface affiche les fichiers présents et leur statut.

**Protection :** aucune suppression automatique ; sélection manuelle, dialogue
et saisie de `SUPPRIMER` obligatoires. Le nettoyeur ne possède que ces deux
chemins autorisés à la racine et vérifie les SHA-256 exacts de l'archive
précédente. Un fichier manquant, modifié, un dossier, un lien symbolique ou un
chemin extérieur est ignoré. Aucun fichier canonique, workspace ou exemple
n'est ciblé. Il n'y a aucun déplacement de fichiers métier nécessaire.

Le programme fonctionne exclusivement sur le dossier qui contient le `.pyw` :
il ne modifie pas d'autres copies d'Authoring Kit et ne touche pas GitHub.
Si vous souhaitez conserver les anciens index, ne lancez simplement pas la
suppression. Ils ne sont pas chargés par le Kit.
