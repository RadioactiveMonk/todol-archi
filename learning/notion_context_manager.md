# Notions : Context Managers personnalisés

## 1. Qu'est-ce qu'un context manager ?

Un **context manager** est une construction Python qui gère une ressource à l'entrée et à la sortie d'un bloc `with`.

Exemples connus :
```python
with open("file.txt") as f:
    data = f.read()
```

---

## 2. Deux façons d'écrire un context manager personnalisé

### a) Façon 1 : Avec une **classe** et les méthodes magiques

```python
class OpenFile:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
```

Utilisation :
```python
with OpenFile("test.txt", "w") as f:
    f.write("Hello")
```

### b) Façon 2 : Avec un **générateur** + `@contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def open_file(path, mode="r"):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
```

Utilisation :
```python
with open_file("test.txt", "w") as f:
    f.write("Hello")
```

---

## 3. Pourquoi utiliser `@contextmanager` ?

- Plus **rapide à écrire** que la version classe
- Parfait pour **gérer une ressource simple** (fichier, connexion, settings)
- **Lisible** et Pythonic

> Sous le capot, `@contextmanager` transforme ta fonction en **objet qui implémente `__enter__` / `__exit__`**, grâce à un générateur

---

## 4. Exemple concret dans Todol-Archi : `settings_context()`

```python
from contextlib import contextmanager
from settings_manager import SettingsManager

@contextmanager
def settings_context():
    sm = SettingsManager()
    sm.load()
    try:
        yield sm
    finally:
        sm.save()
```

Utilisation :
```python
with settings_context() as settings:
    settings.set("theme", "dark")
```

---

## 5. Exemple alternatif : verrouillage de base de données

```python
@contextmanager
def db_lock(conn):
    conn.execute("BEGIN")
    try:
        yield conn
        conn.commit()
    except:
        conn.rollback()
        raise
```

---

## 6. Exemples supplémentaires inspirés de Todol-Archi

### a) `log_context()` : rediriger les logs temporairement
```python
@contextmanager
def log_context(file="temp_log.txt"):
    from sys import stdout
    original = stdout
    with open(file, "w") as f:
        try:
            import sys
            sys.stdout = f
            yield
        finally:
            sys.stdout = original
```

### b) `theme_context()` : appliquer un thème temporairement
```python
@contextmanager
def theme_context(settings, temp_theme):
    original = settings.get("theme")
    settings.set("theme", temp_theme)
    try:
        yield
    finally:
        settings.set("theme", original)
```

### c) `temp_override()` : remplacer temporairement un paramètre
```python
@contextmanager
def temp_override(settings, key, temp_value):
    original = settings.get(key)
    settings.set(key, temp_value)
    try:
        yield
    finally:
        settings.set(key, original)
```

---

## 7. 🔎 Résumé : Quand utiliser quel style ?

| Besoin                                  | Recommande...                     |
|----------------------------------------|-----------------------------------|
| Tu gères une ressource simple           | `@contextmanager` + `yield`       |
| Tu veux encapsuler un comportement plus complexe | Classe avec `__enter__` / `__exit__` |

---

## 8. ✨ Mental model :

- "Je veux **encadrer** une action : ouvrir / fermer, activer / désactiver"
- J'utilise `@contextmanager` si je veux aller vite
- Je place le `yield` **au moment où je veux donner accès à la ressource**
- Le `finally:` est **garanti d'être exécuté à la sortie du bloc**
