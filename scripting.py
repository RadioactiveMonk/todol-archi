from typing import List, Optional, Any
import sqlite3
from backend.logger import logger
from backend.config.constants import DB_PATH
from backend.models.task import Task


class DatabaseController:
    """Gestion des requêtes SQL brutes et de la connexion à la base de données."""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path

    def _execute_query(
        self,
        query: str,
        params: tuple = (),
        fetchone: bool = False,
        fetchall: bool = False,
    ) -> Any:
        """Exécute une requête SQL avec gestion automatique des erreurs."""
        logger.debug(f"*SQL*: '{query}' | PARAMS: '{params}'")
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("BEGIN TRANSACTION;")
                cursor.execute(query, params)

                if fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                else:
                    result = cursor.lastrowid

                conn.commit()
                return result
        except sqlite3.DatabaseError as e:
            logger.error(f"Erreur SQL: {e}")
            return None


class DatabaseManager:
    """Interface haut niveau pour manipuler les données de la base via DatabaseController."""

    def __init__(self) -> None:
        self.db = DatabaseController()

    def add_task(self, task: Task) -> Optional[int]:
        """Ajoute une nouvelle tâche et retourne son ID."""
        query = "INSERT INTO tasks (status, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?);"
        params = (task.status, task.category, task.expiration, task.title, task.notes)

        task_id = self.db._execute_query(query, params)
        return task_id if task_id else None

    def update_task(self, task: Task) -> bool:
        """Met à jour une tâche existante."""
        if not task.tid:
            logger.warning("Impossible de mettre à jour une tâche sans ID.")
            return False

        query = "UPDATE tasks SET status = ?, category = ?, expiration = ?, title = ?, notes = ? WHERE id = ?;"
        params = (
            task.status,
            task.category,
            task.expiration,
            task.title,
            task.notes,
            task.tid,
        )

        result = self.db._execute_query(query, params)
        return result is not None

    def get_tasks(self, task_id: Optional[int] = None) -> List[dict]:
        """Récupère toutes les tâches ou une tâche spécifique si `task_id` est fourni."""
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
        """Supprime une tâche de la base de données."""
        query = "DELETE FROM tasks WHERE id = ?;"
        params = (task_id,)

        result = self.db._execute_query(query, params)
        return result is not None
