from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)


class BaseDialog(QDialog):
    """Fenêtre générique avec boutons 'OK' et 'Cancel'."""

    def __init__(self, title: str, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setFixedSize(400, 350)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        self.main_layout.addLayout(button_layout)
