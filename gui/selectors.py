from PyQt6.QtWidgets import QComboBox, QDateEdit
from PyQt6.QtCore import QDate


class DateSelector(QDateEdit):
    """Sélecteur de date générique utilisé dans plusieurs dialogues."""

    def __init__(self, default_date=None, parent=None) -> None:
        super().__init__(parent)
        self.setCalendarPopup(True)
        self.setDate(default_date if default_date else QDate.currentDate())


class PrioritySelector(QComboBox):
    """Menu déroulant pour la sélection de la priorité, réutilisable."""

    def __init__(self, default_priority="Medium", parent=None) -> None:
        super().__init__(parent)
        self.addItems(["Low", "Medium", "High"])
        self.setCurrentText(default_priority)
