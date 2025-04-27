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

## Structure non définitive (27-04-25)

```bash
src/
├── config
│   └── __init__.py
├── core
│   ├── api
│   │   ├── api_utils.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── app_metadata.py
│   ├── db.py
│   ├── __init__.py
│   ├── settings_manager.py
│   
├── factory
│   ├── dialog_factory.py
│   ├── factory_utils.py
│   ├── handler_factory.py
│   ├── icon_factory.py
│   ├── __init__.py
│   ├── mainwindow_factory.py
│   └── notification_factory.py
├── handlers
│   ├── __init__.py
│   └── task_handlers.py
├── helpers
│   ├── contextmanagers.py
│   ├── converters.py
│   └── __init__.py
├── models
│   ├── __init__.py
│   ├── task_core.py
│   ├── task.py
│   └── task_table_model.py
├── ui
│   ├── containers
│   │   ├── __init__.py
│   │   ├── menu_bar.py
│   │   ├── search_tasks.py
│   │   └── task_table_view.py
│   ├── controls
│   │   ├── category_selector.py
│   │   ├── custom_button.py
│   │   ├── expiration_selector.py
│   │   ├── __init__.py
│   │   └── theme_selector.py
│   ├── delegates
│   │   ├── edit_delegate.py
│   │   ├── __init__.py
│   │   └── status_delegate.py
│   ├── dialogs
│   │   ├── add_task_dialog.py
│   │   ├── edit_parameters_dialog.py
│   │   └── __init__.py
│   ├── resources
│   │   ├── icons
│   │   │   ├── app_icon.png
│   │   │   ├── delete_task.png
│   │   │   ├── edit_settings.png
│   │   │   ├── edit_task.png
│   │   │   └── new_task.png
│   │   └── stylesheets
│   │       ├── dark.qss
│   │       ├── default.qss
│   │       └── system.qss
│   ├── theme
│   │   ├── style_loader.py
│   │   └── themes.json
│   ├── __init__.py
│   └── main_window.py
├── utils
│   ├── category_utils.py
│   ├── csv_utils.py
│   ├── db_utils.py
│   ├── default_values.py
│   ├── init_db.py
│   ├── __init__.py
│   ├── log_utils.py
│   ├── path_utils.py
│   ├── README.md
│   ├── status_utils.py
│   ├── task_table_column_utils.py
│   ├── ui_geometry_utils.py
│   ├── ui_icons_utils.py
│   ├── ui_text_utils.py
│   ├── ui_theme_utils.py
│   └── view_utils.py
├── __init__.py
└── main.py
```



