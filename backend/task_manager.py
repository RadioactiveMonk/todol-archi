from uuid import uuid4
from backend.storage import Storage


class TaskManager:
    """Gère les tâches depuis storage"""

    def __init__(self) -> None:
        self.storage = Storage()

    def add_task(self, task_data):
        """Ajoute une tâche et la sauvegarde"""
        self.storage.save_task(task_data)

    def get_all_tasks(self):
        """Retourne toutes les tâches"""
        tasks = self.storage.load_tasks()
        return [task.to_dict() for task in tasks]
