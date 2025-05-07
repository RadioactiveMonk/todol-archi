1. parser = argparse.ArgumentParser(...)

On crée un "parseur d’arguments" = un petit moteur qui va comprendre ce que tu tapes dans le terminal.

C’est lui qui gère :

les options (--dry-run, --force)

les valeurs ("from PyQt6", "from PySide6")

les erreurs si tu oublies un truc ou te trompes



---

2. parser.add_argument(...)

Tu définis ici les arguments acceptés par ton script.

Exemple :

parser.add_argument("old", help="Texte à remplacer")
parser.add_argument("new", help="Texte de remplacement")
parser.add_argument("--dry-run", action="store_true")

"old" et "new" = obligatoires

"--dry-run" = optionnel, c’est un flag (True/False)


Et action="store_true" ?

> Ça veut dire : “si l’utilisateur écrit --dry-run, on met True, sinon False”




---

3. args = parser.parse_args()

C’est ici qu’on analyse ce que l’utilisateur a tapé.

Tu lances le parseur et il te retourne un objet avec tous les arguments :

python script.py "from PyQt6" "from PySide6" --dry-run

Te donne :

args.old == "from PyQt6"
args.new == "from PySide6"
args.dry_run == True


---

4. Le return {...}, args.dry_run

Tu renvoies :

{args.old: args.new}, args.dry_run

un dict (utile pour faire plusieurs remplacements plus tard si tu veux étendre),

et un booléen pour savoir si on est en mode dry-run