from pathlib import Path
from typing import Any, Dict


def ask_replacements() -> Dict[str, str]:
    text = input("Type text to replace (src/): ")
    new_text = input("Type new text: ")
    return {text: new_text}


def preview_and_apply(replacements: Dict[str, str], src_dir: Path = Path("src")) -> Any:
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
            original_lines = original_content.splitlines()
            modified_lines = content.splitlines()

            print(f"\n🟦 Lines modification in: {file}")
            print("-" * 50)

            for orig, mod in zip(original_lines, modified_lines):
                if orig != mod:
                    print(f"🟧 {orig}")
                    print(f"🟩 {mod}")

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
    replacements = ask_replacements()
    preview_and_apply(replacements)
