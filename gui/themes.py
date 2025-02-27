import os


def load_stylesheet(theme: str):
    """Charge le fichier QSS du thème sélectionné."""
    base_path = os.path.dirname(
        os.path.abspath(__file__)
    )  # 📂 Récupère le dossier `stylesheets`
    file_path = os.path.join(base_path, f"{theme}.qss")

    if not os.path.exists(file_path):
        print(
            f"❌ Le fichier {file_path} n'existe pas. Chargement du style par défaut."
        )
        return ""

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
