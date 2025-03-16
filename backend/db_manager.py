from backend.logger import logger
from backend.models.task import Task
from typing import List, Dict, Any
from backend.db_controller import DbController


class DbManager:
    """Interface haut niveau pour manipuler les données SQL de DbController"""

    def __init__(self) -> None:
        self.db = DbController()

    def add_task(self, task: Task) -> int | None:
        """Ajoute une nouvelle tâche et retourne son ID"""
        query = "INSERT INTO tasks (status, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?);"
        params = (
            int(task.status),
            task.category,
            task.expiration,
            task.title,
            task.notes,
        )

        task_id = self.db._execute_query(query, params)
        return task_id if task_id else None

    def update_task(self, task: Task) -> bool:
        """Met à jour une tâche existente, retourne un booléen"""
        if not task.tid:
            logger.warning("Impossible de mettre à jour une tâche sans ID")
            return False

        query = "UPDATE tasks SET status = ?, category = ?, expiration = ?, title = ?, notes = ? WHERE id = ?;"
        params = (
            int(task.status),
            task.category,
            task.expiration,
            task.title,
            task.notes,
            task.tid,
        )

        result = self.db._execute_query(query, params)
        return result is not None

    def get_tasks(self, task_id: int | None = None) -> List[dict]:
        """Récupère toutes les tâches ou UNE tâche spécifique si 'task_id' est donné"""

        query = "SELECT id, status, category, expiration, title, notes FROM tasks"
        if task_id:
            query += " WHERE id = ?"

        params = (task_id,) if task_id else ()
        results = self.db._execute_query(query, params, fetchall=True)

        return (
            [
                {
                    "id": row[0],
                    "status": row[1],
                    "category": row[2],
                    "expiration": row[3],
                    "title": row[4],
                    "notes": row[5],
                }
                for row in results
            ]
            if results
            else []
        )

    def delete_task(self, task_id: int) -> bool:
        """Supprime une tâche en DB.

        Parameters
        ----------
        task_id : int
            l'id de la tâche en DB

        Returns
        -------
        bool
            True si la tâche est supprimée, sinon False.
        """
        if not self.get_tasks(task_id):
            return False
        
        query = "DELETE FROM tasks WHERE id = ?"
        params = (task_id,)

        result = self.db._execute_query(query, params)
        return self.get_tasks(task_id) is None
