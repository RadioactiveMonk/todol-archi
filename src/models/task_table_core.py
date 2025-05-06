from typing import Any, List, Optional, Sequence

from core.log_manager import logger
from models.task import Task
from models.task_table_column import TaskTableColumn


class TaskTable:
    """Representation of the task table. Columns, rows, cells, ..."""

    def __init__(
        self, tasks: Sequence[Task], columns: Sequence[TaskTableColumn]
    ) -> None:
        """
        Initialize the TaskTableCore object.

        Parameters
        ----------
        tasks : List[Task]
            A list of Task objects representing the tasks to be managed.
        columns : List[TaskTableColumn]
            A list of TaskTableColumn objects representing the columns in the task table.

        Returns
        -------
        None
        """

        self._tasks = list(tasks)
        self._columns = list(columns)

    def __str__(self) -> str:
        """
        Returns a string representation of the object for console output.
        """

        return self.to_console_str()

    def __repr__(self) -> str:
        """Returns a description of the object 'TaskTable'. 
        """
        return f"<TaskTable rows={self.row_count} cols={self.column_count}>"

    def __len__(self) -> int:
        """Returns length of the table (number of rows)
       """
        return self.row_count

    def __getitem__(self, index: int | slice) -> Task | list[Task]:
   """Returns a task by its index or a list of tasks by a given slice (e.g.: index = slice(0, 5)"""
    return self._tasks[index]

    @property
    def row_count(self) -> int:
        """
        Returns the number of rows (tasks) in the task table.
        Returns
        -------
        int
            The number of tasks in the task table.
        """
        return len(self._tasks)

    @property
    def column_count(self) -> int:
        """
        Returns the number of columns in the task table.

        Returns
        -------
        int
            The total number of columns.
        """
        return len(self._columns)

    @property
    def column_names(self) -> List[str]:
        """
        Retrieves the names of all columns in the table.

        Returns:
            List[str]: A list of column names.
        """
        return [col.name for col in self._columns]

    @property
    def column_fields(self) -> List[str]:
        """
        Retrieves a list of field names from the columns.

        Returns:
            List[str]: A list of field names extracted from the column objects.
        """

        return [col.field for col in self._columns]

    def headers(
        self, as_tuple: Optional[bool] = False
    ) -> list[str] | list[tuple[str, str]]:
        """
        Generate a list of column headers for the task table.

        Parameters
        ----------
        as_tuple : bool, optional
            If True, returns a list of tuples where each tuple contains the column
            name and its corresponding field. If False, returns a list of column
            names only. Default is False.

        Returns
        -------
        list of str or list of tuple of str
            If `as_tuple` is False, returns a list of column names as strings.
            If `as_tuple` is True, returns a list of tuples, where each tuple
            contains the column name and its corresponding field.
        """

        if as_tuple:
            return [(col.name, col.field) for col in self._columns]
        return [col.name for col in self._columns]

    def get_cell_value(self, row_index: int, col_index: int) -> Any:
        """
        Retrieves the value of a specific cell in the task table.

        Parameters
        ----------
        row_index : int
            The index of the row in the task table.
        col_index : int
            The index of the column in the task table.

        Returns
        -------
        Any
            The value of the cell located at the specified row and column.

        Notes
        -----
        This method assumes that `_tasks` is a list of task objects and `_columns`
        is a list of column objects, where each column object has a `field` attribute
        that corresponds to an attribute of the task object.
        """
        task = self._tasks[row_index]
        column = self._columns[col_index]
        return getattr(task, column.field)

    def get_column_name(self, index: int) -> str:
        """
        Retrieve the name of a column based on its index.

        Parameters
        ----------
        index : int
            The index of the column whose name is to be retrieved.

        Returns
        -------
        str
            The name of the column at the specified index.

        Raises
        ------
        IndexError
            If the provided index is out of range for the columns.
        """
        try:
            return self._columns[index].name
        except IndexError as e:
            logger.error(e)
            raise

    def get_column_tooltip(self, index: int) -> Optional[str]:
        """
        Retrieve the tooltip of a column based on its index.

        Parameters
        ----------
        index : int
            The index of the column whose tooltip is to be retrieved.

        Returns
        -------
        Optional[str]
            The tooltip of the column at the specified index, or None if no tooltip is set.

        Raises
        ------
        IndexError
            If the provided index is out of range for the columns.
        """
        try:
            return self._columns[index].tooltip
        except IndexError as e:
            logger.error(e)
            raise

    def add_task(self, task: Task) -> bool:
        """
        Add a task to the task list.

        Parameters
        ----------
        task : Task
            The task object to be added. Must be an instance of the Task class.

        Returns
        -------
        bool
            True if the task was successfully added, False if the task type is invalid.

        Notes
        -----
        Logs a warning if the provided task is not an instance of the Task class.
        """

        if not isinstance(task, Task):
            logger.warning("Invalid task type provided. %r", task)
            return False
        self._tasks.append(task)
        return True
    
    def remove_tasks(self, task_ids: tuple[int]) -> bool:
        """
        Remove tasks from the task list based on their IDs.

        Parameters
        ----------
        task_ids : tuple[int]
            A tuple of task IDs to be removed from the task list.

        Returns
        -------
        bool
            True if at least one task was removed, False otherwise.

        Raises
        ------
        ValueError
            If no task IDs are provided.
        """
        remaining_tasks = []
        removed_ids = []

        if not task_ids:
            logger.warning("No task ID given", task_ids)
            raise ValueError("You must provide at least one task ID")

        for task in self._tasks:
            if task.id in task_ids:
                removed_ids.append(task.id)
            else:
                remaining_tasks.append(task)

        self._tasks = remaining_tasks

        if removed_ids:
            logger.info("Removed tasks with IDs: %s", removed_ids)
            return True

        logger.info("No matching task IDs found to remove: %s", task_ids)
        return False


    def remove_by_id(self, task_id: int) -> bool:
        """
        Removes a single task by its ID
        """        
        return self.remove_tasks((task_id,))


    def to_matrix(self) -> list[list[str]]:
        """
        Converts the tasks and their attributes into a 2D matrix representation.
        Columns without corresponding fields in Task are skipped.
        """
        matrix = []
        for task in self._tasks:
            row = []
            for column in self._columns:
                if hasattr(task, column.field):
                    value = getattr(task, column.field)
                    row.append(str(value))
            matrix.append(row)
        return matrix

    def to_console_str(self) -> str:
        """
        Converts the task table data into a formatted string suitable for console output.

        Returns
        -------
        str
            A string representation of the task table, where the first line contains
            the column headers separated by " | ", and subsequent lines contain the
            rows of data formatted in the same way.
        """
        headers = [
            col.name for col in self._columns if hasattr(self._tasks[0], col.field)
        ]
        rows = self.to_matrix()
        lines = [" | ".join(headers)]
        lines += [" | ".join(row) for row in rows]
        return "\n".join(lines)
