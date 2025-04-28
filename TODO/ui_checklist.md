# 🧹 UI Checklist – Bloc C (Nettoyage et Structuration)

## 🎯 Objectif général

- Clarifier la séparation entre :
  - **Affichage pur** (headers, tailles, visibilité, tooltips…)
  - **Comportements** (delegates interactifs)
  - **Signaux** (connexion des actions personnalisées)
- Rendre l’UI **modulaire**, **propre**, **facile à maintenir** et **agréable à étendre**.

---

## 🛠️ Plan de migration étape par étape

### 1. Séparation des responsabilités

| Cible | Action |
|:------|:-------|
| `apply_column_config(view, columns)` | Conserver ➔ dans `view_utils.py` |
| `apply_delegate_for_column(view, columns)` | Créer ➔ (poser les delegates interactifs) |
| `connect_delegate_signals(view)` | Créer ➔ (connecter dynamiquement les signaux) |

---

### 2. Nettoyage du `TaskTableView`

| Action | Détail |
|:-------|:-------|
| Nettoyer `setup_ui()` | Ne laisser que l'affichage visuel |
| Nettoyer `setup_signals()` | Remplacer par un appel à `connect_delegate_signals()` |
| Supprimer `setup_delegates()` actuel | (plus utile, remplacé par `apply_delegate_for_column`) |
| Appeler proprement les 2-3 helpers dans `__init__()` | Ex : `apply_column_config`, `apply_delegate_for_column`, `connect_delegate_signals` |

---

### 3. Typage et sécurité

| Action | Détail |
|:-------|:-------|
| Vérifier les attributs (`column_delegates`) | OK avec `hasattr()` ou cast dynamique si besoin |
| Vérifier la présence des signaux avant connexion (`hasattr(delegate, "editClicked")`) | |

---

### 4. Tri des fichiers UI (bonus)

| Action | Détail |
|:-------|:-------|
| S'assurer que tout ce qui est "comportement" est dans un fichier dédié | (ex: `delegate_utils.py`) |
| S'assurer que tout ce qui est "connexion de signaux" est proprement isolé | (ex: `signal_utils.py` si besoin) |
| Regrouper les helpers visuels de base dans `view_utils.py` | |

---

## 📋 Détail par fichier

| Fichier | Contenu prévu |
|:--------|:--------------|
| `view_utils.py` | Helpers visuels purs (colonnes, headers, tooltips…) |
| `delegate_utils.py` ou `view_behavior_utils.py` | Helpers pour poser les delegates |
| `signal_utils.py` (optionnel) | Helpers pour connecter dynamiquement les signaux |
| `task_table_view.py` | Code UI ultra léger : instanciation + appels propres aux helpers |

---

## 🔥 Objectif final visé

- `TaskTableView` qui contient **seulement** 5-10 lignes dans `setup_ui` / `setup_signals`
- Aucun comportement codé en dur
- Possibilité d’ajouter/modifier des colonnes/delegates/signaux en **modifiant uniquement la config** (`TASK_TABLE_COLUMNS`)

---

# ✨ Note finale
**On ne rush pas.**
**On découpe. On trie.**
**On transforme petit à petit ce vieux bloc hérité en un vrai bijou modulable.**
