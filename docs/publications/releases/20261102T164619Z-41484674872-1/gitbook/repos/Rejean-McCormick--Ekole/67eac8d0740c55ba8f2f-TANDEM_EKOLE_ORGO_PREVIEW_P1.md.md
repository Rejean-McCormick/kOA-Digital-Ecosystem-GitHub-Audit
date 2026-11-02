<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole/blob/0ae6f634e223b7e2fafd68faf6f151730578e490/docs/TANDEM_EKOLE_ORGO_PREVIEW_P1.md | commit: 0ae6f634e223b7e2fafd68faf6f151730578e490 | SHA-256: 67a4f94ee89df066616fd7650da3d87cb13f993d090cc00dcc6721ed05089f9c -->

# Ekole — Tournée Tandem P1 — projection pédagogique synthétique (2026-10-19)

## Statut réel

**Implémenté dans ce correctif :** import contrôlé d'une *projection de démonstration*, lecture seule et **enseignant seulement** via `/api/tandem/preview.json`. Corpus, cours, éditeur et publication existants inchangés. Pas de modification des dépôts frères `ekole-quebec` / `ecole-pastorale`.

**Non implémenté :** connexion OIDC, identité d'élève, permissions distribuées, API Orgo distante, import d'un `Case` / `Task` authentifié, traduction MissionFrame → WorkflowVersion, distribution d'indices à des enfants, preuve scolaire certifiée, notifications, consentement média. Cette étape ne fournit **aucune** de ces garanties.

## Propriété des données (Kontexte ADR-009)

- **Orgo** décide les attributions, dépendances et transitions, y compris pour une mission solo. Ne pas ajouter de « MissionRuntime » à Ekole.
- **Orgo_Worlds** est le control-plane du World et de sa release, sans Task/Case.
- **Ekole** possède les contenus, les affichages pédagogiques et les preuves d'apprentissage, sans inférer une compétence d'un `Task COMPLETED`.
- Le `teacher-preview/1.0` **n'est ni le contrat officiel Orgo, ni un profil IK, ni une preuve signée** : c'est uniquement un modèle Ekole de préparation des vues.

## Essai sûr (aucun réseau externe, aucune DB)

```powershell
cd 'C:\mycode\Ekole\ekole'
py -3 launcher.py --contenu none --tandem-preview tandem/fixtures/fete-sorciere.synthetic.json --verifier
py -3 launcher.py --contenu none --tandem-preview tandem/fixtures/fete-sorciere.synthetic.json
```

Utiliser le lien enseignant affiché dans le terminal, puis ouvrir `http://127.0.0.1:8766/api/tandem/preview.json` dans **la même session enseignant**. Le port public 8765 répond 404 sur cette route. Si `--tandem-preview` n'est pas fourni, le endpoint retourne 404 même à l'enseignant.

L'exemple de la fête est **100 % fictif** : ses UUID ne sont PAS ceux de FakePlant. Aucun fragment de mission n'est poussé à Orgo ou à un enfant; pas d'interactions sortantes. Les tâches sont des placeholders de prévisualisation, et leurs états ne sont pas des états Orgo attestés.

La validation refuse les clés inconnues, références non canoniques, scope tenant/World/release absent ou mal formé, doublons, contenus personnels non prévus, JSON dupliqué, symlinks et payloads excessifs. Elle ne remplace pas une autorisation IAM : **ne jamais exposer ce moteur local à un réseau d'école**.

## Étapes d'intégration ultérieures — hors de cette installation

1. Orgo établit l'authentification effective, la portée tenant/World et la version de workflow; les écoles ne peuvent pas l'inférer d'en-têtes HTTP arbitraires.
2. Le véritable adaptateur reçoit une projection filtrée et autorisée du Work/Case/Task Orgo via un transport authentifié; il vérifie identité, audience, release et fraîcheur.
3. Ekole délivre uniquement les fragments permis à chaque élève connecté selon un mécanisme de session scolaire dédié; le preview enseignant ne peut jamais servir d'API élève.
4. Les preuves d'apprentissage passent par revue et conservation appropriées; elles ne sont jamais égales au statut de Task.
5. Vérifier supervision humaine, séparation de classes, confidentialité, identités mineures et non-publication par défaut des médias.

## Qualification

Test `python -m unittest tests.test_tandem_projection -v` autonome en Python stdlib, sans dépôts frères ni réseau externe. La suite `tests/test_launcher.py` exige les 202 cours du dépôt frère `ekole-quebec`; ne pas la présenter comme validée dans cette tournée si le dépôt n'est pas disponible. 
