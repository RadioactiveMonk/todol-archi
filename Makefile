# Makefile - commandes pratiques pour Todol-Archi

# Variables
PYTHON := python
VENV := .venv
SRC := src
TESTS := tests
REQUIREMENTS := requirements.txt

# Cibles principales
.PHONY: run test ruffall reload gadd clean install venv update_deps coverage typecheck sec_check help

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

venv:
	@echo "📦 Création de l'environnement virtuel..."
	$(PYTHON) -m venv $(VENV)

update_deps:
	@echo "📦 Mise à jour des dépendances..."
	pip install --upgrade -r $(REQUIREMENTS)

coverage:
	@echo "📊 Mesure de la couverture de code..."
	coverage run -m pytest $(TESTS)
	coverage report
	coverage html

typecheck:
	@echo "🔍 Vérification des types avec Mypy..."
	mypy $(SRC) $(TESTS)

sec_check:
	@echo "🔐 Vérification de la sécurité avec Bandit..."
	bandit -r $(SRC)

help:
	@echo "Commandes disponibles :"
	@echo "  make run           → Lancer l'application"
	@echo "  make test          → Lancer les tests"
	@echo "  make ruffall       → Lint et formate avec Ruff"
	@echo "  make reload        → Lancer IPython avec reload_all"
	@echo "  make clean         → Nettoyer les fichiers temporaires"
	@echo "  make gadd m="msg"  → Add, commit, push"
	@echo "  make install       → Installer les dépendances"
	@echo "  make venv          → Créer l'environnement virtuel"
	@echo "  make update_deps   → Mettre à jour les dépendances"
	@echo "  make coverage      → Mesurer la couverture de code"
	@echo "  make typecheck     → Vérifier les types avec Mypy"
	@echo "  make sec_check     → Vérifier la sécurité avec Bandit"
	@echo "  make help          → Afficher cette aide"