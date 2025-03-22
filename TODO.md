# Todol-Pro — Roadmap Backend & Optimisation

---

## ✅ Étape 1 – Refonte Backend & Base de données

- [x] Structure du backend avec `DbController` et `DbManager`
- [x] Injection de `DbController` dans `DbManager`
- [x] Tests en `file::memory:?cache=shared` pour la base
- [x] Isolation des handlers dans `TaskHandlers`
- [x] Conversion de `tid` dans `Task` avec suivi dynamique
- [x] Tests unitaires fonctionnels (add / update / delete)

---

## 🔁 Étape 2 – Connexion persistante (DbController)

- [x] Créer `self.conn` dans `DbController.__init__()`
- [x] Modifier `_execute_query()` pour utiliser `self.conn`
- [x] Fermer la connexion dans `__del__()`
- [x] Vérifier l'impact sur les tests `in_memory_db`

---

## 🔁 Étape 3 – Mise en cache (`lru_cache`) des accès fichiers

### 📁 `backend/core/cached_utils.py`

- [ ] Ajouter `get_categories()` avec `@lru_cache`
- [ ] Ajouter `get_stylesheet(theme)` avec `@lru_cache`
- [ ] Ajouter (optionnel) `get_available_themes()` avec cache

---

## 🔁 Étape 4 – Tests des fonctions mises en cache

- [ ] Créer `test_cached_utils.py`
- [ ] Tester que `get_categories()` retourne bien une liste
- [ ] Tester que `get_stylesheet()` retourne bien un contenu de `.qss`

---

## 🔁 Étape 5 – Intégration dans l’app

- [ ] Remplacer lecture directe des `.qss` par `get_stylesheet(theme)`
- [ ] Utiliser `get_categories()` dans les dialogues si besoin
- [ ] Ajouter un log (facultatif) à l’appel des fonctions cachées

---

## 🧠 Étape 6 – Bonus (profiling & cache invalidation)

- [ ] Ajouter un système de `clear_cache()` si fichier modifié
- [ ] Ajouter `@profile` ou `perf_counter()` sur certaines fonctions
- [ ] Mesurer l’impact de `@lru_cache` sur les perfs globales

---

_Fichier généré automatiquement — Dernière mise à jour : {{ aujourd’hui }}_
