# ✅ todo_db.md — Refactoring de la couche DB (approche AskDB)

> Objectif : rendre l’accès à la base de données plus clair, modulaire, DRY, et expressif.
> On passe d’un bloc brut répétitif à un langage quasi-humain, testable, maintenable.

---

## ✅ Étapes validées — AskDB V1 : fondations solides

- [x] Créer `src/core/database/ask_db.py`
- [x] Implémenter `__init__` avec une connexion SQLite
- [x] Méthodes de base : `create()`, `insert()`, `select()`, `update()`, `delete()`, `drop()`, `exec()`
- [x] Créer un dict dispatch (`self.routes`)
- [x] Implémenter `dispatch(action, sql, *args)` avec vérification
- [x] Ajouter des logs avec `loguru` dans chaque méthode
- [x] Créer `helpers/contextmanagers.py` avec `open_db()`
- [x] Assurer ouverture/fermeture auto de la DB avec `with open_db(...) as db`
- [x] Tester en IPython → OK

---

## 🔁 Étape suivante – AskDB V2 : expressivité & ergonomie

- [x] Ajouter `lastrowid` dans `.insert()` (retour de l’ID inséré)
- [x] Ajouter une méthode `.select_one()` (équivalent de `.fetchone()`)
- [x] Créer une méthode `.ask(action, sql, *args)` unifiée
- [ ] Ajouter des alias métier (`add_task()`, `get_tasks_by_category()`, etc.)
- [ ] Faire un init_db()
- [x] Migration officielle vers `ask_db.py` et suppression de `db_controller.py`
- [ ] Ajouter une gestion d’erreur propre (`try/except`, `raise`)
- [ ] Ajouter un paramètre `debug=True` pour afficher les requêtes exécutées
- [ ] Créer des alias d’action (`.add()`, `.get()`, `.remove()`...)

---

## 🔁 Étape AskDB V3 : intégration au projet

- [ ] Supprimer progressivement `db_controller.py`
- [ ] Adapter `db_manager.py` pour utiliser `AskDB` via `with open_db()`
- [ ] Identifier les appels SQL encore faits ailleurs et les router via `AskDB`
- [ ] Créer des tests ciblés autour d’`AskDB`

---

## 💡 Idées bonus à évaluer plus tard

- [ ] Créer une `DbFactory()` pour gérer plusieurs connexions (multi-db)
- [ ] Ajouter un logger interne à la classe (plutôt que global)
- [ ] Ajouter un décorateur `@db_action` pour logguer automatiquement
- [ ] Ajouter des options de type `fetch="all"`, `fetch="one"` dans `.ask()`
- [ ] Accepter aussi des requêtes SQL auto-générées depuis `dict` (future piste ORM-like)

---

## 🧪 Objectif final

Un système de gestion SQLite :
- Simple à utiliser
- Solide à maintenir
- Facile à tester
- Proprement loggué
- Adapté au style Pythonic que tu vises

