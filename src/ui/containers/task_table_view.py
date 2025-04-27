from typing import Any, Dict, List

from PySide6.QtWidgets import QTableView, QWidget

from handlers.task_handlers import TaskHandlers
from helpers.contextmanagers import open_db
from models.task_table_model import TaskTableModel
from ui.delegates.edit_delegate import EditDelegate
from ui.delegates.status_delegate import StatusEditDelegate
from utils.path_utils import DB_FILE
from utils.task_table_column_utils import TASK_TABLE_COLUMNS, get_column_index
from utils.view_utils import apply_column_config


class TaskTableView(QTableView):
    """Display the tasks in a table"""

    def __init__(self, parent: QWidget | None = None) -> None:
        """Init the table: db, handlers, model, ui, delegates, signals

        Parameters
        ----------
        parent : QWidget | None, optional
            the parent widget, by default None
        """

        super().__init__(parent)
        with open_db(DB_FILE) as db:
            tasks: List[Dict[str, Any]] = db.get_all_tasks()
        self.task_handlers = TaskHandlers()
        self.table_model = TaskTableModel(
            parent=self, task_handlers=self.task_handlers, tasks=tasks
        )  # Create the model

        self.setModel(self.table_model)  # Set the model to the table
        self.setup_ui()
        self.setup_delegates()
        self.setup_signals()

    def setup_ui(self):
        """Table UI setup"""
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setShowGrid(False)

        vheader = self.verticalHeader()
        header = self.horizontalHeader()

        if header:
            header.setStretchLastSection(True)
        if vheader:
            vheader.setVisible(False)

        apply_column_config(self, TASK_TABLE_COLUMNS)

    def setup_delegates(self):
        """Setup the delegates for the table"""
        self.delegate = EditDelegate(self)

        # Trouver dynamiquement l'index pour "Edit"
        edit_column_index = get_column_index("edit")

        if edit_column_index is not None:
            self.setItemDelegateForColumn(edit_column_index, self.delegate)

        # Trouver dynamiquement l'index pour "Status"
        status_column_index = get_column_index("completed")

        if status_column_index is not None:
            self.setItemDelegateForColumn(status_column_index, StatusEditDelegate())

    def setup_signals(self):
        """Connect the signals to the slots"""
        self.delegate.deleteClicked.connect(self.table_model.handle_delete_task)
        self.delegate.editClicked.connect(self.table_model.handle_edit_task)
