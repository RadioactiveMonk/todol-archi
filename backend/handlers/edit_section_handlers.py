from backend.database.db_manager import DbManager
from backend.core.logger import logger


class TaskHandlers:
    """Manages the interaction with the db for edit sections handlers"""

    def __init__(self) -> None:
        self.db = DbManager()

    def delete_handler(self, task_id: int) -> bool:
        """Deletes the row task from the DB."""

        result = self.db.delete_task(task_id)
        if result:
            logger.info(f"EDIT SECTION: task deleted successfully -- {task_id}")
        else:
            logger.warning(f"EDIT SECTION: task couldn't be deleted -- {task_id}")
        return result

    def edit_handler(self, task_id: int, **kwargs) -> bool:
        """Updates a task in the DB"""
        if not kwargs:
            logger.info(f"EDIT SECTION: Nofields provided to update task {task_id}")

        result = self.db.update_task(task_id, **kwargs)

        if result:
            logger.info(f"EDIT SECTION: task {task_id} updated successfully -- Changes: {kwargs}")
        else: logger.warning(f"EDIT SECTION: task {task_id} couldn't be updated -- No changes applied")

        return result