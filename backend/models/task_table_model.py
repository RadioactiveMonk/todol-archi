from typing import List, Any
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from backend.database import DatabaseManager
from backend.task import Task
from backend.config.constants import TASK_TABLE_HEADERS, COLUMN_MAPPING, NO_ID
from gui.widgets.edit_section_icons import get_icons


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
        self.edit_icons = get_icons()

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

            return "Edit"  # ✅ Dernière colonne = Boutons d'action

        return None

    def data(
        self,
        index: QModelIndex = QModelIndex(),
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        """Retourne les données dans chaque cellule"""

        if not index.isValid():
            return None

        # ✅ Si c'est la colonne Actions, on affiche une icône supprimer
        if (
            index.column() == len(TASK_TABLE_HEADERS)
            and role == Qt.ItemDataRole.DecorationRole
        ):  # Dernière colonne

            return self.edit_icons["delete"]

        # ✅ Affichage normal pour les autres colonnes
        if (
            index.column() < len(TASK_TABLE_HEADERS)
            and role == Qt.ItemDataRole.DisplayRole
            and index.column() != 0
        ):

            column_name = TASK_TABLE_HEADERS[index.column()]
            attribute = COLUMN_MAPPING.get(column_name, "")

            return getattr(self.tasks[index.row()], attribute, None)

        if index.column() == 0 and role == Qt.ItemDataRole.DisplayRole:
            return (
                "✅"
                if getattr(self.tasks[index.row()], "status", None) == True
                else "🟨"
            )

        return None

    def setData(self, index: QModelIndex, value, role=Qt.ItemDataRole.EditRole) -> bool:
        """Gère l'interaction avec une cellule (suppression ou autre action future)"""

        if not index.isValid():
            return False

        # ✅ Dictionnaire d'actions en fonction de la colonne cliquée
        actions = {
            len(TASK_TABLE_HEADERS): self.delete_task,
        }  # setData avec dict dispatch: les méthodes sont stoquées dans un dict.
        # Ici les actions de la colone 'edit'.

        # Si l'index de la colone est une clé dans 'actions', on appelle la méthode avec cette clé,
        # sur la tâche de la rangée ou l'action est située
        if index.column() in actions and role == Qt.ItemDataRole.EditRole:
            actions[index.column()](index.row())  # = self.delete_task(rangée)
            return True

        return super().setData(
            index, value, role
        )  #  super().setData() permet de garder le comportement natif de PyQt pour les cellules
        # qui ne font pas partie du dict dispatch.

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        """Définit les propriétés des cellules (éditable, sélectionnable, etc.)"""
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags  # ✅ Correction ici

        if index.column() == len(TASK_TABLE_HEADERS):  # Colonne Edit
            return (
                Qt.ItemFlag.ItemIsEnabled
                | Qt.ItemFlag.ItemIsSelectable
                | Qt.ItemFlag.ItemIsEditable
            )  # ✅ Correction ici

        return super().flags(index)

    def delete_task(self, row: int) -> None:
        """Supprime visuellement une tâche, supprime dans la DB et rafraichit le tableau"""

        task = self.tasks[row]

        if task.tid != NO_ID:  # Vérifie que la tâche est dans la DB
            self.database.del_task(task.tid)

        del self.tasks[row]  # Supprime du modèle
        self.layoutChanged.emit()
