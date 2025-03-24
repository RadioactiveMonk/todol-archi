from PyQt6.QtWidgets import QTableView, QWidget
from backend.models.task_table_model import TaskTableModel
from backend.models.task_table_utils import (
    EDIT_COLUMN,
    COLUMN_WIDTHS,
    TASK_TABLE_HEADERS,
)
from gui.delegates.edit_delegate import EditDelegate
from PyQt6.QtWidgets import QTableView
from PyQt6.QtCore import QModelIndex
from backend.handlers.task_handlers import TaskHandlers
from backend.database.db_manager import DbManager
from backend.core.logger import logger
from gui.delegates.status_delegate import StatusEditDelegate


class TaskTable(QTableView):
    """Configuration graphique des tâches. Aucune logique métier, gérée par backend.TaskTableModel"""

    def __init__(self, db: DbManager | None = None, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.db = db if db is not None else DbManager()
        self.task_handlers = TaskHandlers()
        self.table_model = TaskTableModel(parent=self, db=self.db, task_handlers=self.task_handlers)  # Connexion de la logique

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
        self.setItemDelegateForColumn(
            TASK_TABLE_HEADERS.index(EDIT_COLUMN), self.delegate
        )
        self.setItemDelegateForColumn(0, StatusEditDelegate())

    def setup_signals(self):
        """Connexion des icones aux signaux"""
        self.delegate.deleteClicked.connect(self.table_model.handle_delete_task)
        self.delegate.editClicked.connect(self.table_model.handle_edit_task)

    def mousePressEvent(self, event):
        """Gère le clic dans la colonne 'Status' pour inverser l'état d'une tâche"""
        super().mousePressEvent(event)
