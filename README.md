# 🧠 Todol-Archi

Version modulaire et refactorisée de Todol-Pro.  
Expérimentation de patterns avancés (Factory, SOLID, Inversion de dépendance, etc.)

## Objectifs

- 🔁 Repenser la structure du projet pour plus de clarté et de réutilisabilité
- 🏭 Implémenter des factories pour tous les composants majeurs
- 🧩 Modulariser au maximum chaque élément (UI, logique, backend)
- 🧪 Faciliter les tests et les extensions futures

## Base

- PyQt6
- SQLite
- Architecture modulaire orientée objets

## Structure (07-04-25)

```bash
src
├── core
│   ├── api
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── utils.py
│   ├── database
│   │   ├── ask_db.py
│   │   ├── init_db.py
│   │   ├── __init__.py
│   │   └── todo_db.md
│   ├── app_constants.py
│   ├── config.py
│   ├── database_config.py
│   ├── default_values.py
│   ├── __init__.py
│   ├── path.py
│   ├── settings_manager.py
│   └── sql_schema.py
├── factory
│   ├── dialog_factory.py
│   ├── factory_utils.py
│   ├── handler_factory.py
│   ├── icon_factory.py
│   ├── __init__.py
│   ├── mainwindow_factory.py
│   └── notification_factory.py
├── handlers
│   ├── __init__.py
│   └── task_handlers.py
├── helpers
│   ├── cached_utils.py
│   ├── contextmanagers.py
│   ├── converters.py
│   ├── csv_utils.py
│   ├── __init__.py
│   ├── log_utils.py
│   ├── status_constants.py
│   └── ui_helpers.py
├── models
│   ├── __init__.py
│   ├── task_core.py
│   ├── task.py
│   ├── task_table_model.py
│   └── task_table_utils.py
├── ui
│   ├── containers
│   │   ├── __init__.py
│   │   ├── menu_bar.py
│   │   ├── search_tasks.py
│   │   └── task_table.py
│   ├── controls
│   │   ├── category_selector.py
│   │   ├── custom_button.py
│   │   ├── expiration_selector.py
│   │   ├── __init__.py
│   │   └── theme_selector.py
│   ├── delegates
│   │   ├── edit_delegate.py
│   │   ├── __init__.py
│   │   └── status_delegate.py
│   ├── dialogs
│   │   ├── add_task_dialog.py
│   │   ├── edit_parameters_dialog.py
│   │   └── __init__.py
│   ├── resources
│   │   ├── icons
│   │   │   ├── app_icon.png
│   │   │   ├── check_task.png
│   │   │   ├── check_task.svg
│   │   │   ├── delete_task.png
│   │   │   ├── delete_task.svg
│   │   │   ├── edit_settings.png
│   │   │   ├── edit_task.png
│   │   │   ├── edit_task.svg
│   │   │   └── new_task.png
│   │   └── stylesheets
│   │       ├── dark.qss
│   │       ├── default.qss
│   │       └── system.qss
│   ├── theme
│   │   ├── style_loader.py
│   │   └── themes.json
│   ├── cell_properties.py
│   ├── __init__.py
│   ├── main_window.py
│   └── ui_constants.py
├── __init__.py
└── main.py
```



