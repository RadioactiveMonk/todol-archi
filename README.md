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
├── config/                  # Fichiers de configuration de l'application
│   └── __init__.py
│
├── core/                     # Composants centraux (logique principale et fondations)
│   ├── api/                  # Endpoints de l'API et schémas de validation
│   ├── factory/              # Fabriques d'objets complexes (UI, dialogues, icônes)
│   ├── app_metadata.py       # Métadonnées de l'application
│   ├── db.py                 # Gestion de la base de données
│   ├── settings_manager.py   # Gestion centralisée des paramètres utilisateur
│   └── __init__.py
│
├── handlers/                 # Logique métier spécifique aux actions de l'application
│   ├── task_handlers.py      # Gestion des actions sur les tâches
│   └── __init__.py
│
├── helpers/                  # Utilitaires spécialisés (context managers, conversions)
│   ├── contextmanagers.py
│   ├── converters.py
│   └── __init__.py
│
├── models/                   # Représentation des entités métier (modèles de données)
│   ├── task.py
│   ├── task_core.py
│   ├── task_table_model.py
│   └── __init__.py
│
├── ui/                       # Composants visibles et interactifs (interface graphique)
│   ├── containers/           # Grandes sections UI (menus, tables)
│   ├── controls/             # Composants interactifs (boutons, sélecteurs)
│   ├── delegates/            # Délégués de rendu / édition pour les vues
│   ├── dialogs/              # Fenêtres de dialogue (ajout, édition)
│   ├── resources/            # Ressources statiques (icônes, stylesheets)
│   ├── theme/                # Gestion des thèmes graphiques
│   ├── main_window.py        # Fenêtre principale de l'application
│   └── __init__.py
│
├── utils/                    # Fonctions utilitaires transversales (non spécifiques à un module)
│   ├── category_utils.py
│   ├── csv_utils.py
│   ├── db_utils.py
│   ├── default_values.py
│   ├── init_db.py
│   ├── log_utils.py
│   ├── path_utils.py
│   ├── status_utils.py
│   ├── task_table_column_utils.py
│   ├── ui_geometry_utils.py
│   ├── ui_icons_utils.py
│   ├── ui_text_utils.py
│   ├── ui_theme_utils.py
│   ├── view_utils.py
│   ├── README.md
│   └── __init__.py
│
├── main.py                   # Point d'entrée principal de l'application
└── __init__.py
```



