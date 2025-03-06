from PyQt6.QtWidgets import QTableView, QWidget
from backend.database import DatabaseManager
from backend.models.task_table_model import TaskTableModel
from gui.widgets.delete_button_delegate import DeleteButtonDelegate


class TaskTable(QTableView):
    """Configuration graphique des tâches. Aucune logique métier, gérée par backend.TaskTableModel"""

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.db = (
            DatabaseManager()
        )  # On amene le gestionnaire partout ou il faut gerer les tâches
        self.table_model = TaskTableModel(self, self.db)  # Connexion de la logique

        self.setModel(self.table_model)  # Association du modèle a TaskTable(QTableView)
        self.setItemDelegateForColumn(
            self.table_model.columnCount() - 1, DeleteButtonDelegate(self)
        )
        self.setup_ui()

    def setup_ui(self):
        """Configuration de l'affichage de la table"""
        self.setSortingEnabled(True)
