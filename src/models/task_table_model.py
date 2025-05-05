from typing import Any, Optional

from PySide6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from PySide6.QtGui import QBrush, QColor

from core.log_manager import logger
from handlers.task_handlers import TaskHandlers
from helpers.status_helpers import status_color
from models.task_table_config import TASK_TABLE_COLUMNS


class TaskTableModel(QAbstractTableModel):
    """Data model for the task table"""

    def __init__(
        self,
        parent: Optional[QObject] = None,
        task_handlers: Optional[TaskHandlers] = None,
        tasks: Optional[list[dict[str, Any]]] = None,
    ) -> None:
        """Initialize tasks and handlers at init"""
        super().__init__(parent)
        self._tasks = tasks if tasks is not None else []
        self.task_handlers = (
            task_handlers or TaskHandlers()
        )  # FIXME see TaskHandlers, refresh_callback ?

    def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
        """Returns the number of rows equal to number of tasks"""
        return len(self._tasks)

    def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
        """Returns the number of columns in 'TASK_TABLE_COLUMNS'"""
        return len(TASK_TABLE_COLUMNS)

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        """Set header datas for the table"""
        if orientation == Qt.Orientation.Horizontal:
            column = TASK_TABLE_COLUMNS[section]
            if role == Qt.ItemDataRole.DisplayRole:
                return column.name
            elif role == Qt.ItemDataRole.ToolTipRole and column.tooltip:
                return column.tooltip
        return None

    def data(self, index, /, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        """Table datas"""
        if not index.isValid():
            return None

        row, col_index = index.row(), index.column()
        task = self._tasks[row]
        column = TASK_TABLE_COLUMNS[col_index]
        value = task.get(column.field)

        if column.field == "completed" and isinstance(value, bool):
            if role == Qt.ItemDataRole.BackgroundRole:
                return QBrush(QColor(status_color(value)))
            elif role == Qt.ItemDataRole.CheckStateRole:
                return Qt.CheckState.Checked if value else Qt.CheckState.Unchecked

        return super().data(index, role)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        """Returns columns flags if any, otherwise returns flag 'ItemIsEnabled'"""
        column = TASK_TABLE_COLUMNS[index.column()]
        return column.flags or Qt.ItemFlag.ItemIsEnabled

    def setData(
        self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole
    ) -> bool:
        """Set table datas"""
        if not index.isValid() or role != Qt.ItemDataRole.EditRole:
            return False

        row, col_index = index.row(), index.column()
        column = TASK_TABLE_COLUMNS[col_index]
        task = self._tasks[row]

        if column.field == "completed":
            task_id = task["id"]
            self.task_handlers.toggle_task_status(task_id)
            task["completed"] = not task["completed"]
            logger.debug(f"[setData] Toggle task ID {task_id} -> {task['completed']}")
            self.dataChanged.emit(index, index)
            return True

        return False

    def refresh(self):
        pass
