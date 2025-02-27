from typing import Optional
from PyQt6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QHeaderView,
    QTableView,
    QWidget,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QDir
from backend.constants import TASK_HEADERS


class CustomButton(QPushButton):
    """Bouton personnalisé avec icône et tooltip."""

    def __init__(
        self, icon_name: str, tooltip: str, parent: Optional[QWidget] = None
    ) -> None:
        super().__init__(parent)
        icon_path = QDir.current().filePath(f"resources/icons/{icon_name}")
        self.setIcon(QIcon(icon_path))
        self.setToolTip(tooltip)


class SearchBar(QLineEdit):
    """Barre de recherche"""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setPlaceholderText(" Search tasks ...")
        self.setFixedHeight(40)


class TaskTable(QTableView):
    """Configuration graphique des tâches. Aucune logique métier, gérée par backend.TaskTableModel"""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setSortingEnabled(True)
