from pathlib import Path
from typing import Any

# Mapping des constantes déplacées
replacements = {
    "from PyQt6": "from PySide6",
}


def preview_and_apply(src_dir: Path = Path("src")) -> Any:
    """
    Display a preview of the changes and ask confirmation before applying.
    """
    changes_found = False

    for file in src_dir.rglob("*.py"):
        content = file.read_text(encoding="utf-8")
        original_content = content 

        # Applique les remplacements
        for old, new in replacements.items():
            content = content.replace(old, new)

        if content != original_content:
            changes_found = True
            print(f"\n--- Changes proposed for: {file} ---")
            print("-" * 50)
            print(
                "\n".join(content.splitlines()[:20])
            )  # <--- Affiche seulement les 20 lignes modifiées
            print("-" * 50)

            choice = input("Do you wish to apply these changes? (y/n): ").lower()

            if choice == "y":
                file.write_text(content, encoding="utf-8")
                print(f"[✔] Updated: {file}")
            elif choice == "n":
                print(f"[!] No changes applied to {file}")
            else:
                print("[!] Invalid input. No changes applied to this file.")

    if not changes_found:
        print("\n[✔] No changes to preview. All files are already clean.")


if __name__ == "__main__":
    preview_and_apply()
