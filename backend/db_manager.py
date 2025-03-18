from backend.logger import logger
from backend.models.task import Task
from typing import List
from backend.db_controller import DbController
from backend.config.constants import SQL_DELETE_TASK, SQL_INSERT_TASK, SQL_SELECT_TASKS


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

        query = SQL_INSERT_TASK
        params = (
            int(task.status),
            task.category,
            task.expiration,
            task.title,
            task.notes,
        )

        task_id = self.db._execute_query(query, params, lastrowid=True)
        return task_id if task_id else None

    def update_task(
        self,
        task_id: int,
        status: bool | None = None,
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
        status : bool (optional)
            new status of the task (if provided)
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
            logger.warning(f"WARNING: can't add a task without ID -- {task_id}")
            return False

        updates = []
        params = []

        fields = {
            "status": int(status) if status is not None else None,
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

        result = self.db._execute_query(query, tuple(params), rowcount=True)
        return result > 0

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
                    "status": row[1],
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
            the task id in DB

        Returns
        -------
        bool
            True if deleted, false if not.
        """
        if not self.get_tasks(task_id):
            return False

        query = SQL_DELETE_TASK
        params = (task_id,)

        result = self.db._execute_query(query, params, rowcount=True)

        return result > 0
