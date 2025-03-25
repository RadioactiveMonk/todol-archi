# 🧠 Todol-Archi

Version modulaire et refactorisée de Todol-Pro.  
Expérimentation de patterns avancés (Factory, SOLID, Inversion de dépendance, etc.)

## Objectifs

- 🔁 Repenser la structure du projet pour plus de clarté et de réutilisabilité
- 🏭 Implémenter des factories pour tous les composants majeurs
- 🧩 Modulariser au maximum chaque élément (UI, logique, backend)
- 🧪 Faciliter les tests et les extensions futures

## Base

- PyQt6
- SQLite
- Architecture modulaire orientée objets

## Démarrage

```bash
git clone git@github.com:RadioactiveMonk/todol-archi.git
cd todol-archi
python -m venv .venv
source .venv/bin/activate  # ou .venv\\Scripts\\activate sous Windows
pip install -r requirements.txt
python main.py
