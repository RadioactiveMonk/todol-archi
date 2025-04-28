# Notions : Générateurs & `yield` en Python

## 1. Qu'est-ce qu'un générateur ?

Un **générateur** est une fonction ou un objet qui produit des valeurs **une à une**, à la demande. Contrairement à une fonction classique qui renvoie une valeur unique via `return`, un générateur utilise `yield` pour produire une valeur **sans quitter la fonction**.

---

## 2. Fonctionnement de `yield`

- `yield` suspend l'exécution de la fonction et renvoie une valeur
- L'état de la fonction est **conservé** (pile, variables, curseur)
- L'exécution reprend **au `yield` suivant** quand on appelle `next()` ou qu'on boucle

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

---

## 3. Unpacking et consommation des générateurs

```python
print(*count_up_to(3))         # 1 2 3
list(count_up_to(3))           # [1, 2, 3]
```

- `*generator` ou `list(generator)` = **force l'exécution complète**
- Un générateur est **à usage unique**. Une fois vidé, il ne peut plus être re-parcouru.

```python
gen = count_up_to(3)
print(list(gen))      # [1, 2, 3]
print(list(gen))      # []  (vide !)
```

---

## 4. Comment penser la création d'un générateur ?

> “Je veux produire une série de résultats, progressivement, sans tout calculer ou stocker à l'avance.”

### 🏛️ Étapes mentales :

1. **Quel est le flux à produire ?** (liste de valeurs ? lignes ? filtres ?)
2. **Est-ce que je veux faire ça paresseusement ?** (lazy)
3. **Quel est le critère ou la logique de production ?**
4. **Où placer le `yield` pour produire la valeur souhaitée ?**

---

## 5. Générateur avec donnée externe ou interne

### ✅ Avec un argument itérable passé à l'appel
```python
def even_only(seq):
    for n in seq:
        if n % 2 == 0:
            yield n
```
```python
for i in even_only(range(10)):
    print(i)
```

### ✅ Avec une séquence construite dans le générateur
```python
def even_up_to(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
```

---

## 6. Cas d'usage concrets

### a) Génération d'export CSV paresseux
```python
def export_rows(data):
    yield ["title", "url"]
    for fav in data:
        yield [fav["title"], fav["url"]]
```

### b) Fichier ligne par ligne
```python
def read_lines(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()
```

### c) Générateur infini
```python
def count_forever(start=0):
    while True:
        yield start
        start += 1
```

---

## 7. Différence avec `__iter__` / `__next__`

- `yield` permet de **créer un générateur simplement**
- `__iter__` / `__next__` sont utiles pour **implémenter un itérateur personnalisé dans une classe**
- Dans 90% des cas, `yield` est **plus simple et suffisant**

---

## 8. Bonus : `yield from`

Permet de **déléguer la génération à un autre itérable**
```python
def gen():
    yield from range(3)
    yield "fin"
```

---

## 9. Exemple spécifique Todol-Archi : export paresseux des tâches au format CSV

```python
def generate_task_export(tasks):
    yield ["id", "title", "completed"]
    for task in tasks:
        yield [task.id, task.title, task.completed]
```

Tu peux l'utiliser avec :
```python
with open("tasks.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in generate_task_export(list_of_tasks):
        writer.writerow(row)
```

Avantages :
- ✅ Aucun besoin de construire la liste complète en mémoire
- ✅ Export clair, ligne par ligne
- ✅ Générateur facile à tester, à injecter, à mocker

---

## ✨ Résumé mental :

- `yield` = je **produis une valeur à la fois**
- Le générateur **attend qu'on le consomme**
- Il se vide **et ne se réutilise pas**
- Il est **parfait pour les flux, les gros volumes, les pipelines, les exports**
- On pense "**ce que je veux produire, et comment je le découpe**"
