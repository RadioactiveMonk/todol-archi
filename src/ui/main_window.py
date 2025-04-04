from typing import Any, Dict, List, Union

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from core.database.ask_db import AskDB
from core.path import ICONS_DIR
from models.task import Task
from ui.containers.menu_bar import MenuBar
from ui.containers.search_tasks import SearchTasks
from ui.containers.task_table import TaskTable
from ui.controls.custom_button import CustomButton
from ui.dialogs.add_task_dialog import AddTaskDialog
from ui.dialogs.edit_parameters_dialog import EditParametersDialog
from ui.ui_constants import MAIN_WINDOW_GEOMETRY, MAIN_WINDOW_TITLE


class MainWindow(QMainWindow):
    """Main window of the application"""

    def __init__(self, db: AskDB) -> None:
        """Init the main window

        Parameters
        ----------
        db : AskDB
            context manager to manage database via open_db()
        """
        super().__init__()
        self._tasks: List[Dict[str, Any]] = db.get_all_tasks()
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setGeometry(*MAIN_WINDOW_GEOMETRY)
        self.setWindowIcon(QIcon(str(ICONS_DIR / "app_icon.png")))
        self.setMenuBar(MenuBar(self))
        self.init_ui()

    def init_ui(self) -> None:
        """Init the main window UI
        1. Create the main layout
        2. Create the action layout
        3. Create the search bar
        4. Create the custom buttons
        5. Create the task table
        6. Set the layout
        """

        central_widget: QWidget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout: QVBoxLayout = QVBoxLayout()
        action_layout: QHBoxLayout = QHBoxLayout()

        self.search_tasks_bar = SearchTasks(self)
        # ️🚩 connect......
        action_layout.addWidget(self.search_tasks_bar)

        self.add_task_button = CustomButton("new_task.png", "Add new task", self)
        self.add_task_button.clicked.connect(self.open_add_task_dialog)
        action_layout.addWidget(self.add_task_button)

        self.edit_parameters_button = CustomButton(
            "edit_settings.png", "Settings", self
        )
        self.edit_parameters_button.clicked.connect(self.open_edit_parameters_dialog)
        action_layout.addWidget(self.edit_parameters_button)

        main_layout.addLayout(action_layout)

        # Task table
        self.task_table = TaskTable()
        main_layout.addWidget(self.task_table)

        central_widget.setLayout(main_layout)

    def open_add_task_dialog(self, task: Union["Task", None] = None) -> None:
        """Open a dialog to add a task

        Parameters
        ----------
        task : Task, optional
            If given, the dialog will be pre-filled with the task data, by default None
        """
        dialog = AddTaskDialog(self)
        dialog.ok_signal.connect(self.task_table.table_model.refresh)
        dialog.exec()

    def open_edit_parameters_dialog(self):
        """Open a dialog to edit parameters"""

        dialog = EditParametersDialog(self)
        dialog.exec()

    def search_tasks(self):
        """Search tasks"""
        pass
