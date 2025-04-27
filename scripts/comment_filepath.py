from pathlib import Path


def find_py_files(dir: Path = Path("src")) -> list[Path]:
    """Returns a list of paths to .py files for the given directory"""
    return list(dir.rglob("*.py"))


def check_path_comment(file: Path) -> bool:
    """Check if the file has a # Path: comment at first line."""
    content = file.read_text(encoding="utf-8")
    lines = content.splitlines()
    if not lines:
        return False
    return lines[0].startswith("# Path:")


def insert_path_comment(file: Path) -> None:
    """If the file doesn't have a path comment at first line, write it."""
    content = file.read_text(encoding="utf-8").splitlines()

    if not check_path_comment(file):
        path_comment = (
            f"# Path: {file.as_posix()}"  # format propre avec des / même sous Windows
        )
        new_content = [path_comment] + content  # on insère en tête
        file.write_text(
            "\n".join(new_content) + "\n", encoding="utf-8"
        )  # On recolle le tout et on sauvegarde


def main(src_dir: Path = Path("src")) -> None:
    """
    Main function to scan Python files and insert path comments if missing.
    """
    py_files = find_py_files(src_dir)

    for file in py_files:
        if not check_path_comment(file):
            print(f"[!] Adding path comment to: {file}")
            insert_path_comment(file)

    print("\n[✔] Path comments updated where needed.")


if __name__ == "__main__":
    main()
