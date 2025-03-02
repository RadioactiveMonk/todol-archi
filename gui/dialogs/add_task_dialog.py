from PyQt6.QtWidgets import (
    QDialog,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
    QWidget,
)
from PyQt6.QtCore import pyqtSignal
from gui.selectors import CategorySelector, ExpirationSelector
from backend.config import TASK_DIALOG_TITLE, TASK_DIALOG_GEOMETRY
from backend.database import DatabaseManager


class AddTaskDialog(QDialog):
    """Fenêtre pour ajouter une nouvelle tâche."""

    task_added = (
        pyqtSignal()
    )  # Envoie un signal, pour éviter d'incorporer logique métier

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setWindowTitle(TASK_DIALOG_TITLE)
        self.setGeometry(*TASK_DIALOG_GEOMETRY)
        self.db_manager = DatabaseManager()

        # Layout principal
        main_layout = QVBoxLayout(self)
        # Layout propre pour aligner les champs
        form_layout = QFormLayout()

        # Champs de saisie
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter task title ...")
        self.category_selector = CategorySelector()
        self.datetime_selector = ExpirationSelector()
        self.notes_input = QTextEdit(self)
        self.notes_input.setPlaceholderText("Enter task notes ...")

        # Ajout des champs dans le layout FORM
        form_layout.addRow("Title: ", self.title_input)
        form_layout.addRow("Category: ", self.category_selector)
        form_layout.addRow("Expiration date: ", self.datetime_selector)
        form_layout.addRow("Notes: ", self.notes_input)

        main_layout.addLayout(form_layout)  # Ajout du formulaire au layout principal

        self.ok_button = QPushButton("➕ Add", self)
        self.ok_button.clicked.connect(self.add_task)  # Ferme la fenêtre au click
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)

    def add_task(self):
        """Récupère les données du formulaire et les enregistre dans la base de données"""

        title = self.title_input.text().strip()
        category = self.category_selector.currentText()
        expiration = self.datetime_selector.dateTime().toString(
            "yyyy-MM-dd HH:mm"
        )  # Convertit en str la date séléctionnée
        notes = self.notes_input.toPlainText().strip()

        if not title:  # Vérifie qu'un titre est saisi
            return

        # 🔥 On appelle directement DatabaseManager.add_task() pour ajouter la tâche
        self.db_manager.add_task(
            status=False,
            category=category,
            expiration=expiration,
            title=title,
            notes=notes,
        )

        self.task_added.emit()  # 🔥 Émet le signal pour prévenir MainWindow
        self.accept()  # 🔥 Ferme la boîte de dialogue
