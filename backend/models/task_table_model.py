from typing import List, Any
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from backend.database import DatabaseManager
from backend.task import Task
from backend.config.constants import TASK_TABLE_HEADERS, COLUMN_MAPPING, NO_ID


class TaskTableModel(QAbstractTableModel):
    """Modèle de données à afficher dans TaskTable (widgets.py)"""

    def __init__(
        self,
        parent: QObject | None = None,
        database: DatabaseManager = DatabaseManager(),
    ) -> None:
        """Initialise les données à afficher pour chaque tâche"""
        super().__init__(parent)
        self.database: DatabaseManager = database
        self.tasks: List[Task] = self.database.get_tasks()

    def rowCount(self, parent: QModelIndex | None = None) -> int:
        """Retourne le nombre de lignes en fonction du nombre de tâches stockées."""
        return len(self.tasks)

    def columnCount(self, parent: QModelIndex | None = QModelIndex()) -> int:
        """Retourne le nombre de colonnes en fonction du nombre de sections dans le header"""
        return len(TASK_TABLE_HEADERS) + 1  # +1 pour la colonne "Edit"

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any:
        """Retourne les noms des colonnes affichées dans le header du tableau."""
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return (
                TASK_TABLE_HEADERS[section]
                if section < len(TASK_TABLE_HEADERS)
                else "Edit"
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

            if index.column() < len(TASK_TABLE_HEADERS):  # Colonnes normales
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
        """Définit les propriétés des cellules (éditable, sélectionnable, etc.)"""
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags

        if index.column() == len(TASK_TABLE_HEADERS):  # Colonne Edit
            return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

        return super().flags(index)

    def delete_task(self, row: int) -> None:
        """Supprime visuellement une tâche, supprime dans la DB et rafraîchit le tableau"""
        task = self.tasks[row]

        if task.tid != NO_ID:  # Vérifie que la tâche est dans la DB
            self.database.del_task(task.tid)

        del self.tasks[row]  # Supprime du modèle
        self.layoutChanged.emit()
