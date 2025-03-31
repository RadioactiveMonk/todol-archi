import json
import re
from pathlib import Path
from typing import Any, Dict, List


def main() -> Any:
    """Entry point"""
    data = load_data(verbose=True)

    while True:
        choice = prompt_main_menu_choice()
        handle_choices(data, choice)


def get_path(path: str) -> Path | None:
    """Returns the given path"""
    current_file = Path(__file__).resolve()

    path_dict = {
        "current_file": current_file,
        "current_path": current_file.parent,
        "json": current_file.parent / "favorites.json",
    }

    return path_dict.get(path, None)


def load_data(verbose: bool = False) -> List[Dict[str, str]]:
    """Returns a list of favorites as dicts"""
    if verbose:
        print(f"[INFO] Chargement de : {get_path('json')}")

    try:
        json_file = str(get_path("json"))
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        if verbose:
            print(f"[INFO] {json_file} non trouvé. Création d'un fichier vide.")
        Path(json_file).write_text("[]", encoding="utf-8")
        return []

    except json.JSONDecodeError:
        print(
            f"[ERREUR] Le fichier {json_file} est corrompu. Utilisation d'une liste vide."
        )
        return []


def save_data(data: List[Dict[str, str]], verbose: bool = False) -> bool:
    """Return true if data are saved, otherwise returns false"""
    try:
        json_file = str(get_path("json"))
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        if verbose:
            print(f"[INFO] Données sauvegardées dans {json_file}")
        return True
    except Exception as e:
        print(f"[ERREUR] Impossible de sauvegarder les données : {e}")
        return False


def add_favorite(data: List[Dict[str, str]], favorite: Dict[str, str]) -> bool:
    """Validate and add user inputs to the storage. Return false if inputs are not valid."""
    if validate_url(favorite["url"]) and favorite["title"]:
        data.append(favorite)
        save_data(data)
        print(f"{favorite} ajouté avec succès.")
        list_favorites(data)
        return True
    else:
        print("Titre ou URL invalide. Réessaye.")
        return False


def show_add_favorite() -> Dict[str, str]:
    """Show add favorite section to ask user for inputs"""
    title = strip_lower(input("Entrez un titre:"))
    url = strip_lower(input("Entrez une url:"))

    return {"title": title, "url": url}


def validate_url(url: str) -> bool:
    """Returns false is url is not valid, otherwise returns True"""

    pattern = r"^(http|https|ftp)://[^\s]+\.[a-z]{2,}$"

    return bool(re.match(pattern, url))


def delete_favorite(data: List[Dict[str, str]]) -> bool:
    """Supprime le favoris par son index"""
    if not data:
        print("Aucun favoris à supprimer")
        return False

    list_favorites(data)

    try:
        index = int(input("\nNuméro du favoris à supprimer: ")) - 1
        if not (0 <= index < len(data)):
            print("Erreur: index hors limite")
            return False

        removed = data.pop(index)
        save_data(data, verbose=True)
        print(f"Favori supprimé: {removed['title']} - {removed['url']}")
        return True

    except ValueError:
        print("Erreur: entrée invalide. Tapez un ID existant.")
        return False


def list_favorites(data: List[Dict[str, str]]):
    """Shows the list of favorites"""
    if not data:
        print("Aucun favori enregistré.")
    for i, fav in enumerate(data, 1):
        print(f"{i}. {fav['title']} - {fav['url']}")


def prompt_main_menu_choice() -> str:
    """Prompt a menu for the user to choose an option, return the input."""
    print("\nQue veux-tu faire ?")
    print("1 - Lister les favoris")
    print("2 - Ajouter un favori")
    print("3 - Supprimer un favori")
    print("q - Quitter")

    input_choice = strip_lower(input("Ton choix + ENTER: "))
    return input_choice


def handle_choices(
    data: List[Dict[str, str]],
    choice: str,
) -> Any:
    """Handle the user choice with a dict dispatch to redirect to the asked section"""
    valid_choices = {
        "1": lambda: list_favorites(data),
        "2": lambda: add_favorite(data, show_add_favorite()),
        "3": lambda: delete_favorite(data),
        "q": lambda: quit_program(),
    }

    if choice not in valid_choices:
        print(f"{choice} n'est pas une option valide")
    else:
        valid_choices.get(choice, lambda: print("Choix invalide"))()


def quit_program():
    """Quit with code 0"""
    exit(0)


def strip_lower(text: str) -> str:
    """Lower the text to strip it"""
    return text.strip().lower()


if __name__ == "__main__":
    main()
