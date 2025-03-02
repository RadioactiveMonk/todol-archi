from typing import List, Dict, Any, Optional, Union
from PyQt6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QTableView,
    QWidget,
    QMenuBar,
    QMessageBox,
    QMenu,
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QDir
from backend.database import DatabaseManager
from backend.models.task_table_model import TaskTableModel


class CustomButton(QPushButton):
    """Bouton personnalisé avec icône et tooltip."""

    def __init__(self, icon_name: str, tooltip: str, parent: QWidget) -> None:
        super().__init__(parent)
        icon_path = QDir.current().filePath(f"resources/icons/{icon_name}")
        self.setIcon(QIcon(icon_path))
        self.setToolTip(tooltip)


class SearchTasks(QLineEdit):
    """Barre de recherche"""

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setPlaceholderText(" Search tasks ...")
        self.setFixedHeight(40)


class TaskTable(QTableView):
    """Configuration graphique des tâches. Aucune logique métier, gérée par backend.TaskTableModel"""

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.database = (
            DatabaseManager()
        )  # On amene le gestionnaire partout ou il faut gerer les tâches
        self.table_model = TaskTableModel(
            self, self.database
        )  # Connexion de la logique

        self.setModel(self.table_model)  # Association du modèle a TaskTable(QTableView)
        self.setup_ui()

    def setup_ui(self):
        """Configuration de l'affichage de la table"""
        self.setSortingEnabled(True)


class MenuBar(QMenuBar):
    """Barre de menu simple"""

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        # Création explicite des menus
        file_menu = QMenu("File", self)
        help_menu = QMenu("Help", self)

        # Ajout du menu à la barre de menu
        self.addMenu(file_menu)
        self.addMenu(help_menu)

        # Ajout de l'action Quitter
        quit_action = QAction("Quit", self)
        quit_action.setShortcut("Ctrl+Q")  # Raccourci clavier
        quit_action.triggered.connect(
            parent.close
        )  # Fermeture de la fenêtre principale
        file_menu.addAction(quit_action)  # Ajout correct au menu Fichier

        # Ajout de l'action "À propos"
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)  # Ajout correct au menu Aide

    def show_about(self) -> None:
        """Affiche une boîte de dialogue À propos"""
        QMessageBox.information(
            self,
            "About",
            "Todol-Pro V1.0 - A task manager project in Python with PyQt6\nby doyouDance",
        )
