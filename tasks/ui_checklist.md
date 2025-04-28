# 🧹 UI Checklist – Bloc C (Nettoyage et Structuration)

## 🎯 Objectif général

- Clarifier la séparation entre :
  - **Affichage pur** (headers, tailles, visibilité, tooltips…)
  - **Comportements** (delegates interactifs)
  - **Signaux** (connexion des actions personnalisées)
- Réaligner **TaskTableModel** et **TaskTableView** sur la nouvelle base **TASK_TABLE_COLUMNS**
- Rendre l’UI **modulaire**, **propre**, **facile à maintenir**, et **évolutive**.

---

## 🛠️ Plan de migration étape par étape

### 1. Séparation des responsabilités

- [x] `apply_column_config(view, columns)` ➔ dans `view_utils.py`
- [x] `apply_delegate_for_column(view, columns)` ➔ créé dans `delegate_utils.py`
- [x] `connect_delegate_signals(view)` ➔ créé dans `signal_utils.py`

---

### 2. Refondre le `TaskTableModel`

- [ ] Nettoyer `rowCount()` et `columnCount()` (basés sur `TASK_TABLE_COLUMNS`)
- [ ] Adapter `headerData()` (utiliser `TaskTableColumn.name`)
- [ ] Adapter `data()` (utiliser `TaskTableColumn.field`)
- [ ] Adapter `flags()` (utiliser `get_flags_for_column()`)
- [ ] Adapter alignements (utiliser `text_alignment()`)
- [ ] Supprimer l’usage de `TASK_TABLE_HEADERS` et reliques

---

### 3. Nettoyage du `TaskTableView`

- [x] Nettoyer `setup_ui()` (séparer affichage uniquement)
- [x] Nettoyer `setup_signals()` (connecter via `connect_delegate_signals()`)
- [x] Supprimer `setup_delegates()` actuel (remplacé par `apply_delegate_for_column`)
- [ ] Vérifier l'appel clair aux helpers dans `__init__()`

---

### 4. Typage et sécurité

- [x] Vérifier les attributs (`column_delegates`) (OK avec `hasattr()`)
- [x] Vérifier la présence des signaux avant connexion (`hasattr(delegate, "editClicked")`)

---

### 5. Tri des fichiers UI (bonus)

- [x] Créer `view_utils.py` pour helpers visuels purs
- [x] Créer `delegate_utils.py` pour helpers delegates
- [x] Créer `signal_utils.py` pour helpers signaux
- [ ] Nettoyage final si d’autres petits helpers spécifiques apparaissent

---

## 📋 Détail par fichier

| Fichier | Contenu prévu |
|:--------|:--------------|
| `view_utils.py` | Helpers visuels purs (colonnes, headers, tooltips…) |
| `delegate_utils.py` | Helpers pour poser les delegates |
| `signal_utils.py` | Helpers pour connecter dynamiquement les signaux |
| `task_table_model.py` | Modèle basé sur `TASK_TABLE_COLUMNS` uniquement |
| `task_table_view.py` | UI ultra légère : instanciation + appels propres aux helpers |

---

## 🔥 Objectif final visé

- `TaskTableView` minimaliste
- `TaskTableModel` piloté uniquement par `TASK_TABLE_COLUMNS`
- Plus aucun affichage ou comportement codé en dur
- UI totalement pilotée par la config, évolutive et professionnelle

---

# ✨ Note finale

**Pas de rush.**
**On découpe. On trie.**
**On reconstruit calmement pour un projet solide et durable.**
