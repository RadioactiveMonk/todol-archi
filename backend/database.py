import sqlite3
from typing import List, Dict, Any, Optional
from backend.task import Task
from backend.config.configs import DB_PATH
from backend.config.constants import DEFAULT_STATUS, NO_ID


class DatabaseManager:
    """Gestion de la base de donnée en utilisant un Singleton"""

    _instance = None  # Stocke l'instance unique
    _conn: sqlite3.Connection | None = None

    def __new__(cls, db_path: str = DB_PATH):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.db_path = db_path
            cls._instance._conn = sqlite3.connect(db_path)
            cls._instance._create_table()
        return cls._instance

    def _connect(self) -> sqlite3.Connection:
        """Etablit la connexion avec SQLite. Condition pour détecter la connexion"""
        assert self._conn, "Connection to database not initialized"
        return self._conn

    def _request(
        self, db_path: str = DB_PATH, request: str = "", params: tuple = ()
    ) -> list | None:
        """Exécute une requête SQL et retourne les résultats si nécessaire(ex: SELECT)."""

        self.db_path = db_path
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(request, params)

        data = (
            cursor.fetchall() if request.strip().upper().startswith("SELECT") else None
        )  # 🔥 Récupère les résultats si SELECT

        conn.commit()  # ON NE FERME PAS LA CONNEXION, on la ferme a la fermeture de l'appli (main.py)

        return data

    def _create_table(self) -> None:
        """Crée la table des tâches si elle n'existe pas"""

        self._request(
            self.db_path,
            """
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status BOOLEAN,
            category TEXT,
            expiration TEXT,
            title TEXT NOT NULL,
            notes TEXT)
            """,
        )

    def _close_connection(self) -> None:
        """Ferme la connexion a la db si ouverte"""
        if self._conn:
            self._conn.close()
            self._conn = None

    def add_task(
        self, status: bool, category: str, expiration: str, title: str, notes: str
    ) -> Task:
        """Ajoute une tâche à la base et retourne l'objet Task correspondant."""

        request = "INSERT INTO tasks (status, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?)"

        # 🔥 On exécute la requête et récupère l'ID de la tâche insérée
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(request, (status, category, expiration, title, notes))
        task_id = cursor.lastrowid or NO_ID  # Récupère l'ID de la tâche ajoutée
        conn.commit()

        # 🔥 On retourne une instance Task avec l'ID récupéré
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

        request = """
            UPDATE tasks 
            SET status = ?, category = ?, expiration = ?, title = ?, notes = ?
            WHERE id = ?
        """

        self._request(
            self.db_path,
            request,
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
        request = "DELETE FROM tasks WHERE id = ?"
        if task_id != NO_ID:
            self._request(self.db_path, request, (task_id,))

    def get_tasks(self) -> List[Task] | List:
        """Récupère toutes les tâches de la BDD en utilisant _request()"""

        rows = self._request(
            self.db_path,
            "SELECT id, status, category, expiration, title, notes FROM tasks",
        )

        return (
            [
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
            if rows
            else []
        )
