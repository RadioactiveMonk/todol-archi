from typing import List, Dict, Any, Optional, Union
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from backend.database import DatabaseManager
from backend.task import Task
from backend.constants import TASK_TABLE_HEADERS, COLUMN_MAPPING


class TaskTableModel(QAbstractTableModel):
    """Modèle de donnée a afficher dans TaskTable (widgets.py)"""

    def __init__(self, parent: QObject, database: DatabaseManager) -> None:
        """Initialise les données à afficher pour chaque tâche"""

        super().__init__(parent)

        self.database = database
        self.tasks: List[Task] = self.database.get_tasks()

    def rowCount(self, parent: QModelIndex) -> int:
        """Retourne le nombre de lignes en fonction du nombre de tâches stoquées."""

        return len(self.tasks)

    def columnCount(self, parent: QModelIndex) -> int:
        """Retourne le nombre de colone en fonction du nombre de sections dans le header"""

        return len(TASK_TABLE_HEADERS)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any:
        """Retourne le nom des colones"""

        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return TASK_TABLE_HEADERS[section]  # retourne le titre du header
        return None

    def data(self, index: QModelIndex, role: int) -> Any:
        """Retourne les données dans chaque cellule"""

        if not index.isValid():
            return None

        task = self.tasks[index.row()]  # Récupère la tâche par l'index de la ligne

        if role == Qt.ItemDataRole.DisplayRole:
            column_name = TASK_TABLE_HEADERS[index.column()]  # Ex: "Title"
            attribute = COLUMN_MAPPING.get(column_name, "")  # Ex: "title"
            return getattr(task, attribute, None)  # ✅ Récupère la valeur sans erreur

        return None
