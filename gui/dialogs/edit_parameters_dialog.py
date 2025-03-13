from PyQt6.QtWidgets import (
    QDialog,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFormLayout,
    QLineEdit,
    QHBoxLayout,
    QApplication,
)
from PyQt6.QtCore import pyqtSignal
from gui.selectors import CategorySelector, ThemeSelector
from backend.config.constants import (
    EDIT_PARAMETERS_DIALOG_GEOMETRY,
    EDIT_PARAMETERS_DIALOG_TITLE,
)
from backend.settings_manager import SettingsManager
from backend.style_loader import load_stylesheet


class EditParametersDialog(QDialog):
    """Fenêtre d'édition des paramètres"""

    SETTINGS_UPDATED: pyqtSignal = pyqtSignal(dict)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent or QWidget())
        self.settings = SettingsManager()
        self.current_settings = self.settings.load_settings()
        self.current_theme = self.current_settings.get("theme", "default")

        self.setup_ui()

    def setup_ui(self):
        """Création de l'UI"""
        self.setWindowTitle(EDIT_PARAMETERS_DIALOG_TITLE)
        self.setGeometry(*EDIT_PARAMETERS_DIALOG_GEOMETRY)

        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        # 🔥 CategorySelector gère les catégories directement
        self.category_selector = CategorySelector()
        self.theme_selector = ThemeSelector()
        self.theme_selector.setCurrentText(self.current_theme)

        # Ajout des catégories
        add_category_layout = QHBoxLayout()
        self.add_category_input = QLineEdit(self)
        self.add_category_input.setPlaceholderText("Category name ...")

        self.add_category_button = QPushButton("➕", self)
        self.add_category_button.setMaximumWidth(40)
        self.add_category_button.clicked.connect(self.category_selector.add_category)

        add_category_layout.addWidget(self.add_category_input)
        add_category_layout.addWidget(self.add_category_button)

        # Suppression des catégories
        remove_category_layout = QHBoxLayout()
        self.remove_category_button = QPushButton("➖", self)
        self.remove_category_button.setMaximumWidth(40)
        self.remove_category_button.clicked.connect(self.category_selector.remove_category)

        remove_category_layout.addWidget(self.category_selector)
        remove_category_layout.addWidget(self.remove_category_button)

        form_layout.addRow("New category: ", add_category_layout)
        form_layout.addRow("Categories: ", remove_category_layout)
        form_layout.addRow("Theme: ", self.theme_selector)

        main_layout.addLayout(form_layout)

        self.ok_button = QPushButton("✔️Apply", self)
        self.ok_button.clicked.connect(self.accept)
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)

    def add_category(self) -> None:
        """Ajoute une catégorie via CategorySelector"""
        category_name = self.add_category_input.text().strip()
        if category_name:
            self.category_selector.add_category(category_name)
            self.add_category_input.clear()
            self.SETTINGS_UPDATED.emit(
                self.settings.load_settings()
            )  # 🔥 Signal de mise à jour

    def remove_category(self) -> None:
        """Supprime une catégorie via CategorySelector"""
        category_name = self.category_selector.currentText()
        self.category_selector.remove_category(category_name)
        self.SETTINGS_UPDATED.emit(
            self.settings.load_settings()
        )  # 🔥 Signal de mise à jour

    def accept(self) -> None:
        """Applique immédiatement le thème et ferme la boîte de dialogue"""
        new_theme = self.theme_selector.currentText()
        self.settings.update_settings("theme", new_theme)

        app = QApplication.instance()
        if isinstance(app, QApplication):
            load_stylesheet(app)

        self.SETTINGS_UPDATED.emit(self.settings.load_settings())
        self.close()
