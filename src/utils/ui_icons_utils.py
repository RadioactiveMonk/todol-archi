from functools import lru_cache
from pathlib import Path
from typing import Optional

from PyQt6.QtGui import QIcon

from utils.log_utils import logger
from utils.path_utils import get_path

# === Icon mapping (logical name → filename) ===

_ICONS = {
    "edit": "edit_task.png",
    "delete": "delete_task.png",
    "settings": "edit_settings.png",
    "new": "new_task.png",
    "app": "app_icon.png",
}

# === Public API ===


def get_icon_path(name: str) -> Path:
    """
    Return the full path to the icon file corresponding to the given logical name.
    """
    icons_dir = get_path("icons")
    if name in _ICONS:
        return icons_dir / _ICONS[name]
    logger.warning(f"Unknown icon name: {name}")
    return icons_dir / "app_icon.png"  # fallback


@lru_cache
def get_icon(name: str) -> Optional[QIcon]:
    """
    Return a cached QIcon for the given name, or None if not found.
    """
    path = get_icon_path(name)
    if path.exists():
        return QIcon(str(path))
    logger.warning(f"Icon file not found at: {path}")
    return None
