from PyQt6.QtWidgets import QTableView, QWidget
from backend.models.task_table_model import TaskTableModel
from backend.models.task_table_utils import (
    EDIT_COLUMN,
    COLUMN_WIDTHS,
    TASK_TABLE_HEADERS,
)
from gui.delegates.edit_delegate import EditDelegate
from PyQt6.QtWidgets import QTableView, QAbstractItemView
from PyQt6.QtCore import QModelIndex, QPoint
from backend.handlers.status_handler import toggle_task_status
from backend.database.db_manager import DbManager


class TaskTable(QTableView):
    """Configuration graphique des tâches. Aucune logique métier, gérée par backend.TaskTableModel"""

    def __init__(self, db: DbManager, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.db = db
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
        self.setItemDelegateForColumn(
            TASK_TABLE_HEADERS.index(EDIT_COLUMN), self.delegate
        )

    def setup_signals(self):
        """Connexion des icones aux signaux"""
        self.delegate.deleteClicked.connect(self.table_model.handle_delete_task)
        self.delegate.editClicked.connect(self.table_model.handle_edit_task)


    def mousePressEvent(self, event):
        """Gère le clic dans la colonne 'Status' pour inverser l'état d'une tâche"""
        index: QModelIndex = self.indexAt(event.pos())
        if index.isValid():
            col = index.column()
            row = index.row()

            # Colonne 1 = 'Status' (completed)
            if col == 1:
                task_id = self.table_model.index(row, 0).data()
                if toggle_task_status(task_id, self.db):
                    self.table_model.refresh()

        super().mousePressEvent(event)
