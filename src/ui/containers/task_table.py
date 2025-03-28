from PyQt6.QtWidgets import QTableView, QWidget
from core.database.db_manager import DbManager
from handlers.task_handlers import TaskHandlers
from models.task_table_model import TaskTableModel
from models.task_table_utils import (
    COLUMN_WIDTHS,
    EDIT_COLUMN,
    TASK_TABLE_HEADERS,
)
from ui.delegates.edit_delegate import EditDelegate
from ui.delegates.status_delegate import StatusEditDelegate


class TaskTable(QTableView):
    """Display the tasks in a table"""

    def __init__(
        self, db: DbManager | None = None, parent: QWidget | None = None
    ) -> None:
        """Init the table: db, handlers, model, ui, delegates, signals

        Parameters
        ----------
        db : DbManager | None, optional
            the database manager, by default None
        parent : QWidget | None, optional
            the parent widget, by default None
        """

        super().__init__(parent)
        self.db = db if db is not None else DbManager()
        self.task_handlers = TaskHandlers()
        self.table_model = TaskTableModel(
            parent=self, db=self.db, task_handlers=self.task_handlers
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

        for col, width in COLUMN_WIDTHS.items():
            self.setColumnWidth(col, width)

    def setup_delegates(self):
        """Setup the delegates for the table"""
        self.delegate = EditDelegate(self)
        self.setItemDelegateForColumn(
            TASK_TABLE_HEADERS.index(EDIT_COLUMN), self.delegate
        )
        self.setItemDelegateForColumn(0, StatusEditDelegate())

    def setup_signals(self):
        """Connect the signals to the slots"""
        self.delegate.deleteClicked.connect(self.table_model.handle_delete_task)
        self.delegate.editClicked.connect(self.table_model.handle_edit_task)
