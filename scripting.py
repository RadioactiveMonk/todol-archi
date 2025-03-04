import sqlite3
from typing import List, Optional
from backend.task import Task
from backend.config import DB_PATH


class DatabaseManager:
    """Gestion de la base de donnée avec Singleton."""

    _instance = None  # Stocke l'instance unique

    def __new__(cls, db_path: str = DB_PATH):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.db_path = db_path
            cls._instance._create_table()
            cls._instance._conn = sqlite3.connect(db_path)  # Connexion unique
        return cls._instance

    def _connect(self):
        """Renvoie la connexion existante."""
        return self._conn

    def _create_table(self):
        """Crée la table des tâches si elle n'existe pas."""
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

    def _request(self, request: str, params: tuple = ()) -> Optional[list]:
        """Exécute une requête SQL et retourne les résultats si nécessaire."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(request, params)
        data = (
            cursor.fetchall() if request.strip().upper().startswith("SELECT") else None
        )
        conn.commit()
        return data

    # 🔥 Pas besoin de changer get_tasks, add_task, del_task, update_task, ils utilisent _request()
