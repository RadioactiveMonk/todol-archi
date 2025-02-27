from PyQt6.QtWidgets import QComboBox, QDateEdit
from backend.constants import CATEGORIES, DEFAULT_CATEGORY, DEFAULT_EXPIRATION


class DateSelector(QDateEdit):
    """Sélecteur de date générique utilisé dans plusieurs dialogues."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setCalendarPopup(True)
        self.setDate(DEFAULT_EXPIRATION)


class CategorySelector(QComboBox):
    """Menu déroulant pour la sélection de catégorie."""

    def __init__(self, default=DEFAULT_CATEGORY, parent=None) -> None:
        super().__init__(parent)
        self.addItems(CATEGORIES)
        self.setCurrentText(default)
