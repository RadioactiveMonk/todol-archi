# Plan de structuration des fichiers `utils/`

Ce document t'aide à organiser proprement les fichiers `*_utils.py`, en regroupant les constantes, fonctions et accès spécifiques à une responsabilité métier ou technique.

---

## 📦 Structure recommandée

Organiser par **responsabilité fonctionnelle**, pas uniquement par type de contenu (constantes / fonctions), ex :

- `default_values.py` → valeurs métier de base (titre, notes, etc.)
- `status_utils.py` → gestion de l’état d’une tâche (label, couleur, etc.)
- `db_utils.py` → requêtes SQL métier (CRUD sur les tâches)
- `sql_schema.py` (optionnel) → requêtes DDL (création/modif de tables)
- `ui_utils.py` → constantes d’UI (titres, dimensions, icônes, etc.)
- `path_utils.py` → chemins vers fichiers, ressources
- `app_utils.py` → infos globales (version, nom app, etc.)
- `cached_utils.py` → accès memoïsés (`get_categories()`, `get_available_themes()`...)

---

## ✅ Pour chaque fichier `xxx_utils.py`

### 1. Constantes
- Les définir clairement (`DEFAULT_THEME`, `APP_THEMES`, `STATUS_LABELS`)
- Préfixer si nécessaire (ex: `DEFAULT_`, `SQL_`, etc.)

### 2. Dictionnaire d’accès (optionnel)
- Ex : `_DEFAULTS`, `CATEGORY_MAP`, `THEME_OPTIONS`

### 3. Fonctions associées
- `get_default()`, `get_all_defaults()`, `status_label()`, etc.
- Utiliser `@lru_cache` si lecture répétée / coûteuse et non dynamique

---

## 🔁 Fusions possibles

- Si deux fichiers ont moins de 3 constantes/fonctions → les fusionner
- Si un fichier devient trop général → scinder

---

## 🔍 Critères pour décider où mettre une constante

| Cas | Emplacement conseillé |
|-----|------------------------|
| Utilisée uniquement dans un `xxx_utils.py` | Mettre dans ce fichier |
| Partagée entre plusieurs fichiers | Extraire dans un `shared_utils.py` ou fichier plus global |
| UI, DB, App... | Préfixer (`ui_`, `db_`, etc.) et structurer par domaine |

---

## 📌 Bonnes pratiques

- Tout fichier `*_utils.py` doit :
  - être autonome
  - exposer uniquement ce qui est utile (`__all__ = [...]` optionnel)
  - rester lisible et testable facilement dans IPython

- Ne jamais mélanger :
  - logique métier (core) avec des helpers transversaux
  - config dynamique avec des constantes statiques
