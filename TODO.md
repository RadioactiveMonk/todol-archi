✅ TODO.md — Plan de refactoring structuré (progressif & pédagogique)


---

Bloc A — Stabilisation & helpers fondamentaux

> Préparer un socle propre, testable, et modulaire



[x] Nettoyer le code mort, les print, les logs temporaires

[x] Créer dossier helpers/ et y isoler les fonctions clés :

[x] dataclass_to_dict()

[x] status_label()

[ ] task_from_row() (à refaire sur base stable)


[x] Valider reload_all.py et l'accès IPython

[x] Créer une Task propre

[x] @dataclass complète

[ ] Préparer base task_core si besoin (en branche task-core-exp)




---

Bloc B — Organisation claire des responsabilités

> Clarifier ce qui relève du domaine, de l’UI, de la DB...



[ ] Nettoyer default_values.py

[ ] Distinguer : status_constants, default_*, core.*

[ ] Créer factory_utils.py si besoin de constructeurs spécialisés

[ ] Centraliser la config du projet :

[ ] Makefile unifié (test, format, lint...)

[ ] dev.sh vs Makefile

[ ] pyproject.toml pour pytest/ruff/config




---

Bloc C — Refactoring Pythonic & bonnes pratiques

> Rendre le code élégant, DRY, et idiomatique



[ ] Ajouter des propriétés @property, __str__, __repr__

[ ] Ajouter safe_get(dict, key, default)

[ ] Ajouter log_task() pour trace propre

[ ] Ajouter format_datetime() helper lisible

[ ] Préparer l'usage de *args, **kwargs, @staticmethod où pertinent

[ ] Créer contextmanagers.py utiles



---

Bloc D — UI / UX (affichage et interactions)

> Rendre l'application agréable à l’usage



[ ] Améliorer TaskTableModel avec helpers

[ ] Ajouter recherche et filtres

[ ] Ajuster l’UI pour l’affichage dynamique (fond, hover...)

[ ] Regrouper les helpers UI dans ui_helpers.py



---

Bloc E — Tests, packaging, intégration

> Valider, tester, distribuer proprement



[ ] Phase 5 : Réactivation de pytest

[ ] Ajouter tests unitaires pour les helpers

[ ] Tester task_from_row(), status_label()...

[ ] Ajouter tests d’intégration (add → delete)


[ ] Packaging clean

[ ] pyproject.toml complet

[ ] entry_point CLI ?

[ ] README & badge CI




---

Bonus — Explorations futures (Branche expérimentale)

> Concepts avancés ou usages spécifiques



[ ] Créer branche task-core-exp

[ ] Tester : héritage Task vs TaskCore

[ ] Ajouter structures avancées : deque, NamedTuple, contextlib, asyncio, yield...


