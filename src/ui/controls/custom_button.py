
from PyQt6.QtCore import QDir
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QWidget


class CustomButton(QPushButton):
    """Bouton personnalisé avec icône et tooltip."""

    def __init__(
        self, icon_name: str = "", tooltip: str = "", parent: QWidget | None = None
    ) -> None:
        super().__init__(parent or QWidget())
        icon_path = QDir.current().filePath(f"gui/resources/icons/{icon_name}")
        self.setIcon(QIcon(icon_path))
        self.setToolTip(tooltip)
