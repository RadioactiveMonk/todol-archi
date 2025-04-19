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
- [x] `status_constants.py` ➜ utils/status_utils.py
- [x] `log_utils.py` ➜ utils/
- [x] `task_table_utils.py` ➜ utils/
- [x] `csv_utils.py` ➜ utils/
- [x] `path.py` ➜ utils/path_utils.py
- [x] `ui_utils.py` ➜ découpé en plusieurs fichiers spécialisés
- [x] `cached_utils.py` ➜ contenu redispatché dans `category_utils.py` et `ui_theme_utils.py`

---

## ✅ 4. Factoriser les utils pour gérer les constantes

- [x] default_values.py
- [x] category_utils.py
- [x] path_utils.py
- [x] ui_theme_utils.py
- [x] status_utils.py
- [x] db_utils.py
- [x] task_table_utils.py
- [x] task_table_headers_utils.py ➜ intégré dans `task_table_column_utils.py`
- [x] task_table_geometry_utils.py
- [x] task_table_cell_utils.py ➜ contenu migré dans `task_table_column_utils.py`
- [x] task_table_column_utils.py
- [ ] ui_icons_utils.py
- [ ] ui_text_utils.py
- [ ] ui_geometry_utils.py
- [ ] app_utils.py
- [ ] csv_utils.py

- [ ] faire les vérification de paramètres dans les fonctions

---

## ✅ 5. Revoir les usages et les imports

- [x] Vider temporairement `core/__init__.py`
- [x] Corriger les imports à la main au fil des tests
- [ ] (Optionnel) Automatiser le remplacement avec `replace_imports.py`

---

## ✅ 6. Valider tous les modules dans IPython

- [x] `get_path()` / `get_all_paths()`
- [x] `get_categories()` + cache
- [x] `get_available_themes()` + validation
- [x] `status_label()` / `status_color()` / `get_status_ui()`
- [x] db_utils.py
- [x] task_table_column_utils.py (remplace headers/cell/geometry)

---

## ✅ 7. Refactorings appliqués

- [x] Ajout de `open_settings()` dans `helpers/contextmanagers.py`
- [x] Application du modèle “3 blocs” (constantes + dict + fonctions)
- [x] Logs ajoutés sur les fonctions accédant à des fichiers ou caches

---

## ✅ 8. Finalisation

- [ ] Réécrire un `__init__.py` propre pour `core/`
- [ ] Finaliser le remplacement des anciens imports
- [ ] Ajouter des tests unitaires `utils/` (plus tard)
- [ ] Documenter l'organisation des `utils` dans README ou `docs/`

---

## 🛠️ À venir / sous le coude

- [ ] Ajouter `visible`, `tooltip`, ou `flags` dynamiques à `TaskTableColumn`
- [ ] Créer `apply_column_config(view)` pour appliquer les configs aux `QTableView`
- [ ] Étudier un switch vers `PySide6` (officiel Qt) :
    - `poetry remove pyqt6`
    - `poetry add pyside6`
    - remplacer les imports `from PyQt6` → `from PySide6`
- [ ] Explorer une future `LogManager` (structurée)
- [ ] Revoir les cas où l’approche par `dataclass` est pertinente
- [ ] Penser au pattern Strategy pour un futur `export_utils.py`