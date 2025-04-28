# src/core/factory/mainwindow_factory.py

from PySide6.QtWidgets import QMainWindow

from helpers.contextmanagers import open_db
from ui.main_window import MainWindow
from utils.path_utils import DB_FILE


class MainWindowFactory:
    """Create a main window instance with all the components"""

    @staticmethod
    def create() -> QMainWindow:
        """Create a main window instance with all the components"""

        with open_db(DB_FILE) as db:
            main_window = MainWindow(db=db)
            return main_window
