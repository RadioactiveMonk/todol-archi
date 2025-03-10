import sqlite3
from typing import Any

from backend.config.configs import DB_PATH


class DatabaseControler:
    """Méthodes privées pour la manipulation de la BDD"""

    _instance = None  # Stocke l'instance unique
    _queries = {
        "create_table": """CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        status BOOLEAN,
                        category TEXT,
                        expiration TEXT,
                        title TEXT NOT NULL,
                        notes TEXT
                    )
                """,
        "insert_task": "INSERT INTO tasks (status, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?)",
        "update_task": "UPDATE tasks SET status = ?, category = ?, expiration = ?, title = ?, notes = ? WHERE id = ?",
        "update_task_status": "UPDATE tasks SET status = ? WHERE id = ?",
        "delete_task": "DELETE FROM tasks WHERE id = ?",
        "get_tasks": "SELECT id, status, category, expiration, title, notes FROM tasks",
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._queries
            cls._instance._create_table()
        return cls._instance

    def _exec_query(
        self, query: str, params: tuple = (), return_lastrowid: bool = False
    ) -> Any:
        """Execute une requête SQL avec gestion de la connexion automatique"""

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

            if return_lastrowid:
                return cursor.lastrowid

            return (
                cursor.fetchall()
                if query.strip().upper().startswith("SELECT")
                else None
            )  # Retourne les résultats si requête SELECT

    def _request(self, query_key: str, params: tuple = ()):
        """Execute une requête SQL du dict dispatch 'self.queries'"""
        if query_key not in self._queries:
            raise ValueError(f"Requête inconnue: {query_key}")

        return self._exec_query(self._queries.get(query_key, ""), params)

    def _create_table(self) -> None:
        """Crée la table des tâches si elle n'existe pas"""

        self._request("create_table")
