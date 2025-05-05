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

- [x] Injecter `TASK_TABLE_COLUMNS` dans le modèle
- [x] Nettoyer `rowCount()` / `columnCount()`
- [x] Adapter `headerData()` (name + tooltip)
- [x] Adapter `data()` (field + alignment + checkbox)
- [x] Adapter `flags()` (via column.flags)


### 3b. Simplification du statut + réorganisation pré-helpers

- [x] Supprimer `StatusDelegate` (delegate supprimé, checkbox suffira)
- [x] Nettoyer `status_utils.py` (ou déplacer `status_color()` dans un `ui_helpers`)
- [x] Supprimer les mappings `ROCKED!`, etc.
- [x] Supprimer constantes mortes liées au statut
- [x] Déplacement default_values.py > core/defaults.py
- [x] Split `task_table_column_utils.py` :
    - `TaskTableColumn` + data = à déplacer vers `models/task_table_config.py`
    - `get_flags_for_column`, `text_alignment`, etc. → vers `helpers/ui_helpers.py`
- [ ] Préparer `helpers/` (premiers modules cohérents à thème, tri des utils)
- [ ] Recalibrer le modele
- [ ] Migration log

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
| `core/log_manager.py` | Gestion centralisée du logging |
| `models/task_table_model.py` | Modèle refondu basé sur `TASK_TABLE_COLUMNS` |
| `models/task_table_config.py` | Structure des colonnes (métier pur) |
| `helpers/ui_helpers.py` | Alignement, flags Qt, rôles d'affichage |
| `helpers/status_helpers.py` (éventuel) | Couleur ou labels pour completed |
| `core/defaults.py` (bonus) | Valeurs par défaut centralisées |

---

## 🔥 Objectif final visé

- Core solide et fonctionnel
- Modèle aligné à 100% sur la config
- Plus aucun vieux code dur ou fragile
- UI prête à consommer le système en mode "service stable"