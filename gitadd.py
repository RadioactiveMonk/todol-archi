#!/usr/bin/env python3
import subprocess
import sys


def gitadd(message: str):
    """
    Automatiser git add, commit et push.

    Parameters
    ----------
    message : str
        Le message du commit.
    """
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Push réussi !")

    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur Git : {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        gitadd(" ".join(sys.argv[1:]))
    else:
        print("❌ Erreur : Vous devez fournir un message de commit.")
