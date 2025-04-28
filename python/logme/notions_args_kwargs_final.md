
# IPython:

```python
In [3]: log("Seb", "Utilisateur", sep= " | ", prefix="[INFO]", upper=True)
[INFO] SEB | UTILISATEUR
```

✅ Ce que tu pratiques ici :

| Élément   | Ce que tu apprends                                      |
|-----------|----------------------------------------------------------|
| `*args`   | Récupérer une suite d’éléments dynamiques               |
| `**kwargs`| Créer un système d’options souple et élégant            |
| `.get()`  | Fournir des valeurs par défaut                          |
| `print()` | Gérer le formatage à la main (`sep`, `end`)             |

---

## 🧠 Démarche mentale pour construire une fonction avec `*args` / `**kwargs`

### 🎯 Étape 1 : Quel est l’objectif de cette fonction ?
```python
Je veux afficher un message flexible, avec plusieurs morceaux, et des options de personnalisation.
```

### 🔩 Étape 2 : Quels types d’inputs je veux gérer ?

**a) Des morceaux de message** (texte brut, variable, etc.)  
→ J’en veux autant que je veux → donc : `*args` ✅
```python
log("Erreur", "serveur", "offline", "dans 5min")
```

**b) Des options de style** : séparateur, majuscules, etc.  
→ Ce sont des options nommées, parfois omises → donc : `**kwargs` ✅
```python
log(..., sep=" - ", upper=True)
```

---

## 🧱 Étape 3 : Je découpe la fonction en 3 blocs

🔹 **Bloc 1 : Préparer les options (`kwargs`)**
```python
sep = kwargs.get("sep", " ")
prefix = kwargs.get("prefix", "")
upper = kwargs.get("upper", False)
end = kwargs.get("end", "\n")
```
🧠 "Je veux que l’utilisateur puisse personnaliser, mais s’il ne précise rien, je garde un comportement par défaut."

🔹 **Bloc 2 : Construire le message principal (`args`)**
```python
message = sep.join(str(arg) for arg in args)
if upper:
    message = message.upper()
```
🧠 "Je transforme les morceaux `args` en texte final, en tenant compte du style (uppercase, sep, etc.)"

🔹 **Bloc 3 : Afficher le tout**
```python
print(f"{prefix}{message}", end=end)
```
🧠 "Je combine mon environnement (prefix, suffix) + message final."

---

## ✨ Version enrichie avec Rich + écriture fichier

### 🎯 Objectifs ajoutés :
- Ajouter une couleur avec `rich`
- Écrire dans un fichier si demandé

### 🔁 Bloc optionnel 4 : Colorisation du message avec Rich
```python
color = kwargs.get("color")
if color:
    from rich import print as rich_print
    rich_print(f"[{color}]{prefix}{message}[/{color}]", end=end)
else:
    print(f"{prefix}{message}", end=end)
```

### 📝 Bloc optionnel 5 : Écriture dans un fichier
```python
to_file = kwargs.get("to_file", False)
filename = kwargs.get("filename", "log.txt")

if to_file:
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{prefix}{message}\n")
```

---

### 🧠 Subtilités à retenir :
- `[color]...[/color]` est une syntaxe **spécifique à `rich`** (comme du BBCode)
- `print(..., end="")` ≠ `f.write(...)` → `.write()` **n’a pas de `end`**, il faut ajouter `\n` soi-même
- `open(..., "a")` **crée le fichier automatiquement s’il n’existe pas**

---

💥 Résumé ultra clair :

| Étape | But                           | Code                              |
|-------|--------------------------------|-----------------------------------|
| 1     | Gérer les options              | `kwargs.get(...)`                |
| 2     | Construire le message          | `join(args)` + `.upper()`        |
| 3     | Afficher proprement            | `print()` ou `rich_print()`      |
| 4     | Écrire dans un fichier         | `open(..., "a").write(...)`     |

---

🧠 **Mindset général** :
- `*args` = le contenu du message
- `**kwargs` = le style, les options, le contexte
- On construit une fonction **extensible et robuste**, facile à faire évoluer !
