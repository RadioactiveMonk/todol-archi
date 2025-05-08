# Méthodologie de construction – `comment_filepath.py`

Objectif : Créer un script CLI propre qui ajoute en haut de chaque fichier `.py` une ligne de commentaire indiquant son chemin relatif (`# Path: ...`), **s'il n'existe pas déjà**.

---

## 1. Clarification de l’objectif

- Parcourir tous les fichiers `.py` du dossier `src/`
- Lire la première ligne de chaque fichier
- Si la ligne ne commence pas par `# Path:`, insérer une ligne `# Path: chemin_relatif`
- Sauvegarder le fichier mis à jour

---

## 2. Bloc de logique à identifier

- `find_py_files()` : Trouver tous les fichiers `.py`
- `check_path_comment(file: Path)` : Vérifie si le commentaire de chemin est présent
- `insert_path_comment(file: Path)` : Ajoute la ligne manquante si besoin
- `main()` : Orchestration du processus

---

## 3. Ce que chaque fonction reçoit et retourne

| Fonction | Paramètres | Retour |
|----------|------------|--------|
| `find_py_files()` | (optionnel: dossier) | `list[Path]` |
| `check_path_comment(file)` | `Path` | `bool` |
| `insert_path_comment(file)` | `Path` | `None` |
| `main()` | — | `None` |

---

## 4. Étapes de travail recommandées

1. Écrire d’abord la logique en **langage naturel ou pseudo-code**
2. Puis écrire le squelette des fonctions en Python avec des `pass`
3. Implémenter `find_py_files()` et tester en console
4. Implémenter `check_path_comment()`, tester sur un seul fichier
5. Implémenter `insert_path_comment()`
6. Rassembler le tout dans `main()`
7. **(Optionnel)** : Ajouter un `--dry-run` ou un `--verbose` avec `argparse` plus tard

---

## 5. Conseils

- Garde les fonctions **indépendantes** : pas de variable globale
- Commence simple (sans argparse)
- Utilise `Path.relative_to()` ou `Path.as_posix()` pour un affichage propre
- N'ajoute pas de `# Path:` si le fichier est vide ou si la ligne existe déjà

---

Quand tu auras fait ta version bloc-note, tu pourras me l’envoyer et on la pimpera ensemble !