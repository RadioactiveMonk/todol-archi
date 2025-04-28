# Cheat Sheet — Structures de Données Python

## 1. Stack (Pile) — LIFO (Last In, First Out)

**Usages :**
- Historique (annuler)
- Navigation (retour en arrière)
- Algorithmes récursifs (DFS)

```python
stack = []
stack.append("étape 1")
stack.append("étape 2")
last = stack.pop()  # "étape 2"
```

---

## 2. Queue (File) — FIFO (First In, First Out)

**Usages :**
- Tâches à traiter dans l’ordre
- Gestion de file d’attente

```python
from collections import deque
queue = deque()
queue.append("Seb")
queue.append("Lucie")
first = queue.popleft()  # "Seb"
```

---

## 3. Deque (Double-Ended Queue)

**Usages :**
- Historique navigable
- Buffer circulaire
- Structure versatile (stack + queue)

```python
d = deque(["a", "b"])
d.appendleft("urgent")
d.pop()  # "b"
```

---

## 4. Enum (Énumération)

**Usages :**
- Statuts constants
- Sécurité, lisibilité, maintenabilité

```python
from enum import Enum

class Status(Enum):
    TODO = 1
    DONE = 2
```

---

## 5. Node / Arbre / Arborescence

**Usages :**
- Structure hiérarchique (menus, dossiers)
- Recursion, navigation haut/bas

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
```

---

## 6. NamedTuple / Dataclass

**Usages :**
- Objets simples
- Moins verbeux qu’une classe classique

```python
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    completed: bool
```

---

## 7. defaultdict

**Usages :**
- Regroupement par clé
- Initialisation automatique des valeurs

```python
from collections import defaultdict

grouped = defaultdict(list)
grouped["chat"].append("Miaou")
```

---

## 8. set / frozenset

**Usages :**
- Ensemble unique sans doublons
- Vérifications rapides, opérations d’ensemble

```python
tags = {"python", "bash", "qt"}
if "python" in tags:
    ...
```