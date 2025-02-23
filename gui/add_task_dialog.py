from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox
from backend.validators import Validators
from gui.selectors import PrioritySelector, DateSelector


class AddTaskDialog(QDialog):
    """Fenêtre pour ajouter une nouvelle tâche."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Add New Task")

        # Layout propre pour aligner les champs
        form_layout = QFormLayout()

        # Champs de saisie
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter task title ...")
        self.priority_selector = PrioritySelector()
        self.date_selector = DateSelector()

        # Ajout des champs dans le layout FORM
        form_layout.addRow("Titre: ", self.title_input)
        form_layout.addRow("Priority: ", self.priority_selector)
        form_layout.addRow("Expiration date: ", self.date_selector)

        self.setLayout(form_layout)

        # Connexion du bouton 'OK'
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.validate_and_accept)
        form_layout.addWidget(self.ok_button)  # ✅ Ajout correct du bouton OK

    def validate_and_accept(self):
        """Vérifie les champs et retourne les données si valides"""
        title = self.title_input.text().strip()
        priority = self.priority_selector.currentText()
        due_date = self.date_selector.date()

        try:
            Validators.validate_title(title, self)
            if not Validators.validate_due_date(due_date, self):  # ✅ Vérifie la date
                return  # ✅ Stoppe l'ajout si la date est invalide
            Validators.validate_priority(priority, self)

            self.task_data = {
                "title": title,
                "priority": priority,
                "due_date": due_date.toString("yyyy-MM-dd"),
            }
            self.accept()  # ✅ Ferme le dialogue si les données sont valides

        except ValueError as e:
            QMessageBox.warning(
                self, "Erreur de validation", str(e)
            )  # ✅ Affiche un message d'erreur propre
