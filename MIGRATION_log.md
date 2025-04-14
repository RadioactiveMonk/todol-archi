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

## 📆 2025-04-13 — Ajout de db_utils.py + helpers SQL dynamiques

**Objectif :**
- Extraire les requêtes SQL statiques de la classe AskDB - Créer une base de helpers SQL réutilisables et testables 

**Actions réalisées :**
- [x] Création de utils/db_utils.py 
- [x] Ajout de toutes les requêtes SQL liées à la table tasks 
- [x] Implémentation de get_query() et is_query() 
- [x] Helpers dynamiques : - build_where_clause() (avec retour tuple clause +
args) - build_update_query() (génération de requête UPDATE et valeurs) 
- [x] Tests interactifs dans IPython sur tous les helpers 
- [x] Validation de la compatibilité avec cursor.execute(...) 

**Résultat :** 
- db.py (ex ask_db.py) sera allégé et plus lisible - La couche SQL est désormais centralisée, modulaire et testé

## 📆 2025-04-14 — Intégration de db_utils dans DB + validation IPython

**Objectif :**
- Refactorer `update_task()` avec `build_update_query()`
- Ajouter une méthode `filter_tasks()` basée sur `build_where_clause()`
- Vérifier la cohérence entre les requêtes SQL et les helpers dynamiques

**Actions réalisées :**
- [x] `update_task()` refait proprement avec requête dynamique
- [x] `filter_tasks()` ajoutée avec clause WHERE générée dynamiquement
- [x] Suppression du point-virgule dans les constantes SQL concaténées
- [x] Logs intégrés pour chaque appel
- [x] Tests interactifs dans IPython sur `update_task()` et `filter_tasks()`

**Résultat :**
- Interface `DB` plus propre et modulaire
- Helpers SQL utilisés en conditions réelles
- Fonctionnement validé étape par étape avec logs et retours attendus

## 📆 2025-04-14 — Découpage complet de `task_table_utils.py` en modules spécialisés

**Objectif :**
- Répartir proprement les constantes liées à l’interface de la table des tâches
- Séparer la logique par type : entêtes, géométrie, comportements cellule

**Actions réalisées :**
- [x] Création de `task_table_headers_utils.py` pour les entêtes et index
- [x] Création de `task_table_geometry_utils.py` pour les largeurs de colonnes
- [x] Création de `task_table_cell_utils.py` pour les Qt.ItemFlags et alignements
- [x] Suppression de `task_table_utils.py` (devenu vide)
- [x] Ajout de `get_column_index()` et `get_column_name()` avec gestion d’erreurs
- [x] Test fonctionnel dans IPython (`get_column_index("Title")` → OK)

**Résultat :**
- Structure plus claire et modulaire
- Responsabilités isolées, facilement testables et maintenables
