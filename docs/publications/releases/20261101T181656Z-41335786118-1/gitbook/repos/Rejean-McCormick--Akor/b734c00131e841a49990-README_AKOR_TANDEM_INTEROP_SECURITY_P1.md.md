<!-- Frozen source: https://github.com/Rejean-McCormick/Akor/blob/cc86fccc9dd9a73aec937486a7e3cfbc917d0fdb/README_AKOR_TANDEM_INTEROP_SECURITY_P1.md | commit: cc86fccc9dd9a73aec937486a7e3cfbc917d0fdb | SHA-256: 1fd727a13d94d9f44eb70ec2fd131f47ac3495c1e432424aae32980bfd40501f -->

# Akor Tandem P1 — verification locale, aucune activation Orgo

Extraire ce ZIP **dans la racine du depot Akor** contenant `src/akor/preflight.py`.
Dans PowerShell : executer `PREVIEW_AKOR_TANDEM_INTEROP_P1.cmd`, `INSTALL_AKOR_TANDEM_INTEROP_P1.cmd`, puis `VERIFY_AKOR_TANDEM_INTEROP_P1.cmd`.
En cas de besoin : `ROLLBACK_AKOR_TANDEM_INTEROP_P1.cmd`.

Le controle Tandem exige Kontexte, Kompose V3 et Ekole P1 installs localement.
Le test de l'installateur est autonome et lecture seule. Les 7 tests historiques impliquant six autres depots sont ignores tant que ces depots ne sont pas reunis dans la copie isolee. Le controle reel croise les validateurs de Kompose et Ekole; voir `docs/TANDEM_AKOR_INTEROP_SECURITY_P1.md`.

Le programme ajoute un **controle read-only**, sans modifier le preflight Boulangerie existant ni aucun autre depot, base de donnees, service ou VPS.
