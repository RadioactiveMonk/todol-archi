from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QTextEdit,
    QMessageBox,
    QFormLayout,
)
from gui.selectors import DateSelector, PrioritySelector
from gui.stylesheets.styles import load_stylesheet


class BaseDialog(QDialog):
    """Fenêtre générique avec boutons 'OK' et 'Cancel'."""

    def __init__(self, title: str, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setFixedSize(400, 350)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.setStyleSheet(load_stylesheet("default"))

        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        self.main_layout.addLayout(button_layout)

    def add_form_field(self, label: str, widget) -> None:
        """Ajoute un champ de formulaire avec une étiquette.

        Args:
            label (str): Le texte de l'étiquette associée au champ.
            widget (QWidget): Le widget de saisie ou de sélection associé.

        Cette méthode permet d'insérer dynamiquement un champ de formulaire avant
        les boutons existants dans la boîte de dialogue. Elle assure l'ordre cohérent
        des éléments du formulaire.
        """

        self.main_layout.insertWidget(self.main_layout.count() - 2, QLabel(label))
        self.main_layout.insertWidget(self.main_layout.count() - 2, widget)


class AddTaskDialog(BaseDialog):
    """Fenêtre pour ajouter une nouvelle tâche."""

    def __init__(self, parent=None) -> None:
        super().__init__("Add New Task", parent)

        # Layout propre pour aligner les champs
        form_layout = QFormLayout()

        # Champs de saisie
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter task title ...")
        self.priority_selector = PrioritySelector()  # Medium par défaut
        self.date_selector = DateSelector()

        # Ajout des champs dans le layout FORM
        form_layout.addRow("", self.title_input)
        form_layout.addRow("Priority:", self.priority_selector)
        form_layout.addRow("Expiration date:", self.date_selector)

        # Ajout du form_layout au main_layout avant les boutons
        self.main_layout.insertLayout(
            0, form_layout
        )  # ✅ Ajoute bien le layout FORM en haut

        # Connexion du bouton 'OK'
        self.ok_button.clicked.connect(self.validate_and_accept)

    def validate_and_accept(self):
        """Vérifie les champs et retourne les données si valides"""

        title = self.title_input.text().strip()
        priority = self.priority_selector.currentText()
        due_date = (
            self.date_selector.date().toPyDate().isoformat()
        )  # ✅ Fix pour récupérer une vraie date

        if not title:
            QMessageBox.warning(self, "Erreur", "Le titre ne peut pas être vide.")
            return  # Bloque la fermeture du dialogue

        self.task_data = {
            "title": title,
            "priority": priority,
            "due_date": due_date,
        }
        self.accept()  # Ferme le dialogue si les données sont correctes


class EditTaskDialog(BaseDialog):
    """Fenêtre pour modifier une tâche existante."""

    def __init__(self, task_data, parent=None) -> None:
        super().__init__("Edit Task", parent)

        self.title_input = QLineEdit(task_data.get("title", ""))
        self.add_form_field("Title:", self.title_input)

        self.priority_combo = PrioritySelector(task_data.get("priority", "Medium"))
        self.add_form_field("Priority:", self.priority_combo)

        self.expiration_date = DateSelector(task_data.get("expiration"))
        self.add_form_field("Expiration Date:", self.expiration_date)

        self.notes_field = QTextEdit()
        self.notes_field.setText(task_data.get("notes", ""))
        self.add_form_field("Notes:", self.notes_field)


class FilterDialog(BaseDialog):
    """Fenêtre pour filtrer les tâches affichées."""

    def __init__(self, parent=None) -> None:
        super().__init__("Filter Tasks", parent)

        self.status_combo = QComboBox()
        self.status_combo.addItems(["All", "Pending", "Completed"])
        self.add_form_field("Status:", self.status_combo)

        self.priority_combo = PrioritySelector("All")
        self.add_form_field("Priority:", self.priority_combo)
