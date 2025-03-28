from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QWidget
from core.path import ICONS_DIR


class CustomButton(QPushButton):
    """Bouton personnalisé avec icône et tooltip."""

    def __init__(
        self, icon_name: str = "", tooltip: str = "", parent: QWidget | None = None
    ) -> None:
        super().__init__(parent or QWidget())
        icon_path = ICONS_DIR / icon_name
        self.setIcon(QIcon(str(icon_path)))
        self.setToolTip(tooltip)
