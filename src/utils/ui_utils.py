# =====================================
# UI-RELATED CONSTANTS
# =====================================

# Main Window
MAIN_WINDOW_TITLE: str = "Todol archi"
MAIN_WINDOW_GEOMETRY: tuple = (250, 100, 1080, 600)

# Dialogs
TASK_DIALOG_TITLE: str = "New task"
EDIT_TASK_DIALOG_TITLE: str = "Edit task"
TASK_DIALOG_GEOMETRY: tuple = (1150, 200, 400, 350)
EDIT_PARAMETERS_DIALOG_TITLE: str = "Parameters"
EDIT_PARAMETERS_DIALOG_GEOMETRY: tuple = (1150, 200, 400, 200)

# Icons
EDIT_ICON_SIZE: int = 18
EDIT_ICON_SPACING: int = 4
EDIT_ICON_TOP_OFFSET: int = 2
EDIT_SECTION_POSITIONS: list[str] = ["delete", "edit"]

# Themes
APP_THEMES: list[str] = ["default", "dark", "system"]
DEFAULT_THEME: str = APP_THEMES[0]
