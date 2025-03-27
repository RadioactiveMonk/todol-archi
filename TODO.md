# ✅ TODO.md — Feuille de route finale pour Todol-Archi

> Une roadmap structurée, pédagogique et progressive pour finir Todol-Archi avec maîtrise et clarté. Chaque étape renforce tes compétences, prépare la suivante, et t’ancre dans un code robuste, modulaire et élégant.

---

## Phase 1 – Stabilisation finale
- [x] Ajouter les `__init__.py` dans tous les sous-dossiers
- [x] Vérifier l’importabilité avec `python -m src.main`
- [ ] Redecouper les constantes
- [ ] Corriger les imports restants si besoin (absolus/relatifs)
- [ ] Lancer l’application et valider : tâches, toggle, thème, catégories
- [ ] Mettre à jour `README.md` et `MIGRATION_LOG.md`

---

## Phase 2 – Design Patterns & Réutilisabilité
- [ ] Créer `icon_factory.py` et l’utiliser dans toute l’UI
- [ ] Créer une `notification_factory.py` non-bloquante (QLabel + Timer)
- [ ] Extraire des helpers/fonctions réutilisables (`get_icon`, `get_category_list`, etc.)
- [ ] (Optionnel) Créer `factory_utils.py` si logique partagée

---

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

---

> ✨ À chaque phase : on introduit les bénéfices, les best practices, et on s’adapte aux questions ou imprévus.  
> Tu avances avec lucidité, et chaque étape te prépare pour la suivante.  

**On trace une vraie ligne d’arrivée, solide et formatrice.**