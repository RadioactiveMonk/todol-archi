# Checklist — Migration vers `utils/`

Suivre cette checklist étape par étape pour organiser proprement les fichiers de constantes, config, et fonctions utilitaires dans `src/utils/`.

---

## ✅ 1. Brancher proprement

- [x] Créer une branche dédiée : `git checkout -b todol-utils`

---

## ✅ 2. Préparer l’environnement

- [x] Créer le dossier `src/utils/`
- [x] Ajouter un fichier `__init__.py` vide

---

## ✅ 3. Migrer les fichiers existants

- [x] `default_values.py` ➜ utils/
- [x] `status_constants.py` ➜ utils/
- [x] `log_utils.py` (si applicable) ➜ utils/
- [x] `task_table_utils.py` ➜ utils/
- [x] `csv_utils.py` (à évaluer) ➜ utils/
- [x] Autres `*_utils.py` à identifier -> la majorité des fichiers de config ont migrés vers utils/

---

## ✅ 4. Nettoyer et organiser

- [x] Renommer les fichiers si nécessaire (ex: `ui_utils.py`, `db_utils.py`, etc.)
🔄 Étape suivante : Revue ciblée des fichiers

Objectif → passer fichier par fichier, maintenant que tout est centralisé, pour :

    🧹 Nettoyer le code résiduel (non utilisé, dupliqué…)

    🧠 Regrouper ou fusionner si des fichiers se recoupent

    🧰 Ajouter des fonctions de gestion simples et utiles :

        get_columns(), get_column_width(), get_status_label(), etc.

    📦 Poser les bases d’APIs propres pour l’UI, la DB, etc.

    🔁 Plan d’enchaînement proposé :
    Étape	Fichier	Objectif
    1	status_utils.py	Vérifier label, color, et ajouter une fonction get_all_statuses() ?
    2	task_table_utils.py	Encapsuler accès aux colonnes (get_column_index("Edit"))
    3	ui_utils.py	Clarifier les constantes par catégorie (window/dialog/icons...)
    4	path_utils.py	Ajouter des helpers comme get_log_path()
    5	default_values.py	Re-check des usages, alias possibles, éventuel split ?
    6	app_utils.py	Fusion possible avec config.py ? Regrouper les infos globales.
    🔄 Ensuite :

        On scanne le reste (sql_utils, db_utils, etc.) pour voir si on factorise des requêtes ou des modèles communs.

        Et on prépare la transition vers le Bloc C, en te listant ce qu’on pourra "refactorer proprement".

---

## ✅ 5. Identifier les usages

- [ ] Lister les fichiers impactés par les imports déplacés
- [ ] Identifier ce qui doit rester dans `helpers/`

---

## ✅ 6. Modifier les imports

- [ ] Modifier manuellement les imports
- [ ] Utiliser `scripts/replace_imports.py` si utile

---

## ✅ 7. Vérifier le fonctionnement

- [ ] Lancer `todolab` pour tester les imports
- [ ] Tester les fonctions `get_default()`, `status_label()`, etc.
- [ ] Lancer `make test` si disponible

---

## Résultat attendu

- [ ] Tous les fichiers `*_utils.py` centralisés dans `utils/`
- [ ] Structure claire et cohérente
- [ ] Imports fonctionnels dans tout le projet
