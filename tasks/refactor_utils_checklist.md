# ✅ Refactor soft : Checklist `utils/` & nettoyage

Objectif : épurer, renommer, regrouper, redonner du sens aux outils existants  
_(sans casser le fonctionnement, mais en préparant le terrain pour la suite)_

---

## 1. Tri & regroupement des `ui_*.py`

- [ ] Identifier les doublons, fichiers trop petits ou trop spécialisés  
- [ ] Fusionner ce qui va ensemble (`ui_geometry_utils`, `ui_icons_utils`, `ui_text_utils`, etc.)
- [ ] Créer si besoin un dossier `ui_helpers/` avec fichiers clairs :
  - `geometry.py`
  - `icons.py`
  - `text.py`

---

## 2. Créer `formatter_utils.py`

- [ ] Déplacer ou écrire :
  - `format_datetime(dt)` (bonus : avec options de format court/long)
  - formatages de texte, dates, durations…
- [ ] Clarifier la frontière entre logique UI et formatage pur

---

## 3. Nettoyer les `*_utils.py` généralistes

- [ ] Vérifier la cohérence de `path_utils.py`, `db_utils.py`, `csv_utils.py`, etc.
- [ ] Fusionner ou renommer si besoin (`init_db.py` → `db_setup.py`, etc.)
- [ ] Ajouter docstring/module-level description sur les fichiers encore flous

---

## 4. Préparer des mini outils transverses

- [ ] Créer un `safe_get()` et autres petits helpers récurrents
- [ ] Si ça grossit : faire un `common_utils.py` ou `dict_utils.py` à part

---

## 5. (bonus) Marquer ce qui pourrait devenir testable

- [ ] Annoter les fonctions pures ou isolables pour futur test unitaire
- [ ] Lister ce qui dépend encore trop de PyQt ou de l’UI pour le séparer plus tard
