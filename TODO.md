# TODO - Todol Archi Clean Reboot

## ✅ État actuel
- Nouvelle structure appliquée (`src/` avec `configuration/`, `handlers/`, `components/`, etc.)
- Backend fonctionnel (DbController, DbManager, SettingsManager)
- UI reconnectée (dialogs, TaskHandlers, etc.)
- Thèmes, settings, handlers testés
- Connexion persistante intégrée

---

## 🧹 Étape 1 – Nettoyage & Imports
- [ ] Désactiver Ruff et Pylance strict temporairement
- [x] Nettoyer tous les imports
- [ ] Corriger tous les imports `from src.` → structure relative
- [ ] Retester les fichiers un par un dans IPython pour valider les modules

---

## ⚙️ Étape 2 – Reconstruction des Fonctions
### [1] Toggle Status
- [x] Finaliser `toggle_status()` dans `handlers/status_handler.py`
- [x] Appliquer `[PENDING]` / `[ROCKED]` dans la colonne
- [x] Mettre une couleur de fond verte/rouge selon le statut

### [2] Recherche
- [ ] Brancher barre de recherche à la table
- [ ] Ajouter méthode dans `DbController` pour filtrer les tâches

### [3] UI & Delegates
- [ ] Vérifier fonctionnement d’`EditDelegate`
- [ ] Nettoyer `cell_properties.py` si encore nécessaire

---

## ✅ Étape 3 – Tests à réécrire
- [ ] `test_status_handler.py`
- [ ] `test_settings_manager.py`
- [ ] `test_search_functionality.py`
- [ ] Ajouter fixtures propres si besoin (`in_memory_db`, `test_settings_file`)

---

## 🌀 Étape 4 – À faire plus tard
- [ ] Réactiver Ruff + Pylance strict
- [ ] Ajouter les `__init__.py` manquants
- [ ] Documentation (README)
- [ ] Tests UI + détection erreurs via IPython
- [ ] Packaging / API avec FastAPI si souhaité

---

## ☕ Mantra
**Nettoyer → Structurer → Reprendre une brique à la fois.**
