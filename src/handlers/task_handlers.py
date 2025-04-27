from dataclasses import asdict
from typing import Callable

from utils.path_utils import DB_FILE
from helpers.contextmanagers import open_db
from utils.log_utils import logger
from models.task import Task


class TaskHandlers:
    """Manages the interaction with the db for deleting and editing a task"""

    def __init__(self, refresh_callback: Callable | None = None) -> None:
        self.refresh_callback = refresh_callback

    def delete_handler(self, task_id: int) -> bool:
        """Deletes a task from the DB"""
        with open_db(DB_FILE) as db:
            result = db.delete_task(task_id)

        if result:
            logger.info(f"🗑 Task deleted successfully (id={task_id})")
        else:
            logger.warning(f"❌ Failed to delete task (id={task_id})")

        if self.refresh_callback:
            self.refresh_callback()

        return result

    def edit_handler(self, task: "Task") -> bool:
        """Edits a task in the DB"""
        if task.id is None:
            logger.warning("✏️ Cannot edit task: missing ID")
            return False

        data = asdict(task)
        task_id = data.pop("id")
        filtered_data = {k: v for k, v in data.items() if v is not None}

        if not filtered_data:
            logger.warning(f"✏️ No fields provided for editing task (id={task_id})")
            return False

        with open_db(DB_FILE) as db:
            result = db.update_task(task_id, **filtered_data)

        if result:
            logger.info(f"✅ Task updated (id={task_id}) -- Changes: {filtered_data}")
        else:
            logger.warning(
                f"⚠️ Task update failed (id={task_id}) -- No changes detected"
            )

        if self.refresh_callback:
            self.refresh_callback()

        return result

    def toggle_task_status(self, task_id: int) -> bool:
        """Toggles the status of a task (completed or not)"""
        with open_db(DB_FILE) as db:
            tasks = db.get_all_tasks()
            task = next((t for t in tasks if t["id"] == task_id), None)

            if not task:
                logger.warning(f"[toggle_status] Task ID {task_id} introuvable.")
                return False

            new_status = not bool(task["completed"])
            success = db.update_task(task_id=task_id, data=task)

        if success:
            logger.info(
                f"[toggle_status] Tâche ID {task_id} -> completed = {new_status}"
            )
        else:
            logger.warning(f"[toggle_status] Échec de mise à jour pour ID {task_id}")

        if self.refresh_callback:
            self.refresh_callback()

        return success
