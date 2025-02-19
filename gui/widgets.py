from PyQt6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem,
)
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
        """Construit le tableau de tâches"""
        super().__init__(parent)
        self.setColumnCount(6)
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

    def load_tasks(self, tasks):
        """Charge et affiche les tâches dans la table"""

        self.setRowCount(
            len(tasks)
        )  # Définit le nombre de rangées par nombre de tâches
        for row, task in enumerate(tasks):
            self.setItem(row, 0, QTableWidgetItem(task["status"]))  # Correction ici
            self.setItem(row, 1, QTableWidgetItem(task["priority"]))
            self.setItem(row, 2, QTableWidgetItem(task["category"]))
            self.setItem(row, 3, QTableWidgetItem(task["due_date"]))
            self.setItem(row, 4, QTableWidgetItem(task["title"]))
            self.setItem(
                row, 5, QTableWidgetItem(task.get("notes", ""))
            )  # Notes optionnelles

            # Ajout d'un bouton d'action pour modifier/supprimer la tâche
            action_button = CustomButton("edit.png", "Modifier", self)
            self.setCellWidget(row, 6, action_button)
