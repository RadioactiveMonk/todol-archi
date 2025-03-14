import pytest
import os
import json
from pathlib import Path
from pytestqt.qtbot import QtBot
from PyQt6.QtWidgets import QApplication
from backend.config.configs import SETTINGS_FILE
from backend.settings_manager import SettingsManager
from gui.dialogs.edit_parameters_dialog import EditParametersDialog

LOG_FILE = Path("logs/app.log")
TEMP_DIR = Path("tests/temp")


@pytest.fixture
def settings_manager():
    """Fixture globale pour un SettingsManager propre."""
    SETTINGS_FILE.write_text(
        json.dumps({"theme": "dark", "categories": ["Work", "Personal"]})
    )
    return SettingsManager()


@pytest.fixture(scope="session", autouse=True)  # Obligatoire pour les tests PyQt
def app():
    """Crée une instance de QApplication. Assure qu'elle ne soit pas détruite prématurément."""
    app = QApplication.instance() or QApplication([])
    yield app
    app.quit()


@pytest.fixture
def edit_parameters_dialog(qtbot: QtBot, app):
    """Fixture pour éviter la suppression prématurée de EditParametersDialog."""
    dialog = EditParametersDialog()
    app.dialog = (
        dialog  # 🔥 On attache le dialog à QApplication pour éviter qu'il soit supprimé
    )
    qtbot.addWidget(dialog)
    yield dialog
    dialog.close()


@pytest.fixture(scope="function", autouse=True)
def clean_logs():
    """Vide le fichier de logs avant chaque test."""
    if LOG_FILE.exists():
        LOG_FILE.write_text("")


@pytest.fixture(scope="function", autouse=True)
def reset_temp_dir():
    """Supprime et recrée un dossier temporaire avant chaque test."""
    if TEMP_DIR.exists():
        for file in TEMP_DIR.iterdir():
            file.unlink()
    else:
        TEMP_DIR.mkdir()


@pytest.fixture(scope="session", autouse=True)
def set_test_mode():
    """Force le mode test pour tous les tests"""
    os.environ["APP_MODE"] = "test"
