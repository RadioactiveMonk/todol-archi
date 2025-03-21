from PyQt6.QtWidgets import QComboBox, QWidget
from configuration.constants import APP_THEMES, DEFAULT_THEME

class ThemeSelector(QComboBox):
    """Menu déroulant pour les thèmes"""

    def __init__(
        self, default: str = DEFAULT_THEME, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.addItems(APP_THEMES)
        self.setCurrentText(default)
