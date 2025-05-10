- [ ] Améliorer comment_filepath.py
- [ ] Faire un dossier tools/ pour les scripts utilitaires plutôt que scripts/
- [ ] Améliorer replace imports


Liste d'idées d'outils CLI "bons pour Todol + pour progresser"

Manipulation de fichiers (file ops)

[✔] comment_filepath.py ➔ ajouter les chemins en commentaire (en cours)

[✔] replace_imports.py ➔ modifier automatiquement certains imports (en cours)


À venir :

format_headers.py ➔ Ajouter un modèle standardisé d'entête sur tous les .py (# Author: Seb, Date: 2025-XX-XX, Description:)

check_empty_files.py ➔ Lister tous les fichiers .py vides ou quasi vides (moins de 5 lignes)

delete_tmp_files.py ➔ Nettoyer tous les .pyc, __pycache__/, fichiers temporaires .tmp

check_missing_docstrings.py ➔ Scanner tous les .py et signaler les fonctions sans docstring



---

Outils de navigation et aide projet

tree_slim.py ➔ Faire un affichage simplifié du projet (src/, tests/) sans montrer tous les fichiers cachés/bidons

find_large_files.py ➔ Trouver les fichiers .py ou autres de plus de X Ko (analyser où le projet grossit)

generate_readme_index.py ➔ Créer automatiquement un README.md listant tous les modules et scripts avec leurs chemins

open_random_file.py ➔ Ouvre au hasard un fichier .py pour faire un petit refactoring surprise (super fun pour t'entraîner !)



---

Outils de qualité de code

scan_tabs_vs_spaces.py ➔ Vérifier qu’il n’y a que des espaces, pas de tabulations crades

check_trailing_whitespaces.py ➔ Supprimer les espaces inutiles en fin de ligne

lint_project_summary.py ➔ Lancer flake8 ou ruff et résumer les erreurs trouvées

analyze_todo_comments.py ➔ Repérer tous les # TODO, # FIXME du projet pour ne rien oublier



---

Outils bonus “un peu plus poussés”

dependency_checker.py ➔ Scanner tous les import dans src/, repérer ceux qui ne sont pas utilisés

rename_module.py ➔ Renommer proprement un fichier .py + mettre à jour tous les imports qui pointaient dessus

backup_before_refactor.py ➔ Faire une copie rapide de src/ dans src_backup/ avant une session de refactoring

generate_script_template.py ➔ Créer automatiquement un squelette de fichier .py avec header + imports de base


