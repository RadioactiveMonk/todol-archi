import sqlite3
from typing import List
from backend.task import Task

class DatabaseManager:
    """Gestion de la base de données SQLite."""

    def __init__(self, db_path: str = "tasks.db") -> None:
        """Initialise la connexion et crée la table si nécessaire."""
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        """Établit une connexion avec SQLite."""
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        """Crée la table des tâches si elle n'existe pas."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN DEFAULT 0
            )
        """
        )
        conn.commit()
        conn.close()

    def add_task(self, title: str) -> Task:
        """Ajoute une tâche dans la base de données."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, ?)", (title, False)
        )
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return Task(task_id=task_id, title=title, completed=False)

    def update_task(self, task_id: int, completed: bool) -> None:
        """Met à jour l'état d'une tâche."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id)
        )
        conn.commit()
        conn.close()

    def del_task(self, task_id: int) -> None:
        """Supprime une tâche par son ID."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

    def get_tasks(self) -> List[Task]:
        """Récupère toutes les tâches."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, completed FROM tasks")
        rows = cursor.fetchall()
        conn.close()
        return [
            Task(task_id=row[0], title=row[1], completed=bool(row[2])) for row in rows
        ]
