import sqlite3
from typing import List, Dict, Any, Optional, Union
from backend.task import Task
from backend.config import DB_PATH
from backend.constants import DEFAULT_STATUS


class DatabaseManager:
    """Gestion de la base de donnée."""

    def __init__(self, db_path: str = DB_PATH) -> None:
        """Initialise la connexion et crée une table si besoin"""

        self.db_path = db_path
        self._create_table()

    def _connect(self):
        """Etablit la connexion avec SQLite"""

        return sqlite3.connect(self.db_path)

    def _create_table(self):
        """Crée la table des tâches si elle n'existe pas"""

        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status BOOLEAN,
            category TEXT,
            expiration TEXT,
            title TEXT NOT NULL,
            notes TEXT)
            """
        )

        conn.commit()
        conn.close()

    def add_task(
        self, status: bool, category: str, expiration: str, title: str, notes: str
    ) -> Task:
        """Ajoute ue tâche à la base"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (status, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?)",
            (status, category, expiration, title, notes),
        )

        conn.commit()

        task_id = cursor.lastrowid

        conn.close()
        return Task(
            tid=task_id,
            status=status,
            category=category,
            expiration=expiration,
            title=title,
            notes=notes,
        )

    def update_task(self, task_id: int) -> None:
        pass

    def del_task(self, task_id: int) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        """Récupère toutes les tâches de la BDD"""

        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, status, category, expiration, title, notes FROM tasks"
        )

        rows = cursor.fetchall()
        conn.close()

        return [
            Task(
                tid=row[0],
                status=bool(row[1]),
                category=row[2],
                expiration=row[3],
                title=row[4],
                notes=row[5],
            )
            for row in rows
        ]
