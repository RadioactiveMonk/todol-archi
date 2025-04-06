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
	ruff check $(SRC) $(TESTS) --fix


ruffall:
	@echo "🎨 Formatage avec Ruff..."
	ruff format $(SRC) $(TESTS)
	@echo "🧼 Linting avec Ruff (fix)..."
 	ruff check $(SRC) $(TESTS) --fix 

reload:
	@echo "🚀 Lancement d'IPython avec reload_all.py..."
	ipython -i scripts/reload_all.py || echo '⚠️ IPython a rencontré une erreur.'

gadd:
	@echo "Ajout des fichiers au dépôt Git..."
	$(PYTHON) scripts/gitadd.py "$(msg)"

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
	@echo "  make format    → Formatter le code avec Ruff"
	@echo "  make lint      → Linter le code avec Ruff"
	@echo "  make ruffall   → Lint et formate avec Ruff"
	@echo "  make reload    → Lancer IPython avec reload_all"
	@echo "  make clean     → Nettoyer les fichiers temporaires"
	@echo "  make gadd      → Ajouter les fichiers au dépôt Git"
	@echo "  make install   → Installer les dépendances"
	@echo "  make help      → Afficher cette aide"
