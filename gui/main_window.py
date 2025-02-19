from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtGui import QIcon
import sys
from gui.widgets import CustomButton, SearchBar, TaskTable


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application To-Do List."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Todol - Task Manager")  # Définition du titre de la fenêtre

        self.setGeometry(100, 100, 800, 600)  # Position et taille de la fenêtre
        self.setWindowIcon(
            QIcon("gui/icons/app_icon.png")
        )  # Ajout d'une icône personnalisée

        self.init_ui()  # Initialisation de l'interface
        self.load_stylesheet()  # Chargement du fichier QSS après l'init UI

    def load_stylesheet(self) -> None:
        """Charge et applique le fichier QSS."""
        try:
            with open("gui/styles.qss", "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("⚠️ Fichier styles.qss introuvable, le style ne sera pas appliqué.")

    def init_ui(self) -> None:
        """Initialise l'interface graphique."""
        central_widget: QWidget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout: QVBoxLayout = QVBoxLayout()  # Layout principal (vertical)

        # Layout pour la barre de recherche et les boutons associés
        search_layout: QHBoxLayout = QHBoxLayout()

        # Barre de recherche personnalisée
        self.search_bar = SearchBar()
        search_layout.addWidget(self.search_bar)

        # Boutons personnalisés
        self.add_task_button = CustomButton("add.png", "Add new task")
        search_layout.addWidget(self.add_task_button)

        self.add_category_button = CustomButton("add-category.png", "Add new category")
        search_layout.addWidget(self.add_category_button)

        self.filter_task_button = CustomButton("filter.png", "Filter tasks")
        search_layout.addWidget(self.filter_task_button)

        main_layout.addLayout(search_layout)  # Ajout du layout de recherche et boutons

        # Création du tableau des tâches personnalisé
        self.task_table = TaskTable()
        main_layout.addWidget(self.task_table)

        central_widget.setLayout(main_layout)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.show()
    sys.exit(app.exec())
