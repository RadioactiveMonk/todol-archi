import sqlite3
from typing import List
from backend.database_controler import DatabaseControler
from backend.task import Task
from backend.logger import logger
from backend.config.constants import NO_ID


class DatabaseManager:
    """Gestion de la base de données en utilisant un Singleton"""

    def __init__(self) -> None:
        self.actions = {
            "add_task": self.add_task,
            "update_task": self.update_task,
            "update_task_status": self.update_task_status,
            "delete_task": self.del_task_db,
            "get_tasks": self.get_tasks,
        }
        self.db = DatabaseControler()

    def execute(self, action: str, *args, **kwargs):
        """Exécute une action sur la base de données via dict dispatch."""
        if action not in self.actions:
            raise ValueError(f"Action inconnue: {action}")
        return self.actions[action](*args, **kwargs)

    def add_task(
        self, status: bool, category: str, expiration: str, title: str, notes: str
    ) -> Task:
        """Ajoute une tâche à la base et retourne l'objet Task correspondant."""
        query = self.db._queries["insert_task"]
        params = (status, category, expiration, title, notes)

        task_id = self.db._exec_query(query, params)

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

        logger.info(
            f"Mise à jour de la tâche: ID={task.tid}, Title='{task.title}', Status={task.status}"
        )
        self.db._request(
            "update_task",
            (
                int(task.status),
                task.category,
                task.expiration,
                task.title,
                task.notes,
                task.tid,
            ),
        )

    def update_task_status(self, status: bool, task_id: int) -> None:
        """Met à jour le statut d'une tâche dans la DB"""

        self.db._request(
            "update_task_status",
            (int(status), task_id),
        )

    def del_task_db(self, task_id: int) -> None:
        """Supprime une tâche"""

        if task_id != NO_ID:
            self.db._request("delete_task", (task_id,))

    def get_tasks(self) -> List[Task] | List:
        """Récupère toutes les tâches de la BDD et convertit `status` en bool"""
        rows = self.db._request("get_tasks")
        return (
            [
                Task(
                    tid=row[0],
                    status=bool(row[1]),  # Convertit `0/1` en `False/True`
                    category=row[2],
                    expiration=row[3],
                    title=row[4],
                    notes=row[5],
                )
                for row in rows
            ]
            if rows
            else []
        )
