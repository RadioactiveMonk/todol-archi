from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QMenu,
    QMenuBar,
    QMessageBox,
    QWidget,
)


class MenuBar(QMenuBar):
    """Application menu bar"""

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
            "Todol Pro - Tasks manager desktop application.\n\n"
            "Author: Sébastien Reisen\n"
            "Link: https://github.com/RadioactiveMonk/",
        )
