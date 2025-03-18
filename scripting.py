def handle_check(self, row: int) -> None:
        """Inverse le statut de la tâche (✅ ↔️ 🟨) et met à jour la DB."""
        task = self.tasks[row]
        task.completed = not task.completed

        logger.info(f"TOGGLE (Status): ID='{task.tid}', Status='{task.completed}'")

        self.db_manager.execute("update_task_completed", task.completed, task.tid)
        self._update_task(task)

    def handle_edit(self, row: int) -> None:
        """Ouvre le formulaire d'édition pour une tâche."""
        task = self.tasks[row]
        parent_widget = self.parent() if isinstance(self.parent(), QWidget) else None
        dialog = AddTaskDialog(parent=parent_widget, task=task)

        if dialog.exec():
            task.title = dialog.title_input.text().strip()
            task.category = dialog.category_selector.currentText()
            task.expiration = dialog.expiration_selector.dateTime().toString(
                "yyyy-MM-dd HH:mm"
            )
            task.notes = dialog.notes_input.toPlainText().strip()
            self._update_task(task)

    def handle_delete(self, row):
        """Supprime visuellement une tâche, supprime dans la DB et rafraîchit le tableau"""
        task = self.tasks[row]

        if task.tid != None:  # Vérifie que la tâche est dans la DB
            self.db_manager.execute("delete_task", task.tid)
            logger.info(f"DELETE (Task): ID='{task.tid}', Title='{task.title}'")

        del self.tasks[row]  # Supprime du modèle
        self.layoutChanged.emit()