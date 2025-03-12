import json
from pathlib import Path
from typing import Dict, List, Any
from backend.config.configs import SETTINGS_FILE, DEFAULT_THEME
from backend.logger import logger


class SettingsManager:
    """Gestionnaire de paramètres"""

    SETTINGS = SETTINGS_FILE

    @classmethod
    def load_settings(cls) -> Dict:
        """Charge les parametres en 'dict'. Retourne les parametres par defaut
        si aucun fichier settings trouvé"""

        if cls.SETTINGS.exists():
            try:
                with cls.SETTINGS.open("r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.error(f"JSON ERROR (load_settings()): {e}")
                return cls.reset()
        return cls.default_settings()

    @classmethod
    def save_settings(cls, settings: dict) -> None:
        """Sauvegarde les parametres en Json"""

        try:
            with cls.SETTINGS.open("w", encoding="utf-8") as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)
        except IOError as e:
            logger.error(f"JSON ERROR (save_settings()): {e}")

    @classmethod
    def update_settings(cls, key: str, value: Any) -> None:
        """Met à jour les paramètres dans le Json"""
        settings = cls.load_settings()
        settings[key] = value
        cls.save_settings(settings)

    @classmethod
    def reset(cls) -> dict:
        """Rétablit les parametres par défault"""
        default = cls.default_settings()
        cls.save_settings(default)
        return default

    @staticmethod
    def default_settings() -> dict:
        """Definit les parametres par defaut"""
        DEFAULT_CATEGORIES = ["General", "Work", "Hobbies"]
        return {"theme": DEFAULT_THEME, "categories": DEFAULT_CATEGORIES}
