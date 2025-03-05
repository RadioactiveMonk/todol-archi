from typing import List, Dict, Any, Optional, Union
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from backend.database import DatabaseManager
from backend.task import Task
from backend.constants import TASK_TABLE_HEADERS, COLUMN_MAPPING, NO_ID


class TaskTableModel(QAbstractTableModel):
    """Modèle de donnée a afficher dans TaskTable (widgets.py)"""

    def __init__(self, parent: QObject, database: DatabaseManager) -> None:
        """Initialise les données à afficher pour chaque tâche"""

        super().__init__(parent)

        self.database = database
        self.tasks: List[Task] = self.database.get_tasks()

    def rowCount(self, parent: int) -> int:
        """Retourne le nombre de lignes en fonction du nombre de tâches stoquées."""

        return len(self.tasks)

    def columnCount(self, parent: int) -> int:
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
            else:
                return "Actions"  # ✅ Dernière colonne = Boutons d'action

        return None

    def data(self, index: QModelIndex, role: int) -> Any:
        """Retourne les données dans chaque cellule"""

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

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        """Supprime une tâche lorsqu'on clique sur le bouton 'Supprimer'."""
        if role == Qt.ItemDataRole.EditRole and index.column() == len(
            TASK_TABLE_HEADERS
        ):
            task = self.tasks[index.row()]

            if task.tid != NO_ID:  # 🔥 Vérification avant suppression
                self.database.del_task(task.tid)  # Suppression dans la DB
                self.tasks.pop(index.row())  # Suppression dans le modèle
                self.layoutChanged.emit()  # 🔥 Mise à jour de l'affichage
                return True

        return False
