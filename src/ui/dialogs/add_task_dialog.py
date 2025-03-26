from PyQt6.QtCore import QDateTime, pyqtSignal
from PyQt6.QtWidgets import (
    QDialog,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from src.core.database.db_manager import DbManager
from src.models.task import Task
from src.ui.controls.category_selector import CategorySelector
from src.ui.controls.expiration_selector import ExpirationSelector

from core.app_constants import (
    DEFAULT_STATUS,
    EDIT_TASK_DIALOG_TITLE,
    TASK_DIALOG_GEOMETRY,
    TASK_DIALOG_TITLE,
)


class AddTaskDialog(QDialog):
    """Dialog window to add a task or to edit a task in edit mode"""

    ok_signal: pyqtSignal = pyqtSignal()
     # Envoie un signal, pour éviter d'incorporer logique métier

    def __init__(self, parent: QWidget, task: Task | None = None) -> None:
        super().__init__(parent)

        self.db = DbManager()
        self.task = task
        self.setup_ui()
        self.populate_fields()

    def setup_ui(self):
        """Creation du de la fenetre et du formulaire"""

        self.setWindowTitle(
            TASK_DIALOG_TITLE if not self.task else EDIT_TASK_DIALOG_TITLE
        )
        self.setGeometry(*TASK_DIALOG_GEOMETRY)

        # Layout principal
        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        # Champs de saisie
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter task title ...")
        self.title_input.setFocus()  # Focus sur le titre
        self.category_selector = CategorySelector()
        self.expiration_selector = ExpirationSelector()
        self.notes_input = QTextEdit(self)
        self.notes_input.setPlaceholderText("Enter task notes ...")

        # Ajout des champs dans le layout 'form_layout'
        form_layout.addRow("Title: ", self.title_input)
        form_layout.addRow("Category: ", self.category_selector)
        form_layout.addRow("Expiration date: ", self.expiration_selector)
        form_layout.addRow("Notes: ", self.notes_input)

        main_layout.addLayout(form_layout)  # Ajout du formulaire au layout principal

        self.ok_button = QPushButton("➕ Add" if not self.task else "✔️ Apply", self)
        self.ok_button.setEnabled(
            False
        )  # Gestion du boutton ok en fonction du titre (vide=False, entrée=True)
        self.title_input.textChanged.connect(
            lambda: self.ok_button.setEnabled(bool(self.title_input.text().strip()))
        )
        self.ok_button.clicked.connect(self.save_task)
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)

    def populate_fields(self):
        """Pré-rempli les champs si une tâche est passée en paramètre"""

        if self.task:
            self.title_input.setText(self.task.title)
            self.category_selector.setCurrentText(self.task.category)
            self.expiration_selector.setDateTime(
                QDateTime.fromString(self.task.expiration, "yyyy-MM-dd HH:mm")
            )
            self.notes_input.setPlainText(self.task.notes)

    def save_task(self):
        """Crée ou met à jour une tâche en base"""

        title = self.title_input.text().strip()
        if not title:
            return

        task_data = Task(
            title=title,
            category=self.category_selector.currentText(),
            expiration=self.expiration_selector.dateTime().toString("yyyy-MM-dd HH:mm"),
            notes=self.notes_input.toPlainText().strip(),
            completed=DEFAULT_STATUS,
        )

        if self.task:
            assert self.task.tid is not None
            self.db.update_task(
                task_id=self.task.tid,
                completed=task_data.completed,
                category=task_data.category,
                expiration=task_data.expiration,
                title=task_data.title,
                notes=task_data.notes,
            )
        else:
            self.db.add_task(task_data)

        self.ok_signal.emit()
        self.accept()
