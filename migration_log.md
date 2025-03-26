🛠️ MIGRATION_LOG.md — Todol-Pro -> Todol-archi

🗓️ Contexte

À partir de [26-03-2025], un chantier de restructuration majeure a été lancé sur le projet Todol-Pro. L’objectif était de clarifier l’architecture, mieux séparer les responsabilités, et préparer le projet à des évolutions futures (API, packaging, tests avancés...).

Ce document retrace les étapes clés de cette migration.

🔁 Objectif de la migration

Clarifier l’arborescence du projet (via un dossier src/)

Séparer proprement les responsabilités (UI, core, data, resources, handlers...)

Préparer une structure modulaire, testable, scalable

Supprimer les imports flous ou cassants

Rendre le projet maintenable à long terme

🧩 Étapes principales

1. 📁 Création d’un dossier src/ racine

Migration de tout le code source vers src/

Mise à jour automatique des imports via grep | sed

2. 📦 Refonte de l’arborescence interne

Todol-archi/
├── data
│   ├── settings.json
│   ├── tasks.db
│   └── themes.json
├── docs
│   ├── setup_notes.md
│   ├── tree250325.txt
│   └── workflow.md
├── logs
│   ├── app.log
│   └── errors.log
├── scripts
│   ├── dev.sh
│   └── gitadd.py
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
│   │   ├── __init__.py
│   │   ├── ipython_cfg.py
│   │   ├── logger.py
│   │   ├── path.py
│   │   ├── settings_manager.py
│   │   └── style_loader.py
│   ├── factory
│   │   ├── dialog_factory.py
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
│   └── ui
│       ├── containers
│       │   ├── __init__.py
│       │   ├── menu_bar.py
│       │   ├── search_tasks.py
│       │   └── task_table.py
│       ├── controls
│       │   ├── category_selector.py
│       │   ├── custom_button.py
│       │   ├── expiration_selector.py
│       │   ├── __init__.py
│       │   └── theme_selector.py
│       ├── delegates
│       │   ├── edit_delegate.py
│       │   ├── __init__.py
│       │   └── status_delegate.py
│       ├── dialogs
│       │   ├── add_task_dialog.py
│       │   ├── edit_parameters_dialog.py
│       │   └── __init__.py
│       ├── resources
│       │   ├── fonts
│       │   ├── icons
│       │   │   ├── app_icon.png
│       │   │   ├── check_task.png
│       │   │   ├── check_task.svg
│       │   │   ├── delete_task.png
│       │   │   ├── delete_task.svg
│       │   │   ├── edit_settings.png
│       │   │   ├── edit_task.png
│       │   │   ├── edit_task.svg
│       │   │   └── new_task.png
│       │   ├── images
│       │   ├── stylesheets
│       │   │   ├── dark.qss
│       │   │   ├── default.qss
│       │   │   └── system.qss
│       │   └── translations
│       ├── cell_properties.py
│       ├── __init__.py
│       ├── main_window.py
│       └── ui_constants.py
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
│   ├── test_style_loader.py
│   ├── test_task_handlers.py
│   ├── test_task.py
│   └── test_task_table_model.py
├── credits.txt
├── LICENSE
├── main.py
├── migration_log.md
├── pyproject.toml
├── README.md
└── TODO.md


3. 🔁 Mise à jour des chemins dynamiques

Création de path.py dans core/

Suppression des chemins relatifs fragiles (QDir.current()...)

Utilisation de pathlib propre

4. 🧠 Gestion du cache & débogage CategorySelector

Mise en cache via @lru_cache dans get_categories()

Correction d’un bug d’affichage : refresh_categories() ajouté dans le __init__()

5. 🧪 Reconfiguration de l’environnement IPython

Nettoyage de ~/.ipython/profile_default/startup/

Mise à jour des chemins dans reload_all()

6. ✅ Rétablissement complet du fonctionnement de l'app

Ajout, édition, suppression de tâches opérationnels

Thème fonctionnel avec reload_theme

Toggle status OK avec fond vert/rouge + texte [PENDING] / [ROCKED]

7. 🚧 Ce qu’il reste à finaliser :

Configurer les __init__.py pour faciliter les imports

Implémentation de icon_factory.py

Préparation de la notification_factory

Nettoyage final + rédaction d’un TODO.md à jour


Le projet est désormais prêt pour des phases plus avancées (tests, patterns, API).

