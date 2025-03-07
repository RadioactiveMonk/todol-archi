def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
    """Retourne les données à afficher pour chaque cellule"""

    if not index.isValid():
        return None

    # ✅ Dictionnaire qui gère les différentes données affichées
    data_dispatch = {
        Qt.ItemDataRole.DecorationRole: {
            len(TASK_TABLE_HEADERS): lambda i: self.edit_icons[
                "delete"
            ],  # Icône de suppression
        },
        Qt.ItemDataRole.DisplayRole: {
            0: lambda i: (
                "✅" if getattr(self.tasks[i], "status", None) else "🟨"
            ),  # Statut
            **{
                col: lambda i, col=col: getattr(
                    self.tasks[i], COLUMN_MAPPING.get(TASK_TABLE_HEADERS[col], ""), None
                )
                for col in range(1, len(TASK_TABLE_HEADERS))
            },
        },
    }

    return data_dispatch.get(role, {}).get(index.column(), lambda i: None)(index.row())
