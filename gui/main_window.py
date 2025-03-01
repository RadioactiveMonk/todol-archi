from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
)
from typing import List, Dict, Any, Optional, Union
from PyQt6.QtGui import QIcon
from gui.dialogs.add_task_dialog import AddTaskDialog
from gui.dialogs.edit_parameters_dialog import EditParametersDialog
from gui.widgets import CustomButton, SearchTasks, TaskTable, MenuBar
from backend.task_manager import TaskManager
from backend.config import MAIN_WINDOW_TITLE, MAIN_WINDOW_GEOMETRY


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application To-Do List."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(MAIN_WINDOW_TITLE)  # Définition du titre de la fenêtre
        self.setGeometry(*MAIN_WINDOW_GEOMETRY)  # Position et taille de la fenêtre
        self.setWindowIcon(
            QIcon("resources/icons/app_icon.png")
        )  # Ajout d'une icône personnalisée

        self.task_manager = TaskManager()
        
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
        self.add_task_button = CustomButton("add.png", "Add new task", self)
        self.add_task_button.clicked.connect(self.open_add_task_dialog)
        action_layout.addWidget(self.add_task_button)

        self.edit_parameters_button = CustomButton(
            "app-parameters.png", "Edit parameters", self
        )
        self.edit_parameters_button.clicked.connect(self.open_edit_parameters_dialog)
        action_layout.addWidget(self.edit_parameters_button)

        main_layout.addLayout(action_layout)  # Ajout du layout de recherche et boutons

        # Création du tableau des tâches personnalisé
        self.task_table = TaskTable(self)
        main_layout.addWidget(self.task_table)

        self.refresh_task_list()  # ✅ Charge les tâches dès l’ouverture de l’appli

        central_widget.setLayout(main_layout)

    def open_add_task_dialog(self) -> None:
        """Ouvre la boîte de dialogue d'ajout de tâche"""

        dialog = AddTaskDialog(self)
        dialog.exec()

    def open_edit_parameters_dialog(self):
        """Ouvre la boite d'édition des paramètres"""
        dialog = EditParametersDialog(self)
        dialog.exec()

    def refresh_task_list(self):
        """Met à jour l'affichâge des tâches"""
        pass

    def search_tasks(self):
        """Affiche les tâches recherchées (à définir comment)"""
        pass
