# Checklist — Migration vers `utils/`

Suivre cette checklist étape par étape pour organiser proprement les fichiers de constantes, config, et fonctions utilitaires dans `src/utils/`.

---

## ✅ 1. Brancher proprement

- [x] Créer une branche dédiée : `git checkout -b todol-utils`

---

## ✅ 2. Préparer l’environnement

- [x] Créer le dossier `src/utils/`
- [x] Ajouter un fichier `__init__.py` vide

---

## ✅ 3. Migrer les fichiers existants

- [x] `default_values.py` ➜ utils/
- [x] `status_constants.py` ➜ utils/
- [x] `log_utils.py` (si applicable) ➜ utils/
- [x] `task_table_utils.py` ➜ utils/
- [x] `csv_utils.py` (à évaluer) ➜ utils/
- [x] Autres `*_utils.py` à identifier -> la majorité des fichiers de config ont migrés vers utils/

---

## ✅ 4. Nettoyer et organiser

- [x] Renommer les fichiers si nécessaire (ex: `ui_utils.py`, `db_utils.py`, etc.)
- [ ] Supprimer ou fusionner les doublons
- [ ] Regrouper constantes et fonctions associées

---

## ✅ 5. Identifier les usages

- [ ] Lister les fichiers impactés par les imports déplacés
- [ ] Identifier ce qui doit rester dans `helpers/`

---

## ✅ 6. Modifier les imports

- [ ] Modifier manuellement les imports
- [ ] Utiliser `scripts/replace_imports.py` si utile

---

## ✅ 7. Vérifier le fonctionnement

- [ ] Lancer `todolab` pour tester les imports
- [ ] Tester les fonctions `get_default()`, `status_label()`, etc.
- [ ] Lancer `make test` si disponible

---

## Résultat attendu

- [ ] Tous les fichiers `*_utils.py` centralisés dans `utils/`
- [ ] Structure claire et cohérente
- [ ] Imports fonctionnels dans tout le projet
