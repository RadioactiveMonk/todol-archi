# ✅ todo_db.md — Refactoring de la couche DB (approche DB)

> Objectif : rendre l’accès à la base de données plus clair, modulaire, DRY, et expressif.
> On passe d’un bloc brut répétitif à un langage quasi-humain, testable, maintenable.

---

## ✅ Étapes validées — DB V1 : fondations solides

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

## 🔁 Étape suivante – DB V2 : expressivité & ergonomie

- [x] Ajouter `lastrowid` dans `.insert()` (retour de l’ID inséré)
- [x] Ajouter une méthode `.select_one()` (équivalent de `.fetchone()`)
- [x] Créer une méthode `.ask(action, sql, *args)` unifiée
- [x] Ajouter des alias métier (`add_task()`, `get_tasks_by_category()`, etc.)
- [x] Faire un init_db()
- [x] Suppression de `db_controller.py`

## 🧪 Migration finale vers DB (phase de nettoyage) 

- [x] Remplacer DbManager par open_db() + alias DB
- [x] Corriger tous les __init__.py impactés
- [x] Corriger tous les handlers/, models/ qui importent DbManager
- [x] Supprimer db_manager.py définitivement
- [x] Refaire reload_all.py proprement avec DB
- [x] Revalider l’ensemble du projet (make run, pytest, ipython) # FIX: id quand add_task

## 🧪 Nettoyage & robustesse

- [ ] Ajouter try/except dans ask_db.py pour les erreurs critiques
- [x] Ajouter debug=True pour afficher dynamiquement les requêtes
- [x] Ajouter les alias lisibles .add(), .get(), .remove() (optionnels)

---

## 💡 Idées bonus à évaluer plus tard

- [ ] Créer une `DbFactory()` pour gérer plusieurs connexions (multi-db)
- [ ] Ajouter un logger interne à la classe (plutôt que global)
- [ ] Ajouter un décorateur `@db_action` pour logguer automatiquement
- [ ] Ajouter des options de type `fetch="all"`, `fetch="one"` dans `.ask()`
- [ ] Accepter aussi des requêtes SQL auto-générées depuis `dict` (future piste ORM-like)

## 🧪 Objectif final

Un système de gestion SQLite :
- Simple à utiliser
- Solide à maintenir
- Facile à tester
- Proprement loggué


