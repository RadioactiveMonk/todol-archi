# 🧠 Todol-Archi

Version modulaire et refactorisée de Todol-Pro.  
Expérimentation de patterns avancés (Factory, SOLID, Inversion de dépendance, etc.)

## Objectifs

- 🔁 Repenser la structure du projet pour plus de clarté et de réutilisabilité
- 🏭 Implémenter des factories pour tous les composants majeurs
- 🧩 Modulariser au maximum chaque élément (UI, logique, backend)
- 🧪 Faciliter les tests et les extensions futures

## Base

- PySide6
- SQLite
- Architecture modulaire orientée objets

## Structure non définitive (09-05-25)

```bash
src/
├── config
│   └── __init__.py
├── core
│   ├── api
│   │   ├── api_utils.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── factories
│   │   ├── dialog_factory.py
│   │   ├── factory_utils.py
│   │   ├── handler_factory.py
│   │   ├── icon_factory.py
│   │   ├── __init__.py
│   │   ├── mainwindow_factory.py
│   │   └── notification_factory.py
│   ├── app_metadata.py
│   ├── custom_exceptions.py
│   ├── db.py
│   ├── defaults.py
│   ├── __init__.py
│   ├── log_manager.py
│   ├── settings.bak
│   ├── settings_manager.py
│   └── settings_pydantic.bak
├── handlers
│   ├── __init__.py
│   └── task_handlers.py
├── helpers
│   ├── ui
│   │   ├── icon_loader.py
│   │   ├── signal_connectors.py
│   │   ├── table_view_config.py
│   │   └── ui_helpers.py
│   ├── contextmanagers.py
│   ├── converters.py
│   ├── __init__.py
│   ├── settings_helpers.py
│   └── status_helpers.py
├── models
│   ├── __init__.py
│   ├── task_core.py
│   ├── task.py
│   ├── task_table_column.py
│   ├── task_table_core.py
│   ├── task_table_data.py
│   └── task_table_model.py
├── ui
│   ├── constants
│   │   ├── geometry.py
│   │   ├── __init__.py
│   │   └── text.py
│   ├── containers
│   │   ├── __init__.py
│   │   ├── menu_bar.py
│   │   ├── search_tasks.py
│   │   └── task_table_view.py
│   ├── controls
│   │   ├── category_selector.py
│   │   ├── custom_button.py
│   │   ├── expiration_selector.py
│   │   ├── __init__.py
│   │   └── theme_selector.py
│   ├── delegates
│   │   ├── edit_delegate.py
│   │   └── __init__.py
│   ├── dialogs
│   │   ├── add_task_dialog.py
│   │   ├── edit_parameters_dialog.py
│   │   └── __init__.py
│   ├── resources
│   │   ├── icons
│   │   │   ├── app_icon.png
│   │   │   ├── delete_task.png
│   │   │   ├── edit_settings.png
│   │   │   ├── edit_task.png
│   │   │   └── new_task.png
│   │   └── stylesheets
│   │       ├── dark.qss
│   │       ├── default.qss
│   │       └── system.qss
│   ├── theme
│   │   ├── __init__.py
|   |   ├── style_loader.py
│   │   └── themes.json
│   ├── __init__.py
│   └── main_window.py
├── utils
│   ├── db_initializer.py
│   ├── db_utils.py
│   ├── export_utils.py
│   ├── __init__.py
│   ├── path_utils.py
│   └── README.md
├── __init__.py
└── main.py

20 directories, 77 files

```



