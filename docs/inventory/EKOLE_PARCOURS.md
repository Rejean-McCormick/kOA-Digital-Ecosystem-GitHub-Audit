# kOA Graph — parcours focalisé autour d’eKole

**Source étudiée :** archive locale `ekole(3).zip` reçue le 1er novembre 2026. Les fichiers sources cités ci-dessous sont des instantanés ; la présence d’une interface dans un dépôt ne signifie pas une qualification de bout en bout.

## Ligne principale : contenu → eKole → travail → revue

1. **Pack de cours sélectionné.** `ekole-quebec` (202 cours, six parcours dans ce snapshot) ou `ecole-pastorale` (32 cours, sept parcours ; prototype non approuvé). Les contenus sont dans des dépôts distincts, non fusionnés. L'appartenance d'un contenu au pack ne certifie ni les acquis ni l'autorisation de publier.
2. **eKole Core.** Moteur commun neutre (`pack.json`, `cours/*.json`, API JSON), indépendant de la religion et du programme. Le service et ses éditeurs sont locaux ; lecture seule par défaut.
3. **Interfaces d’apprentissage et d’enseignement.** Portail apprenant et vue enseignant/éditeur. La personnalisation des rôles et des visuels n'accorde aucune permission opérationnelle.
4. **Travail de l’apprenant.** Une activité ou une tâche accomplie ne signifie pas une compétence maîtrisée. Les traces pédagogiques appartiennent au domaine eKole.
5. **Revue éducative.** Revue par l’enseignant, avec données protégées. Le workflow complet de preuves/notations authentifiées ne doit pas être présenté comme intégralement qualifié.

## Circuits entourant eKole

| Circuit | Propriétaire / fonction | État établi par les fichiers | Source dans l’archive |
|---|---|---|---|
| **Québec** | Pack de contenu autonome | 202 cours candidats ; aucune certification ministérielle | `ekole/README.md`, `ekole/docs/Integration-Verification-2026-10-27.md`, `ekole-quebec/README.md` |
| **Pastorale** | Pack de contenu autonome, sources Kristal v11 draft | 32 cours, sept parcours, non approuvé pour publication publique ou ecclésiale | `ecole-pastorale/README.md`, `docs/DECISIONS_ARCHITECTURE.md` |
| **Kristal** | Sources, états sémantiques et projections | Provenance et version nécessaires ; la projection n'établit pas la maîtrise | `ecole-pastorale/README.md`, `docs/DECISIONS_ARCHITECTURE.md` |
| **Kontexte** | Scénarios, situations, intentions de rôles | Export synthétique `ekole.tandem-teacher-preview/1.0`, sans élève ni API Orgo réelle | `Kontexte/docs/ekole-orgo/TANDEM_P1_EKOLE_PREVIEW_EXPORT.md` |
| **Kompose** | Vérification de plans et aperçus | Contrôle local, synthétique, sans autorisation | `Kompose.wiki/Ekole-P1-Preview.md` |
| **Akor** | Préflight et jointures du tandem éducatif | P2 produit une intention de revue; P3 une demande `AWAITING_SERVER_VERIFICATION`. Ne crée pas de tâches Orgo réelles | `Akor/docs/STATUS.md`, `Akor/docs/TANDEM_EDUCATION_P3_AUTHORITY_REQUEST.md` |
| **Orgo / Orgo_Worlds** | État opérationnel vs contexte World/Release | Orgo est moteur canonique des missions interactives même solo ; Worlds possède WorldRelease ; **intégration cible**, pas de runtime complet qualifié | `Kontexte/docs/ekole-orgo/02_ARCHITECTURE_CIBLE.md` |
| **Aperçu enseignant** | eKole | Endpoint synthétique et local désactivé par défaut ; pas de token, d'identité d'élève ni de grade | `ekole/docs/TANDEM_EKOLE_ORGO_PREVIEW_P1.md` |
| **Personnages** | Catalogue, rôles et couche visuelle | Les archives Kolor/Karacter ont leurs propres responsabilités. Leur relation directe avec eKole reste à qualifier | `ekole/docs/PERSONNAGES_ALIGNMENT.md`, `Kolor/README.md`, `Karacter/README.md` |
| **Inkuisite** | Banque d’items, examen et correction distincts | Import eKole en candidats ; scores et corrigés privés ; pas de synchronisation officielle ou Moodle | `Inkuisite/docs/04_INTEGRATIONS.md` |

## Frontières indispensables

- `Ekole` possède les surfaces pédagogiques et les contenus effectivement chargés, **pas** les tâches Orgo.
- `Orgo` possède `Work/Case/Task/Signal` pour une mission interactive authentifiée ; `Orgo_Worlds` possède les Worlds et leurs releases.
- Un `teacher-preview/1.0` et un synthetically valid `authority: orgo` ne constituent **jamais** une autorisation ou une tâche authentifiée.
- Terminer une tâche Orgo ne prouve **jamais** une compétence scolaire ; il faut une revue et des preuves pédagogiques spécifiques.
- Les corpus Québec et Pastorale restent distincts ; aucun des deux n'autorise la publication de l'autre.
- **Ne pas exposer de données d’enfants** : le graphe contient des noms de systèmes, des contrats et des sources publiques, aucune identité ou résultat privé.
- `ekole-quebec`, Inkuisite, Karacter et Kolor ne sont pas tous présents dans l'inventaire architectural de référence de 49 dépôts : le graphe les représente à titre **d’artefacts/candidats sans identité propriétaire canonique**, en attendant leur admission. Ne pas inventer de `repo` dans le fichier du graphe.

## English

The focal spine is **selected content pack → neutral eKole Core → learner/teacher interfaces → learning work → human pedagogical review**. The surrounding interactive-mission circuit involves **Kontexte → Kompose → Akor → Orgo**, with `Orgo_Worlds` owning WorldRelease context. P1 teacher previews and P2/P3 review/authority requests are synthetic and are **not** proof of a working classroom-integrated Orgo runtime. Quebec and Pastorale packs are separate, with no official curricular or ecclesiastical approval implied. Inkuisite, Karacter and Kolor are shown as candidate/optional relationships until authoritative graph admissions and qualified integration evidence exist.
