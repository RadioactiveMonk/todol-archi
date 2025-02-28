from PyQt6.QtWidgets import (
    QDialog,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
)
from gui.selectors import CategorySelector, DateTimeSelector
from backend.config import TASK_DIALOG_TITLE, TASK_DIALOG_GEOMETRY


class AddTaskDialog(QDialog):
    """Fenêtre pour ajouter une nouvelle tâche."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle(TASK_DIALOG_TITLE)
        self.setGeometry(*TASK_DIALOG_GEOMETRY)

        # Layout principal
        main_layout = QVBoxLayout(self)
        # Layout propre pour aligner les champs
        form_layout = QFormLayout()

        # Champs de saisie
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter task title ...")
        self.category_selector = CategorySelector()
        self.date_selector = DateTimeSelector()
        self.notes_input = QTextEdit(self)
        self.notes_input.setPlaceholderText("Enter task notes ...")

        # Ajout des champs dans le layout FORM
        form_layout.addRow("Title: ", self.title_input)
        form_layout.addRow("Category: ", self.category_selector)
        form_layout.addRow("Expiration date: ", self.date_selector)
        form_layout.addRow("Notes: ", self.notes_input)

        main_layout.addLayout(form_layout)  # Ajout du formulaire au layout principal

        self.ok_button = QPushButton("➕ Add", self)
        self.ok_button.clicked.connect(self.accept)  # Ferme la fenêtre au click
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)
