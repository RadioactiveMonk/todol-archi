from typing import List, Any
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from backend.database import DatabaseManager
from backend.task import Task
from backend.config.constants import TASK_TABLE_HEADERS, COLUMN_MAPPING, NO_ID


class TaskTableModel(QAbstractTableModel):
    """Modèle de donnée a afficher dans TaskTable (widgets.py)"""

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
        """Retourne le nombre de lignes en fonction du nombre de tâches stoquées."""

        parent = parent or QModelIndex()
        return len(self.tasks)

    def columnCount(self, parent: QModelIndex | None = QModelIndex()) -> int:
        """Retourne le nombre de colone en fonction du nombre de sections dans le header"""

        return (
            len(TASK_TABLE_HEADERS) + 1
        )  # Sépararation des données et des actions (+ 1 pour actions)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any:
        """Retourne les noms des colonnes affichées dans le header du tableau."""

        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            if section < len(TASK_TABLE_HEADERS):
                return TASK_TABLE_HEADERS[section]  # ✅ Retourne les colonnes normales

            return "Actions"  # ✅ Dernière colonne = Boutons d'action

        return None

    def data(self, index: QModelIndex = QModelIndex(), role: int = int()) -> Any:
        """Retourne les données dans chaque cellule"""

        index = index or QModelIndex()
        if not index.isValid():
            return None

        task = self.tasks[index.row()]  # Récupère la tâche par l'index de la ligne

        if index.column() == len(
            TASK_TABLE_HEADERS
        ):  # SI c'est la dernière colone, pas de texte (colone 'actions')
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            column_name = TASK_TABLE_HEADERS[index.column()]  # Ex: "Title"
            attribute = COLUMN_MAPPING.get(column_name, "")  # Ex: "title"
            return getattr(task, attribute, None)  # Récupère la valeur sans erreur

        return None

    def delete_task(self, row: int) -> None:
        """Supprime visuellement une tâche, supprime dans la DB et rafraichit le tableau"""

        task = self.tasks[row]

        if task.tid != NO_ID:  # Vérifie que la tâche est dans la DB
            self.database.del_task(task.tid)

        del self.tasks[row]  # Supprime du modèle
        self.layoutChanged.emit()
