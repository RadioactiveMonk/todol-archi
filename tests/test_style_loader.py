from pathlib import Path
import pytest
from backend.config.configs import STYLESHEET_PATH
from backend.style_loader import load_stylesheet


def test_load_qss(app, settings_manager):
    """Vérifie que le bon fichier .qss est chargé en fonction du thème."""
    settings_manager.update("theme", "dark")

    stylesheet_file = Path(STYLESHEET_PATH) / "dark.qss"
    applied_stylesheet = load_stylesheet(app)

    assert (
        applied_stylesheet == stylesheet_file
    )  # ✅ Vérifie que c'est bien le bon fichier


def test_invalid_theme(app, settings_manager):
    """Vérifie que si un thème invalide est défini, on charge le default.qss."""
    settings_manager.update("theme", "invalid_theme")

    default_stylesheet = Path(STYLESHEET_PATH) / "default.qss"
    applied_stylesheet = load_stylesheet(app)

    assert (
        applied_stylesheet == default_stylesheet
    )  # ✅ On doit tomber sur le thème par défaut


def test_set_stylesheet(app, settings_manager):
    """Vérifie que le fichier .qss est bien appliqué dans l'application."""
    settings_manager.update("theme", "dark")

    stylesheet_file = Path(STYLESHEET_PATH) / "dark.qss"
    applied_stylesheet = load_stylesheet(app)

    with open(applied_stylesheet, "r", encoding="utf-8") as f:
        stylesheet_content = f.read()

    assert stylesheet_content.strip() != ""  # ✅ Vérifie que le fichier n'est pas vide
