from typing import Any, Optional

from core.log_manager import logger
from models.task import Task
from models.task_table_column import TaskTableColumn
from models.task_table_core import TaskTable


class AppLogic:
    def __init__(self, tasks: list[Task], columns: list[TaskTableColumn]):
        """
        Initializes the application logic with tasks and columns, and sets up the task table, filters, sorting, and selection state.

        Args:
            tasks (list[Task]): A list of Task objects to be managed.
            columns (list[TaskTableColumn]): A list of columns for displaying tasks in the table.
        """

        self.tasks = tasks
        self.columns = columns
        self.task_table = TaskTable(self.tasks, self.columns)
        self.filters = {}
        self.sort_column: Optional[str] = None
        self.sort_reverse = False
        self.selected_task_id: Optional[int] = None

    def add_task(self, task: Task) -> None:
        """
        Adds a new task to the task table.

        Args:
            task (Task): The task object to be added.
        Returns:
            None
        """

        self.task_table.add_task(task)

    def remove_task_by_id(self, task_id: int) -> None:
        """
        Removes a task from the task table by its unique identifier.

        Args:
            task_id (int): The unique identifier of the task to be removed.
        Returns:
            None
        """

        self.task_table.remove_by_id(task_id)

    def delete_selected_task(self) -> bool:
        """
        Deletes the currently selected task from the task table.

        Returns:
            bool: True if the task was successfully deleted, False if no task was selected or deletion failed.
        """

        if self.selected_task_id is None:
            return False
        return self.task_table.remove_by_id(self.selected_task_id)

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggles the completion status of a task with the given task ID.

        Args:
            task_id (int): The unique identifier of the task to toggle.
        Returns:
            bool: The new completion status of the task (True if completed, False otherwise).
        Raises:
            ValueError: If no task ID is provided or if no task with the given ID is found.
        """

        if not task_id:
            logger.warning("No task ID provided")
            raise ValueError("Task ID must be provided")

        for task in self.task_table:
            if task.id == task_id:
                task.toggle_status()
                return task.completed

        logger.warning(f"No task found with ID {task_id}")
        raise ValueError(f"Task with ID {task_id} not found")

    def toggle_selected_task_status(self) -> Optional[bool]:
        """
        Toggles the completion status of the currently selected task.

        Returns:
            bool: The new completion status of the selected task if a task is selected,
                  otherwise False.
        """

        task = self.get_selected_task()
        if task:
            task.toggle_status()
            return task.completed
        return None

    def edit_task(self, task_id: int, updates: dict[str, Any]) -> bool:
        """
        Update the attributes of a task with the specified ID.

        Args:
            task_id (int): The unique identifier of the task to update.
            updates (dict[str, Any]): A dictionary containing attribute names as keys and their new values.

        Returns:
            bool: True if the task was found and updated, False otherwise.
        """

        for task in self.task_table:
            if task.id == task_id:
                task.update_fields(updates)
                return True
        return False

    def get_selected_task(self) -> Optional[Task]:
        """
        Returns the currently selected task based on the selected_task_id.
        Iterates through the task_table to find and return the Task object whose id matches selected_task_id.
        If no task is selected or no matching task is found, returns None.

        Returns:
            Optional[Task]: The selected Task object if found, otherwise None.
        """

        if self.selected_task_id is None:
            return None
        for task in self.task_table:
            if task.id == self.selected_task_id:
                return task
        return None

    def edit_selected_task(self, updates: dict[str, Any]) -> Optional[bool]:
        """
        Edits the currently selected task with the provided updates.

        Args:
            updates (dict[str, Any]): A dictionary containing the fields to update and their new values.
        Returns:
            bool: True if a task was selected and updated, False otherwise.
        """

        task = self.get_selected_task()
        if task:
            task.update_fields(updates)
            return True
        return None

    def apply_filter(self, **criteria) -> None:
        """
        Apply filter criteria to the current instance.

        Parameters:
            **criteria: Arbitrary keyword arguments representing filter conditions to be applied.
        Returns:
            None
        """

        self.filters = criteria

    def get_filtered_tasks(self) -> list[Task]:
        """
        Returns a list of tasks filtered according to the current filter criteria.
        The method applies the filters stored in `self.filters` to the task table and returns
        the resulting list of `Task` objects.

        Returns:
            list[Task]: A list of tasks that match the specified filters.
        """

        return self.task_table.filter_by(**self.filters)

    def sort_tasks(self, column: str, reverse: bool = False) -> None:
        """
        Sorts the tasks based on the specified column and order.

        Args:
            column (str): The name of the column to sort by.
            reverse (bool, optional): If True, sort in descending order. Defaults to False.
        Returns:
            None
        """

        self.sort_column = column
        self.sort_reverse = reverse

    def refresh_view(self) -> TaskTable:
        """
        Refreshes and returns the task table view based on current filters and sorting.
        Retrieves the list of tasks filtered according to the current filter settings.
        If a sort column is specified, sorts the filtered tasks by that column in either
        ascending or descending order, depending on the sort_reverse flag.
        Returns a TaskTable instance containing the processed list of tasks and the current columns.

        Returns:
            TaskTable: The updated task table reflecting current filters and sorting.
        """

        filtered_tasks = self.get_filtered_tasks()
        if self.sort_column is not None:
            filtered_tasks.sort(
                key=lambda t: getattr(t, self.sort_column),  # type: ignore[arg-type]
                reverse=self.sort_reverse,
            )
        return TaskTable(filtered_tasks, self.columns)
