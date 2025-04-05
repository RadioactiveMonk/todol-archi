from typing import Any, cast

from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import QWidget

from core.path import DB_FILE
from handlers.task_handlers import TaskHandlers
from helpers.contextmanagers import open_db
from helpers.log_utils import logger
from models.task import Task
from models.task_table_utils import (
    STATUS_COLUMN,
    STATUS_DONE_UI,
    STATUS_PENDING_UI,
    TASK_TABLE_HEADERS,
)
from ui.dialogs.add_task_dialog import AddTaskDialog


class TaskTableModel(QAbstractTableModel):
    """Data model for the task table"""

    def __init__(
        self,
        parent: QObject | None = None,
        task_handlers: TaskHandlers | None = None,
        tasks=None,
    ) -> None:
        """Init the the database, the data model, the task handlers (edit, delete).

        Parameters
        ----------
        parent : QObject | None, optional
            parent object, by default None
        task_handlers : TaskHandlers | None, optional
            the task handlers, by default None
        """

        super().__init__(parent)

        self._tasks = tasks if tasks is not None else []

        self.task_handlers = (
            task_handlers
            if task_handlers
            else TaskHandlers(refresh_callback=self.refresh)
        )

    def rowCount(self, parent: QModelIndex | None = None) -> int:
        """Retuor the number of rows in the table

        Parameters
        ----------
        parent : QModelIndex | None, optional
            parent index, by default None

        Returns
        -------
        int
            the number of tasks
        """
        return len(self._tasks)

    def columnCount(self, parent: QModelIndex | None = None) -> int:
        """Return the number of columns in the table

        Parameters
        ----------
        parent : QModelIndex | None, optional
            parent index, by default None

        Returns
        -------
        int
            the number of columns
        """

        return len(TASK_TABLE_HEADERS)

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        """Return the header data for the table

        Parameters
        ----------
        section : int
            column index
        orientation : Qt.Orientation
            horizontal or vertical
        role : int
            role of the data

        Returns
        -------
        Any
            the header data for columns
        """

        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return TASK_TABLE_HEADERS[section]

        return None

    def setData(
        self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole
    ) -> bool:
        """Set the data in the table

        Parameters
        ----------
        index : QModelIndex
            index of the cell
        value : Any
            value to set
        role : int, optional
            role of the data, by default Qt.ItemDataRole.EditRole

        Returns
        -------
        bool
            True if the data is set, False otherwise
        """
        if not index.isValid() or role != Qt.ItemDataRole.EditRole:
            return False

        row, column = index.row(), index.column()
        task = self._tasks[row]

        if TASK_TABLE_HEADERS[column] == STATUS_COLUMN:
            task_id = task["id"]

            self.task_handlers.toggle_task_status(task_id)
            task["completed"] = not bool(task["completed"])
            logger.debug(f"[setData] Toggle task ID {task_id} -> {task['completed']}")
            self.dataChanged.emit(index, index)

            return True
        return False

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        """Return the data for the table

        Parameters
        ----------
        index : QModelIndex
            index of the cell
        role : int, optional
            role of the data, by default Qt.ItemDataRole.DisplayRole

        Returns
        -------
        Any
            the data for the cell
        """

        from ui.cell_properties import get_alignment

        if not index.isValid():
            return None

        row, column = index.row(), index.column()
        task = self._tasks[row]

        match role:
            case Qt.ItemDataRole.DisplayRole:
                return self._get_display_value(task, column)
            case Qt.ItemDataRole.BackgroundRole if column == 0:
                return self._get_status_background(task)
            case Qt.ItemDataRole.TextAlignmentRole:
                return get_alignment(column)
            case _:
                return None

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        """Return the flags for the table

        Parameters
        ----------
        index : QModelIndex
            index of the cell

        Returns
        -------
        Qt.ItemFlag
            the flags for the cell
        """
        from ui.cell_properties import get_flags

        return get_flags(index)

    def refresh(self) -> None:
        """Refresh the table with new tasks."""
        with open_db(DB_FILE) as db:
            self._tasks = db.get_all_tasks()
        self.layoutChanged.emit()

    def handle_edit_task(self, row: int) -> None:
        """Logic to handle the edit task action for a given row

        Parameters
        ----------
        row : int
            the row index
        """

        if row < 0 or row >= len(self._tasks):
            return

        task_data = self._tasks[row]

        task = Task(
            id=task_data["id"],
            completed=bool(task_data["completed"]),
            category=task_data["category"],
            expiration=task_data["expiration"],
            title=task_data["title"],
            notes=task_data["notes"],
        )

        dialog = AddTaskDialog(cast(QWidget, self.parent()), task=task)
        dialog.ok_signal.connect(self.refresh)
        dialog.exec()

    def handle_delete_task(self, row: int) -> None:
        """Logic to handle the delete task action for a given row

        Parameters
        ----------
        row : int
            the row index
        """

        if row < 0 or row >= len(self._tasks):
            return

        task_id = self._tasks[row]["id"]
        logger.debug(f"🗑 Suppression demandée pour la tâche {task_id}")
        self.task_handlers.delete_handler(task_id)
        self.refresh()

    def _get_display_value(self, task: dict[str, Any], column: int) -> str | None:
        """Return the value to show in the cell

        Parameters
        ----------
        task : dict
            the task data
        column : int
            column index

        Returns
        -------
        str | None
            the value to show in the cell or None if column is not found
        """
        match column:
            case 0:
                return (
                    STATUS_DONE_UI
                    if task.get("completed", False)
                    else STATUS_PENDING_UI
                )
            case 1:
                return task.get("category", "")
            case 2:
                return task.get("expiration", "")
            case 3:
                return task.get("title", "")
            case 4:
                return task.get("notes", "")
            case _:
                return None

    def _get_status_background(self, task: dict[str, Any]) -> QBrush:
        """Return the background color for the status column

        Parameters
        ----------
        task : dict
            the task data

        Returns
        -------
        QBrush
            the background color
        """
        color = "#b0db43" if task["completed"] else "#db2763"
        return QBrush(QColor(color))
