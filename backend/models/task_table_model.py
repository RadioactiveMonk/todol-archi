from typing import Any, List, Dict
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from backend.database.db_manager import DbManager
from backend.models.task import Task
from configuration.cell_properties import get_flags
from backend.models.task_table_utils import (
    STATUS_COLUMN,
    TASK_TABLE_HEADERS,
    COLUMN_MAPPING,
    EDIT_COLUMN,
)
from backend.handlers.edit_section_handlers import TaskHandlers
from backend.core.logger import logger


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
                return "[ROCKED]" if task["completed"] else "[PENDING]"

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

    def handle_edit_task(self, row: int):
        """Ouvre la boîte de dialogue d'édition pour la tâche sélectionnée"""
        if row < 0 or row >= len(self.tasks):
            return

        task_data = self.tasks[row]

        task = Task(
            tid=task_data["id"],
            completed=bool(task_data["completed"]),
            category=task_data["category"],
            expiration=task_data["expiration"],
            title=task_data["title"],
            notes=task_data["notes"],
        )

        from gui.dialogs.add_task_dialog import AddTaskDialog

        dialog = AddTaskDialog(self.parent(), task=task)
        dialog.ok_signal.connect(self.refresh)
        dialog.exec()

    def handle_delete_task(self, row: int):
        """Gère la suppression d'une tâche via le TaskHandlers"""
        if row < 0 or row >= len(self.tasks):
            return

        task_id = self.tasks[row]["id"]
        logger.debug(
            f"🗑 Suppression demandée pour la tâche {task_id}"
        )  # ✅ Vérification
        self.task_handlers.delete_handler(task_id)
        self.refresh()  # ✅ Rafraîchir l'affichage après suppression
