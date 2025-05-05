from typing import Any, Optional

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from handlers.task_handlers import TaskHandlers
from helpers.contextmanagers import open_db
from helpers.status_helpers import status_color
from models.task import Task
from models.task_table_data import TASK_TABLE_COLUMNS, TaskTableColumn
from utils.path_utils import DB_FILE


class TaskTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._tasks: list[Task] = self._load()
        self._columns: list[TaskTableColumn] = TASK_TABLE_COLUMNS
        self.handlers = TaskHandlers(refresh_callback=self.refresh)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._tasks)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._columns)

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self._columns[section].name
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.ToolTipRole
        ):
            return self._columns[section].tooltip
        return None

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid():
            return None

        task = self._tasks[index.row()]
        column = self._columns[index.column()]
        value = getattr(task, column.field)

        if role == Qt.ItemDataRole.DisplayRole:
            return value

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return column.alignment

        if role == Qt.ItemDataRole.CheckStateRole and isinstance(value, bool):
            return Qt.CheckState.Checked if value else Qt.CheckState.Unchecked

        if role == Qt.ItemDataRole.BackgroundRole and column.field == "completed":
            return status_color(value)

        return None

    def setData(
        self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole
    ) -> bool:
        if not index.isValid():
            return False

        column = self._columns[index.column()]
        if role == Qt.ItemDataRole.CheckStateRole and column.field == "completed":
            task = self._tasks[index.row()]
            if task.id:
                self.handlers.toggle_task_status(task.id)
                return True

        return False

    def flags(self, index: QModelIndex) -> Optional[Qt.ItemFlag]:
        if not index.isValid():
            return Qt.ItemFlag.ItemIsEnabled

        return self._columns[index.column()].flags

    def refresh(self):
        self.beginResetModel()
        self._tasks = self._load()
        self.endResetModel()

    def _load(self) -> list[Task]:
        with open_db(DB_FILE) as db:
            rows = db.get_all_tasks()
            return [Task(**row) for row in rows]
