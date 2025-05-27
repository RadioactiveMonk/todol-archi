import random
from typing import Any, List, Optional, Sequence

from core.log_manager import logger
from models.task import Task
from models.task_table_column import TaskTableColumn


class TaskTable:
    """Represents the task table (rows, columns, and associated operations)."""

    def __init__(
        self, tasks: Sequence[Task], columns: Sequence[TaskTableColumn]
    ) -> None:
        """Initialize the TaskTable with a list of tasks and columns.

        Args:
            tasks (Sequence[Task]): List of Task instances.
            columns (Sequence[TaskTableColumn]): List of column definitions.
        """
        self._tasks = list(tasks)
        self._columns = list(columns)

    def __str__(self) -> str:
        """String representation suitable for console output.

        Returns:
            str: Formatted string of the task table.
        """
        return self.to_console_str()

    def __repr__(self) -> str:
        """Debug representation of the TaskTable.

        Returns:
            str: Developer-friendly string.
        """
        return f"<TaskTable rows={self.row_count} cols={self.column_count}>"

    def __len__(self) -> int:
        """Return number of tasks (rows).

        Returns:
            int: Number of rows.
        """
        return self.row_count

    def __getitem__(self, index: int | slice) -> Task | list[Task]:
        """Get a task or a list of tasks by index or slice.

        Args:
            index (int | slice): Index or slice of tasks.

        Returns:
            Task | list[Task]: Task(s) from the table.
        """
        return self._tasks[index]

    def __iter__(self):
        """Allow iteration over the tasks.

        Returns:
            Iterator[Task]: Iterator over task list.
        """
        return iter(self._tasks)

    def __contains__(self, task: Task) -> bool:
        """Check if a task exists in the table.

        Args:
            task (Task): Task instance.

        Returns:
            bool: True if present, False otherwise.
        """
        return task in self._tasks

    def __bool__(self) -> bool:
        """Evaluate if the table is non-empty.

        Returns:
            bool: True if contains tasks.
        """
        return bool(self._tasks)

    @property
    def row_count(self) -> int:
        """Get the number of tasks.

        Returns:
            int: Number of rows.
        """
        return len(self._tasks)

    @property
    def column_count(self) -> int:
        """Get the number of columns.

        Returns:
            int: Number of columns.
        """
        return len(self._columns)

    @property
    def column_names(self) -> List[str]:
        """Get all column names.

        Returns:
            List[str]: Column name list.
        """
        return [col.name for col in self._columns]

    @property
    def column_fields(self) -> List[str]:
        """Get all field names from columns.

        Returns:
            List[str]: Column field list.
        """
        return [col.field for col in self._columns]

    def headers(self, as_tuple: bool = False) -> list[str] | list[tuple[str, str]]:
        """Return column headers.

        Args:
            as_tuple (bool, optional): Whether to return as (name, field) tuples.

        Returns:
            list[str] | list[tuple[str, str]]: List of headers.
        """
        if as_tuple:
            return [(col.name, col.field) for col in self._columns]
        return [col.name for col in self._columns]

    def get_cell_value(self, row_index: int, col_index: int) -> Any:
        """Retrieve a specific cell value.

        Args:
            row_index (int): Row index.
            col_index (int): Column index.

        Returns:
            Any: Cell value or None if error occurs.
        """
        try:
            task = self._tasks[row_index]
            column = self._columns[col_index]
            return getattr(task, column.field)
        except IndexError:
            logger.warning(f"Tried to access invalid cell: ({row_index, col_index})")
            return None
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return None

    def get_column_name(self, index: int) -> str:
        """Get the name of a column by index.

        Args:
            index (int): Column index.

        Returns:
            str: Column name.

        Raises:
            IndexError: If index is invalid.
        """
        try:
            return self._columns[index].name
        except IndexError as e:
            logger.error(e)
            raise

    def get_column_tooltip(self, index: int) -> Optional[str]:
        """Get the tooltip of a column by index.

        Args:
            index (int): Column index.

        Returns:
            Optional[str]: Tooltip or None.

        Raises:
            IndexError: If index is invalid.
        """
        try:
            return self._columns[index].tooltip
        except IndexError as e:
            logger.error(e)
            raise

    def add_task(self, task: Task) -> bool:
        """Add a task to the table.

        Args:
            task (Task): Task to add.

        Returns:
            bool: True if added, False if invalid.
        """
        if not isinstance(task, Task):
            logger.warning("Invalid task type provided. %r", task)
            return False
        self._tasks.append(task)
        return True

    def remove_tasks(self, task_ids: tuple[int]) -> bool:
        """Remove tasks by their IDs.

        Args:
            task_ids (tuple[int]): Tuple of IDs.

        Returns:
            bool: True if any removed.

        Raises:
            ValueError: If no IDs given.
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
        """Remove a single task by ID.

        Args:
            task_id (int): Task ID.

        Returns:
            bool: True if removed.
        """
        return self.remove_tasks((task_id,))

    def filter_by(self, **criteria) -> list[Task]:
        """Filter tasks based on field criteria.

        Returns:
            list[Task]: Matching tasks.
        """
        if not criteria:
            logger.info("No filter criteria provided. Returning original table")
            return self._tasks.copy()

        for field in criteria:
            if not hasattr(self._tasks[0], field):
                logger.warning(f"filter_by(): ignored unknown field '{field}'")

        filtered = [
            task
            for task in self._tasks
            if all(
                getattr(task, field, None) == value
                for field, value in criteria.items()
                if hasattr(task, field)
            )
        ]

        logger.info(
            f"Filtered tasks: {len(filtered)} match(es) for criteria {criteria}"
        )
        return filtered

    def to_matrix(self) -> list[list[str]]:
        """Convert tasks to a matrix of strings.

        Returns:
            list[list[str]]: 2D list of string values.
        """
        if not self._tasks:
            logger.info("No tasks available")
            return []

        if not self._columns:
            logger.info("No columns available")
            return [[] for _ in self._tasks]

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
        """Format task table for console display.

        Returns:
            str: Multi-line string of headers and rows.
        """
        if not self._tasks:
            headers = [col.name for col in self._columns]
            logger.info("No tasks available to display.")
            return " | ".join(headers) + "\n[Empty Table]"

        headers = [
            col.name for col in self._columns if hasattr(self._tasks[0], col.field)
        ]
        rows = self.to_matrix()
        lines = [" | ".join(headers)]
        lines += [" | ".join(row) for row in rows]
        return "\n".join(lines)

    def to_dicts(self) -> list[dict]:
        """Convert tasks to a list of dictionaries.

        Returns:
            list[dict]: List of task dicts.
        """
        dicts = []
        for task in self._tasks:
            row = {}
            for col in self._columns:
                if hasattr(task, col.field):
                    row[col.field] = getattr(task, col.field)
            dicts.append(row)
        return dicts

    def head(self, n: int = 5) -> "TaskTable":
        """Return the first `n` rows.

        Args:
            n (int): Number of rows. Default is 5.

        Returns:
            TaskTable: Subtable with top rows.
        """
        return TaskTable(self._tasks[:n], self._columns)

    def tail(self, n: int = 5) -> "TaskTable":
        """Return the last `n` rows.

        Args:
            n (int): Number of rows. Default is 5.

        Returns:
            TaskTable: Subtable with bottom rows.
        """
        return TaskTable(self._tasks[-n:], self._columns)

    def sample(self, n: int = 3) -> "TaskTable":
        """Return a random sample of `n` tasks.

        Args:
            n (int): Number of tasks. Default is 3.

        Returns:
            TaskTable: Subtable with sampled rows.
        """
        if n <= 0:
            return TaskTable([], self._columns)

        sampled_tasks = random.sample(self._tasks, min(n, len(self._tasks)))
        return TaskTable(sampled_tasks, self._columns)
