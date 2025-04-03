# ✅ todo_db.md — Refactoring de la couche DB (approche AskDB)

> Objectif : rendre l’accès à la base de données plus clair, modulaire, DRY, et expressif.
> On passe d’un bloc brut répétitif à un langage quasi-humain, testable, maintenable.

---

## 🔧 Étapes de refactoring

### 1. Création du fichier de brouillon
- [x] Créer `src/core/database/ask_db.py`

### 2. Classe `AskDB` de base
- [x] Implémenter `__init__` avec une connexion SQLite
- [x] Méthodes de base : `create()`, `insert()`, `select()`, `update()`, `delete()`, `drop()`, `exec()`

### 3. Simplification DRY
- [ ] Utiliser un point d’entrée unique `execute()` en interne
- [ ] Centraliser `commit()` et `fetchall()` selon action

### 4. Ajout de `*args`, `**kwargs`
- [ ] Permettre de passer souplement des paramètres dans les requêtes
- [ ] Rendre les appels plus souples et lisibles

### 5. Introduction du `dict dispatch`
- [x] Créer un routeur `self.routes` ou `self.dispatch()` pour router dynamiquement vers `insert`, `select`, etc.
- [ ] Ajouter une méthode `.ask(action, sql, *args)` pour unifier l’usage

### 6. Création d’un context manager propre
- [x] Implémenter `open_db(path)` avec `contextlib.contextmanager`
- [ ] Assurer ouverture/fermeture auto, et usage simple :

```python
with open_db(DB_FILE) as db:
    db.insert(SQL_INSERT_TASK, "todo", "dev", False)
```

---

## ✨ Objectif d’élégance

- Appels lisibles, comme un mini-DSL interne pour requêtes
- Syntaxe humaine : `db.insert(...)`, `db.select(...)`, etc.
- Isolation claire entre exécution SQL et logique métier
- Compatible avec IPython pour tests interactifs

---

## 🧠 Idées bonus à évaluer plus tard

- [ ] Créer une Factory `DbFactory()` ? (si plusieurs bases à gérer)
- [ ] Injecter un logger (`loguru`) dans la classe pour suivre les requêtes
- [ ] Ajouter un fallback en cas d’échec (try/except autour des `.execute`)
- [ ] Ajouter un mode `debug=True` pour afficher les requêtes exécutées
- [ ] Créer des alias `.add()`, `.get()` pour certaines actions fréquentes

---

## ✅ Étapes validées (à cocher ensemble)
- [ ] Structure de base
- [ ] Test via IPython
- [ ] Intégration dans un handler/test
- [ ] Adoption finale si pertinent

---

Let's build a readable and smart DB layer!
