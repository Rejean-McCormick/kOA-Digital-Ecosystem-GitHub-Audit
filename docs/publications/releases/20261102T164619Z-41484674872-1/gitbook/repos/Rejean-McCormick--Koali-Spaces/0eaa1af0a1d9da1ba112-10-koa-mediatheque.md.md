<!-- Frozen source: https://github.com/Rejean-McCormick/Koali-Spaces/blob/74e321432844bcf102f6671e6f5449afae8acf08/docs/11-integrations/10-koa-mediatheque.md | commit: 74e321432844bcf102f6671e6f5449afae8acf08 | SHA-256: 82eb791ec2f113283a45663f251fc3e524d8d497ac7b47bc0d896e8d495c3c00 -->

# Médiathèque kOA

Médiathèque est une application propriétaire hébergée par Koali, sans transfert d’autorité métier.

## Frontière moteur / données

- `mycode/kOA_Mediatheque/mediatheque` : moteur, schémas, services, interface Streamlit et contrat Koali.
- `mycode/kOA_Mediatheque/mediatheque-blank` : instance locale de données, sélectionnée par défaut pour le workspace intégré.
- Koali ne copie pas les données dans le moteur et ne fusionne pas les deux répertoires.

## Démarrage

Le bootstrap Koali crée l’environnement Python 3.12 du moteur, puis initialise `01_DB/koa_mediatheque.sqlite` seulement si la base n’existe pas. Le processus propriétaire est ensuite lancé avec `KOA_CONTENT_ROOT` pointant vers l’instance sœur. Les démarrages suivants réutilisent la même base et le même stockage.

## Présentation

Le contrat `koa_mediatheque` expose la surface locale `http://127.0.0.1:8501` et sa sonde Streamlit `/_stcore/health`. Koali présente cette surface sous `/apps/koa_mediatheque`; la navigation et les données internes restent sous l’autorité de Médiathèque.

## Kristal

Les bridges et contrats Kristal déjà implémentés dans Médiathèque restent des capacités du produit. Ils ne rendent pas le Kristal Framework propriétaire de Médiathèque et n’importent pas sa théorie dans Koali. Le dépôt Kristal autonome reste `reference_only`.
