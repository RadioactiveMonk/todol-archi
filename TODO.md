# ✅ TODO.md — Plan de refactoring avancé (version organisée)

> Une checklist progressive pour refactorer Todol-Archi avec une approche artisanale, élégante et pédagogique.

---

## Phase 1 – 🔧 Stabilisation & nettoyage de fondation
- [x] Nettoyer le code mort, les doublons, les `print` oubliés
- [x] Déplacer le logger dans `helpers/`, le style loader dans `ui/theme/`, changer les imports
- [x] Identifier les fonctions/helpers réutilisables (DRY)
- [ ] Créer un dossier `helpers/` :
  - `dataclass_to_dict()` OK
  - status_label(task) OK
  - task_from_row(dict) (à refaire sur base stable, créer une branche git)
  - safe_get(dict, key, default)
  - format_datetime(str)
  - log_task(task)
  - task_to_csv_row(task)
- [ ] Créer un `factory_utils.py` si logique partagée
- [ ] Centraliser les configurations :
  - PYTHONPATH (Makefile, pytest, scripts/dev.sh)
  - Options de test/lint/format dans pyproject.toml
  - Fusionner dev.sh / reload / Makefile si possible

---

## Phase 2 – 🧠 Refactoring avancé (notions Python modernes)
- [ ] Rendre les interfaces cohérentes (`add(data: List)`, `del(data: List)`)
- [ ] Réduire les `if` via `dict dispatch` ou stratégie
- [ ] Utiliser `@property` pour des accès propres
- [ ] Intégrer `*args`, `**kwargs` où pertinent (UI, handlers)
- [ ] Ajouter ou généraliser `@lru_cache` (ex: config, constantes)
- [ ] Intégrer `yield` pour CSV/logs paresseux
- [ ] Utiliser `defaultdict` pour éviter les vérifications inutiles
- [ ] Introduire `:=` (walrus operator) dans des affectations lisibles
- [ ] Créer un `context manager` custom (`with open_settings():`)
- [ ] Utiliser `@staticmethod`, `@classmethod` proprement

---

## Phase 3 – 🧩 Design Pythonic & architecture élégante
- [ ] Rendre les classes plus idiomatiques (`__str__`, `__repr__`, `__eq__`)
- [ ] Revoir l'usage des dataclasses (`asdict()` → helper `dataclass_to_dict`)
- [ ] Regrouper les classes/fonctions similaires (SoC, SRP)
- [ ] Créer une vraie `notification_factory.py` (QLabel + Timer)
- [ ] Nettoyer les logs et créer un `log_utils.py` propre
- [ ] (prévoir branche "task-core-exp" pour version alternative basée sur héritage clean)

---

## Phase 4 – 🎨 UI & UX avancée
- [ ] Implémenter une **barre de recherche**
- [ ] Ajouter un filtrage dans `TaskTableModel` (`filterTasks()`)
- [ ] Améliorer la présentation visuelle du tableau (alignement, focus, style)
- [ ] Ajouter des interactions UX : hover, fond dynamique…

---

## Phase 5 – ✅ Tests & validation (à réactiver plus tard)
- [ ] Valider chaque helper dans IPython avant intégration
- [ ] Ajouter des tests unitaires pour les fonctions refactorisées
- [ ] Compléter les tests unitaires (handlers, db, settings)
- [ ] Ajouter des tests d’intégration (workflow : add → toggle → delete)
- [ ] Nettoyer les anciens tests ou doublons
- [ ] (Optionnel) Badge GitHub Actions + README

---

## Phase 6 – 📦 Packaging propre
- [ ] Relire le projet final
- [ ] Supprimer tout code mort ou inutilisé
- [ ] Compléter le `pyproject.toml` pour un packaging clean
- [ ] Ajouter une commande `entry_point` (CLI optionnelle)

---

## Phase 7 – 🧪 Todol-Experimental (libre)
  # Structures de données avancées et programmation asynchrone
- [ ] Cloner le projet en version "expérimentale"
- [ ] deque (collections, queue, stack efficaces)
- [ ] Enum (valeurs symboliques propres et lisibles)
- [ ] NamedTuple / dataclass vs tuple classique
- [ ] LinkedList / Node (manuellement pour comprendre le chaînage)
- [ ] Heap, Set, frozenset, defaultdict
- [ ] Tester des `context managers` persos
- [ ] Ajouter des décorateurs custom (`@log_event`, `@require_setting`)
- [ ] Approcher `threading`, `asyncio`, `yield`, `contextlib`...
