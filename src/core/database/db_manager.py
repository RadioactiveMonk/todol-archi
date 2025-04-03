import sqlite3
from typing import TYPE_CHECKING, List

# from core.database.db_controller import DbController
from core.database_config import (
    SQL_DELETE_TASK_BY_ID,
    SQL_INSERT_TASK,
    SQL_SELECT_TASKS,
)
from helpers.log_utils import logger

if TYPE_CHECKING:
    from models.task import Task


class DbManager:
    """Higher interface to manage DbController."""

    def __init__(self, controller: DbController | None = None) -> None:
        """Setting up DB with DbController()"""
        self.controller = controller if controller else DbController()

    def add_task(self, task: "Task") -> int | None:
        """Add a task in the DB.

        Parameters
        ----------
        task : Task
            instance of a task (task.py)

        Returns
        -------
        int | None
            return the id of the task if added, None if not
        """

        if not task.title:
            logger.error(f"Cannot add task without title -- {task}")
            return None

        query = SQL_INSERT_TASK
        params = (
            int(task.completed),
            task.category,
            task.expiration,
            task.title,
            task.notes,
        )
        try:
            task_id = self.controller._execute_query(query, params, lastrowid=True)
            if task_id:
                logger.info(f"Task added: {task_id}")
                task.tid = task_id
            else:
                logger.warning("Task insertion returned None")

            return task_id

        except sqlite3.DatabaseError as e:
            logger.error(f"Task couldn't be added: {e}")
            return None

    def update_task(
        self,
        task_id: int,
        completed: bool | None = None,
        category: str | None = None,
        expiration: str | None = None,
        title: str | None = None,
        notes: str | None = None,
    ) -> bool:
        """Update task in DB

        Parameters
        ----------
        task_id : int
            id of the task to update
        completed : bool (optional)
            new completed of the task (if provided)
        category : str (optional)
            new category of the task (if provided)
        expiration : str (optional)
            new due date of the task (if provided)
        title : str (optional)
            new title of the task (if provided)
        notes : str (optional)
            new notes of the task (if provided)

        Returns
        -------
        bool
            True if task updated, false if not
        """

        if not task_id:
            logger.warning(f"Can't update a task without ID -- {task_id}")
            return False

        updates = []
        params = []

        fields = {
            "completed": int(completed) if completed is not None else None,
            "category": category,
            "expiration": expiration,
            "title": title,
            "notes": notes,
        }

        filtered_fields = {k: v for k, v in fields.items() if v is not None}
        updates = [f"{k} = ?" for k in filtered_fields]
        params = list(filtered_fields.values())

        if not updates:
            logger.info("No fields to update for task ID %d", task_id)
            return False  # Rien à mettre à jour

        query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
        params.append(task_id)

        try:
            result = self.controller.execute_and_confirm(
                query, tuple(params), log_context=f"Updating task ID {task_id}"
            )

            if result == 0:
                logger.warning(
                    f"SQL query executed but no row was affected for task ID {task_id}"
                )
                return False

            if result > 0:
                logger.info(f"Task updated (ID: {task_id}): {fields}")

            return result > 0

        except sqlite3.DatabaseError as e:
            logger.error(f"Task couldn't be updated (ID: {task_id}): {e}")
            return False

    def get_tasks(self, task_id: int | None = None) -> List[dict[str, object]]:
        """Return all tasks by a list of dictionnaries. If task_id is provided, return the corresponding task.

        Parameters
        ----------
        task_id : int | None, optional
            the task id in db, by default None

        Returns
        -------
        List[dict]
            a list of dictionnaries representing a task
        """

        query = SQL_SELECT_TASKS
        if task_id:
            query += " WHERE id = ?"

        params = (task_id,) if task_id else ()

        results = self.controller._execute_query(query, params, fetchall=True)

        return (
            [
                {
                    "id": row[0],
                    "completed": row[1],
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
        """Delete a task in DB.

        Parameters
        ----------
        task_id : int
            The task ID in DB

        Returns
        -------
        bool
            True if deleted, False if not.
        """

        if not self.get_tasks(task_id):
            logger.warning(f"Task ID {task_id} not found, cannot delete.")
            return False

        query = SQL_DELETE_TASK
        params = (task_id,)

        logger.debug(f"Attempting to delete task ID {task_id}")

        try:
            result = self.controller.execute_and_confirm(
                query, params, log_context=f"Deleting task ID {task_id}"
            )

            if result == 0:
                logger.warning(f"Task ID {task_id} not found in DB, deletion failed.")
                return False

            logger.info(f"Task ID {task_id} deleted successfully.")
            return True

        except sqlite3.DatabaseError as e:
            logger.error(f"Couldn't delete task ID {task_id}: {e}")
            return False
