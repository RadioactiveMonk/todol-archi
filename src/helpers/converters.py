from dataclasses import asdict, is_dataclass
from typing import Any, Dict


def dataclass_to_dict(obj: Any, exclude: set[str] | None = None) -> Dict[str, Any]:
    """
    Convertit une dataclass (obj) en dictionnaire, avec possibilité d'exclure certains champs.

    Args:
        obj: Instance d'une dataclass.
        exclude: Ensemble de champs à ignorer dans le dictionnaire retourné.

    Returns:
        Un dictionnaire représentant la dataclass.
    """
    if not is_dataclass(obj) or isinstance(obj, type):
        raise TypeError(
            "L'objet fourni doit être une instance de dataclass, pas une classe."
        )

    exclude = exclude or set()
    return {k: v for k, v in asdict(obj).items() if k not in exclude}
