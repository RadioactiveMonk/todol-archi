from dataclasses import asdict
from typing import Union

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

from core.default_values import DEFAULT_STATUS
from core.path import DB_FILE
from helpers.contextmanagers import open_db
from models.task import Task
from ui.controls.category_selector import CategorySelector
from ui.controls.expiration_selector import ExpirationSelector
from ui.ui_constants import (
    EDIT_TASK_DIALOG_TITLE,
    TASK_DIALOG_GEOMETRY,
    TASK_DIALOG_TITLE,
)


class AddTaskDialog(QDialog):
    """Dialog window to add a task or to edit a task in edit mode"""

    ok_signal: pyqtSignal = pyqtSignal()
    # Envoie un signal, pour éviter d'incorporer logique métier

    def __init__(self, parent: QWidget, task: Union["Task", None] = None) -> None:
        super().__init__(parent)

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

        task = Task(
            title=title,
            category=self.category_selector.currentText(),
            completed=bool(int(DEFAULT_STATUS)),
            expiration=self.expiration_selector.dateTime().toString("yyyy-MM-dd HH:mm"),
            notes=self.notes_input.toPlainText().strip(),
        )

        if self.task:
            assert self.task.id is not None
            with open_db(DB_FILE) as db:
                db.update_task(task_id=self.task.id, **asdict(task))
        else:
            with open_db(DB_FILE) as db:
                db.add_task(**task.to_dict(exclude={"id"}))

        self.ok_signal.emit()
        self.accept()
