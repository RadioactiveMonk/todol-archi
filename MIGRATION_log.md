# 📦 Migration Log – Bloc Objet Pur

## 📅 Date : 6 mai 2025
## 🎯 Objectif : Détacher la logique métier de l’interface graphique (Qt), en créant une représentation autonome et testable du tableau de tâches.

---

## ✅ Nouvelles structures ajoutées :

### 🔹 `models/task_table_core.py`
- Création de la classe `TaskTable` (Python pur)
- Stocke des `Task` et des `TaskTableColumn`
- Méthodes disponibles :
  - `row_count()`, `column_count()`
  - `get_cell_value(row, col)`
  - `get_column_name(index)`, `get_column_tooltip(index)`
  - `to_matrix()`, `to_console_str()`
  - `__str__()` pour affichage direct

---

## ✅ Tests réalisés en console (IPython)
- Instanciation d’une liste de `Task`
- Construction du tableau avec `TaskTable(tasks, TASK_TABLE_COLUMNS)`
- Affichage en console validé avec `print(table)`
- Gestion automatique des colonnes non présentes dans `Task` (ex: "edit")

---

## 🧱 Étapes à venir :
- Ajouter des méthodes métier (`add_task()`, `filter_by()`, etc.)
- Créer un cœur applicatif avec état global (`app_logic.py`)
- Laisser Qt de côté pour l’instant : ne travailler que sur le modèle logique

---

## 🌱 Remarque :
Ce bloc initie une architecture centrée sur le domaine (domain-driven), où l’interface 
n’est qu’une vue projetée du modèle.


========================================================================================
## 📅 Date : 9 mai 2025
## 🎯 Objectif
Rendre le modèle `TaskTable` stable, défensif et exploitable dans tous les cas de figure.

---

## 🔐 Sécurisations ajoutées

### ✅ Robustesse de navigation
- `get_cell_value(row, col)` protégé contre les `IndexError`
- Log clair en cas d’accès invalide
- Retour neutre (`None`) si cellule inaccessible

### ✅ Cas limites gérés
- Zéro tâche → affichage clair `[Empty Table]`
- Zéro colonne → matrice = lignes vides
- Méthodes `to_matrix()` et `to_console_str()` tolérantes à tous les cas

---

## 🔍 Validation douce des critères
- `filter_by(...)` log les champs inconnus, les ignore proprement
- `sort_by(...)` vérifie la validité du champ, log en cas d'erreur

---

## 🧰 Fonctions métiers ajoutées

- `to_dicts()` → export propre des données (filtré selon les colonnes)
- `all()` → accès clair à toutes les tâches
- `head(n)` / `tail(n)` → manipulation partielle du tableau

---

## 🧪 Tests interactifs validés
- `table.head(3).to_dicts()`
- `table[3]` → accès direct à une tâche
- `filter_by(done=True)` → champ ignoré, logué, pas de crash
- Enchaînements confirmés (`.head().filter_by(...)`, etc.)

---

## 🧠 Statut
Le bloc `TaskTable` est désormais :
- solide
- testable
- lisible
- complet pour les usages métier

Prêt à être exposé dans l’UI ou testé avec `pytest`.