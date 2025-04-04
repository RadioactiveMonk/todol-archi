import sqlite3
from typing import Any, Dict, List

from core.database_config import (
    SQL_DELETE_TASK_BY_ID,
    SQL_INSERT_TASK,
    SQL_SELECT_TASK_BY_ID,
    SQL_SELECT_TASKS,
    SQL_UPDATE_TASK_BY_ID,
)
from helpers.log_utils import logger


class AskDB:
    def __init__(self, conn: sqlite3.Connection):
        conn.row_factory = sqlite3.Row
        self.conn = conn
        self.routes = {
            "exec": self.exec,
            "create": self.create,
            "insert": self.insert,
            "select": self.select,
            "select_one": self.select_one,
            "update": self.update,
            "delete": self.delete,
            "drop": self.drop,
        }

    def ask(self, action: str, sql: str, *args: Any) -> Any:
        """Docstrings"""

        if action not in self.routes:
            raise ValueError(f"Unknown DB action: '{action}'")

        logger.debug(
            f"Dispatching SQL actions via ask(): {action} -> {sql} | args={args}"
        )

        return self.routes[action](sql, *args)

    def exec(self, sql: str, *args: Any) -> None:
        logger.debug(f"Executing: {sql} | args={args}")

        self.conn.execute(sql, args)

    def create(self, sql: str) -> None:
        logger.debug(f"Executing CREATE TABLE: {sql}")

        self.conn.execute(sql)

    def insert(self, sql: str, *args: Any) -> int | None:
        logger.debug(f"Executing INSERT INTO: {sql} | args={args}")

        cursor = self.conn.execute(sql, args)
        self.conn.commit()
        return cursor.lastrowid

    def select(self, sql: str, *args: Any) -> List[Dict[str, Any]]:
        logger.debug(f"Executing SELECT: {sql} | args={args}")

        rows = self.conn.execute(sql, args).fetchall()
        return [dict(row) for row in rows]

    def select_one(self, sql: str, *args: Any) -> Dict[str, Any] | None:
        logger.debug(f"Executing SELECT: {sql} | args={args}")

        row = self.conn.execute(sql, args).fetchone()
        return dict(row) if row else None

    def update(self, sql: str, *args: Any) -> int:
        logger.debug(f"Executing UPDATE FROM: {sql} | args={args}")

        cursor = self.conn.execute(sql, args)
        self.conn.commit()
        return cursor.rowcount

    def delete(self, sql: str, *args: Any) -> int:
        logger.debug(f"Executing DELETE FROM: {sql} | args={args}")

        cursor = self.conn.execute(sql, args)
        self.conn.commit()
        return cursor.rowcount

    def drop(self, sql: str) -> None:
        logger.debug(f"Executing DROP TABLE: {sql}")

        self.conn.execute(sql)

    def add_task(
        self, title: str, category: str, completed: bool, expiration: str, notes: str
    ) -> int | None:
        return self.insert(
            SQL_INSERT_TASK, title, category, int(completed), expiration, notes
        )

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        return self.select(SQL_SELECT_TASKS)

    def get_task_by_id(self, task_id: int) -> Dict[str, Any] | None:
        return self.select_one(SQL_SELECT_TASK_BY_ID, task_id)

    def update_task(self, task_id: int, **kwargs) -> bool:
        """
        Met à jour une tâche avec les champs précisés.
        Tous les paramètres sont optionnels, sauf l'ID.
        """
        valid_keys = ("title", "category", "completed", "expiration", "notes")
        fields = []
        values = []

        for key in valid_keys:
            if key in kwargs:
                fields.append(f"{key} = ?")
                value = kwargs[key]
                if key == "completed":
                    value = int(value)
                values.append(value)

        if not fields:
            logger.warning(f"⚠️ Aucun champ fourni pour mise à jour de la tâche ID {task_id}")
            return False

        sql = f"UPDATE tasks SET {', '.join(fields)} WHERE id = ?;"
        values.append(task_id)

        logger.debug(f"Executing DYNAMIC UPDATE: {sql} | args={tuple(values)}")
        cursor = self.conn.execute(sql, values)
        self.conn.commit()
        return cursor.rowcount > 0


    def delete_task(self, task_id: int) -> bool:
        deleted = self.delete(SQL_DELETE_TASK_BY_ID, task_id)
        return deleted > 0
