import json
import re
from pathlib import Path
from typing import Any, Dict, List


def main() -> Any:
    """Entry point"""
    data = load_data(verbose=True)

    while True:
        user_choice = show_menu()
        handle_choices(user_choice, data)


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
    """Show add favorite section"""
    title = strip_lower(input("Entrez un titre:"))
    url = strip_lower(input("Entrez une url:"))

    return {"title": title, "url": url}


def validate_url(url: str) -> bool:
    """Returns false is url is not valid, otherwise returns True"""

    pattern = r"^(http|https|ftp)://[^\s]+\.[a-z]{2,}$"

    return bool(re.match(pattern, url))


def delete_favorite():
    pass


def list_favorites(data: List[Dict[str, str]]):
    pass


def show_menu() -> str:
    print("\nQue veux-tu faire ?")
    print("1 - Lister les favoris")
    print("2 - Ajouter un favori")
    print("3 - Supprimer un favori")
    print("q - Quitter")

    input_choice = strip_lower(input("Ton choix + ENTER: "))
    return input_choice


def handle_choices(choice: str, data: List[Dict[str, str]]) -> Any:
    valid_choices = {
        "1": lambda: list_favorites(data),
        "2": lambda: add_favorite(data, show_add_favorite()),
        "3": lambda: delete_favorite(),
        "q": lambda: quit_program(),
    }

    if choice not in valid_choices:
        print(f"{choice} n'est pas une option valide")
    else:
        valid_choices.get(choice, lambda: print("Choix invalide"))()


def quit_program():
    exit(0)


def strip_lower(text: str) -> str:
    return text.strip().lower()


if __name__ == "__main__":
    main()
