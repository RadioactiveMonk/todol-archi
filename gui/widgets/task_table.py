from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QTableView, QWidget
from backend.database import DatabaseManager
from backend.models.task_table_model import TaskTableModel
from backend.config.constants import EDIT_COLUMN_INDEX, TASK_TABLE_HEADERS
from gui.widgets.edit_delegate import EditDelegate


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
        self.setColumnWidth(5, 100)  # Colonne 'Edit'

        delegate = EditDelegate(self)
        self.setItemDelegateForColumn(EDIT_COLUMN_INDEX, delegate)

        # Connexion des signaux
        delegate.checkClicked.connect(self.handle_check)
        delegate.editClicked.connect(self.handle_edit)
        delegate.deleteClicked.connect(self.handle_delete)

    def handle_check(self, row):
        """Change le status de la tâche"""
        print("change le status")

    def handle_edit(self, row):
        """Ouvre le dialogue d'édition pour la tâche sélectionnée."""
        print(f"Édition de la ligne {row}")
        # Ici, tu peux ouvrir une fenêtre de modification (AddTaskDialog en mode édition)

    def handle_delete(self, row):
        """Supprime la tâche sélectionnée."""
        self.table_model.delete_task(row)  # Appelle la méthode de suppression
