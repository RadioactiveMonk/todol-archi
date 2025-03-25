from PyQt6.QtWidgets import QLineEdit, QWidget


class SearchTasks(QLineEdit):
    """Barre de recherche"""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent or QWidget())
        self.setPlaceholderText(" Search tasks ...")
        self.setFixedHeight(40)
