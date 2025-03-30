import json
from pathlib import Path
from typing import Any, Dict, List


def main() -> Any:
    data = load_data(verbose=True)

    while True:
        show_menu()
        input_choice = strip_lower(input("Ton choix + ENTER: "))
        handle_choices(input_choice, data)


def get_path(path: str) -> Path | None:
    """Returns the given path"""
    CURRENT_FILE = Path(__file__).resolve()

    path_dict = {
        "current_file": CURRENT_FILE,
        "current_path": CURRENT_FILE.parent,
        "json": CURRENT_FILE.parent / "favorites.json",
    }

    if path in path_dict.keys():
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


def add_favorite(data):
    pass


def delete_favorite(data):
    pass


def list_favorites(data):
    pass


def show_menu():
    print("\nQue veux-tu faire ?")
    print("1 - Lister les favoris")
    print("2 - Ajouter un favori")
    print("3 - Supprimer un favori")
    print("q - Quitter")


def handle_choices(choice: str, data: List[Dict[str, str]]) -> Any:
    valid_choices = {
        "1": lambda: list_favorites(data),
        "2": lambda: add_favorite(data),
        "3": lambda: delete_favorite(data),
        "q": lambda: quit_program(),
    }

    if choice not in valid_choices.keys():
        return f"{choice} n'est pas une option valide"
    else:
        valid_choices.get(choice, lambda: print("Choix invalide"))()


def quit_program():
    exit(0)

def strip_lower(input: str) -> str:
    return input.strip().lower()


if __name__ == "__main__":
    main()
