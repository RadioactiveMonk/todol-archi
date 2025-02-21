from PyQt6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem,
    QHBoxLayout,
    QWidget,
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

    def load_tasks(self, tasks):
        """Charge et affiche les tâches dans la table"""

        self.clearContents()  # ✅ Vide la table avant de recharger
        self.setRowCount(len(tasks))  # ✅ Ajuste le nombre de lignes

        for row, task in enumerate(tasks):
            status = "🎯" if task.get("status", False) else "🕔"
            self.setItem(row, 0, QTableWidgetItem(status))
            self.setItem(row, 1, QTableWidgetItem(task.get("priority", "Medium")))
            self.setItem(row, 2, QTableWidgetItem(task.get("category", "No Category")))
            self.setItem(row, 3, QTableWidgetItem(task.get("due_date", "No Date")))
            self.setItem(row, 4, QTableWidgetItem(task.get("title", "No Title")))
            self.setItem(row, 5, QTableWidgetItem(task.get("notes", "")))

            # Ajout des boutons Modifier/Supprimer
            button_layout = QHBoxLayout()
            button_layout.setContentsMargins(0, 0, 0, 0)

            edit_button = CustomButton("edit.png", "Modifier")
            edit_button.setObjectName("taskButton")

            delete_button = CustomButton("delete.png", "Supprimer")
            delete_button.setObjectName("taskButton")

            button_widget = QWidget()
            button_layout.addWidget(edit_button)
            button_layout.addWidget(delete_button)
            button_widget.setLayout(button_layout)
            self.setCellWidget(row, 6, button_widget)

        self.update()  # ✅ Force l’affichage (méthode PyQt)
