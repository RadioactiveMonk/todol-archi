# Todol-Pro

> Application minimaliste de gestion de tâches, moderne et modulaire, pensée pour être maintenable, testable et extensible.

---

[![Tests](https://img.shields.io/badge/tests-pytest-green?style=flat-square)](https://pytest.org)
[![Python](https://img.shields.io/badge/python-3.12+-blue?style=flat-square)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](./LICENSE)

## ℹ️ Présentation

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

## ✨ Contribuer

Même si le projet est mené en solo à des fins pédagogiques, toute suggestion est la bienvenue !
N'hésitez pas à ouvrir une issue ou à forker pour proposer une amélioration.

## 📜 Licence

Ce projet est sous licence MIT.
Libre à toi de t’en inspirer, le forker, ou contribuer ✌️

## 👤 Auteur: doyouDance

Ce projet est un terrain d’apprentissage avancé, mené avec rigueur et souci de qualité de code.
L'objectif n'est pas une application parfaite et multifonctionnelle dans son utilisation, 
mais optimisée dans sa conception dans un premier temps. 

## Note pour les autodidactes tels que moi:

Soyez curieux, car quand j'ai commencé ce projet, je codais encore avec Sam, Alice, Tom et toute l'équipe (des étudiants ou des employés bien connus). Ces bases sont nécessaires, mais rien ne vous amènera plus haut que de vous lancer dans un projet, quel qu'il soit. Si vous ne voyez pas ou vous allez avec ce que vous apprenez, lancez vous ! Il y a 3 mois, je ne savais même pas faire une requête SQL. Aujourd'hui, je sais gérer une base de donnée directement depuis mon terminal. Je tenais à faire cette remarque, je ne suis pas un expert, mais je suis sûr qu'ils vous diront la même chose. ✌️✌️


