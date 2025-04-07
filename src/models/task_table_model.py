from typing import Any, Optional, cast

from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import QWidget

from core.path import DB_FILE
from handlers.task_handlers import TaskHandlers
from helpers.contextmanagers import open_db
from helpers.log_utils import logger
from helpers.status_constants import status_color, status_label
from models.task import Task
from models.task_table_utils import (
    STATUS_COLUMN,
    TASK_TABLE_HEADERS,
)
from ui.dialogs.add_task_dialog import AddTaskDialog


class TaskTableModel(QAbstractTableModel):
    """Data model for the task table"""

    def __init__(
        self,
        parent: Optional[QObject] = None,
        task_handlers: Optional[TaskHandlers] = None,
        tasks: Optional[list[dict[str, Any]]] = None,
    ) -> None:
        """Init the the database, the data model, the task handlers (edit, delete).

        Parameters
        ----------
        parent : Optional[QObject], optional
            parent object, by default None
        task_handlers : Optional[TaskHandlers], optional
            the task handlers, by default None
        tasks : Optional[list[dict[str, Any]]], optional
            initial tasks, by default None
        """
        super().__init__(parent)
        self._tasks = tasks if tasks is not None else []
        self.task_handlers = (
            task_handlers
            if task_handlers
            else TaskHandlers(refresh_callback=self.refresh)
        )

    def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
        """Return the number of rows in the table"""
        return len(self._tasks)

    def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
        """Return the number of columns in the table"""
        return len(TASK_TABLE_HEADERS)

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        """Return the header data for the table"""
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return TASK_TABLE_HEADERS[section]
        return None

    def setData(
        self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole
    ) -> bool:
        """Set the data in the table"""
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
        """Return the data for the table"""
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
        """Return the flags for the table"""
        from ui.cell_properties import get_flags

        return get_flags(index)

    def refresh(self) -> None:
        """Refresh the table with new tasks."""
        with open_db(DB_FILE) as db:
            self._tasks = db.get_all_tasks()
        self.layoutChanged.emit()

    def handle_edit_task(self, row: int) -> None:
        """Logic to handle the edit task action for a given row"""
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
        """Logic to handle the delete task action for a given row"""
        if row < 0 or row >= len(self._tasks):
            return

        task_id = self._tasks[row]["id"]
        logger.debug(f"🗑 Suppression demandée pour la tâche {task_id}")
        self.task_handlers.delete_handler(task_id)
        self.refresh()

    def _get_display_value(self, task: dict[str, Any], column: int) -> Optional[str]:
        """Return the value to show in the cell"""
        match column:
            case 0:
                return status_label(task.get("completed", False))
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
        """Return the background color for the status column"""
        color = status_color(task.get("completed", False))
        return QBrush(QColor(color))
