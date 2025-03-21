import sqlite3
from backend.core.logger import logger
from backend.models.task import Task
from typing import List
from backend.database.db_controller import DbController
from configuration.constants import SQL_DELETE_TASK, SQL_INSERT_TASK, SQL_SELECT_TASKS


class DbManager:
    """Higher interface to manage DbController."""

    def __init__(self) -> None:
        """Setting up DB with DbController()"""
        self.db = DbController()

    def add_task(self, task: Task) -> int | None:
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
            logger.error(f"ERROR: Cannot add task without title -- {task}")
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
            task_id = self.db._execute_query(query, params, lastrowid=True)
            if task_id:
                logger.info(f"Task added: {task_id}")
            else:
                logger.warning(f"Task insertion returned None")

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
            logger.warning(f"WARNING: can't update a task without ID -- {task_id}")
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

        updates = [f"{key} = ?" for key, value in fields.items() if value is not None]
        params = [value for value in fields.values() if value is not None]

        if not updates:
            logger.info("INFO: No fields to update for task ID %d", task_id)
            return False  # Rien à mettre à jour

        query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
        params.append(task_id)

        try:
            result = self.db._execute_query(query, tuple(params), rowcount=True)

            if result is None:
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

    def get_tasks(self, task_id: int | None = None) -> List[dict]:
        """Return all tasks by a list of dictionnaries.

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

        results = self.db._execute_query(query, params, fetchall=True)

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
            result = self.db._execute_query(query, params, rowcount=True)

            if result == 0:
                logger.warning(f"Task ID {task_id} not found in DB, deletion failed.")
                return False

            logger.info(f"Task ID {task_id} deleted successfully.")
            return True

        except sqlite3.DatabaseError as e:
            logger.error(f"Couldn't delete task ID {task_id}: {e}")
            return False



        
