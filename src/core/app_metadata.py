# =====================================
# APP METADATA
# =====================================
APP_NAME = "Todol archi"
APP_VERSION = "0.1.0"
APP_AUTHOR = "Sébastien 'doyouDance' Reisen"
APP_DESCRIPTION = "A simple task manager in Python"
APP_COPYRIGHT = "Copyright (c) 2023 Sébastien Reisen"
APP_LICENSE = "MIT"
APP_WEBSITE = "https://github.com/RadioactiveMonk/todol-archi"


# =====================================
# CONFIGURATION DE L'APPLICATION
# =====================================
DEBUG: bool = False
AUTO_SAVE_INTERVAL: int = 5


# =====================================
# HELPERS
# =====================================

def get_app_title() -> str:
    return f"{APP_NAME} v{APP_VERSION}"
