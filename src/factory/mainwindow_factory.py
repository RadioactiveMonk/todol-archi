from PyQt6.QtWidgets import QMainWindow

from ui.main_window import MainWindow


class MainWindowFactory:
    """Create a main window instance with all the components"""

    @staticmethod
    def create() -> QMainWindow:
        """Create a main window instance with all the components"""
        # dialog_factory = DialogFactory()
        # handler_factory = HandlerFactory()
        # notification_factory = NotificationFactory()
        main_window = MainWindow()
        return main_window
