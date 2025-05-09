"""
replace_imports.py

Outil CLI pour remplacer des chaînes de texte (par exemple des imports) dans tous les fichiers .py d'un projet.

Fonctionnalités :
- Passe les arguments en ligne de commande : texte à remplacer, nouveau texte
- Option --dry-run pour prévisualiser sans modifier les fichiers
- Affiche un diff lisible entre l'ancien et le nouveau contenu
- Utilise argparse pour un usage pro et structuré
- Utilise pathlib pour parcourir les fichiers proprement
- Utilise difflib pour générer un diff lisible

Exemples :
    python replace_imports.py "foo" "bar" (replace)
    python replace_imports.py "foo" "bar" --dry-run (preview)

Auteur : doyouDance + ChatGPT
"""

import argparse
import difflib
from pathlib import Path
from typing import Dict, Tuple


def parse_args() -> Tuple[Dict[str, str], bool]:
    """
    Récupère les arguments passés en ligne de commande.
    Retourne un dictionnaire de remplacement + un booléen dry-run.
    """
    parser = argparse.ArgumentParser(
        description="Replace imports or text in Python files."
    )
    parser.add_argument("old", help="Text to replace")
    parser.add_argument("new", help="New text")
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview changes without applying them"
    )
    args = parser.parse_args()  # . parse_args() est interne à .ArgumentParser()
    return {args.old: args.new}, args.dry_run


def show_diff(file: Path, original: str, modified: str) -> None:
    """
    Affiche un diff lisible ligne par ligne entre l'ancien et le nouveau contenu.
    """
    print(f"\n\u001b[34m--- Changes in: {file} ---\u001b[0m")
    diff = difflib.unified_diff(
        original.splitlines(),
        modified.splitlines(),
        fromfile="original",
        tofile="modified",
        lineterm="",
    )
    for line in sorted(diff):
        if line.startswith("+") and not line.startswith("+++"):
            print(f"\u001b[32m{line}\u001b[0m")  # Vert = ajout
        elif line.startswith("-") and not line.startswith("---"):
            print(f"\u001b[31m{line}\u001b[0m")  # Rouge = suppression


def apply_replacements(
    replacements: Dict[str, str], dry_run: bool = False, src_dir: Path = Path("src")
) -> None:
    """
    Parcourt tous les fichiers .py du dossier et applique les remplacements demandés.
    Affiche les changements et applique si ce n'est pas un dry-run.
    """
    changes_found = False

    for file in src_dir.rglob("*.py"):
        original_content = file.read_text(encoding="utf-8")
        modified_content = original_content

        for old, new in replacements.items():
            modified_content = modified_content.replace(old, new)

        if modified_content != original_content:
            changes_found = True
            show_diff(file, original_content, modified_content)

            if not dry_run:
                file.write_text(modified_content, encoding="utf-8")
                print(f"\u001b[32m[✔] Updated: {file}\u001b[0m")
            else:
                print(f"[DRY-RUN] No changes applied to: {file}")

    if not changes_found:
        print("\n[✔] No changes to preview. All files are already clean.")


if __name__ == "__main__":
    replacements, dry_run = parse_args()
    apply_replacements(replacements, dry_run)
