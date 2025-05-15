# ✅ Bloc C — Refactoring Pythonic & Bonnes pratiques

## 🎯 Objectifs
- Raffiner le noyau métier (lisibilité, robustesse, idiomaticité)
- Préparer un socle solide avant d’ajouter la couche UI
- Valider le comportement en conditions réelles (IPython ou console)

---

## 🔬 1. Tests interactifs (IPython)

- [x] Instancier `AppLogic` avec des tâches fictives
- [x] Tester les méthodes : `add_task()`, `toggle_task_status()`, `edit_task()`
- [x] Tester filtres, tri, (sélection)
- [x] Vérifier le rendu via `.refresh_view().to_console_str()` (fonctionne mais affichage bancal)

---

## ✅ 2. Validations métier (optionnel)

- [ ] Protéger `id` via `__setattr__`
- [ ] Ajouter validations type ou champ si besoin
- [ ] Créer un `validators.py` si logique réutilisable

---

## 🧼 3. Pythonic touch & améliorations

- [x] Ajouter `__contains__`, `__bool__`, ou `__eq__` si utile
- [ ] Harmoniser les noms / docs / signatures
- [ ] Alléger certaines fonctions métier

---

## 💡 4. Méthodes orientées sélection (préparation UI)

- [x] `get_selected_task()`
- [x] `edit_selected_task()`
- [x] `delete_selected_tasks()`
- [ ] `check_task()` ou équivalent (non util)

---

## 🧪 Bonus exploratoire

- [ ] Exports modulaires (Pattern Strategy)
- [ ] Helpers de formatage (dates, durées)
- [ ] Localisation ou centralisation des strings
- [ ] Premiers tests automatisés (`doctest`, `pytest`...)

---

## 🔚 Objectif final
Un noyau métier **robuste, clair, idiomatique**, prêt à être branché à l’interface (Bloc D).