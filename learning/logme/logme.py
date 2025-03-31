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

    message = sep.join(str(arg) for arg in args)
    if upper:
        message = message.upper()

    print(f"{prefix} {message}", end=end)