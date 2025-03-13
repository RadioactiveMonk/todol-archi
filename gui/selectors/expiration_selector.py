from PyQt6.QtWidgets import QDateTimeEdit, QWidget
from PyQt6.QtCore import QDateTime
from backend.config.constants import DEFAULT_DATETIME


class ExpirationSelector(QDateTimeEdit):
    """Sélecteur de date"""

    def __init__(
        self, default: QDateTime = DEFAULT_DATETIME, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.setCalendarPopup(True)
        self.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.setCurrentSection(QDateTimeEdit.Section.HourSection)
        self.setDateTime(default)
