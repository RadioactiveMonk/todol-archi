import json
from pathlib import Path
from typing import Any, Dict, List

CURRENT_FILE = Path(__file__).resolve()
CURRENT_PATH = CURRENT_FILE.parent
FAV_PATH = CURRENT_PATH / "favorites.json"


def main():
    data = load_data(verbose=True)

    while True:
        print("\nQue veux-tu faire ?")
        print("1 - Lister les favoris")
        print("2 - Ajouter un favori")
        print("3 - Supprimer un favori")
        print("Q - Quitter")

        valid_choices = {"1": list_favorites,
                         "2": add_favorite,
                         "3": delete_favorite,
                         "Q": quit}

        choice = input("Ton choix: ").strip().lower()

        if choice not in valid_choices.keys():
            print(f"{choice} n'est pas une option valide")
            continue
        else:
            action = valid_choices.get(choice, None)
            action(data, FAV_PATH, verbose=True)



def load_data(verbose: bool = False) -> List[Dict[str, str]]:
    if verbose:
        print(f"[INFO] Chargement de : {FAV_PATH}")

    try:
        with open(FAV_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        if verbose:
            print(f"[INFO] {FAV_PATH} non trouvé. Création d'un fichier vide.")
        FAV_PATH.write_text("[]", encoding="utf-8")
        return []

    except json.JSONDecodeError:
        print(
            f"[ERREUR] Le fichier {FAV_PATH.name} est corrompu. Utilisation d'une liste vide."
        )
        return []


def save_data(data: List[Dict[str, str]], verbose: bool = False) -> bool:
    try:
        with open(FAV_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        if verbose:
            print(f"[INFO] Données sauvegardées dans {FAV_PATH}")
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

def quit():
    exit(0)


if __name__ == "__main__":
    main()
