from backend.core.cached_utils import get_available_themes
from configuration.settings_manager import get_setting
from PyQt6.QtWidgets import QComboBox


class ThemeSelector(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh_themes()
        self.setCurrentText(get_setting("theme"))

    def refresh_themes(self):
        self.clear()
        self.addItems(get_available_themes())
