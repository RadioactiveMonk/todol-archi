from sqlite3 import Row
from PyQt6.QtWidgets import QTableView, QWidget
from backend.database import DatabaseManager
from backend.models.task_table_model import TaskTableModel


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
