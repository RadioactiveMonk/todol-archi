# ✅ Todol-Pro – Plan de développement avant packaging

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

---

## 🔜 Étapes suivantes 

- [ ] Revoir la gestion du thème (fusion `load_stylesheet` / `reload_theme`)
- [ ] Ajouter un bouton “🔁 Reset default settings”
- [ ] Préparer le passage à FastAPI (profil, endpoints, pydantic ?)
- [ ] Refactor léger `theme/category` pour centraliser

---

📅 Dernière mise à jour : {{ 23-03-25 }}
