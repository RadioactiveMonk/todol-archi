from PyQt6.QtCore import QDateTime
from PyQt6.QtWidgets import QDateTimeEdit, QWidget

from core.default_values import DEFAULT_DATETIME


class ExpirationSelector(QDateTimeEdit):
    """Sélecteur de date"""

    def __init__(
        self, default: QDateTime = DEFAULT_DATETIME, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.setCalendarPopup(True)
        self.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.setCurrentSection(QDateTimeEdit.Section.MinuteSection)
        self.setDateTime(default)
