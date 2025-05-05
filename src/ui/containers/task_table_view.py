from typing import Any, Dict, List

from PySide6.QtWidgets import QStyledItemDelegate, QTableView, QWidget

from handlers.task_handlers import TaskHandlers
from helpers.contextmanagers import open_db
from helpers.ui.table_view_config import apply_column_config, apply_delegate_for_column
from models.task_table_data import TASK_TABLE_COLUMNS
from models.task_table_model import TaskTableModel
from utils.path_utils import DB_FILE
from helpers.ui.signal_connectors import connect_delegate_signals


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
        self.table_model = TaskTableModel()
        self.column_delegates: dict[int, QStyledItemDelegate] = {}

        self.setModel(self.table_model)  # Set the model to the table
        self.setup_ui()
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
        apply_delegate_for_column(self, TASK_TABLE_COLUMNS)

    def setup_signals(self):
        """Connect the signals to the slots dynamically based on delegates"""
        connect_delegate_signals(self)
