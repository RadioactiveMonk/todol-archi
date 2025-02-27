from PyQt6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QHeaderView,
    QTableView,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QDir
from backend.constants import TASK_HEADERS


class CustomButton(QPushButton):
    """Bouton personnalisé avec icône et tooltip."""

    def __init__(self, icon_name: str, tooltip: str, parent=None) -> None:
        super().__init__(parent)
        icon_path = QDir.current().filePath(f"resources/icons/{icon_name}")
        self.setIcon(QIcon(icon_path))
        self.setToolTip(tooltip)


class SearchBar(QLineEdit):
    """Barre de recherche"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setPlaceholderText(" Search tasks ...")
        self.setFixedHeight(40)


class TaskTable(QTableView):
    """Tableau des tâches avec configuration personnalisée."""

    pass
