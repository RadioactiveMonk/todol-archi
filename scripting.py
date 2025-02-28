from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton
from gui.selectors import CategorySelector, DateTimeSelector


class AddTaskDialog(QDialog):
    """Fenêtre pour ajouter une nouvelle tâche."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Add New Task")
        self.setGeometry(100, 100, 400, 200)

        # ✅ Layout principal (vertical) pour organiser proprement
        main_layout = QVBoxLayout(self)

        # ✅ Layout formulaire pour aligner les champs
        form_layout = QFormLayout()

        # ✅ Champs de saisie
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter task title ...")
        self.category_selector = CategorySelector()
        self.date_selector = DateTimeSelector()

        # ✅ Ajout des champs dans le layout formulaire
        form_layout.addRow("Title:", self.title_input)
        form_layout.addRow("Category:", self.category_selector)
        form_layout.addRow("Expiration date:", self.date_selector)

        main_layout.addLayout(
            form_layout
        )  # ✅ Ajout du formulaire dans le layout principal

        # ✅ Bouton 'OK'
        self.ok_button = QPushButton("➕ Add", self)
        self.ok_button.clicked.connect(self.accept)  # ✅ Ferme la boîte de dialogue
        main_layout.addWidget(self.ok_button)  # ✅ Ajout du bouton en bas

        self.setLayout(main_layout)  # ✅ Applique le layout principal

    def get_task_data(self) -> dict:
        """Récupère les données saisies dans le formulaire."""
        return {
            "title": self.title_input.text().strip(),
            "category": self.category_selector.currentText(),
            "expiration": self.date_selector.dateTime(),
        }
