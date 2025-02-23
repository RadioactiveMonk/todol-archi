from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex
from typing import List, Dict, Any, Optional, Union
from backend.constants import (
    TASK_HEADERS,
    STATUS_DONE,
    STATUS_PENDING,
    PRIORITY_HIGH,
    PRIORITY_MEDIUM,
    PRIORITY_LOW,
)


class TaskTableModel(QAbstractTableModel):
    """Modèle de données pour afficher les tâches dans un QTableView"""

    HEADERS = TASK_HEADERS  # Intégration des constantes

    def __init__(self, tasks: Optional[List[Dict[str, Any]]] = None) -> None:
        """
        Initialise une liste de tâches sous forme de dict ou une liste vide si aucune tâche

        Parameters
        ----------
        self, tasks : List
            Une liste de tâches
        """

        super().__init__()
        self.tasks: List[Dict[str, Any]] = tasks or []  # Les tâches ou une liste vide

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Retourne le nombre de lignes (tâches).
        """
        return len(self.tasks)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Retourne le nombre de colonnes (sections)
        """
        return len(self.HEADERS)

    def data(self, index: QModelIndex, role: Qt.ItemDataRole) -> Optional[str]:
        """
        Retourne la donnée à afficher selon l'index et le rôle.

        Parameters
        ----------
        index : Qt.ModelIndex
            Index de la tâche
        role : Qt.ItemDataRole
            Le rôle de l'objet (un status, une date ...)


        Returns
        -------
        role OR None:
            Si le role est précisé -> Role, sinon -> None
        """

        if not index.isValid():
            return None

        task = self.tasks[index.row()]
        column = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            return {
                0: STATUS_DONE if task.get("status", False) else STATUS_PENDING,
                1: task.get("priority", PRIORITY_MEDIUM),
                2: task.get("category", "No Category"),
                3: task.get("due_date", "No Date"),
                4: task.get("title", "No Title"),
                5: task.get("notes", ""),
            }.get(
                column, None
            )  # ✅ Type `Optional[str]` car `None` est possible

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: int
    ) -> Optional[str]:
        """
        Retourne les headers de colonnes.

        Parameters
        ----------
        section : int
            l'index de la section dans la liste HEADERS
        orientation: Qt.Orientation
            l'orientation (horizontale ou verticale) des headers

        Returns
        -------
        Optional[str]
            la valeur de la section OU None
        """

        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):  # SI orientation horizontale et rôle existant
            return self.HEADERS[section]  # retourne la valeur de l'header
        return None  # Si conditions pas remplies, return None

    def update_data(self, tasks: List[Dict[str, Any]]) -> None:
        """
        Met à jour les données du modèle

        Parameters
        ----------
        tasks : List
            La liste de tâches
        """

        self.beginResetModel()  # Phase de mise à jour
        self.tasks = tasks  # Objet mis à jour
        self.endResetModel()  # Fin de mise à jour
