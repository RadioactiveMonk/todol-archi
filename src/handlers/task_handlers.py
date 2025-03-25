from dataclasses import asdict

from src.core.logger import logger
from src.core.database.db_manager import DbManager
from src.models.task import Task


class TaskHandlers:
    """Manages the interaction with the db for deleting and editing a task"""

    def __init__(self, db: DbManager | None = None) -> None:
        self.db = db if db is not None else DbManager()

    def delete_handler(self, task_id: int) -> bool:
        """Deletes a task from the DB

        Parameters
        ----------
        task_id : int
            ID of the task to delete

        Returns
        -------
        bool
            True if the task was deleted successfully, False otherwise
        """

        result = self.db.delete_task(task_id)
        if result:
            logger.info(f"🗑 Task deleted successfully (id={task_id})")
        else:
            logger.warning(f"❌ Failed to delete task (id={task_id})")
        return result

    def edit_handler(self, task: Task) -> bool:
        """Edits a task in the DB

        Parameters
        ----------
        task : Task
            Task object to edit

        Returns
        -------
        bool
            True if the task was edited successfully, False otherwise
        """

        if task.tid is None:
            logger.warning("✏️ Cannot edit task: missing ID")
            return False

        data = asdict(task)
        task_id = data.pop("tid")  # ID à part
        filtered_data = {k: v for k, v in data.items() if v is not None}

        if not filtered_data:
            logger.warning(f"✏️ No fields provided for editing task (id={task_id})")
            return False

        result = self.db.update_task(task_id, **filtered_data)

        if result:
            logger.info(f"✅ Task updated (id={task_id}) -- Changes: {filtered_data}")
        else:
            logger.warning(
                f"⚠️ Task update failed (id={task_id}) -- No changes detected"
            )

        return result

    def toggle_task_status(self, task_id: int) -> bool:
        """Toggles the status of a task (completed or not)

        Parameters
        ----------
        task_id : int
            ID of the task to toggle

        Returns
        -------
        bool
            True if the task status was toggled successfully, False otherwise
        """

        tasks = self.db.get_tasks()
        task = next((t for t in tasks if t["id"] == task_id), None)

        if not task:
            logger.warning(f"[toggle_status] Task ID {task_id} introuvable.")
            return False

        new_status = not bool(task["completed"])
        success = self.db.update_task(task_id=task_id, completed=new_status)

        if success:
            logger.info(
                f"[toggle_status] Tâche ID {task_id} -> completed = {new_status}"
            )
        else:
            logger.warning(f"[toggle_status] Échec de mise à jour pour ID {task_id}")

        return success
