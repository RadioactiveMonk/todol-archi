from backend.logger import logger
from backend.models.task import Task
from typing import List, Dict, Any
from backend.db_controller import DbController


class DbManager:
    """Higher interface to manager DbController."""

    def __init__(self) -> None:
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
            logger.error("ERROR: task must contain a valid title.")

        query = "INSERT INTO tasks (status, category, expiration, title, notes) VALUES (?, ?, ?, ?, ?);"
        params = (
            int(task.status),
            task.category,
            task.expiration,
            task.title,
            task.notes,
        )

        task_id = self.db._execute_query(query, params, lastrowid=True)
        return task_id if task_id else None

    def update_task(self, task: Task) -> bool:
        """Update a task in DB.

        Parameters
        ----------
        task : Task
            instance of a task

        Returns
        -------
        bool
            True is updated, False if not
        """
        if not task.tid:
            logger.warning("WARNING: can't add a task without ID")
            return False

        query = "UPDATE tasks SET status = ?, category = ?, expiration = ?, title = ?, notes = ? WHERE id = ?;"
        params = (
            int(task.status),
            task.category,
            task.expiration,
            task.title,
            task.notes,
            task.tid,
        )

        result = self.db._execute_query(query, params, rowcount=True)
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
            a list of dictionnaries
        """
        query = "SELECT id, status, category, expiration, title, notes FROM tasks"
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

        query = "DELETE FROM tasks WHERE id = ?"
        params = (task_id,)

        result = self.db._execute_query(query, params)
        return not self.get_tasks(task_id)
