## 📆 2024-04-10 — Centralisation des fichiers utils

**Objectif** :
Création d’un dossier `utils/` pour regrouper tous les fichiers de constantes, valeurs par défaut, helpers spécialisés, requêtes SQL, etc.

**Actions** :
- Création de `utils/` + `__init__.py`
- Déplacement de :
  - `default_values.py`
  - `status_constants.py` → renommé `status_utils.py`
  - `task_table_utils.py`, `log_utils.py`, `sql_utils.py`, `db_utils.py`
  - `ui_utils.py`, `cached_utils.py`, `path.py` → renommé `path_utils.py`
- Révision complète des noms pour uniformiser : `*_utils.py`
- Nettoyage des imports à venir avec `replace_imports.py`

**Prochaines étapes** :
- Évaluer le déplacement de :
  - `core/config.py` (→ `app_utils.py` ?)
  - `ui/cell_properties.py` (→ `cell_utils.py` ?)
  - `core/api/utils.py` (→ `api_utils.py` ?)
