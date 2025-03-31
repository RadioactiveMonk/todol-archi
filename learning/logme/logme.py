from rich import print as rich_print


def log(*args, **kwargs):
    """
    Log un message construit a partir des *args.
    Options via **kwargs:
    - sep (str): séparateur entre les args (par défaut: " ")
    - prefix (str): texte affiché avant le message
    - upper (bool): passe le message en majuscules
    - end (str): fin de ligne (defaut: "\\n")
    """

    sep = kwargs.get("sep", " ")
    prefix = kwargs.get("prefix", "")
    upper = kwargs.get("upper", False)
    end = kwargs.get("end", "\n")
    color = kwargs.get("color")
    to_file = kwargs.get("to_file", False)
    filename = kwargs.get("filename", "log.txt")

    message = sep.join(str(arg) for arg in args)
    if upper:
        message = message.upper()

    if color:
        rich_print(f"[{color}] {prefix} {message} [/{color}]", end=end)
    else:
        print(f"{prefix} {message}", end=end)

    if to_file:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{prefix} {message}\n")
