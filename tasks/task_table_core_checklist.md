# ✅ Perfectionnement de l’objet `TaskTable` (Bloc Objet Pur)

## 🎯 Objectif
Faire de `TaskTable` un objet central, robuste, pythonique, testable, et évolutif.  
Support idéal pour pratiquer les bonnes pratiques orientées objet.

---

## 1. Propriétés & accès structurés

- [x] `row_count` et `column_count` en `@property`
- [x] Ajouter `columns_names` / `columns_fields`
- [x] Ajouter une méthode `.headers()` pour l’export

---

## 2. Méthodes métier

- [x] `.add_task(task: Task)`
- [x] `.remove_task(index: int)` ou `.remove_by_id(id)`
- [x] `.filter_by(**criteria)`
- [ ] `.sort_by(column: str, reverse=False)`

---

## 3. Représentations

- [x] `__str__()` pour affichage lisible
- [x] `.to_console_str()` → vue en texte
- [x] `.to_matrix()` → structure exportable
- [ ] `.to_dicts()` ou `.to_json()` ?
- [x] `__repr__()` clair et compact
- [ ] getter setter 

---

## 4. Validation / robustesse

- [ ] Gérer les index invalides proprement
- [ ] Ajouter des assertions / exceptions claires
- [ ] Tester les cas limites : 0 tâche, 0 colonne

---

## 5. Pythonic touch

- [x] `__len__()` → `len(table)` donne `row_count`
- [x] `__getitem__()` → `table[0]` retourne une ligne
- [x] `__iter__()` → itérable sur les tâches

---

## 6. Préparation aux tests

- [ ] `.get_tasks()` ou `.all()` pour accès clair
- [ ] Méthode `.sample()` pour jeux de données fictifs
- [ ] Gérer des cas d’erreurs simples à simuler

---

## 🧠 Objectif final
Faire de `TaskTable` un objet de référence :  
clairement modélisé, réutilisable, et 100% indépendant de l’UI.
