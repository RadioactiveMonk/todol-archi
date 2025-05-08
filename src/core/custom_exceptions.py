# src/core/custom_exceptions.py

class TaskNotFoundError(Exception):
    """Raised when no task matches the given ID."""
    pass

class InvalidCategoryError(Exception):
    """Raised when a category is not in the allowed list."""
    pass

class InvalidStatusError(Exception):
    """Raised when a status value is unrecognized."""
    pass 

class SettingsValidationError(Exception):
    """Raised when settings data is invalid or incomplete."""
    pass

class DatabaseOperationError(Exception):
    """Raised when a database operation fails unexpectedly."""
    pass