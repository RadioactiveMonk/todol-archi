# Path: src/utils/signal_utils.py

from PySide6.QtWidgets import QTableView


def connect_delegate_signals(view: QTableView):
    """
    Connect dynamically the delegate signals (like editClicked, deleteClicked)
    to the appropriate handlers in the view's model.
    """

    if not hasattr(view, "column_delegates"):
        return  # Safety: view doesn't have delegates

    model = view.model()
    if model is None:
        return  # Safety: view has no model set

    for delegate in view.column_delegates.values():
        # Connect editClicked signal if both delegate and model provide them
        if hasattr(delegate, "editClicked") and hasattr(model, "handle_edit_task"):
            delegate.editClicked.connect(model.handle_edit_task)

        # Connect deleteClicked signal if both delegate and model provide them
        if hasattr(delegate, "deleteClicked") and hasattr(model, "handle_delete_task"):
            delegate.deleteClicked.connect(model.handle_delete_task)
