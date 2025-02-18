from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from PyQt6.QtGui import QFont
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

        # Création du tableau pour afficher les tâches
        self.task_table: QTableWidget = QTableWidget()
        self.task_table.setColumnCount(
            5
        )  # Nombre de colonnes (Statut, Titre, Expiration)
        self.task_table.setHorizontalHeaderLabels(
            ["Statut", "Titre", "Priorité", "Notes", "Expiration"]
        )

        # Ajustement des colones en fonction du texte header (titre des colones)
        self.task_table.resizeColumnsToContents()

        # Vérification avant d'appliquer setSectionResizeMode
        header = self.task_table.horizontalHeader()
        if header:
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.task_table.setFont(QFont("Arial", 12))  # Style du tableau
        main_layout.addWidget(self.task_table)

        # Layout horizontal pour organiser les boutons
        button_layout: QHBoxLayout = QHBoxLayout()

        # Création des boutons
        self.add_task_button: QPushButton = QPushButton("➕ Ajouter")
        self.edit_task_button: QPushButton = QPushButton("✏ Modifier")
        self.toggle_status_button: QPushButton = QPushButton("✔ Basculer Statut")
        self.delete_task_button: QPushButton = QPushButton("🗑 Supprimer")

        # Ajout des boutons au layout horizontal
        button_layout.addWidget(self.add_task_button)
        button_layout.addWidget(self.edit_task_button)
        button_layout.addWidget(self.toggle_status_button)
        button_layout.addWidget(self.delete_task_button)

        # Ajout du layout des boutons au layout principal
        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.show()
    sys.exit(app.exec())
