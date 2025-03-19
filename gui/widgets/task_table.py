from PyQt6.QtWidgets import QTableView, QWidget, QHeaderView
from PyQt6.QtCore import Qt
from backend.models.task_table_model import TaskTableModel
from backend.models.task_table_utils import EDIT_COLUMN_INDEX, COLUMN_WIDTHS
from gui.widgets.edit_delegate import EditDelegate


class TaskTable(QTableView):
    """Configuration graphique des tâches. Aucune logique métier, gérée par backend.TaskTableModel"""

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.table_model = TaskTableModel(self)  # Connexion de la logique

        self.setModel(self.table_model)  # Association du modèle a TaskTable(QTableView)
        self.setup_ui()
        self.setup_delegates()
        self.setup_signals()

    def setup_ui(self):
        """Configuration de l'affichage de la table"""
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setShowGrid(False)

        vheader = self.verticalHeader()
        header = self.horizontalHeader()

        if header:
            header.setStretchLastSection(True)
        if vheader:
            vheader.setVisible(False)

        for col, width in COLUMN_WIDTHS.items():
            self.setColumnWidth(col, width)

    def setup_delegates(self):
        """Config de l'affichage des actions dans 'edit'"""
        self.delegate = EditDelegate(self)
        self.setItemDelegateForColumn(EDIT_COLUMN_INDEX, self.delegate)

    def setup_signals(self):
        """Connexion des icones aux signaux"""
        self.delegate.deleteClicked.connect(self.table_model.handle_delete_task)
        self.delegate.editClicked.connect(self.table_model.handle_edit_task)
