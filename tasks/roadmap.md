# 🗺️ Roadmap – Fin Bloc B et entrée en Bloc C (Mai 2025)

## ✅ Étapes terminées
- `TaskTable` Python pur (terminé)
- Comportements métier intégrés
- Représentation console, slice, export

---

## 🔥 Étape actuelle : `AppLogic` (Coordination métier)

**Fichier :** `core/app_logic.py`

- [ ] Gérer l’état global de l’app : filtres actifs, tri, sélection
- [ ] Méthodes métier : `add_task()`, `toggle_status()`, `apply_filter()`, etc.
- [ ] Lien clair entre `AppLogic` et `TaskTableCore`

🎯 Objectif : un chef d’orchestre indépendant de toute interface graphique.

---

## 🧪 Étape suivante (optionnelle) : Mini script console

**Fichier :** `scripts/demo_text_mode.py` ou `main.py`

- [ ] Instancier `AppLogic` ou `TaskTable`
- [ ] Afficher les tâches via `.to_console_str()`
- [ ] Tester les ajouts, tris, suppressions, filtres

---

## 🔮 Et ensuite ?

Une fois `TaskTable` et `AppLogic` solides :
- ✅ `SettingsManager` : déjà structuré
- 🟡 `DatabaseManager` : à séparer proprement
- 🟡 `Task` : ajustable si besoin
- 🟡 `AppConfig` / `ThemeManager` : à modéliser si utile


## 🔄 Bloc D à venir : Adaptateurs Qt

➡️ À ne commencer **qu'une fois tous les objets métier sont bien modélisés** (TaskTable, AppLogic, Task, SettingsManager, etc.).
➡️ Objectif : pont clair entre la logique métier finalisée et l’interface graphique Qt.

- [ ] `TaskTableAdapter(QAbstractTableModel)` pour connecter `TaskTable` à Qt
- [ ] Vue `QTableView` reliée uniquement à ce modèle
- [ ] Pilotage via `AppLogic`

---