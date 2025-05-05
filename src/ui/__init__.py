from helpers.ui_helpers import get_flags_for_column

from .main_window import MainWindow

__all__ = [
    "get_flags_for_column",
    "MainWindow",
]
# This module imports and re-exports the MainWindow class and utility functions
# related to cell properties. It serves as a convenient entry point for accessing
# UI components and utility functions in the application. The get_alignment and
# get_flags functions are used for determining cell alignment and flags for
# rendering in the UI, while the MainWindow class represents the main application
