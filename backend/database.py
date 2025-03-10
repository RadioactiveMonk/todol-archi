import sqlite3
from typing import List
from backend.database_controler import DatabaseControler
from backend.task import Task
from backend.config.configs import DB_PATH
from backend.config.constants import NO_ID


class DatabaseManager:
    """Gestion de la base de données en utilisant un Singleton"""

    def __init__(self) -> None:
        self.actions = {
            "add_task": self.add_task,
            "update_task": self.update_task,
            "delete_task": self.del_task,
            "get_tasks": self.get_tasks,
        }
        self.db = DatabaseControler()

    def execute(self, action: str, *args, **kwargs):
        """Exécute une action sur la base de données via dict dispatch."""
        return self.actions.get(action, lambda *a, **kw: None)(*args, **kwargs)

    def add_task(
        self, status: bool, category: str, expiration: str, title: str, notes: str
    ) -> Task:
        """Ajoute une tâche à la base et retourne l'objet Task correspondant."""
        query = self.db.queries["insert_task"]
        params = 
        return Task(
            tid=task_id,
            status=status,
            category=category,
            expiration=expiration,
            title=title,
            notes=notes,
        )

    def update_task(self, task: Task) -> None:
        """Met à jour une tâche existante dans la base de données."""
        query = self.db.queries["update_task"]
        self.db._request(
            query,
            (
                task.status,
                task.category,
                task.expiration,
                task.title,
                task.notes,
                task.tid,
            ),
        )

    def del_task(self, task_id: int) -> None:
        """Supprime une tâche"""

        query = self.db.queries["delete_task"]
        if task_id != NO_ID:
            self.db._request(query, (task_id,))

    def get_tasks(self) -> List[Task] | List:
        """Récupère toutes les tâches de la BDD en utilisant _request()"""
        query = self.db.queries["get_tasks"]
        rows = self.db._request(query)
        return [Task(*row) for row in rows] if rows else []
