from PyQt6.QtWidgets import (
    QDialog,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFormLayout,
    QLineEdit,
)
from gui.selectors import CategorySelector, ThemeSelector
from backend.config import EDIT_PARAMETERS_DIALOG_GEOMETRY, EDIT_PARAMETERS_DIALOG_TITLE
from backend.constants import CATEGORIES


class EditParametersDialog(QDialog):
    """Fenêtre d'édition des paramètres"""

    def __init__(self, parent: QWidget) -> None:
        """
        Layouts de la fenêtre de paramètres

         Parameters
         ----------
         parent : QWidget
             De quelle fenêtre dépend la boite de dialogue

        """

        super().__init__(parent)
        self.setWindowTitle(EDIT_PARAMETERS_DIALOG_TITLE)
        self.setGeometry(*EDIT_PARAMETERS_DIALOG_GEOMETRY)

        # Layout principal vertical
        main_layout = QVBoxLayout(self)

        # Layout pour aligner les éléments
        form_layout = QFormLayout()

        # Parametres

        self.category_selector = CategorySelector()
        self.theme_selector = ThemeSelector()
        self.add_category_input = QLineEdit(self)
        self.add_category_input.setPlaceholderText("Category name ...")
        self.add_category_button = QPushButton("➕ Add", self)
        self.add_category_button.clicked.connect(self.add_category)

        # Affichage par ligne

        form_layout.addRow("Add new category: ", self.add_category_input)
        form_layout.addRow(self.add_category_button)
        form_layout.addRow("Categories: ", self.category_selector)
        form_layout.addRow("Theme: ", self.theme_selector)

        # Ajout des lignes au layout principal

        main_layout.addLayout(form_layout)

        self.ok_button = QPushButton("Apply", self)
        self.ok_button.clicked.connect(self.accept)
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)

    def add_category(self, category: str) -> None:
        """Alonge la liste des catégories"""
        CATEGORIES.append(category)
