# 🧱 Core Checklist – Bloc C (Stabilisation de la base)
[1] Nouvelle fonctionnalité / refacto
[2] Test rapide en IPython
[3] Validation ou micro-correction
[4] Ensuite passage à l'étape suivante

## 🎯 Objectif général

- Solidifier tout ce qui est "bas niveau" (core, modèle, config, gestion).
- Préparer une architecture propre avant de remonter vers l'UI.
- Construire un socle fiable, extensible, maintenable et agréable à utiliser.

---

## 🛠️ Plan de migration étape par étape

### 1. Finalisation du système de configuration

- [x] Créer une vraie classe `SettingsManager` (besoin de helpers ? de utils ?) 
- [x] Permettre chargement, sauvegarde, mise à jour facile du `settings.json`
- [x] Définir clairement où sont stockés les paramètres utilisateurs
- [x] Poser des valeurs par défaut gérées proprement

---

### 2. Finalisation du système de logging

- [x] Réfléchir à l'intérêt de créer un `LogManager`
- [x] Centraliser les logs console et fichiers proprement
- [x] Gérer la rotation et la rétention dans la config
- [x] Préparer une fonction simple de log enrichi (`log_task()`, etc.)

---

### 3. Refondre `TaskTableModel`

- [ ] Injecter `TASK_TABLE_COLUMNS` dans le modèle
- [ ] Nettoyer `rowCount()` / `columnCount()`
- [ ] Adapter `headerData()` (name + tooltip)
- [ ] Adapter `data()` (field + alignment + checkbox)
- [ ] Adapter `flags()` (via column.flags)
- [ ] Supprimer toutes les constantes mortes

---

### 4. Helpers fondamentaux (bonus)

- [ ] Créer `safe_get(d, key, default)` pour accès sûr aux dictionnaires
- [ ] Créer `format_datetime(dt)` pour afficher les dates proprement
- [ ] Ajouter des décorateurs ou outils d'enrichissement (`@property`, `__str__`, `__repr__` sur les dataclass)
- [ ] Préparer `contextmanagers.py` utiles (si besoin futur)

---

## 📋 Détail par fichier

| Fichier | Contenu prévu |
|:--------|:--------------|
| `core/settings_manager.py` | Gestion des paramètres utilisateur |
| `core/log_manager.py` (optionnel) | Gestion centralisée du logging |
| `models/task_table_model.py` | Modèle refondu basé sur `TASK_TABLE_COLUMNS` |
| `helpers/*.py` | Tous les petits outils stables et testables |

---

## 🔥 Objectif final visé

- Core solide et fonctionnel
- Modèle aligné à 100% sur la config
- Plus aucun vieux code dur ou fragile
- UI prête à consommer le système en mode "service stable"

---

## 🔥 On the way

- ThemeManager()

## Bonus — Explorations futures (Branche expérimentale)

> Concepts avancés ou usages spécifiques

[ ] Ajouter structures avancées : deque, NamedTuple, contextlib, asyncio, yield...


