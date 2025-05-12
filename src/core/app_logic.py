from typing import Any, Optional

from core.log_manager import logger
from models.task import Task
from models.task_table_column import TaskTableColumn
from models.task_table_core import TaskTable


class AppLogic:
    def __init__(self, tasks: list[Task], columns: list[TaskTableColumn]):
        self.tasks = tasks
        self.columns = columns
        self.task_table = TaskTable(self.tasks, self.columns)
        self.filters = {}
        self.sort_column: Optional[str] = None
        self.sort_reverse = False
        self.selected_task_id: Optional[int] = None

    def add_task(self, task: Task) -> None:
        self.task_table.add_task(task)

    def remove_task_by_id(self, task_id: int) -> None:
        self.task_table.remove_by_id(task_id)

    def toggle_task_status(self, task_id: int) -> bool:
        """Toggle the 'completed' state of the task and return the new state."""
        if not task_id:
            logger.warning("No task ID provided")
            raise ValueError("Task ID must be provided")

        for task in self.task_table.all():
            if task.id == task_id:
                task.toggle_status()
                return task.completed

        logger.warning(f"No task found with ID {task_id}")
        raise ValueError(f"Task with ID {task_id} not found")

    def edit_task(self, task_id: int, updates: dict[str, Any]) -> bool:
        """Update the task with provided ID with provided attribute and value in dict format"""
        for task in self.task_table.all():
            if task.id == task_id:
                task.update_fields(updates)
                return True
        return False

    def apply_filter(self, **criteria) -> None:
        self.filters = criteria

    def get_filtered_tasks(self) -> list[Task]:
        return self.task_table.filter_by(**self.filters)

    def sort_tasks(self, column: str, reverse: bool = False) -> None:
        self.sort_column = column
        self.sort_reverse = reverse

    def refresh_view(self) -> TaskTable:
        """Combine filtres, tris, etc. et retourne une vue actuelle"""
        filtered_tasks = self.task_table.filter_by(**self.filters)
        if self.sort_column is not None:
            filtered_tasks.sort(
                key=lambda t: getattr(t, self.sort_column),  # type: ignore[arg-type]
                reverse=self.sort_reverse,
            )
        return TaskTable(filtered_tasks, self.columns)
