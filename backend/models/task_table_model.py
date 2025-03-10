from encodings.punycode import T
from typing import List, Any
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from backend.database import DatabaseManager
from backend.database_controler import DatabaseControler
from backend.task import Task
from gui.widgets.cell_properties import get_flags
from backend.config.constants import (
    TASK_TABLE_HEADERS,
    COLUMN_MAPPING,
    NO_ID,
    EDIT_COLUMN_INDEX,
)


class TaskTableModel(QAbstractTableModel):
    """Modèle de données à afficher dans TaskTable (widgets.py)"""

    def __init__(
        self,
        parent: QObject | None = None,
        db_manager: DatabaseManager = DatabaseManager(),
    ) -> None:
        """Initialise les données à afficher pour chaque tâche"""
        super().__init__(parent)
        self.db_manager = DatabaseManager()
        self.tasks = db_manager.execute("get_tasks")

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

    def setData(self, index: QModelIndex, value, role=Qt.ItemDataRole.EditRole) -> bool:
        """Gère l'interaction avec une cellule (suppression ou autre action future)"""
        if not index.isValid():
            return False

        if role == Qt.ItemDataRole.EditRole and index.column() == len(
            TASK_TABLE_HEADERS
        ):
            return False  # Toutes les actions sont maintenant gérées par `EditDelegate`

        return super().setData(index, value, role)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        """Appelle les propriétés de cellules"""
        return get_flags(index, EDIT_COLUMN_INDEX)

    def delete_task(self, row: int) -> None:
        """Supprime visuellement une tâche, supprime dans la DB et rafraîchit le tableau"""
        task = self.tasks[row]

        if task.tid != NO_ID:  # Vérifie que la tâche est dans la DB
            self.db_manager.execute("delete_task", task.tid)

        del self.tasks[row]  # Supprime du modèle
        self.layoutChanged.emit()

    def handle_check(self, row: int) -> None:
        """Inverse le statut de la tâche (✅ ↔️ 🟨) et met à jour la DB."""
        task = self.tasks[row]
        task.status = not task.status  # ✅ Toggle le statut
        self.db_manager.execute(
            "update_task_status", (task.tid, task.status)
        )  # ✅ Mise à jour DB
        self.layoutChanged.emit()  # ✅ Rafraîchit l'affichage

    def handle_edit(self, row: int) -> None:
        """Ouvre le formulaire d'édition pour une tâche."""
        task = self.tasks[row]
        print(
            f"📌 Édition de la tâche : {task.title}"
        )  # ✅ Placeholder (connecter l’UI plus tard)

    def handle_delete(self, row):
        """Supprime la tâche sélectionnée."""
        self.delete_task(row)  # Appelle la méthode de suppression
