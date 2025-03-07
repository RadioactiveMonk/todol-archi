from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QTableView, QWidget
from backend.database import DatabaseManager
from backend.models.task_table_model import TaskTableModel
from backend.config.constants import TASK_TABLE_HEADERS


class TaskTable(QTableView):
    """Configuration graphique des tâches. Aucune logique métier, gérée par backend.TaskTableModel"""

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.db = (
            DatabaseManager()
        )  # On amene le gestionnaire partout ou il faut gerer les tâches
        self.table_model = TaskTableModel(self, self.db)  # Connexion de la logique

        self.setModel(self.table_model)  # Association du modèle a TaskTable(QTableView)
        self.setup_ui()

    def setup_ui(self):
        """Configuration de l'affichage de la table"""
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setColumnWidth(0, 50)  # Colonne 'Status'
        self.setColumnWidth(1, 100)  # Colonne 'Category'
        self.setColumnWidth(2, 150)  # Colonne 'Expiration'
        self.setColumnWidth(3, 250)  # Colonne 'Title'
        self.setColumnWidth(4, 350)  # Colonne 'Notes'
        self.setColumnWidth(5, 124)  # Colonne 'Edit'

    def mousePressEvent(self, event: QMouseEvent):
        """Intercepte le clic sur une cellule et applique l'action associée."""

        index = self.indexAt(
            event.position().toPoint()
        )  # ✅ Récupère la cellule cliquée

        # ✅ Dictionnaire des actions disponibles
        actions = {
            len(
                TASK_TABLE_HEADERS
            ): self.table_model.delete_task,  # Suppression de tâche
            # Ici, on pourra ajouter d'autres actions plus tard (ex: "edit_task")
        }

        if index.isValid() and index.column() in actions:
            actions[index.column()](index.row())  # ✅ Exécute l'action correspondante
            return  # ✅ Empêche le clic d’être traité deux fois

        super().mousePressEvent(
            event
        )  # ✅ Continue le comportement normal pour le reste
