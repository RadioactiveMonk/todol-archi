from typing import Any
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from PyQt6.QtWidgets import QWidget
from backend.db_manager import DbManager
from backend.logger import logger
from gui.dialogs.add_task_dialog import AddTaskDialog
from gui.widgets.cell_properties import get_flags
from backend.models.task_table_utils import (
    TASK_TABLE_HEADERS,
    COLUMN_MAPPING,
    EDIT_COLUMN_INDEX,
)
from backend.models.edit_section_handlers import TaskHandlers


class TaskTableModel(QAbstractTableModel):
    """Modèle de données à afficher dans TaskTable (widgets.py)"""

    def __init__(
        self,
        parent: QObject | None = None,
        db_manager: DbManager = DbManager(),
    ) -> None:
        """Initialise les données à afficher pour chaque tâche"""
        super().__init__(parent)
        self.db = DbManager()
        self.tasks = self.db.get_tasks()
        self.task_handlers = TaskHandlers()

    def _update_task(self, task) -> None:
        """Mise à jour en DB et rafraichit l'affichage"""
        

    def rowCount(self, parent: QModelIndex | None = None) -> int:
        """Retourne le nombre de lignes en fonction du nombre de tâches stockées."""
        return len(self.tasks)

    def columnCount(self, parent: QModelIndex | None = QModelIndex()) -> int:
        """Retourne le nombre de colonnes en fonction du nombre de sections dans le header"""
        return EDIT_COLUMN_INDEX + 1  # +1 pour la colonne "Edit"

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any:
        """Retourne les noms des colonnes affichées dans le header du tableau."""
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return (
                TASK_TABLE_HEADERS[section] if section < EDIT_COLUMN_INDEX else "Edit"
            )
        return None

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        """Retourne les données à afficher dans une cellule"""
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:  # Statut ✅ / 🟨
                return (
                    "✅" if getattr(self.tasks[index.row()], "completed", None) else "🟨"
                )

            if index.column() < EDIT_COLUMN_INDEX:  # Colonnes normales
                column_name = TASK_TABLE_HEADERS[index.column()]
                attribute = COLUMN_MAPPING.get(column_name, "")
                return getattr(self.tasks[index.row()], attribute, None)

        return None  # La colonne "Edit" est gérée par `EditDelegate`

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        """Appelle les propriétés de cellules"""
        return get_flags(index, EDIT_COLUMN_INDEX)

    
