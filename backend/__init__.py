"""
backend
=======
Gere toute la logique métier du projet.

- constants.py : Contient les valeurs immutables du projets(titres de headers, priorités ..)
- database.py : Base de données
- Storage.py : Gère le stockage/chargement des tâches via un fichier JSON (data/tasks.json)
- task_manager.py : Gère la conversion/récupération des tâches pour stockage sous format dictionnaire pour le JSON.
- task.py : Définition d'une tâche dans une @dataclass
- validators.py : Gère la logique de validation des types et des valeurs insérées par l'utilisateur.

"""
