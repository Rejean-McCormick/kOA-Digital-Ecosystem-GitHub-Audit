<!-- Frozen source: https://github.com/Rejean-McCormick/Orgo-Worlds/blob/c2445db8abf78afcb647f22615ad3b9dd132bde8/docs/TANDEM_EDU_P6_P12_BRIDGE_CONTRACT.md | commit: c2445db8abf78afcb647f22615ad3b9dd132bde8 | SHA-256: 54b653fab02175d5da34493cde6f9859c569172105fe20ec3f8f2815c7b87e88 -->

# Tandem P6–P12 : interface de preuve Worlds côté serveur (non exposée)

`createP6TrustedWorldBridge` est un contrat interne pour le futur adaptateur de transport. Il n'ouvre **aucun port**, n'accepte **aucun en-tête d'identité** et ne crée **aucune route HTTP**. Le `peerContext` doit être construit par une véritable couche mTLS **après** validation du certificat de pair, et jamais à partir d'une entrée du client. La vérification de session et des permissions reste la responsabilité d'Orgo.

La nouvelle interface appelle l'émetteur P5 Ed25519 avec une empreinte de certificat de pair épinglée, un identifiant de service attendu et un contexte frais. Elle refuse l'absence d'authentification, la mauvaise empreinte, un contexte périmé, un acteur incohérent ou une portée World invalide. Cette primitive ne peut pas servir de preuve d'approbation enseignante ni d'admission runtime.

**Non terminé :** serveur mTLS, PKI et rotation des clés, anti-rejeu persistant, source Worlds réellement autoritative, registre d'approbations enseignantes et d'autorisations des participants. Le test de ce dépôt reste une simulation du contrat, sans transport réseau.
