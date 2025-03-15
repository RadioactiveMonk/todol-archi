from pytestqt.qtbot import QtBot
from PyQt6.QtCore import Qt
import pytest

def test_add_category(edit_parameters_dialog, settings_manager, qtbot: QtBot):
    """Teste l'ajout d'une catégorie via CategorySelector"""
    edit_parameters_dialog.add_category_input.setText("Fitness")
    qtbot.mouseClick(edit_parameters_dialog.add_category_button, Qt.MouseButton.LeftButton)

    assert "Fitness" in settings_manager.get("categories")
    assert edit_parameters_dialog.category_selector.findText("Fitness") != -1


def test_remove_category(edit_parameters_dialog, settings_manager, qtbot: QtBot):
    """Teste la suppression d'une catégorie via CategorySelector"""
    edit_parameters_dialog.category_selector.setCurrentText("Work")
    qtbot.mouseClick(edit_parameters_dialog.remove_category_button, Qt.MouseButton.LeftButton)

    assert "Work" not in settings_manager.get("categories")
    assert edit_parameters_dialog.category_selector.findText("Work") == -1


def test_update_theme(edit_parameters_dialog, settings_manager, qtbot: QtBot):
    """Teste le changement de thème via ThemeSelector"""
    edit_parameters_dialog.theme_selector.setCurrentText("dark")
    qtbot.mouseClick(edit_parameters_dialog.ok_button, Qt.MouseButton.LeftButton)

    assert settings_manager.get("theme") == "dark"
