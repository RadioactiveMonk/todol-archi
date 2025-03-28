from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from core.settings_manager import (
    get_setting,
    load_settings,
    set_setting,
)
from core.style_loader import reload_theme
from ui.controls.category_selector import CategorySelector
from ui.controls.theme_selector import ThemeSelector
from ui.ui_constants import (
    EDIT_PARAMETERS_DIALOG_GEOMETRY,
    EDIT_PARAMETERS_DIALOG_TITLE,
)


class EditParametersDialog(QDialog):
    """Fenêtre d'édition des paramètres"""

    SETTINGS_UPDATED: pyqtSignal = pyqtSignal(dict)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent if parent is not None else QWidget())

        self.setup_ui()

    def setup_ui(self):
        """Création de l'UI"""
        self.setWindowTitle(EDIT_PARAMETERS_DIALOG_TITLE)
        self.setGeometry(*EDIT_PARAMETERS_DIALOG_GEOMETRY)

        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        #  Utilisation des sélecteurs propres
        self.category_selector = CategorySelector()
        self.theme_selector = ThemeSelector()
        self.theme_selector.setCurrentText(get_setting("theme"))

        # Ajout des catégories
        add_category_layout = QHBoxLayout()
        self.add_category_input = QLineEdit(self)
        self.add_category_input.setPlaceholderText("Category name ...")

        self.add_category_button = QPushButton("➕", self)
        self.add_category_button.setMaximumWidth(40)
        self.add_category_button.clicked.connect(self.add_category)

        add_category_layout.addWidget(self.add_category_input)
        add_category_layout.addWidget(self.add_category_button)

        # Suppression des catégories
        remove_category_layout = QHBoxLayout()
        self.remove_category_button = QPushButton("➖", self)
        self.remove_category_button.setMaximumWidth(40)
        self.remove_category_button.clicked.connect(self.remove_selected_category)

        remove_category_layout.addWidget(self.category_selector)
        remove_category_layout.addWidget(self.remove_category_button)

        # Reset to default
        self.reset_app_button = QPushButton("Reset", self)
        self.reset_app_button.setMaximumWidth(80)
        self.reset_app_button.clicked.connect(self.reset_settings)  # 🚩

        form_layout.addRow("New category: ", add_category_layout)
        form_layout.addRow("Categories: ", remove_category_layout)
        form_layout.addRow("Theme: ", self.theme_selector)
        form_layout.addRow(self.reset_app_button)

        main_layout.addLayout(form_layout)

        self.ok_button = QPushButton("✔️Apply", self)
        self.ok_button.clicked.connect(self.accept)
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)

    def add_category(self) -> None:
        """Ajoute une nouvelle catégorie et met à jour l'UI + JSON"""
        category_name = self.add_category_input.text().strip()
        if category_name:
            self.category_selector.add_category(category_name)
            self.SETTINGS_UPDATED.emit(load_settings())
            self.add_category_input.clear()

    def remove_selected_category(self) -> None:
        """Supprime la catégorie sélectionnée"""
        category = self.category_selector.currentText()
        if category:
            self.category_selector.remove_category(category)
            self.SETTINGS_UPDATED.emit(load_settings())

    def reset_settings(self):
        # 🚩 Qwarning: "Are you sure you want to reset to default ? (all datas will be lost)"
        pass

    def accept(self) -> None:
        """Applique immédiatement le thème et ferme la boîte de dialogue"""
        new_theme = self.theme_selector.currentText()
        set_setting("theme", new_theme)
        app = QApplication.instance()
        if isinstance(app, QApplication):
            reload_theme(app)

        self.SETTINGS_UPDATED.emit(load_settings())
        self.close()
