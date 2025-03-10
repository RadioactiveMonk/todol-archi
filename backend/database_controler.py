import sqlite3
from typing import Any

from backend.config.configs import DB_PATH


class DatabaseControler:
    """Méthodes privées pour la manipulation de la BDD"""

    def __init__(self) -> None:
        """Dictionnaire des requêtes"""
        self.queries = {
            "insert_task": "INSERT INTO tasks (status, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?)",
            "update_task": "UPDATE tasks SET status = ?, category = ?, expiration = ?, title = ?, notes = ? WHERE id = ?",
            "update_task_status": "UPDATE tasks SET status = ? WHERE id = ?",
            "delete_task": "DELETE FROM tasks WHERE id = ?",
            "get_tasks": "SELECT id, status, category, expiration, title, notes FROM tasks",
        }

    def _execute(self, query: str, params: tuple = ()) -> Any:
        """Execute une requête SQL avec gestion de la connexion automatique"""

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()  # Retourne les résultats si requête SELECT

    def _request(self, query_key: str, params: tuple = ()):
        """Execute une requête SQL du dict dispatch 'self.queries'"""

        query = self.queries.get(query_key)
        if query:
            return self._execute(query, params)
        return None
