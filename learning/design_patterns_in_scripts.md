# Design Patterns & Patterns Pythonics utilisés dans des scripts

## 🎯 Objectif
Identifier les petits patterns élégants, efficaces et Pythonic que tu peux réutiliser dans des scripts.

---

## 🏭 1. Mini Factory — `get_path()`

### Description :
Fonction qui centralise la création de chemins (`Path`) à partir de noms symboliques.

```python
def get_path(name: str) -> Path | None:
    base = Path(__file__).resolve()
    paths = {
        "current_file": base,
        "current_path": base.parent,
        "json": base.parent / "favorites.json",
    }
    return paths.get(name)
```

### Pourquoi c’est une factory ?
- Elle construit et retourne des objets prêts à l’emploi (des `Path`)
- Elle masque les détails de construction (`__file__`, `.parent`)
- Elle centralise les chemins → DRY et évolutif

---

## 🧠 2. Dispatch Dynamique — `valid_choices[choice]()`

### Description :
Associer des chaînes de commande (`"1"`, `"2"`, `"q"`) à des actions via des `lambda`.

```python
actions = {
    "1": lambda: list_favoris(data),
    "2": lambda: add_favori(data),
    "q": lambda: quit(),
}
```

### Appel :
```python
actions.get(choice, lambda: print("Choix invalide"))()
```

### Avantages :
- Supprime les `if`/`elif`/`else` imbriqués
- Scalable facilement : une nouvelle action = une nouvelle entrée
- Très lisible et modulaire

---

## 🧼 Bonus : Refus des "variables qui traînent dans le vide"

Au lieu d’avoir :
```python
CURRENT_FILE = Path(__file__).resolve()
CURRENT_PATH = CURRENT_FILE.parent
JSON_PATH = CURRENT_PATH / "favorites.json"
```

Tu les encapsules dans `get_path()` → centralisé, propre, clair.
