from typing import Optional
from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QVBoxLayout
from gui.selectors import CategorySelector, DateTimeSelector


class AddTaskDialog(QDialog):
    """Fenêtre pour ajouter une nouvelle tâche."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Add New Task")
        self.setGeometry(100, 100, 400, 200)

        # Layout principal
        main_layout = QVBoxLayout(self)
        # Layout propre pour aligner les champs
        form_layout = QFormLayout()

        # Champs de saisie
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter task title ...")
        self.category_selector = CategorySelector()
        self.date_selector = DateTimeSelector()

        # Ajout des champs dans le layout FORM
        form_layout.addRow("Title: ", self.title_input)
        form_layout.addRow("Category: ", self.category_selector)
        form_layout.addRow("Expiration date: ", self.date_selector)

        main_layout.addLayout(form_layout)  # Ajout du formulaire au layout principal

        self.ok_button = QPushButton("➕ Add", self)
        self.ok_button.clicked.connect(self.accept)  # Ferme la fenêtre au click
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)
