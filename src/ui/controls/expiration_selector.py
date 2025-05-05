from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QDateTimeEdit, QWidget

from core.defaults import DEFAULT_EXPIRATION


class ExpirationSelector(QDateTimeEdit):
    """Sélecteur de date"""

    def __init__(
        self,
        default: QDateTime = QDateTime.fromString(DEFAULT_EXPIRATION),
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setCalendarPopup(True)
        self.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.setCurrentSection(QDateTimeEdit.Section.MinuteSection)
        self.setDateTime(default)
