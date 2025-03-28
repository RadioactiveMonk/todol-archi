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

## Structure (28-03-25)

```
.todol-archi
├── data
│   ├── settings.json
│   ├── tasks.db
│   └── themes.json
├── docs
│   ├── tree260325.txt
│   └── tree28-03.txt
├── logs
│   ├── app.log
│   └── errors.log
├── scripts
│   ├── dev.sh
│   ├── gitadd.py
│   ├── README_dev.md
│   ├── reload_all.py
│   └── replace_imports.py
├── src
│   ├── core
│   │   ├── api
│   │   │   ├── dependencies.py
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   ├── schemas.py
│   │   │   └── utils.py
│   │   ├── database
│   │   │   ├── db_controller.py
│   │   │   ├── db_manager.py
│   │   │   └── __init__.py
│   │   ├── app_constants.py
│   │   ├── cached_utils.py
│   │   ├── config.py
│   │   ├── database_config.py
│   │   ├── default_values.py
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── path.py
│   │   ├── settings_manager.py
│   │   ├── status_constants.py
│   │   └── style_loader.py
│   ├── factory
│   │   ├── dialog_factory.py
│   │   ├── factory_utils.py
│   │   ├── handler_factory.py
│   │   ├── icon_factory.py
│   │   ├── __init__.py
│   │   ├── mainwindow_factory.py
│   │   └── notification_factory.py
│   ├── handlers
│   │   ├── __init__.py
│   │   └── task_handlers.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── task.py
│   │   ├── task_table_model.py
│   │   └── task_table_utils.py
│   ├── todol_archi.egg-info
│   │   ├── dependency_links.txt
│   │   ├── PKG-INFO
│   │   ├── requires.txt
│   │   ├── SOURCES.txt
│   │   └── top_level.txt
│   ├── ui
│   │   ├── containers
│   │   │   ├── __init__.py
│   │   │   ├── menu_bar.py
│   │   │   ├── search_tasks.py
│   │   │   └── task_table.py
│   │   ├── controls
│   │   │   ├── category_selector.py
│   │   │   ├── custom_button.py
│   │   │   ├── expiration_selector.py
│   │   │   ├── __init__.py
│   │   │   └── theme_selector.py
│   │   ├── delegates
│   │   │   ├── edit_delegate.py
│   │   │   ├── __init__.py
│   │   │   └── status_delegate.py
│   │   ├── dialogs
│   │   │   ├── add_task_dialog.py
│   │   │   ├── edit_parameters_dialog.py
│   │   │   └── __init__.py
│   │   ├── resources
│   │   │   ├── fonts
│   │   │   ├── icons
│   │   │   │   ├── app_icon.png
│   │   │   │   ├── check_task.png
│   │   │   │   ├── check_task.svg
│   │   │   │   ├── delete_task.png
│   │   │   │   ├── delete_task.svg
│   │   │   │   ├── edit_settings.png
│   │   │   │   ├── edit_task.png
│   │   │   │   ├── edit_task.svg
│   │   │   │   └── new_task.png
│   │   │   ├── images
│   │   │   ├── stylesheets
│   │   │   │   ├── dark.qss
│   │   │   │   ├── default.qss
│   │   │   │   └── system.qss
│   │   │   └── translations
│   │   ├── cell_properties.py
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   └── ui_constants.py
│   ├── __init__.py
│   └── main.py
├── tests
│   ├── temp
│   ├── conftest.py
│   ├── __init__.py
│   ├── test_add_task_dialog.py
│   ├── test_cached_utils.py
│   ├── test_connection.py
│   ├── test_constants.py
│   ├── test_database.py
│   ├── test_edit_parameters_dialog.py
│   ├── test_settings.py
│   ├── test_status_handler.py
│   ├── test_style_loader.py
│   ├── test_task_handlers.py
│   ├── test_task.py
│   └── test_task_table_model.py
├── credits.txt
├── learning_map.md
├── LICENSE
├── Makefile
├── migration_log.md
├── pyproject.toml
├── README.md
├── TODO.md
└── TODO_review1.md
```

## Démarrage

```bash
git clone git@github.com:RadioactiveMonk/todol-archi.git
cd todol-archi
python -m venv .venv
source .venv/bin/activate  # ou .venv\\Scripts\\activate sous Windows
pip install -e .

# Lancement de l'app
python -m src.main

