def execute(self, action: str, *args, **kwargs):
    """Exécute une action sur la base de données via dict dispatch."""
    if action not in self.actions:
        raise ValueError(f"Action inconnue : {action}")
    return self.actions[action](*args, **kwargs)
