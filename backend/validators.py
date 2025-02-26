from typing import Any, Optional
from datetime import datetime


class BaseValidator:
    """Classe de base pour la validation des types attributs."""

    def __init__(self, expected_type: type, default_value: Any):
        self.expected_type = expected_type
        self.default_value = default_value

    def validate(self, value):
        """Vérifie si la valeur correspond au type attendu."""

        if not isinstance(value, self.expected_type):
            raise ValueError(
                f"⚠️ Erreur: La valeur {value} doit être de type {self.expected_type.__name__}."
            )
        return True


class DateValidator(BaseValidator):
    """Validation générique des dates et gestion des erreurs."""

    def __init__(self, allow_past=False):
        """Par defaut, interdit les dates passées sauf si allow_past=True"""

        super().__init__(expected_type=datetime, default_value=None)
        self.allow_past = allow_past

    def validate(self, value: Optional[datetime]):
        """SI elle est précisée (Optional), vérifie que la valeur est bien une date [datetime],
        et respecte allow_past. Sinon renvoie None (par defaut de la méthode Optional)
        """

        if value is None:  # C'est que la valeur optionnelle n'est pas renseignée
            return True

        if not super().validate(value):
            return False

        if not self.allow_past and value < datetime.now():  # si self.allow_past=False
            raise ValueError(
                "⚠️ Erreur: La date d'expiration ne peut pas être dans le passé."
            )
        return True


def validate_fields(self) -> bool:
    """Valide tous les champs en utilisant les validateurs définis dans `metadata`."""

    for field_name, field_info in self.__dataclass_fields__.items():
        validator = field_info.metadata.get("validator")
        if validator:
            value = getattr(self, field_name)
            if not validator.validate(value):
                raise ValueError(f"❌ Validation échouée pour {field_name} ({value})")

    print("✅ Toutes les validations sont passées avec succès !")
    return True
