from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
)
from PyQt6.QtGui import QIcon
from gui.add_task_dialog import AddTaskDialog
from gui.widgets import CustomButton, SearchBar, TaskTable
from backend.task_manager import TaskManager


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application Todol"""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Todol - Task Manager")  # Définition du titre de la fenêtre
        self.setGeometry(100, 100, 800, 600)  # Position et taille de la fenêtre
        self.setWindowIcon(
            QIcon("gui/icons/app_icon.png")
        )  # Ajout d'une icône personnalisée

        self.task_manager = TaskManager()
        self.init_ui()  # Initialisation de l'interface

    def init_ui(self) -> None:
        """Initialise l'interface graphique."""

        # 👉 Création d'un widget central pour accueillir les layouts
        central_widget: QWidget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 👉 Création et ouverture du layout principal qui regroupe tous les autres
        main_layout: QVBoxLayout = QVBoxLayout()

        # 👉 Création et ouverture d'un premier layout horizontal.
        action_layout: QHBoxLayout = QHBoxLayout()

        # ➡️ Barre de recherche
        self.search_bar = SearchBar()
        action_layout.addWidget(self.search_bar)

        # ➡️ Boutons d'action
        self.add_task_button = CustomButton("add.png", "Add new task")
        self.add_task_button.clicked.connect(self.open_add_task_dialog)
        action_layout.addWidget(self.add_task_button)

        self.add_category_button = CustomButton("add-category.png", "Add new category")
        action_layout.addWidget(self.add_category_button)

        self.filter_task_button = CustomButton("filter.png", "Filter tasks")
        action_layout.addWidget(self.filter_task_button)

        # ✅ Ajout du layout d'action au layout principal
        main_layout.addLayout(action_layout)

        # ✅ Ajout du tableau des tâches (pas besoin de layout, en général les tableaux prennent
        # le reste de la fenêtre, donc il serat automatiquement ajusté)
        self.task_table = TaskTable()
        main_layout.addWidget(self.task_table)

        # ✅ Rafraîchissement des tâches au lancement
        self.refresh_task_list()

        central_widget.setLayout(
            main_layout
        )  # ✅ Attribution du layout principal à la fenêtre.

    def open_add_task_dialog(self):
        """Ouvre une boîte de dialogue pour ajouter une tâche et met à jour la liste si validée."""
        dialog = AddTaskDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            task_data = dialog.task_data
            self.task_manager.add_task(task_data)
            self.refresh_task_list()

    def refresh_task_list(self):
        """Met à jour l'affichage des tâches."""
        self.task_table.load_tasks(self.task_manager.get_all_tasks())
