from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QPushButton,
    QLineEdit,
)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QDir
import sys


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application To-Do List."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Todol - Task manager")  # Définition du titre de la fenêtre
        self.setGeometry(100, 100, 800, 600)  # Position et taille de la fenêtre

        self.init_ui()  # Initialisation de l'interface

    def init_ui(self) -> None:
        """Initialise l'interface graphique."""
        central_widget: QWidget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout: QVBoxLayout = QVBoxLayout()  # Layout principal (vertical)

        icon_path = QDir.current().filePath("gui/icons/")  # Dossier des icônes

        # Layout pour la barre de recherche et les boutons associés
        search_layout: QHBoxLayout = QHBoxLayout()

        # Barre de recherche
        self.search_bar: QLineEdit = QLineEdit()
        self.search_bar.setPlaceholderText("🔍 Search tasks ...")
        search_layout.addWidget(self.search_bar)

        # Bouton "Ajouter" avec icône
        self.add_task_button: QPushButton = QPushButton()
        self.add_task_button.setIcon(QIcon(icon_path + "add.png"))
        self.add_task_button.setToolTip("Add new task")
        search_layout.addWidget(self.add_task_button)

        # Bouton "Ajouter une catégorie" avec icône
        self.add_category_button: QPushButton = QPushButton()
        self.add_category_button.setIcon(QIcon(icon_path + "add-category.png"))
        self.add_category_button.setToolTip("Add new category")
        search_layout.addWidget(self.add_category_button)

        # Bouton "Filtrer" avec icône
        self.filter_task_button: QPushButton = QPushButton()
        self.filter_task_button.setIcon(QIcon(icon_path + "filter.png"))
        self.filter_task_button.setToolTip("Filter tasks")
        search_layout.addWidget(self.filter_task_button)

        main_layout.addLayout(search_layout)  # Ajout du layout de recherche et boutons

        # Création du tableau pour afficher les tâches
        self.task_table: QTableWidget = QTableWidget()
        self.task_table.setColumnCount(7)  # Colonnes préparées
        self.task_table.setHorizontalHeaderLabels(
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

        # Vérification avant d'appliquer setSectionResizeMode
        header = self.task_table.horizontalHeader()
        if header:
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.task_table.setFont(QFont("Arial", 12))  # Style du tableau
        main_layout.addWidget(self.task_table)

        central_widget.setLayout(main_layout)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.show()
    sys.exit(app.exec())
