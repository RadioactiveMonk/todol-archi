from dataclasses import asdict
from backend.database.db_manager import DbManager
from backend.core.logger import logger
from backend.models.task import Task


class TaskHandlers:
    """Manages the interaction with the db for edit sections handlers"""

    def __init__(self) -> None:
        self.db = DbManager()

    def delete_handler(self, task_id: int) -> bool:
        """Deletes the row task from the DB."""

        result = self.db.delete_task(task_id)
        if result:
            logger.info(f"🗑 Task deleted successfully (id={task_id})")
        else:
            logger.warning(f"❌ Failed to delete task (id={task_id})")
        return result

    def edit_handler(self, task: Task) -> bool:
        """Updates a task in the DB"""

        if task.tid is None:
            logger.warning(f"✏️ Cannot edit task: missing ID")
            return False

        data = asdict(task)
        task_id = data.pop("tid")  # ID à part
        filtered_data = {k: v for k,v in data.items() if v is not None}

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
