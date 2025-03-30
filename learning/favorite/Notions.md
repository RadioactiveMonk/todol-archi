# Notions.md

Ce fichier regroupe toutes les **notions clés, patterns, stratégies** ou détails techniques liés à l’écriture de scripts Python autonomes (comme `favoris.py`).

---

## 🔁 Stratégie : Partage d'état (Option 1)

Dans cette approche, on charge les données **une seule fois** au démarrage du script, puis on les transmet aux fonctions qui en ont besoin. Le script manipule un **état en mémoire unique** tout au long de l’exécution.

### ✅ Avantages

- Moins d’accès disque → plus rapide  
- Moins de bugs liés à des données différentes entre les fonctions  
- Lisible et logique : on garde un “état courant” cohérent

### ⚠️ Attention

- Si le fichier JSON est modifié *pendant* que le script tourne, le `data` en mémoire **ne sera pas mis à jour automatiquement**.

### 📦 Structure typique

```python
# main()
data = load_data()

while True:
    choice = show_menu()
    handle_choices(choice, data)
```

```python
# handle_choices()
"2": lambda: add_favorite(data, show_add_favorite())
```

```python
# add_favorite()
def add_favorite(data, favorite):
    data.append(favorite)
    save_data(data)
```

➡️ Tu modifies **l’objet `data` en mémoire**, puis tu le sauvegardes pour qu’il reflète les changements dans le fichier.

---

## 🧠 Notions à garder à l’œil (à développer + tard si besoin)

- `lambda` qui retourne vs appelle une fonction ✅  
- `dict.get(key, lambda: fallback)()` ✅  
- Passage de liste (ou dict) par **référence**  
- Factory de chemins (`get_path()`)  
- Helpers pour rendre le code fluide (`strip_lower()`)  
- Regex en Python (`re.match`, `re.fullmatch`, `findall`…)  
- `exit()` vs `sys.exit()`  
- Dispatch dynamique dans un menu CLI  
- Gestion d’un menu CLI réactif, minimal, élégant  
- Choix d’un `data` partagé ou non selon la logique du script  
- Code de sortie (`exit(0)`)  
- Modèle `main()` : orchestration mais pas de logique métier directe  

## 🧰 Helpers utiles à intégrer

Fonctions utilitaires simples à ajouter dans le script pour éviter les répétitions et clarifier le code :

🔠 strip_lower(text: str) -> str

Nettoie et normalise une entrée utilisateur :

```python
def strip_lower(text: str) -> str:
    return text.strip().lower()
```
Usage :

```python
choice = strip_lower(input("Ton choix: "))
```

📁 get_path(name: str) -> Path

Factory de chemins standardisés à partir d’un mot-clé :

```python
def get_path(name: str) -> Path:
    base = Path(__file__).resolve()
    return {
        "current_file": base,
        "current_path": base.parent,
        "json": base.parent / "favorites.json",
    }.get(name)
```

Permet d’éviter les constantes globales qui traînent et rend le code plus modulaire.



