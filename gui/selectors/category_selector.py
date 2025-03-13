from PyQt6.QtWidgets import QComboBox, QWidget
from backend.settings_manager import SettingsManager


class CategorySelector(QComboBox):
    """Menu déroulant pour la sélection de catégorie avec gestion intégrée."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.settings = SettingsManager()
        self.refresh_categories()

    def refresh_categories(self):
        """Recharge les catégories depuis settings.json"""
        categories = self.settings.load_settings().get("categories", [])
        self.clear()
        self.addItems(categories)

    def add_category(self, category_name: str):
        """Ajoute une catégorie et met à jour la liste"""
        if category_name and category_name not in [
            self.itemText(i) for i in range(self.count())
        ]:
            categories = self.settings.load_settings().get("categories", [])
            categories.append(category_name)
            self.settings.update_settings("categories", categories)
            self.refresh_categories()  # 🔥 Rafraîchit l'affichage

    def remove_category(self):
        """Supprime la catégorie sélectionnée"""
        category_name = self.currentText()
        categories = self.settings.load_settings().get("categories", [])
        if category_name in categories:
            categories.remove(category_name)
            self.settings.update_settings("categories", categories)
            self.refresh_categories()  # 🔥 Mise à jour de l'affichage
