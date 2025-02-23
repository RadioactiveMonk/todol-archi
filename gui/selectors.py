from PyQt6.QtWidgets import QComboBox, QDateEdit
from PyQt6.QtCore import QDate
from backend.constants import PRIORITY_MEDIUM, task_priorities


class DateSelector(QDateEdit):
    """Sélecteur de date générique utilisé dans plusieurs dialogues."""

    def __init__(self, default_date=None, parent=None) -> None:
        super().__init__(parent)
        self.setCalendarPopup(True)
        self.setDate(default_date if default_date else QDate.currentDate())


class PrioritySelector(QComboBox):
    """Menu déroulant pour la sélection de la priorité, réutilisable."""

    def __init__(self, default_priority=PRIORITY_MEDIUM, parent=None) -> None:
        super().__init__(parent)
        self.addItems(task_priorities)
        self.setCurrentText(default_priority)
