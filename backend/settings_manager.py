from dataclasses import dataclass
import json
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass, field
from backend.config.configs import SETTINGS_FILE
from backend.config.constants import DEFAULT_THEME, CATEGORIES
from backend.logger import logger


@dataclass
class Settings:
    """Représente la configuration chargée en mémoire"""

    theme: str = DEFAULT_THEME
    categories: list[str] = field(default_factory=lambda: CATEGORIES)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Settings":
        """Crée une instance de Settings a partir d'un dictionnaire json"""
        return cls(
            theme=data.get("theme", DEFAULT_THEME),
            categories=data.get("categories", CATEGORIES),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convertit une instance de Settings en dict pour sauvegarde JSON"""
        return {"theme": self.theme, "categories": self.categories}


class SettingsManager:
    """Gestionnaire de paramètres"""

    _instance = None
    _settings: Settings = Settings()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._settings = cls._load()
        return cls._instance

    @classmethod
    def _load(cls) -> Settings:
        """Charge les parametres depuis le JSON (une fois)."""
        if SETTINGS_FILE.exists():
            try:
                with SETTINGS_FILE.open("r", encoding="utf-8") as fhand:
                    data = json.load(fhand)
                return Settings.from_dict(data)

            except (json.JSONDecodeError, IOError) as e:
                logger.error(f"Erreur de chargement de 'settings.json: {e}")
                return Settings()  # 👁️‍🗨️ retourne la dataclass de base si erreur
        return Settings()

    def save(self) -> None:
        """Sauvegarde en mémoire (fichier settings.json)"""
        try:
            with SETTINGS_FILE.open("w", encoding="utf-8") as fhand:
                json.dump(self._settings.to_dict(), fhand, indent=4, ensure_ascii=False)
        except IOError as e:
            logger.error(f"Impossible de sauvegarder settings.json: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Récupere un parametre memoire"""
        return getattr(self._settings, key, default)

    def update(self, key: str, value: Any) -> None:
        if hasattr(self._settings, key):
            setattr(self._settings, key, value)
            self.save()  # 👁️‍🗨️ Une seule sauvegarde
        else:
            logger.warning(f"Clé inconnue dans les paramètres: {key}")

    def get_all(self) -> Dict[str, Any]:
        """Retourne tous les paramètres sous forme de dictionnaire."""
        return self._settings.to_dict()

