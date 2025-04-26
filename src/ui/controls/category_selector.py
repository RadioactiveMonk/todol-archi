from PySide6.QtWidgets import QComboBox

from core.settings_manager import get_setting, set_setting
from helpers.log_utils import logger


class CategorySelector(QComboBox):
    """Menu déroulant pour la sélection de catégorie avec gestion intégrée."""

    def __init__(self, parent: QComboBox | None = None):
        super().__init__(parent)
        self.refresh_categories()

    def refresh_categories(self) -> None:
        """Refreshes the list of categories in the selector."""
        from helpers.cached_utils import get_categories

        self.clear()
        categories: list[str] = list(get_categories())
        self.addItems(categories)

    def add_category(self, category: str) -> None:
        """Ajoute une catégorie dans le sélecteur et dans le fichier settings"""
        current = get_setting("categories", [])
        if category not in current:
            current.append(category)
            set_setting("categories", current)
            self.addItem(category)

    def remove_category(self, category: str) -> None:
        """Supprime une catégorie dans le sélecteur et dans le fichier settings"""
        index = self.findText(category)
        if index == -1:
            logger.warning(f"Category '{category}' not found in selector")
            return

        self.removeItem(index)

        current = get_setting("categories", [])
        if category in current:
            current.remove(category)
            set_setting("categories", current)
