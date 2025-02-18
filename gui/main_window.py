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
        self.setWindowTitle("Task Manager")  # Définition du titre de la fenêtre
        self.setGeometry(100, 100, 800, 600)  # Position et taille de la fenêtre

        self.init_ui()  # Initialisation de l'interface

    def init_ui(self) -> None:
        """Initialise l'interface graphique."""
        central_widget: QWidget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout: QVBoxLayout = QVBoxLayout()  # Layout principal (vertical)

        icon_path = QDir.current().filePath(
            "gui/icons/"
        )  # Dossier qui range les icônes

        # Barre de recherche
        self.search_bar: QLineEdit = QLineEdit()
        self.search_bar.setPlaceholderText("🔍 Search tasks ...")
        main_layout.addWidget(self.search_bar)

        # Création du tableau pour afficher les tâches
        self.task_table: QTableWidget = QTableWidget()
        self.task_table.setColumnCount(
            7
        )  # On prépare 6 colonnes, dont une pour les actions
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

        # Layout pour les boutons Ajouter et Filtrer
        button_layout: QHBoxLayout = QHBoxLayout()

        # Bouton "Ajouter" avec icône
        self.add_task_button: QPushButton = QPushButton(" New task")
        self.add_task_button.setIcon(QIcon(icon_path + "add.png"))
        button_layout.addWidget(self.add_task_button)

        # Bouton "Ajouter" une catégorie
        self.filter_task_button: QPushButton = QPushButton(" New category")
        self.filter_task_button.setIcon(QIcon(icon_path + "add-category.png"))
        button_layout.addWidget(self.filter_task_button)

        # Bouton "Filtrer" avec icône
        self.filter_task_button: QPushButton = QPushButton(" Filter tasks")
        self.filter_task_button.setIcon(QIcon(icon_path + "filter.png"))
        button_layout.addWidget(self.filter_task_button)

        main_layout.addLayout(
            button_layout
        )  # Ajout du layout des boutons dans le layout principal

        central_widget.setLayout(main_layout)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.show()
    sys.exit(app.exec())
