# Emojis: ✅ 🚩 ℹ️ 👉 💭 💯 🛠️ ⚠️ ⁉️

# ✅ Todol-Pro – Plan de refactoring #777

---

## 🔁 Étape 1 – Connexion persistante (DbController)

- [x] Connexion unique avec `self.conn`
- [x] `_execute_query()` mis à jour pour l'utiliser
- [x] `__del__()` pour fermeture propre
- [x] Tests : `test_connection.py`, `test_database.py` validés ✅

---

## ⚡ Étape 2 – Mise en cache `@lru_cache`

- [x] `get_categories()` dans `cached_utils.py`
- [x] `get_stylesheet(theme)` dans `cached_utils.py`
- [x] `get_available_themes()` → liste dynamique des `.qss`
- [x] Tests en IPython → ✅

---

## ⚙️ Étape 3 – Paramètres (Refacto)

- [x] Nouveau `settings_manager.py` simple et pur
- [x] `get_setting()`, `set_setting()` → centralisés
- [x] Plus de cache maison, plus de dataclass

---

## 🧩 Étape 4 – UI (Paramètres / thèmes / catégories)

- [x] `EditParametersDialog` reconnecté (get/set, signal, cache)
- [x] `CategorySelector` + JSON synchro
- [x] `ThemeSelector` + thèmes dynamiques
- [x] `reload_theme(app)` propre, centralisé
- [x] Application live du thème sans redémarrage ✅

---

## 🧪 Étape 5 – Tests IPython

- [x] Vérif complète du flux `settings.json` → UI
- [x] Tests du cache (misses/hits)
- [x] Tests de rechargement live


# ✅ Todol-Pro – Feuille de route finale

---

## 0. Nettoyage du code UI (refacto)

- [x] task_table_utils.py: ce qui est vraiment utile
- [x] cell_properties.py: clarifier les rôles visuels
- [x] edit_delegate.py: découpage et simplification
- [x] task_table_model.py: relecture complète et nettoyage des dépendances, implémenter get_alignment
- [ ] OPTIONNEL: restructuration dans un dossier tables/ ..

## 1. Dernières fonctionnalités de base à implémenter

- [x] Toggle status centralisé (`status_handler.py`)
- [x] Clic sur colonne “Status” via `EditDelegate`
- [x] Couleur dynamique dans `TaskTableModel` (au lieu de l’emoji)
- [ ] THEORIE: SOLID
- [ ] Barre de recherche opérationnelle (`SearchBar`)
- [ ] Bouton “Reset paramètres par défaut”

---

## 2. Peaufinage UI / UX

- [ ] Uniformiser les logs (thèmes, tâches, erreurs)
- [ ] Gérer les cas limites (champ vide, doublon, suppression vide, etc.)
- [ ] Réorganiser les composants si besoin (`components/`, `delegates/`, etc.)

---

## 3. Refactoring global #778

- [ ] Relecture fichier par fichier (comme `DbController`)
- [ ] Centralisation logique (`style`, `status`, `handlers`, etc.)
- [ ] Nettoyage code mort / import inutiles
- [ ] Ajout type hints / docstrings manquants

---

## 4. Ajout d’une API (FastAPI)

- [ ] `GET /tasks`
- [ ] `POST /tasks`
- [ ] `PATCH /tasks/{id}`
- [ ] `DELETE /tasks/{id}`
- [ ] `GET /categories`

---

## 5. Phase Tests avancés

- [ ] Ajouter des tests API (si FastAPI)
- [ ] Tests d’intégration logique (handlers / modèles)
- [ ] Revoir couverture `pytest`

---

## 6. Industrialisation

- [ ] README finalisé (structure, usage, installation)
- [ ] Packaging propre (`pyproject.toml`, setup…)
- [ ] `requirements.txt` mis à jour
- [ ] Git / nettoyage branche
- [ ] (Optionnel) Makefile ou script bash (`dev`, `test`, `clean`…)

---

📌 Dernière mise à jour : 24-03-25
