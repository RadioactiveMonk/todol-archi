from PyQt6.QtWidgets import QComboBox
from backend.settings_manager import SettingsManager


class CategorySelector(QComboBox):
    """Sélecteur de catégories avec chargement dynamique"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = SettingsManager()
        self.refresh_categories()

    def refresh_categories(self):
        """Recharge les catégories depuis settings.json"""
        self.clear()
        categories = self.settings.load_settings().get(
            "categories", ["General", "Work", "Hobbies"]
        )
        self.addItems(categories)

    def add_category(self, category_name: str):
        """Ajoute une catégorie"""
        categories = self.settings.load_settings().get("categories", [])
        if category_name and category_name not in categories:
            categories.append(category_name)
            self.settings.update_settings("categories", categories)
            self.refresh_categories()  # 🔥 Rafraîchit la liste

    def remove_category(self, category_name: str):
        """Supprime une catégorie"""
        categories = self.settings.load_settings().get("categories", [])
        if category_name in categories:
            categories.remove(category_name)
            self.settings.update_settings("categories", categories)
            self.refresh_categories()  # 🔥 Rafraîchit la liste
