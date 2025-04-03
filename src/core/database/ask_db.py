import sqlite3
from typing import Any, List

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

    def select(self, sql: str, *args: Any) -> List[tuple]:
        logger.debug(f"Executing SELECT: {sql} | args={args}")

        return self.conn.execute(sql, args).fetchall()

    def select_one(self, sql: str, *args: Any) -> tuple | None:
        logger.debug(f"Executing SELECT: {sql} | args={args}")

        return self.conn.execute(sql, args).fetchone()

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

    def get_all_tasks(self) -> List[tuple]:
        return self.select(SQL_SELECT_TASKS)

    def get_task_by_id(self, task_id: int) -> tuple | None:
        return self.select_one(SQL_SELECT_TASK_BY_ID, task_id)

    def update_task(
        self,
        task_id: int,
        title: str,
        category: str,
        completed: bool,
        expiration: str,
        notes: str,
    ) -> bool:
        
        updated = self.update(
            SQL_UPDATE_TASK_BY_ID,
            title,
            category,
            int(completed),
            expiration,
            notes,
            task_id,
        )
        return updated > 0

    def delete_task(self, task_id: int) -> bool:

        deleted = self.delete(SQL_DELETE_TASK_BY_ID, task_id)
        return deleted > 0
