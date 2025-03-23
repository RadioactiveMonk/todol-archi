from PyQt6.QtWidgets import QComboBox
from backend.core.cached_utils import get_categories



class CategorySelector(QComboBox):
    """Menu déroulant pour la sélection de catégorie avec gestion intégrée."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh_categories()

    def refresh_categories(self):
        self.clear()
        self.addItems(get_categories())

    def add_category(self, category: str) -> None:
        """Ajoute une nouvelle catégorie si elle n'existe pas encore"""
        if category not in get_categories():
            self.addItem(category)
    
    def remove_category(self, category: str):
        """Supprime une catégorie existante"""
        if category in get_categories():
            self.removeItem()

