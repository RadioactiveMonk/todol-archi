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
from backend.models.edit_section_handlers import


class TaskTableModel(QAbstractTableModel):
    """Modèle de données à afficher dans TaskTable (widgets.py)"""

    def __init__(
        self,
        parent: QObject | None = None,
        db_manager: DbManager = DbManager(),
    ) -> None:
        """Initialise les données à afficher pour chaque tâche"""
        super().__init__(parent)
        self.db_manager = db_manager
        self.tasks = self.db_manager.get_tasks()

    def _update_task(self, task) -> None:
        """Mise à jour en DB et rafraichit l'affichage"""
        self.db_manager.execute("update_task", task)
        logger.info(
            f"UPDATE (Task): ID='{task.tid}', Title='{task.title}', Category='{task.category}', Expiration='{task.expiration}', Status='{task.status}'"
        )

        self.layoutChanged.emit()

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
                    "✅" if getattr(self.tasks[index.row()], "status", None) else "🟨"
                )

            if index.column() < EDIT_COLUMN_INDEX:  # Colonnes normales
                column_name = TASK_TABLE_HEADERS[index.column()]
                attribute = COLUMN_MAPPING.get(column_name, "")
                return getattr(self.tasks[index.row()], attribute, None)

        return None  # La colonne "Edit" est gérée par `EditDelegate`

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        """Appelle les propriétés de cellules"""
        return get_flags(index, EDIT_COLUMN_INDEX)

    def handle_check(self, row: int) -> None:
        """Inverse le statut de la tâche (✅ ↔️ 🟨) et met à jour la DB."""
        task = self.tasks[row]
        task.status = not task.status

        logger.info(f"TOGGLE (Status): ID='{task.tid}', Status='{task.status}'")

        self.db_manager.execute("update_task_status", task.status, task.tid)
        self._update_task(task)

    def handle_edit(self, row: int) -> None:
        """Ouvre le formulaire d'édition pour une tâche."""
        task = self.tasks[row]
        parent_widget = self.parent() if isinstance(self.parent(), QWidget) else None
        dialog = AddTaskDialog(parent=parent_widget, task=task)

        if dialog.exec():
            task.title = dialog.title_input.text().strip()
            task.category = dialog.category_selector.currentText()
            task.expiration = dialog.expiration_selector.dateTime().toString(
                "yyyy-MM-dd HH:mm"
            )
            task.notes = dialog.notes_input.toPlainText().strip()
            self._update_task(task)

    def handle_delete(self, row):
        """Supprime visuellement une tâche, supprime dans la DB et rafraîchit le tableau"""
        task = self.tasks[row]

        if task.tid != NO_ID:  # Vérifie que la tâche est dans la DB
            self.db_manager.execute("delete_task", task.tid)
            logger.info(f"DELETE (Task): ID='{task.tid}', Title='{task.title}'")

        del self.tasks[row]  # Supprime du modèle
        self.layoutChanged.emit()
