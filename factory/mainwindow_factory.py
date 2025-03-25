from PyQt6.QtWidgets import QMainWindow, QApplication
from ui.main_window import MainWindow
from factory.dialog_factory import DialogFactory
from factory.handler_factory import HandlerFactory
from factory.notification_factory import NotificationFactory


class MainWindowFactory:
    """Create a main window instance with all the components"""

    @staticmethod
    def create() -> QMainWindow:
        """Create a main window instance with all the components"""
        dialog_factory = DialogFactory()
        handler_factory = HandlerFactory()
        notification_factory = NotificationFactory()
        main_window = MainWindow()
        return main_window
