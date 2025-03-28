from .edit_delegate import EditDelegate
from .status_delegate import StatusEditDelegate

__all__ = ["EditDelegate", "StatusEditDelegate"]
# This module imports and re-exports the EditDelegate and StatusEditDelegate classes.
# It serves as a convenient entry point for accessing UI components related to task
# editing and status management. The EditDelegate is used for editing task details,
# while the StatusEditDelegate is specifically for managing task status.
