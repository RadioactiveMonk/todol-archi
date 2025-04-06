# Makefile - commandes pratiques pour Todol-Archi

# Variables
PYTHON := python
VENV := .venv
SRC := src
TESTS := tests

# Cibles principales
.PHONY: run test ruffall reload gadd clean install help

run:
	@echo "Lancement de l'application..."
	$(PYTHON) $(SRC)/main.py

test:
	@echo "Lancement des tests Pytest..."
	PYTHONPATH=$(SRC) pytest -v $(TESTS)

ruffall:
	@echo "🎨 Formatage avec Ruff..."
	ruff format $(SRC) $(TESTS)
	@echo "🧼 Linting avec Ruff (fix)..."
	ruff check $(SRC) $(TESTS) --fix 

reload:
	@echo "🚀 Lancement d'IPython avec reload_all.py..."
	ipython -i scripts/reload_all.py

gadd:
	@echo "Ajout des fichiers au dépôt Git..."
	git add .
	git commit -m "$(m)"
	git push origin main

clean:
	@echo "🧹 Nettoyage des fichiers compilés..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@echo "✅ Pyc & __pycache__ supprimés."

install:
	@echo "📦 Installation des dépendances..."
	pip install --upgrade pip
	pip install .[dev]

help:
	@echo "Commandes disponibles :"
	@echo "  make run       → Lancer l'application"
	@echo "  make test      → Lancer les tests"
	@echo "  make ruffall   → Lint et formate avec Ruff"
	@echo "  make reload    → Lancer IPython avec reload_all"
	@echo "  make clean     → Nettoyer les fichiers temporaires"
	@echo "  make gadd m="msg"  → Add, commit, push"
	@echo "  make install   → Installer les dépendances"
	@echo "  make help      → Afficher cette aide"