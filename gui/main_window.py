from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from PyQt6.QtGui import QIcon
from backend.database.db_manager import DbManager
from gui.dialogs.add_task_dialog import AddTaskDialog
from gui.dialogs.edit_parameters_dialog import EditParametersDialog
from gui.controls.custom_button import CustomButton
from gui.containers.search_tasks import SearchTasks
from gui.containers.task_table import TaskTable
from gui.containers.menu_bar import MenuBar
from configuration.constants import MAIN_WINDOW_TITLE, MAIN_WINDOW_GEOMETRY


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application To-Do List."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(MAIN_WINDOW_TITLE)  # Définition du titre de la fenêtre
        self.setGeometry(*MAIN_WINDOW_GEOMETRY)  # Position et taille de la fenêtre
        self.setWindowIcon(
            QIcon("gui/resources/icons/app_icon.png")
        )  # Ajout d'une icône personnalisée

        self.db = DbManager()  # Gestion des tâches en backend via le stockage

        self.setMenuBar(MenuBar(self))
        self.init_ui()  # Initialisation de l'interface

    def init_ui(self) -> None:
        """Initialise l'interface graphique."""

        central_widget: QWidget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout: QVBoxLayout = QVBoxLayout()  # Layout principal (vertical)

        # Layout supérieur
        action_layout: QHBoxLayout = QHBoxLayout()

        # Barre de recherche personnalisée
        self.search_tasks_bar = SearchTasks(self)
        # ️🚩 connect......
        action_layout.addWidget(self.search_tasks_bar)

        # Boutons personnalisés
        self.add_task_button = CustomButton("new_task.png", "Add new task", self)
        self.add_task_button.clicked.connect(self.open_add_task_dialog)
        action_layout.addWidget(self.add_task_button)

        self.edit_parameters_button = CustomButton(
            "edit_settings.png", "Settings", self
        )
        self.edit_parameters_button.clicked.connect(self.open_edit_parameters_dialog)
        action_layout.addWidget(self.edit_parameters_button)

        main_layout.addLayout(action_layout)  # Ajout du layout de recherche et boutons

        # Création du tableau des tâches personnalisé
        self.task_table = TaskTable(self)
        main_layout.addWidget(self.task_table)

        central_widget.setLayout(main_layout)


    def open_add_task_dialog(self, task=None) -> None:
        """Ouvre la boîte de dialogue d'ajout/édition de tâche"""
        dialog = AddTaskDialog(self, task)
        dialog.ok_signal.connect(self.refresh_task_list)
        dialog.exec()

    def open_edit_parameters_dialog(self):
        """Ouvre la boite d'édition des paramètres"""

        dialog = EditParametersDialog(self)
        dialog.exec()

    def search_tasks(self):
        """Affiche les tâches recherchées (à définir comment)"""
        pass

    def refresh_task_list(self):
        """Recharge les tâches et met à jour l'affichage du tableau"""

        self.task_table.table_model.tasks = self.db.get_tasks()
        self.task_table.table_model.layoutChanged.emit()  # Met à jour l'affichage
