
# ✅ TODO_review1.md — Plan de refactoring avancé (concepts à intégrer)

> Une checklist ciblée pour refactorer Todol-Archi avec une approche **artisanale, élégante et pédagogique**, en intégrant les notions avancées de Python.

---

## 🧱 STRUCTURE & SIMPLIFICATION
- [ ] Nettoyer le code mort, les doublons, les `print` oubliés
- [ ] déplacer le logger dns helpers, le style loader dans ui/theme. changer imports
- [ ] Identifier les fonctions/helpers réutilisables (DRY)
- [ ] Réduire les `if` en utilisant `dict dispatch`, `strategy`, etc.
- [ ] Ajouter un `helpers/` pour centraliser : 
  - `dataclass_to_dict()`
  - `get_icon()`
  - `get_category_list()`
  - `export_csv()` (avec `yield`)
- [ ] Créer un `factory_utils.py` si des patterns se répètent

---

## 🧠 NOTIONS AVANCÉES À INTÉGRER
- [ ] cohérence des interfaces. faire passer les même données sur des méthodes qui agissent sur ces données. (exemple del(data: List), add(data: List)). Les données prises sont les mêmes, c'est la méthode qui défini ce qu'on traite.
- [ ] `@property` pour rendre certains accès plus élégants, préparer des des actions sur les données pour les recevoir différement ailleurs dans le code.
- [ ] `*args`, `**kwargs` intelligemment utilisés (ex: handlers, UI)
- [ ] `dict dispatch` pour éviter les `if` chaînés
- [ ] `@lru_cache` (déjà utilisé pour les settings, à généraliser ?)
- [ ] `yield` pour génération paresseuse (CSV, logs…)
- [ ] `defaultdict` pour regroupement sans vérif préalable
- [ ] `:=` (walrus operator) pour gagner en lisibilité
- [ ] Créer un `context manager` custom pour les settings
- [ ] Utiliser `@staticmethod`, `@classmethod` où pertinent

---

## 🧩 DESIGN PYTHONIC
- [ ] Rendre certaines classes plus idiomatiques :
  - `__str__`, `__repr__`, `__eq__`, etc.
  - Revoir les dataclasses et leur usage (`asdict` → `dataclass_to_dict`)
- [ ] Regrouper les classes/fonctions similaires (SoC, SRP)
- [ ] Créer un vrai module `notifications` non bloquant (usine à `QLabel`)
- [ ] Nettoyer les logs et créer un `log_utils.py` si besoin

---

## 🚀 TEST & VALIDATION
- [ ] Valider chaque helper/fonction ajoutée dans IPython avant intégration
- [ ] Ajouter des tests ciblés pour les fonctions refactorisées
- [ ] Mettre à jour les tests existants selon les nouvelles signatures
