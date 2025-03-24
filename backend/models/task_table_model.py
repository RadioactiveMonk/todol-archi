from typing import Any, List, Dict
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from PyQt6.QtGui import QColor, QBrush, QFont
from backend.database.db_manager import DbManager
from backend.models.task import Task
from configuration.cell_properties import get_flags
from backend.models.task_table_utils import (
    STATUS_COLUMN,
    TASK_TABLE_HEADERS,
    COLUMN_MAPPING,
    EDIT_COLUMN,
)
from backend.handlers.task_handlers import TaskHandlers
from backend.core.logger import logger
from backend.models.task_table_utils import STATUS_DONE_UI, STATUS_PENDING_UI
from configuration.cell_properties import get_alignment


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

    def setData(
        self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole
    ) -> bool:
        if not index.isValid() or role != Qt.ItemDataRole.EditRole:
            return False

        row, column = index.row(), index.column()
        task = self.tasks[row]

        if TASK_TABLE_HEADERS[column] == STATUS_COLUMN:
            task_id = task["id"]

            self.task_handlers.toggle_task_status(task_id)
            task["completed"] = not task["completed"]
            # Signale à Qt que les données ont changé (rafraîchissement de la cellule (x,y))
            self.dataChanged.emit(index, index)
            return True
        return False

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid():
            return None

        row, column = index.row(), index.column()
        task = self.tasks[row]

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
        """Appelle les propriétés de cellules"""
        return get_flags(index)

    def refresh(self) -> None:
        """Refresh the table with new tasks."""
        self.tasks = self.db.get_tasks()
        self.layoutChanged.emit()

    def handle_edit_task(self, row: int) -> None:
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

    def handle_delete_task(self, row: int) -> None:
        """Gère la suppression d'une tâche via le TaskHandlers"""
        if row < 0 or row >= len(self.tasks):
            return

        task_id = self.tasks[row]["id"]
        logger.debug(
            f"🗑 Suppression demandée pour la tâche {task_id}"
        )  # ✅ Vérification
        self.task_handlers.delete_handler(task_id)
        self.refresh()  # ✅ Rafraîchir l'affichage après suppression

    def _get_display_value(self, task: dict, column: int) -> str | None:
        """Gere l'affichage des cellules

        Parameters
        ----------
        task : dict
            Task in dict format
        column : int
            column index

        Returns
        -------
        str | None
            the value to show in the cell | None for edit_section
        """
        match column:
            case 0:
                return STATUS_DONE_UI if task["completed"] else STATUS_PENDING_UI
            case 1:
                return task["category"]
            case 2:
                return task["expiration"]
            case 3:
                return task["title"]
            case 4:
                return task["notes"]
            case _:
                return None

    def _get_status_background(self, task: dict) -> QBrush:
        """ "Set background for status column cells"""
        color = "#b0db43" if task["completed"] else "#db2763"
        return QBrush(QColor(color))
