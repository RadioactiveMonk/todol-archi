from PyQt6.QtWidgets import QPushButton, QLineEdit, QTableWidget, QHeaderView
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QDir


class CustomButton(QPushButton):
    """Bouton personnalisé avec icône et tooltip."""

    def __init__(self, icon_name: str, tooltip: str, parent=None) -> None:
        super().__init__(parent)
        icon_path = QDir.current().filePath(f"gui/icons/{icon_name}")
        self.setIcon(QIcon(icon_path))
        self.setToolTip(tooltip)


class SearchBar(QLineEdit):
    """Barre de recherche stylisée avec icône."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setPlaceholderText(" Search tasks ...")
        self.setFixedHeight(40)


class TaskTable(QTableWidget):
    """Tableau des tâches avec configuration personnalisée."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setColumnCount(7)
        self.setHorizontalHeaderLabels(
            [
                "Status",
                "Priority",
                "Category",
                "Expiration",
                "Title",
                "Notes",
                "Actions",
            ]
        )
        self.setFont(QFont("Arial", 12))
        header = self.horizontalHeader()
        if header:
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
