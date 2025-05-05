
✅ Bloc Objet Pur – Checklist de transition (Mai 2025)

## 🎯 Objectif
Représenter l’application en Python pur, en modélisant chaque composant (tableau, tâche, état global...) indépendamment de PySide.  
Découpler totalement la logique métier de la couche UI.

---

## 🧩 1. Modèle de base

- [ ] Créer `TaskTable` en Python pur (`task_table_core.py`)
- [ ] Ajouter les méthodes d’accès : `get_cell_value()`, `row_count`, `column_count`, etc.
- [ ] Ajouter un mini test ou démonstration en console (juste pour jouer avec)

---

## 🧱 2. Cœur logique de l’app

- [ ] Créer un fichier `app_logic.py` (ou `core/app_logic.py`)
- [ ] Gérer l’état global (filtres actifs, thème, sélection…)
- [ ] Définir les actions “métier” (ajouter tâche, changer statut, etc.)

---

## 🧭 3. Adaptateurs vers Qt (plus tard)

- [ ] Créer `TaskTableAdapter` → transforme un `TaskTable` en `QAbstractTableModel`
- [ ] Créer une vue (`QTableView`) branchée uniquement à ce modèle
- [ ] Tester le pont métier ↔ interface

---

## 🧪 4. Tests ou consoles de simulation

- [ ] Créer un mini script console pour manipuler `TaskTable`
- [ ] Simuler un tri ou un filtre sans interface
- [ ] Éventuellement lancer depuis `main.py` (mode démo “texte”)

---

## 🚫 Ce qu’on laisse de côté pour l’instant

- `ui/` complet (on ne modifie rien dedans)
- signaux, layouts, slots, clics
- factories PySide

---

## 🔮 Objectif final
Un noyau applicatif **vivant et cohérent** sans interface, capable d’être exposé via Qt, terminal ou web.

"""

