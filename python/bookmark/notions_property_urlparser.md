🧱 Structure de base
```python
from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class Bookmark:
    title: str
    url: str

    @property
    def domain(self) -> str:
        """Retourne le domaine (ex: openai.com) extrait de l’URL"""
        parsed = urlparse(self.url)
        return parsed.netloc.removeprefix("www.")

    @property
    def is_secure(self) -> bool:
        """Indique si l’URL utilise HTTPS"""
        return self.url.startswith("https://")


# --- zone de test minimaliste ---

def main():
    fav = Bookmark(title="ChatGPT", url="https://chat.openai.com")
    print(f"📌 {fav.title}")
    print(f"🔗 Domaine : {fav.domain}")
    print(f"🔒 Connexion sécurisée : {fav.is_secure}")


if __name__ == "__main__":
    main()
```

✅ Ce que tu peux tester en IPython :

```python
from bookmark import Bookmark
f = Bookmark("Seb test", "https://docs.python.org/3/")
f.domain       # → docs.python.org
f.is_secure    # → True
```
Tu peux aussi tester une URL non sécurisée pour voir la différence :
```python
Bookmark("Unsecure", "http://example.com").is_secure  # False
```

🧠 Ce que tu observes ici :

    @property transforme une méthode en attribut accessible naturellement

    Tu n’écris pas f.domain() → tu accèdes à f.domain, comme si c’était un champ réel

    Tu encapsules une logique de lecture sans avoir à changer l’interface

✅ Le trio magique : @property, @<prop>.setter, @<prop>.deleter
1. @property → getter

@property
def domain(self) -> str:
    ...

→ Accès en lecture : f.domain
2. @domain.setter → setter

@domain.setter
def domain(self, value: str):
    ...

→ Permet de faire : f.domain = "nouveau.com"
(et exécute la logique que tu définis dedans)
3. @domain.deleter → deleter

@domain.deleter
def domain(self):
    ...

→ Permet de faire : del f.domain
🧠 Important :

Tu n'es pas obligé de tout définir.
Tu peux très bien avoir juste un getter (comme dans notre Bookmark)
→ la propriété est alors en lecture seule (ce qui est parfait pour des champs calculés).

------------------------------------

✅ À quoi sert @property vraiment ?

    @property transforme une méthode en un attribut.

Donc tu écris une méthode…
Mais tu l’utilises comme un champ :

class Bookmark:
    @property
    def domain(self):
        return self.url.split("/")[2]

b = Bookmark()
print(b.domain)  # 👈 pas besoin d'appeler b.domain()

🧠 Tu l’utilises quand…
1. Tu veux encapsuler une donnée dérivée :

Exemples :

    is_secure → dépend de url

    domain → est extrait de url

    age → est calculé à partir de birthdate

👉 Ce sont des propriétés calculées à partir de champs internes.
2. Tu veux contrôler l’accès à un attribut :

Tu veux permettre :

    De lire l’attribut (@property)

    De le modifier mais avec validation (@setter)

    Ou d’empêcher la modification (en ne mettant pas de setter)

3. Tu veux préserver ton interface

Tu avais au départ :

def get_domain(self):
    return ...

→ Si tu passes à :

@property
def domain(self):
    ...

Tu ne changes aucune ligne de code ailleurs → obj.domain fonctionne dans les deux cas
Mais maintenant, tu peux facilement :

    changer la logique

    ajouter un setter plus tard

    stocker un cache interne si besoin

❌ Quand ce n’est pas adapté
1. Si c’est une vraie action, pas une donnée

def save_to_json(self):
    ...

→ Pas une propriété ! Tu fais une action → garde ça comme méthode.
2. Si c’est coûteux / lent et ne devrait pas s’exécuter à chaque appel

Une propriété est automatiquement exécutée à chaque accès
→ donc évite si ça fait une requête HTTP, un calcul lourd, etc.
3. Si l’utilisateur doit comprendre qu’il y a une logique derrière

Par exemple, si un delete_account() fait un appel API → mieux vaut une méthode explicite qu’un @property.
📌 En résumé
Situation	Faut-il utiliser @property ?
Lecture d’un attribut dérivé (ex : domaine)	✅ Oui
Vérifier une condition sur l’objet (is_valid)	✅ Oui
Action explicite (enregistrer, exporter)	❌ Non
Long traitement (requête, algo lourd…)	❌ Non
Besoin de validation à la modification	✅ Oui (avec @setter)
Besoin d’un champ en lecture seule	✅ Oui
“on fait un @property, car on sait qu’à un moment on aura peut-être besoin de vérifier ou transformer la donnée”