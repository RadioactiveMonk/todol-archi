from PyQt6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QTableView,  # Migration depuis QTableWidget
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QDir, Qt
from gui.task_table_model import TaskTableModel
from typing import List, Dict, Any, Optional, Union
from backend.constants import TASK_HEADERS


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


class TaskTable(QTableView):
    """Tableau des tâches basé sur QTableView avec un modèle de donnée géré séparément"""

    def __init__(self, parent=None) -> None:
        """Construit le tableau de tâches."""

        super().__init__(parent)
        model = TaskTableModel()  # Utilisation du modèle externe
        self.setModel(model)
        self.setSortingEnabled(True)  # Active le tri dynamique

    def load_tasks(self, tasks: Optional[List[Dict[str, Any]]]) -> None:
        """Met à jour les tâches dans le modèle"""

        model = self.model()  # Récup du modèle via self.model (natif PyQt6)
        if isinstance(model, TaskTableModel):
            model.update_data(tasks or [])
