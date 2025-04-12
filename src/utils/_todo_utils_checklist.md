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
- [ ] Factoriser les utils pour gérer les constantes
    - [x] category_utils.py
    - [x] path_utils.py
    - [x] ui_theme_utils.py
    - [x] status_utils.py
