## 📆 2024-04-10 — Centralisation des fichiers utils

**Objectif** :
Création d’un dossier `utils/` pour regrouper tous les fichiers de constantes, valeurs par défaut, helpers spécialisés, requêtes SQL, etc.

**Actions** :
- Création de `utils/` + `__init__.py`
- Révision complète des noms pour uniformiser : `*_utils.py`
- Nettoyage des imports à venir avec `replace_imports.py`

---

## 📆 2025-04-12 — Validation des premiers `utils` + tests IPython

**Objectif :**
- Vérifier la bonne mise en place des nouveaux fichiers `utils/` de manière indépendante et testable

**Actions réalisées :**
- 🔧 Vidage temporaire de `core/__init__.py` pour permettre l'import modulaire
- 🧪 Tests manuels via `PYTHONPATH=src ipython` :
  - `get_path()` / `get_all_paths()` → OK
  - `get_categories()` + `lru_cache` + `open_settings()` → OK
  - `get_available_themes()` + `is_theme_available()` → OK
  - `get_status_ui()`, `status_label()`, `status_color()` → OK
- ✅ Ajout de logs pour la traçabilité
- ♻️ Quelques imports corrigés au fil des tests

**Résultat :**
- Tous les `utils` testés fonctionnent correctement en isolation
- Cache fonctionnel et contrôlable (`cache_info`, `cache_clear`)
- Chemins, constantes et accès fichiers centralisés et validés
