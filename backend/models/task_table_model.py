from typing import Any, List, Dict
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from backend.db_manager import DbManager
from gui.widgets.cell_properties import get_flags
from backend.models.task_table_utils import (
    STATUS_COLUMN,
    TASK_TABLE_HEADERS,
    COLUMN_MAPPING,
    EDIT_COLUMN,
)
from backend.models.edit_section_handlers import TaskHandlers


class TaskTableModel(QAbstractTableModel):
    """Modèle de données à afficher dans TaskTable (widgets.py)"""

    def __init__(
        self,
        parent: QObject | None = None,
        db_manager: DbManager = DbManager(),
        task_handlers: TaskHandlers = TaskHandlers(),
    ) -> None:
        """Initialise les données à afficher pour chaque tâche"""

        super().__init__(parent)
        self.db = db_manager

        self.tasks: List[Dict[str, Any]] = self.db.get_tasks()
        self.task_handlers = task_handlers

    def rowCount(self, parent: QModelIndex | None = None) -> int:
        """Retourne le nombre de lignes en fonction du nombre de tâches stockées."""
        return len(self.tasks)

    def columnCount(self, parent: QModelIndex | None = QModelIndex()) -> int:
        """Retourne le nombre de colonnes en fonction du nombre de sections dans le header"""
        return len(TASK_TABLE_HEADERS)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any:
        """Retourne les noms des colonnes affichées dans le header du tableau."""
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return TASK_TABLE_HEADERS[section]

        return None

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        """Retourne les données à afficher dans une cellule"""
        if not index.isValid():
            return None

        task = self.tasks[index.row()]
        column_name = TASK_TABLE_HEADERS[index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            if column_name == STATUS_COLUMN:
                return "✅" if task["completed"] else "🟨"

            if column_name == EDIT_COLUMN:
                return None

            return task.get(COLUMN_MAPPING.get(column_name, ""), "")

        return None  # La colonne "Edit" est gérée par `EditDelegate`

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        """Appelle les propriétés de cellules"""
        return get_flags(index, index.column())

    def refresh(self):
        """Refresh the table with new tasks."""
        self.tasks = self.db.get_tasks()
        self.layoutChanged.emit()

    def handle_delete_task(self, task_id: int):
        """Deletes task in db and in table. Refresh the view."""
        if self.task_handlers.delete_handler(task_id):
            self.refresh()

    def handle_edit_task(self, task_id: int, **kwargs):
        """Updates task in db and in table. Refresh the view"""
        if self.task_handlers.edit_handler(task_id, **kwargs):
            self.refresh()
