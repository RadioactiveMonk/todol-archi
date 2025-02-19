from uuid import uuid4
from backend.storage import Storage


class TaskManager:
    """Gère les tâches depuis storage"""

    def __init__(self) -> None:
        self.storage = Storage()

    def add_task(self, task_data):
        """Ajoute une tâche et la sauvegarde"""

        task = {
            "id": str(uuid4()),  # Génération d'un UUID unique
            "title": task_data["title"],
            "priority": task_data["priority"],
            "due_date": task_data["due_date"],
            "status": "Pending",
        }
        self.storage.save_task(task)

    def get_all_tasks(self):
        """Retourne toutes les tâches"""

        return self.storage.load_tasks()
