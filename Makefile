# Makefile - commandes pratiques pour Todol-Archi

# Variables
PYTHON := python
VENV := .venv
SRC := src
TESTS := tests

# Cibles principales
.PHONY: run test format lint reload clean help

run:
	@echo "Lancement de l'application..."
	$(PYTHON) $(SRC)/main.py

test:
	@echo "Lancement des tests Pytest..."
	pytest $(TESTS)

format:
	@echo "Formatage du code avec Ruff..."
	ruff format $(SRC) $(TESTS)

lint:
	@echo "Vérification du code avec Ruff..."
	ruff check --fix $(SRC) $(TESTS)

reload:
	@echo "Lancement d'IPython avec reload_all..."
	ipython -i scripts/reload_all.py

gadd:
	@echo "Ajout des fichiers au dépôt Git..."
	python scripts/gitadd.py "$(msg)"

clean:
	@echo "Nettoyage des fichiers .pyc et __pycache__..."
	find . -type d -name "__pycache__" -exec rm -r {} +;
	find . -type f -name "*.pyc" -delete;

help:
	@echo "Commandes disponibles :"
	@echo "  make run       → Lancer l'application"
	@echo "  make test      → Lancer les tests"
	@echo "  make format    → Formatter le code avec Ruff"
	@echo "  make lint      → Linter le code avec Ruff"
	@echo "  make reload    → Lancer IPython avec reload_all"
	@echo "  make clean     → Nettoyer les fichiers temporaires"
	@echo "  make gadd      → Ajouter les fichiers au dépôt Git"
	@echo "  make help      → Afficher cette aide"
