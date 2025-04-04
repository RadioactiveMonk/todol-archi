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
- [x] Ajouter des alias métier (`add_task()`, `get_tasks_by_category()`, etc.)
- [x] Faire un init_db()
- [x] Suppression de `db_controller.py`

## 🧪 Migration finale vers AskDB (phase de nettoyage) 

- [ ] Remplacer DbManager par open_db() + alias AskDB
- [ ] Corriger tous les __init__.py impactés
- [ ] Corriger tous les handlers/, models/ qui importent DbManager
- [ ] Supprimer db_manager.py définitivement
- [ ] Refaire reload_all.py proprement avec AskDB
- [ ] Revalider l’ensemble du projet (make run, pytest, ipython) 

## 🧪 Nettoyage & robustesse

- [ ] Ajouter try/except dans ask_db.py pour les erreurs critiques
- [ ] Ajouter debug=True pour afficher dynamiquement les requêtes
- [ ] Ajouter les alias lisibles .add(), .get(), .remove() (optionnels)

---

## 💡 Idées bonus à évaluer plus tard

- [ ] Créer une `DbFactory()` pour gérer plusieurs connexions (multi-db)
- [ ] Ajouter un logger interne à la classe (plutôt que global)
- [ ] Ajouter un décorateur `@db_action` pour logguer automatiquement
- [ ] Ajouter des options de type `fetch="all"`, `fetch="one"` dans `.ask()`
- [ ] Accepter aussi des requêtes SQL auto-générées depuis `dict` (future piste ORM-like)

## Structures de données avancées

- [ ] deque (collections, queue, stack efficaces)
- [ ] Enum (valeurs symboliques propres et lisibles)
- [ ] NamedTuple / dataclass vs tuple classique
- [ ] LinkedList / Node (manuellement pour comprendre le chaînage)
- [ ] Heap, Set, frozenset, defaultdict

---

## 🧪 Objectif final

Un système de gestion SQLite :
- Simple à utiliser
- Solide à maintenir
- Facile à tester
- Proprement loggué


