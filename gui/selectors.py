from PyQt6.QtWidgets import QComboBox, QWidget, QDateTimeEdit
from PyQt6.QtCore import QDateTime
from backend.config.constants import (
    DEFAULT_DATETIME,
)
from backend.config.configs import DEFAULT_THEME, APP_THEMES, DEFAULT_CATEGORY, CATEGORIES


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


class CategorySelector(QComboBox):
    """Menu déroulant pour la sélection de catégorie."""

    def __init__(
        self, default: str = DEFAULT_CATEGORY, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.addItems(CATEGORIES)
        self.setCurrentText(default)


class ThemeSelector(QComboBox):
    """Menu déroulant pour les thèmes"""

    def __init__(
        self, default: str = DEFAULT_THEME, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.addItems(APP_THEMES)
        self.setCurrentText(default)
