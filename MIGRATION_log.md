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
Ce bloc initie une architecture centrée sur le domaine (domain-driven), où l’interface n’est qu’une vue projetée du modèle.