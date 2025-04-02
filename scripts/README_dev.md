
## 🚀 Lancer l’environnement de développement

```bash
todoenv
```

Cela :
- Te place dans le dossier `todol-archi`
- Active l’environnement virtuel `.venv`
- Nettoie l’écran et affiche les commandes clés

---

## ⚙️ Commandes disponibles

| Commande        | Effet                                                 |
|-----------------|--------------------------------------------------------|
| `todoenv`       | Active `.venv` et entre dans le projet                |
| `todolab`       | Lance IPython avec auto-reload (`reload_all.py`)      |
| `gadd "msg"`    | Fait un `git add .`, commit avec ton message, push    |
| `make run`      | Lance l’application (`python -m src.main`)            |
| `make test`     | Lance Pytest sur le dossier `tests/` (à configurer)   |
| `make help`     | Affiche toutes les commandes disponibles               |

---

## 🗂️ Arborescence utile

- `src/` : code source principal
- `scripts/` : outils dev (ex: `reload_all.py`, `gitadd.py`)
- `tests/` : fichiers de test unitaires
- `Makefile` : point d’entrée pour toutes les commandes automatisées


---

## 🧠 Aliases définis dans `.bashrc`

```bash
alias todoenv='cd ~/Desktop/Projects/todol-archi && source .venv/bin/activate && clear && echo "🟢 In the lab" && echo "todoenv, todolab, gadd @msg"'
alias todolab='make reload'

gadd() {
    make gadd msg="$1"
}
```

---

## 🧼 Astuces

- Pour replier tous les dossiers dans VSCode : `Ctrl + K`, puis `Ctrl + 0`
- Pour fermer tous les onglets : `Ctrl + K W`
- Pour générer une arborescence propre :
  ```bash
  tree -I '__pycache__|*.pyc|.git|.venv|logs|*.db'
  ```

---

## ✅ Pré-requis pour collaborer

```bash
git clone git@github.com:RadioactiveMonk/todol-archi.git
cd todol-archi
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make run
```


