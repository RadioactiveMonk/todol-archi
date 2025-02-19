from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
)
from gui.selectors import DateSelector, PrioritySelector


class BaseDialog(QDialog):
    """Fenêtre générique avec boutons 'OK' et 'Cancel'."""

    def __init__(self, title: str, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)


class AddTaskDialog(BaseDialog):
    """Fenêtre pour ajouter une nouvelle tâche."""

    def __init__(self, parent=None) -> None:
        super().__init__("Add New Task", parent)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Task title")
        self.layout.insertWidget(0, QLabel("Title:"))
        self.layout.insertWidget(1, self.title_input)

        self.priority_combo = PrioritySelector()
        self.layout.insertWidget(2, QLabel("Priority:"))
        self.layout.insertWidget(3, self.priority_combo)

        self.expiration_date = DateSelector()
        self.layout.insertWidget(4, QLabel("Expiration Date:"))
        self.layout.insertWidget(5, self.expiration_date)


class EditTaskDialog(BaseDialog):
    """Fenêtre pour modifier une tâche existante."""

    def __init__(self, task_data, parent=None) -> None:
        super().__init__("Edit Task", parent)

        self.title_input = QLineEdit(task_data.get("title", ""))
        self.layout.insertWidget(0, QLabel("Title:"))
        self.layout.insertWidget(1, self.title_input)

        self.priority_combo = PrioritySelector(task_data.get("priority", "Medium"))
        self.layout.insertWidget(2, QLabel("Priority:"))
        self.layout.insertWidget(3, self.priority_combo)

        self.expiration_date = DateSelector(task_data.get("expiration"))
        self.layout.insertWidget(4, QLabel("Expiration Date:"))
        self.layout.insertWidget(5, self.expiration_date)


class FilterDialog(BaseDialog):
    """Fenêtre pour filtrer les tâches affichées."""

    def __init__(self, parent=None) -> None:
        super().__init__("Filter Tasks", parent)

        self.status_combo = QComboBox()
        self.status_combo.addItems(["All", "Pending", "Completed"])
        self.layout.insertWidget(0, QLabel("Status:"))
        self.layout.insertWidget(1, self.status_combo)

        self.priority_combo = PrioritySelector("All")
        self.layout.insertWidget(2, QLabel("Priority:"))
        self.layout.insertWidget(3, self.priority_combo)
