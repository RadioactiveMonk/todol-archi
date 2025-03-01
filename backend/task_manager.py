from uuid import uuid4
from backend.storage import Storage
from backend.task import Task
from typing import List, Dict, Any, Optional, Union


class TaskManager:
    """Gère les tâches depuis storage"""

    def __init__(self) -> None:
        self.storage = Storage()

    def add_task(self, task_data):
        """Ajoute une tâche et la sauvegarde"""
        self.storage.save_task(task_data)

    def get_all_tasks(self) -> List[Task]:
        """Retourne toutes les tâches"""
        
        return self.storage.load_tasks()
