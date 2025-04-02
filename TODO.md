
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

## Phase 3 – Fonctionnalités UI finales
- [ ] Implémenter une barre de recherche fonctionnelle
- [ ] Intégrer un filtrage dans `TaskTableModel` (`filterTasks()` ou équivalent)
- [ ] Améliorer la présentation visuelle du tableau (alignements, focus, style)
- [ ] Ajouter interactions UX (hover, fond dynamique, etc.)

---

## Phase 4 – Refactoring DRY / Propreté
- [ ] Identifier et regrouper le code redondant (UI, handlers, settings…)
- [ ] Créer des helpers/fonctions utilitaires génériques (validation, affichage, chemins)
- [ ] Centraliser les logs, constantes, configs inutiles dans `core/`

---

## Phase 5 – Tests & validation finale
- [ ] Compléter les tests unitaires sur tous les modules critiques (handlers, db, settings)
- [ ] Ajouter des tests d’intégration (simulateurs complets : add → toggle → delete)
- [ ] Nettoyer les anciens tests ou doublons
- [ ] (Optionnel) Ajouter un badge GitHub Actions + README

---

## Phase 6 – Préparation au packaging
- [ ] Relire le projet et supprimer le code mort ou inutilisé
- [ ] Compléter `pyproject.toml` pour un packaging propre
- [ ] Ajouter une commande `entry_point` si souhaité (CLI optionnelle)

---

## Phase 7 – Expérimentations (Todol-Experimental)
- [ ] Cloner le projet pour y tester des concepts avancés sans polluer le code stable
- [ ] Tester des `context managers` persos (`with open_settings():`)
- [ ] Ajouter des décorateurs custom (`@log_event`, `@require_setting`)
- [ ] Approcher `threading`, `asyncio`, `yield`, `contextlib`, etc.
