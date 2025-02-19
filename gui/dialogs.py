from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QTextEdit,
)
from gui.selectors import DateSelector, PrioritySelector


class BaseDialog(QDialog):
    """Fenêtre générique avec boutons 'OK' et 'Cancel'."""

    def __init__(self, title: str, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(400, 350)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

    def add_form_field(self, label: str, widget) -> None:
        """Ajoute un champ de formulaire avec une étiquette.

        Args:
            label (str): Le texte de l'étiquette associée au champ.
            widget (QWidget): Le widget de saisie ou de sélection associé.

        Cette méthode permet d'insérer dynamiquement un champ de formulaire avant
        les boutons existants dans la boîte de dialogue. Elle assure l'ordre cohérent
        des éléments du formulaire.
        """

        self.layout.insertWidget(
            self.layout.count() - 1, QLabel(label)
        )  # Ajoute l'étiquette
        self.layout.insertWidget(
            self.layout.count() - 1, widget
        )  # Ajoute le champ correspondant


class AddTaskDialog(BaseDialog):
    """Fenêtre pour ajouter une nouvelle tâche."""

    def __init__(self, parent=None) -> None:
        super().__init__("Add New Task", parent)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Task title")
        self.add_form_field("Title:", self.title_input)

        self.priority_combo = PrioritySelector()
        self.add_form_field("Priority:", self.priority_combo)

        self.expiration_date = DateSelector()
        self.add_form_field("Expiration Date:", self.expiration_date)

        self.notes_field = QTextEdit()
        self.notes_field.setPlaceholderText("Additional notes...")
        self.add_form_field("Notes:", self.notes_field)


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
