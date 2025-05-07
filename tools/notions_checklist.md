# Grimoire Scripting – Seb

Ce fichier regroupe les notions utiles, validées et à explorer progressivement dans tes outils CLI Python.

---

## String Manipulation Essentials

- `str.strip()`, `lstrip()`, `rstrip()`
- `str.split()`, `splitlines()`
- `str.startswith()`, `endswith()`, `replace()`
- `str.lower()`, `upper()`, `title()`
- `str.center()`, `ljust()`, `rjust()` — padding utile pour les tableaux ou affichages
- `"sep".join(list)` — recomposition de chaînes
- `str.partition(sep)` — pour découper en (avant, séparateur, après), plus lisible que `split()`

---

## Structures de données utiles

- `dict.setdefault(key, default)` — permet de simplifier la création dynamique de dictionnaires imbriqués
- Priorité donnée aux structures natives Python avant les regex

---

## File Operations Avancées (`shutil`)

- `shutil.copy(src, dst)`
- `shutil.copytree(src, dst)`
- `shutil.move(src, dst)`
- `shutil.rmtree(path)`
- `shutil.disk_usage(path)`
- `shutil.make_archive(...)`

---

## Fichiers JSON et CSV

- `json.load()`, `json.dump()`
- `csv.reader()`, `csv.writer()`
- À maîtriser pour les outils de config, d’import/export, de sauvegarde légère

---

## Web Scraping

- Objectif : apprendre à **extraire** des données (avec `requests` + `BeautifulSoup`)
- Le module `webbrowser` sert uniquement à **ouvrir une page**, pas à l’analyser

---

## Modules à explorer progressivement (niveau supérieur)

- **`logging`** – structurer tes scripts avec des messages propres, niveaux d’alerte, fichiers log…
- **`argparse` / `click`** – transformer tes scripts en vrais outils CLI avec options (`--dry-run`, `--force`, etc.)
- **`pathlib` avancé** – `.relative_to()`, `.with_suffix()`, `symlink_to()`, navigation propre
- **`timeit` / `perf_counter`** – mesurer les perfs de tes scripts ou de blocs critiques
- **Fichiers réutilisables** – créer des modules comme `utils.py` pour centraliser tes fonctions maison

---

## Regex

- Mis de côté pour l’instant. Bases acquises.
- Priorité donnée à la maîtrise complète des méthodes natives avant d’y revenir.