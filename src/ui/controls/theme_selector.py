from PyQt6.QtWidgets import QComboBox
from src.core.cached_utils import get_available_themes
from src.core.settings.settings_manager import get_setting


class ThemeSelector(QComboBox):
    def __init__(self, parent: QComboBox | None = None):
        super().__init__(parent)
        self.refresh_themes()
        self.setCurrentText(get_setting("theme"))

    def refresh_themes(self):
        self.clear()
        self.addItems(get_available_themes())
