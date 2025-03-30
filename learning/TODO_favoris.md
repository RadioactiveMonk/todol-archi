# TODO - Gestionnaire de Favoris CLI

## Objectif
Créer un script CLI interactif pour gérer une liste de favoris (titre + URL), sauvegardés dans un fichier `favoris.json`.

---

## Étapes à réaliser

### [ ] Initialisation
- [x] Créer le fichier `favoris.json` s'il n'existe pas
- [x] Charger les données (liste de dicts)
- [x] Gérer les erreurs de chargement JSON (try/except)

### [ ] Menu principal
- [x] Afficher les options (ajouter / supprimer / lister / quitter)
- [x] Boucle continue jusqu'à quitter volontairement

### [ ] Ajouter un favori
- [ ] Demander une URL (vérifier qu'elle commence par http(s)/ftp et contient un `.`)
- [ ] Tant qu’elle est invalide, redemander
- [ ] Demander un titre (non vide)
- [ ] Générer un ID (auto ou UUID)
- [ ] Ajouter à la liste
- [ ] Sauvegarder dans le JSON

### [ ] Supprimer un favori
- [ ] Afficher les favoris avec ID
- [ ] Demander un ID à supprimer
- [ ] Vérifier qu’il existe
- [ ] Supprimer + sauvegarder

### [ ] Lister les favoris
- [ ] Afficher tous les favoris avec ID, titre, et URL (format lisible)



📚 Refactoring Avancé à venir

Une fois le script finalisé (toutes les fonctions fonctionnelles), il servira de base pour explorer des notions avancées Python dans un contexte simple et maîtrisé. L’objectif sera d’apprendre à :

- [ ] intégrer des helpers (is_valid_url(), print_favori()...)

- [ ] tester des notions avancées de Python :

- [ ] @property (sur une version dataclass d’un favori)

- [ ] *args / **kwargs (helpers ou print dynamiques)

- [ ] yield pour générer ligne par ligne (ex : export CSV paresseux)

- [ ] @lru_cache pour du cache temporaire

- [ ] defaultdict pour regrouper des favoris (par domaine, par type…)

- [ ] := (walrus) dans une boucle interactive

- [ ] création d’un context manager personnalisé

- [ ] apprendre à structurer un script via des modules (cli.py, helpers.py, storage.py…)

🎯 Le but : s’entraîner sur ce script pour être prêt à refactoriser Todol-Archi avec un vrai bagage.

---

## Bonus (facultatif)
- [ ] Tri par titre
- [ ] Export CSV
- [ ] Confirmation de suppression
- [ ] Sauvegarde automatique de backup (favoris_backup.json)
- [ ] Passer à argparse plus tard pour usage en CLI directe

---

## Notes
- Données = `List[Dict[str, Any]]`
- Fichier = `favoris.json`
- Ne pas écraser le fichier si la liste est vide
- Penser à une structure claire dès le départ (ex: `Favori` en dataclass ?)

---

## Choix de structure (forme du script)

Pour ce projet simple à but non évolutif, l’approche retenue est :

### ✅ Un seul fichier `favoris.py`
- Utilise des fonctions bien séparées (`add`, `delete`, `list`, `save`, `load`, `main`)
- Pas besoin de `argparse` au départ (interface interactive avec `input()`)
- L’approche orientée objet ou modulaire est **inutile ici** sauf si le projet grandit

Structure recommandée :
```python
if __name__ == "__main__":
    main()

def main():
    while True:
        # afficher le menu et rediriger

def load_data(): ...
def save_data(): ...
def add_favori(data): ...
def delete_favori(data): ...
def list_favoris(data): ...
```

Script simple, lisible, maintenable, parfaitement adapté à l’objectif.

---

## Raisonnement détaillé - Fonction `load_data()`

### Objectif :
Charger le fichier `favoris.json` et retourner la liste de favoris (ou créer un fichier vide si besoin).

### Étapes internes :
1. Recevoir un `Path` pointant vers le fichier
2. Vérifier si le fichier existe
   - Si non → le créer avec `[]` à l’intérieur
3. Tenter de charger avec `json.load()`
   - Si le fichier est corrompu → afficher une erreur et retourner une liste vide
4. Retourner la liste obtenue

### Signature suggérée :
```python
def load_data(filepath: Path, verbose: bool = False) -> list:
```

### Questions utiles :
- Doit-on créer un fichier vide s’il n’existe pas ? (→ oui)
- Doit-on afficher un message en cas d’erreur JSON ? (→ oui, clair et simple)
- Doit-on permettre un `verbose=True` pour debug ou logs ? (→ optionnel mais pratique)

---

## Raisonnement détaillé - Fonction `save_data()`

### Objectif :
Sauvegarder la liste des favoris dans le fichier `favoris.json`

### Étapes internes :
1. Recevoir le `Path` vers le fichier cible
2. Recevoir la `liste` des données à sauvegarder
3. Écrire le contenu avec `json.dump(data, file, indent=4, ensure_ascii=False)`
4. Si `verbose=True`, afficher un message de confirmation

### Signature suggérée :
```python
def save_data(filepath: Path, data: list, verbose: bool = False) -> None:
```

### Questions utiles :
- Doit-on sauvegarder même si la liste est vide ? (→ oui)
- Doit-on écraser le fichier à chaque fois ? (→ oui)
- Doit-on créer un backup juste avant ? (→ possible bonus plus tard)

---

## Raisonnement détaillé - Fonction `add_favori()`

### Objectif :
Demander à l’utilisateur un titre et une URL, les valider, puis ajouter le nouveau favori à la liste existante et le sauvegarder.

### Étapes internes :
1. Demander l’URL à l’utilisateur (via `input()`)
   - Tant que l’URL n’est pas valide (`startswith("http")`, `in ["http", "https", "ftp"]`, contient un `.`), redemander
2. Demander un titre (non vide)
3. Générer un ID unique
   - Si UUID : `str(uuid.uuid4())`
   - Ou : `max([f['id'] for f in data], default=0) + 1`
4. Créer le favori : `{"id": id, "title": titre, "url": url}`
5. L’ajouter à la liste des favoris
6. Appeler `save_data()` pour persister
7. Afficher un message de confirmation si `verbose`

### Signature suggérée :
```python
def add_favori(data: list, filepath: Path, verbose: bool = False) -> None:
```

### Questions utiles :
- Doit-on autoriser des URL en doublon ? (→ oui pour l’instant)
- Doit-on interdire les titres vides ? (→ oui)
- Doit-on afficher la nouvelle liste après ajout ? (→ bonus optionnel)
- Doit-on trier après ajout ? (→ pas nécessaire ici)

---

## Raisonnement détaillé - Fonction `delete_favori()`

### Objectif :
Permettre à l’utilisateur de supprimer un favori existant via son ID, puis sauvegarder les modifications.

### Étapes internes :
1. Si la liste est vide → afficher un message et retourner
2. Afficher la liste des favoris (ID, titre, URL)
3. Demander un ID à supprimer via `input()`
   - Vérifier que l’entrée est un `int` (ou UUID valide selon le choix)
   - Vérifier qu’il existe dans la liste
   - Sinon → redemander
4. Supprimer le favori ciblé de la liste
5. Appeler `save_data()` pour persister la suppression
6. Afficher un message de confirmation si `verbose`

### Signature suggérée :
```python
def delete_favori(data: list, filepath: Path, verbose: bool = False) -> None:
```

### Questions utiles :
- Doit-on demander confirmation avant suppression ? (→ bonus)
- Doit-on gérer les erreurs de saisie proprement ? (→ oui)
- Doit-on réafficher la liste après suppression ? (→ bonus)
- Doit-on afficher un message si la liste est vide ? (→ oui)

---

## Raisonnement détaillé - Fonction `list_favoris()`

### Objectif :
Afficher proprement la liste des favoris (ID, titre, URL), ou un message si elle est vide.

### Étapes internes :
1. Vérifier si la liste est vide
   - Si vide → afficher "Aucun favori enregistré."
2. Sinon, afficher chaque favori sur 2 lignes :
   ```
   [1]  Titre : OpenAI
        URL   : https://openai.com
   ```
3. Ajouter des séparateurs ou retour à la ligne entre les entrées si nécessaire

### Signature suggérée :
```python
def list_favoris(data: list, verbose: bool = False) -> None:
```

### Questions utiles :
- Doit-on trier les résultats ? (→ non par défaut, possible bonus)
- Doit-on ajouter des séparateurs visuels ? (→ recommandé)
- Doit-on ajouter un compteur ou résumé en bas ? (→ bonus)
- Est-ce qu’on affiche un message si la liste est vide ? (→ oui)
