from typing import Any, List, Optional

from core.log_manager import logger
from models.task import Task
from models.task_table_column import TaskTableColumn


class TaskTable:
    """Representation of the task table. Columns, rows, cells, ..."""

    def __init__(self, tasks: List[Task], columns: List[TaskTableColumn]) -> None:
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

        self._tasks = tasks
        self._columns = columns

    def row_count(self) -> int:
        """
        Returns the number of rows (tasks) in the task table.
        Returns
        -------
        int
            The number of tasks in the task table.
        """
        return len(self._tasks)

    def column_count(self) -> int:
        """
        Returns the number of columns in the task table.

        Returns
        -------
        int
            The total number of columns.
        """
        return len(self._columns)

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
