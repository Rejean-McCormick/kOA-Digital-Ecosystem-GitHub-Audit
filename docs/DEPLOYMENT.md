# Installation locale

Python 3.11+, Tkinter et, facultativement, Git disponible dans le PATH pour lire HEAD/origin. Décompresser le ZIP, lancer `kOA_GitHub_Audit_Launcher.pyw`, choisir la racine des copies locales des dépôts Git. Aucune GitHub App ni jeton requis.

Le scan s'exécute uniquement sur la machine locale. GitHub Actions CI du dépôt central exécute seulement les **tests unitaires de l'outil** ; cela ne donne pas accès à vos fichiers locaux. Un ancien workflow périodique GitHub API nécessitant des credentials a été retiré de la version locale.
