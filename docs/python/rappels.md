Architecture de modèle dans Todol-Archi

Ce fichier décrit la stratégie architecturale adoptée pour structurer les objets de données dans le projet. Elle repose sur une distinction claire entre modèle de base (core) et modèle étendu (riche/metier).


---

💡 Pourquoi deux versions d'un modèle ?

Cette stratégie permet de :

Clarifier les responsabilités

Favoriser la testabilité

Séparer les couches (métier, UI, base de données)

Faciliter les extensions sans casser le code existant



---

🔢 Modèle de base : TaskCore

Objectifs :

Définir les champs à stocker / transmettre

Centraliser le typage

Poser les méthodes de conversion standard


Contenu :

@dataclass
class TaskCore:
    id: Optional[int] = None
    title: str
    completed: bool = False
    category: str
    expiration: str
    notes: str = ""

    def to_dict(self): ...
    @classmethod
    def from_dict(cls, data): ...
    def label(self) -> str: return ""  # Hook d'extension possible

Ce qu'on n'y met pas :

Pas d'import vers core, ui, helpers

Pas de logique métier complexe

Pas de validation avancée



---

📊 Modèle étendu : Task

Objectifs :

Ajouter la logique métier

Créer des helpers de transformation

Intégrer les dépendances utiles (UI, helpers, etc.)


Contenu :

class Task(TaskCore):
    def label(self) -> str:
        return status_label(self.completed)

    def __str__(self): ...
    def __repr__(self): ...

    def to_dict(self, exclude=None):
        return dataclass_to_dict(self, exclude)

Cas d'usage :

UI (affichage)

DB (insertion / update / export)

Intégration avec les tests



---

🎓 Exemple OOP classique :

Comme dans les exercices OOP :

class Animal:
    def crier(self):
        pass

class Chien(Animal):
    def crier(self):
        return "Wouf"

De même ici :

class TaskCore:
    def label(self): return ""

class Task(TaskCore):
    def label(self): return "ROCKED" if self.completed else "PENDING"


---

🎯 Quand créer un modèle "core" ?

Quand tu veux une version pure, sans logique extérieure

Quand le modèle est appelé depuis des tests, ou des scripts automatisés

Quand tu veux définir un "contrat" de données


✅ Avantages dans Todol-Archi

Les tests peuvent utiliser TaskCore sans UI ni DB

L’UI peut utiliser Task directement, tout en gardant l’objet propre

Le projet est plus modulaire, plus facile à maintenir



---

> 📍 Objectif : garder un modèle simple, robuste, et prêt à être enrichi sans complexifier l'ensemble



