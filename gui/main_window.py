from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
)
from PyQt6.QtGui import QIcon
from gui.dialogs import AddTaskDialog
from gui.widgets import CustomButton, SearchBar, TaskTable
from backend.task_manager import TaskManager


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application To-Do List."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Todol")  # Définition du titre de la fenêtre
        self.setGeometry(100, 100, 800, 600)  # Position et taille de la fenêtre
        self.setWindowIcon(
            QIcon("resources/icons/app_icon.png")
        )  # Ajout d'une icône personnalisée

        self.task_manager = TaskManager()
        self.init_ui()  # Initialisation de l'interface

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
        self.add_task_button.clicked.connect(self.open_add_task_dialog)
        search_layout.addWidget(self.add_task_button)

        self.add_category_button = CustomButton("add-category.png", "Add new category")
        search_layout.addWidget(self.add_category_button)

        self.change_parameters = CustomButton("app-parameters.png", "Edit parameters")

        main_layout.addLayout(search_layout)  # Ajout du layout de recherche et boutons

        # Création du tableau des tâches personnalisé
        self.task_table = TaskTable()
        main_layout.addWidget(self.task_table)

        self.refresh_task_list()  # ✅ Charge les tâches dès l’ouverture de l’appli

        central_widget.setLayout(main_layout)

    def open_add_task_dialog(self):
        """Ouvre une boite de dialogue d'ajout de tâche et ajoute si validée"""

        dialog = AddTaskDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            task_data = dialog.task_data
            self.task_manager.add_task(task_data)
            self.refresh_task_list()

    def refresh_task_list(self):
        """Met à jour l'affichâge des tâches"""

        self.task_table.load_tasks(self.task_manager.get_all_tasks())
