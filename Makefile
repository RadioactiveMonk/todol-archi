# Makefile - commandes pratiques pour Todol-Archi

# Variables
PYTHON := python
VENV := .venv
SRC := src
TOOLS := tools
TESTS := tests
DOCS := docs
REQUIREMENTS := requirements.txt

# Cibles principales
.PHONY: run test ruffall gpush gmain clean install venv update_deps coverage typecheck sec_check black filepath docs help

run:
	@echo "🎬 Lancement de l'application..."
	poetry run python $(SRC)/main.py

test:
	@echo "🧪 Lancement des tests Pytest..."
	poetry run pytest -v $(TESTS)

ruffall:
	@echo "🎨 Formatage et linting avec Ruff via Poetry..."
	poetry run ruff format $(SRC) $(TESTS) $(TOOLS)
	poetry run ruff check $(SRC) $(TESTS) $(TOOLS)

gpush:
	@echo "⬆️ Ajout des fichiers au dépôt Git..."
	git add .
	git commit -m "see tasks/ or MIGRATION_log.md"
	git push -u origin $(git branch --show-current)

gmain:
	@echo "🪐 Switch sur branche 'main'"
	git switch main

clean:
	@echo "🧹 Nettoyage des fichiers compilés..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@echo "*.pyc, __pycache__"
	@echo "✅ DONE"

install:
	@echo "📦 Installation des dépendances avec Poetry..."
	poetry install

venv:
	@echo "📦 Création de l'environnement virtuel avec Poetry..."
	poetry env use $(PYTHON)

update_deps:
	@echo "📦 Mise à jour des dépendances avec Poetry..."
	poetry update

coverage:
	@echo "📊 Mesure de la couverture de code..."
	poetry run coverage run -m pytest $(TESTS)
	poetry run coverage report
	poetry run coverage html

typecheck:
	@echo "🔍 Vérification des types avec Mypy via Poetry..."
	poetry run mypy $(SRC) $(TESTS)

sec_check:
	@echo "🔐 Vérification de la sécurité avec Bandit via Poetry..."
	poetry run bandit -r $(SRC)

black:
	@echo "🎨 Formatage du code avec Black via Poetry..."
	poetry run black $(SRC) $(TESTS)

filepath:
	@echo "🤖 Adding path comment to files ..."
	poetry run $(PYTHON) $(TOOLS)/comment_filepath.py

docs:
	@echo "📚 Génération de la documentation avec Sphinx via Poetry..."
	poetry run sphinx-apidoc -o $(DOCS) $(SRC)
	poetry run sphinx-build -b html $(DOCS) $(DOCS)/_build

help:
	@echo "Commandes disponibles :"
	@echo "  make run           → Lancer l'application"
	@echo "  make test          → Lancer les tests"
	@echo "  make ruffall       → Lint et formate avec Ruff"
	@echo "  make clean         → Nettoyer les fichiers temporaires"
	@echo "  make gpush         → Add, commit, push"
	@echo "  make gmain         → Switch vers la branche principale"
	@echo "  make install       → Installer les dépendances"
	@echo "  make venv          → Créer l'environnement virtuel"
	@echo "  make update_deps   → Mettre à jour les dépendances"
	@echo "  make coverage      → Mesurer la couverture de code"
	@echo "  make typecheck     → Vérifier les types avec Mypy"
	@echo "  make sec_check     → Vérifier la sécurité avec Bandit"
	@echo "  make black         → Formatter le code avec Black"
	@echo "  make filepath      → Ajoute le chemin du fichier en première ligne"
	@echo "  make docs          → Générer la documentation avec Sphinx"
	@echo "  make help          → Afficher cette aide"