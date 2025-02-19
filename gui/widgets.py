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
        self.setFixedSize(40, 40)  # Taille uniforme des boutons


class SearchBar(QLineEdit):
    """Barre de recherche stylisée avec icône."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setPlaceholderText(" Search tasks ...")
        self.setFixedHeight(30)
        icon_path = QDir.current().filePath("gui/icons/search.png")
        self.setStyleSheet(
            f"background-image: url({icon_path}); "
            "background-position: left center; "
            "background-repeat: no-repeat; "
            "padding-left: 25px; "
            "color: black; "
        )


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
