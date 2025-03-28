from pathlib import Path

# mapping des constantes déplacées
replacements = {
    "from core.app_constants import MAIN_WINDOW_TITLE": "from ui.ui_constants import MAIN_WINDOW_TITLE",
}

src_dir = Path("src")

for file in src_dir.rglob("*.py"):
    content = file.read_text()
    original = content
    for old, new in replacements.items():
        content = content.replace(old, new)
    if content != original:
        file.write_text(content)
        print(f"[✔] Updated: {file}")
