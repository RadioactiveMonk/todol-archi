from backend.logger import logger
from backend.models.task import Task
from typing import List, Dict, Any
from backend.db_controller import DbController


class DbManager:
    """Higher interface to manager DbController."""

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
            logger.warning("WARNING: can't add a task without ID")
            return False

        updates = []
        params = []

        if status is not None:
            updates.append("status = ?")
            params.append(int(status))

        if category is not None:
            updates.append("category = ?")
            params.append(category)

        if expiration is not None:
            updates.append("expiration = ?")
            params.append(expiration)

        if title is not None:
            updates.append("title = ?")
            params.append(title)

        if notes is not None:
            updates.append("notes = ?")
            params.append(notes)

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
