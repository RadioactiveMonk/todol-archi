import sqlite3
from typing import Any, Callable

from core.database_config import (
    SQL_DELETE_TASK_BY_ID,
    SQL_INSERT_TASK,
    SQL_SELECT_TASK_BY_ID,
    SQL_SELECT_TASKS,
    SQL_UPDATE_TASK_BY_ID,
)
from core.sql_schema import SQL_CREATE_TASKS_TABLE
from helpers.log_utils import logger


class AskDB:
    """
    Classe d'accès simplifiée à la base de données SQLite.
    Permet d'exécuter des opérations courantes de manière centralisée.
    """

    def __init__(self, conn: sqlite3.Connection) -> None:
        """
        Initialise une instance de AskDB.

        Args:
            conn: Une connexion sqlite3 active.
        """
        self.conn = conn
        self.conn.row_factory = sqlite3.Row  # Récupérer les rangées sous forme de dict

        self.routes: dict[str, Callable[..., Any]] = {
            "create": self.create,
            "insert": self.insert,
            "select": self.select,
            "select_one": self.select_one,
            "delete": self.delete,
        }

    def ask(self, action: str, sql: str, *args: Any) -> Any:
        """
        Route une commande SQL vers la bonne méthode (create, insert, select, etc).

        Args:
            action: Le nom de l'action (doit correspondre à une clé de self.routes)
            sql: La requête SQL à exécuter.
            *args: Les arguments de la requête.

        Returns:
            Le résultat de la méthode appelée.
        """
        logger.debug(
            f"Dispatching SQL actions via ask(): {action} -> {sql} | args={args}"
        )
        return self.routes[action](sql, *args)

    def create(self, sql: str) -> None:
        """
        Exécute une requête SQL de type CREATE TABLE.

        Args:
            sql: Requête SQL de création.
        """
        logger.debug(f"Executing CREATE TABLE: {sql}\n")
        self.conn.execute(sql)
        self.conn.commit()

    def insert(self, sql: str, *args: Any) -> int | None:
        """
        Exécute une requête SQL de type INSERT INTO.

        Args:
            sql: Requête INSERT.
            *args: Paramètres de la requête.

        Returns:
            ID de la dernière ligne insérée.
        """
        logger.debug(f"Executing INSERT INTO: {sql} | args={args}")
        cursor = self.conn.execute(sql, args)
        self.conn.commit()
        return cursor.lastrowid

    def select(self, sql: str, *args: Any) -> list[dict[str, Any]]:
        """
        Exécute une requête SELECT et retourne toutes les lignes.

        Args:
            sql: Requête SELECT.
            *args: Paramètres de la requête.

        Returns:
            Liste de dictionnaires représentant les lignes.
        """
        logger.debug(f"Executing SELECT: {sql} | args={args}")
        cursor = self.conn.execute(sql, args)
        return [dict(row) for row in cursor.fetchall()]

    def select_one(self, sql: str, *args: Any) -> dict[str, Any] | None:
        """
        Exécute une requête SELECT et retourne la première ligne (ou None).

        Args:
            sql: Requête SELECT avec WHERE.
            *args: Paramètres de la requête.

        Returns:
            Un dictionnaire ou None.
        """
        logger.debug(f"Executing SELECT: {sql} | args={args}")
        cursor = self.conn.execute(sql, args)
        row = cursor.fetchone()
        return dict(row) if row else None

    def delete(self, sql: str, *args: Any) -> bool:
        """
        Exécute une requête DELETE.

        Args:
            sql: Requête DELETE.
            *args: Paramètres de la requête.

        Returns:
            True si des lignes ont été supprimées, sinon False.
        """
        logger.debug(f"Executing DELETE FROM: {sql} | args={args}")
        cursor = self.conn.execute(sql, args)
        self.conn.commit()
        return cursor.rowcount > 0

    # Méthodes alias spécifiques à l'application

    def create_tasks_table(self) -> None:
        """Crée la table principale des tâches si elle n'existe pas."""
        self.create(SQL_CREATE_TASKS_TABLE)

    def add_task(
        self, *, title: str, category: str, completed: bool, expiration: str, notes: str
    ) -> int | None:
        """
        Insère une nouvelle tâche dans la base de données.

        Returns:
            ID de la tâche insérée.
        """
        return self.insert(
            SQL_INSERT_TASK, title, category, int(completed), expiration, notes
        )

    def get_all_tasks(self) -> list[dict[str, Any]]:
        """Retourne toutes les tâches enregistrées."""
        return self.select(SQL_SELECT_TASKS)

    def get_task_by_id(self, task_id: int) -> dict[str, Any] | None:
        """Retourne une tâche par son ID, ou None si introuvable."""
        return self.select_one(SQL_SELECT_TASK_BY_ID, task_id)

    def update_task(self, task_id: int, data: dict[str, Any]) -> bool:
        """
        Met à jour une tâche existante.

        Args:
            task_id: L'identifiant de la tâche à modifier.
            data: Un dictionnaire contenant les champs à modifier.

        Returns:
            True si la tâche a été modifiée, sinon False.
        """
        return (
            self.conn.execute(
                SQL_UPDATE_TASK_BY_ID,
                (
                    data["title"],
                    data["category"],
                    int(data["completed"]),
                    data["expiration"],
                    data["notes"],
                    task_id,
                ),
            ).rowcount
            > 0
        )

    def delete_task(self, task_id: int) -> bool:
        """
        Supprime une tâche par son ID.

        Args:
            task_id: ID de la tâche à supprimer.

        Returns:
            True si la tâche a été supprimée, sinon False.
        """
        return self.delete(SQL_DELETE_TASK_BY_ID, task_id)
