# Todol-Pro

> Application minimaliste de gestion de tâches moderne et modulaire, pensée pour être maintenable, testable et extensible.

---

## 🚀 Présentation

**Todol-Pro** est une application de type "To-Do List", développée en Python avec PyQt6. C'est une version améliorée de mon premier projet Python 'Todol' (gestion de tâches en CLI). Cette nouvelle version est dotée :

- d’un backend structuré autour de SQLite,
- d’un système de gestion de thèmes (QSS),
- de fonctionnalités CRUD complètes,
- de handlers séparés et testables,
- d’un support des tests unitaires via `pytest`.

Elle est conçue pour évoluer vers une API REST (FastAPI) et une architecture plus avancée (profiling, caching, packaging...).

---

## ⚙️ Fonctionnalités principales

- Ajout, modification, suppression de tâches
- Expiration des tâches avec sélection de date/heure
- Interface graphique PyQt6 claire et modulaire
- Gestion du thème (dark / light, personnalisable)
- Paramètres sauvegardés dans `settings.json`
- Connexion persistante à la base SQLite 
- Cache LRU pour les accès fichiers

---

## 📁 Structure du projet (simplifiée)

todol-pro/ 
├── backend/
│   ├── core/
│   ├── database/
│   ├── handlers/
│   ├── models/
│   └── __init__.py
├── configuration/
│   ├── cell_properties.py
│   ├── configs.py
│   ├── constants.py
│   ├── ipython_cfg.py
│   └── __init__.py
├── data/
│   ├── settings.json
│   └── tasks.db
├── docs/
├── gui/
│   ├── containers/
│   ├── controls/
│   ├── delegates/
│   ├── dialogs/
│   ├── main_window.py
│   ├── __init__.py
│   └── resources/
├── logs/
│   ├── app.log
│   └── errors.log
├── scripts/
├── tests/
│   ├── conftest.py
│   ├── temp/
│   ├── test_add_task_dialog.py
│   ├── test_constants.py
│   ├── test_database.py
│   ├── test_edit_parameters_dialog.py
│   ├── test_settings.py
│   ├── test_style_loader.py
│   ├── test_task_handlers.py
│   ├── test_task.py
|   ├── __init__.py
│   └── test_task_table_model.py
├── requirements.txt
├── LICENSE
├── credits.txt
├── setup.py
├── README.md
├── main.py
├── pyproject.toml
└── TODO.md

## ✨ Contribuer

Même si le projet est mené en solo à des fins pédagogiques, toute suggestion est la bienvenue !
N'hésitez pas à ouvrir une issue ou à forker pour proposer une amélioration.

## 📜 Licence

Ce projet est sous licence MIT.
Libre à toi de t’en inspirer, le forker, ou contribuer ✌️

## 👤 Auteur: doyouDance

Projet développé par un développeur passionné en quête de qualité, d’apprentissage et de maîtrise des outils pro.


