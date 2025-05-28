# 🧼 Bloc C – Harmonisation & Nettoyage

## 🎯 Objectif
Finaliser le Bloc C avec des ajustements légers pour garantir la cohérence, la lisibilité et la propreté du noyau métier.

---

## ✅ 1. Noms de méthodes

- [ ] Vérifier les préfixes (`get_`, `edit_`, `toggle_`, `check_`, etc.)
- [ ] Supprimer les `get_` inutiles (`get_selected_task()` → `selected_task()` ?)
- [ ] Éviter les redondances (`task.task_id` ou `task.title.title`)

---

## ✅ 2. Docstrings

- [ ] Repérer les docstrings absents ou en français
- [ ] Uniformiser au format Google (choisi)
- [ ] S'assurer que toutes les méthodes publiques sont documentées

---

## ✅ 3. Allègement de code

- [ ] Remplacer `if x: return True else: return False` → `return bool(x)`
- [ ] Favoriser les early return (`if not x: return`)
- [ ] Raccourcir les méthodes verbeuses si possible

---

## ✅ 4. Bonus possibles

- [ ] Ajouter `@property` utiles (ex: `is_done`, `is_empty`)
- [ ] Nettoyer les `import` inutiles ou mal ordonnés
- [ ] Vérifier la cohérence des logs (`logger.info`, `logger.warning`, etc.)

---

## 🔚 Objectif final
Avoir un noyau métier clair, élégant et prêt à être branché au Bloc D (UI) sans retravailler les bases.