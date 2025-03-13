from PyQt6.QtWidgets import QComboBox, QWidget, QDateTimeEdit
from PyQt6.QtCore import QDateTime
from backend.config.constants import (
    DEFAULT_DATETIME,
)
from backend.config.configs import DEFAULT_THEME, APP_THEMES, CATEGORIES
from backend.settings_manager import SettingsManager


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
        self, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.settings = SettingsManager()
        self.categories = self.settings.load_settings().get("categories", CATEGORIES)
        self.refresh_categories()

    def refresh_categories(self):
        """Recharge les catégories depuis settings.json"""
        self.clear()
        self.addItems(self.categories)

    def add_category(self, category_name: str):
        """Ajoute une catégorie"""
        if category_name not in self.categories:
            self.categories.append(category_name)
            self.settings.update_settings("categories", self.categories)
            self.refresh_categories()

    def remove_category(self, category_name: str):
        """Supprime une catégorie"""
        if category_name in self.categories:
            self.categories.remove(category_name)
            self.settings.update_settings("categories", self.categories)


class ThemeSelector(QComboBox):
    """Menu déroulant pour les thèmes"""

    def __init__(
        self, default: str = DEFAULT_THEME, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.addItems(APP_THEMES)
        self.setCurrentText(default)
