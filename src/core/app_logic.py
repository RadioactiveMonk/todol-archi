from typing import Optional

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
