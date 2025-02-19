import json
import os
from backend.task import Task


class Storage:
    """Gestion du stockage Json des tâches."""

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Récupère le dossier actuel
    FILE_PATH = os.path.join(BASE_DIR, "..", "data", "tasks.json")  # Chemin correct

    def load_tasks(self):
        """Charge les tâches depuis le fichier JSON."""
        if not os.path.exists(self.FILE_PATH):
            return []  # Retourne liste vide si le fichier JSON n'existe pas.

        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [
                    Task.from_dict(task) for task in data
                ]  # Convertit JSON -> objets Task
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Erreur de lecture JSON: {e}")
            return []

    def save_task(self, task_data):
        """Ajoute une nouvelle tâche et la sauvegarde."""
        tasks = self.load_tasks()  # Charge les tâches existantes
        task = Task.from_dict(task_data)  # Convertit en objet Task
        tasks.append(task)  # Ajoute la nouvelle tâche

        try:
            os.makedirs(
                os.path.dirname(self.FILE_PATH), exist_ok=True
            )  # Crée `data/` si absent
            with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump([task.to_dict() for task in tasks], f, indent=4)
        except IOError as e:
            print(f"Erreur d'écriture du fichier JSON: {e}")
