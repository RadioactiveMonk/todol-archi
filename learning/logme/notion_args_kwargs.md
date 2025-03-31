# IPython:

```python
In [3]: log("Seb", "Utilisateur", sep= " | ", prefix="[INFO]", upper=True)
[INFO] SEB | UTILISATEUR
```

✅ Ce que tu pratiques ici :
Élément	Ce que tu apprends
*args	Récupérer une suite d’éléments dynamiques (chaînes, nombres, objets…)
**kwargs	Créer un système d’options souple et élégant
.get()	Fournir des valeurs par défaut
print()	Gérer le formatage à la main (sep, end)

🧠 Démarche mentale pour construire une fonction avec *args / **kwargs

🎯 Étape 1 : Quel est l’objectif de cette fonction ?
```
    Je veux afficher un message flexible, avec plusieurs morceaux, et des options de personnalisation.
```

🔩 Étape 2 : Quels types d’inputs je veux gérer ?

a) Des morceaux de message (texte brut, variable, etc.)

→ J’en veux autant que je veux → donc : *args ✅

log("Erreur", "serveur", "offline", "dans 5min")

b) Des options de style : séparateur, majuscules, etc.

→ Ce sont des options nommées, parfois omises → donc : **kwargs ✅
```python
log(..., sep=" - ", upper=True)
```

🧱 Étape 3 : Je découpe la fonction en 3 blocs
🔹 Bloc 1 : Préparer les options (kwargs)

```python
sep = kwargs.get("sep", " ")
prefix = kwargs.get("prefix", "")
upper = kwargs.get("upper", False)
end = kwargs.get("end", "\n")
```

🧠 “Je veux que l’utilisateur puisse personnaliser, mais s’il ne précise rien, je garde un comportement par défaut.”

→ Ici je construis l’environnement du message (son format)

🔹 Bloc 2 : Construire le message principal (args)

message = sep.join(str(arg) for arg in args)
if upper:
    message = message.upper()

🧠 “Je transforme les morceaux args en texte final, en tenant compte du style (uppercase, sep, etc.)”

→ Je construis le contenu à afficher
🔹 Bloc 3 : Afficher le tout

```python
print(f"{prefix}{message}", end=end)
```

🧠 “Je combine mon environnement (prefix, suffix) + message final.”

→ J’affiche le résultat visuel final


💥 Résumé ultra clair :

Étape	But	Code
1	Gérer les options	kwargs.get(...)
2	Construire le message	join(args) + .upper()
3	Afficher proprement	print() avec prefix, end


🧠 Et le mindset général :

    🧱 “Je veux une fonction flexible → donc je sépare la structure (args) et les options (kwargs)”
    🔁 “Je garde les comportements par défaut, mais je laisse la porte ouverte à la customisation”
    🧪 “Chaque bloc est testable ou modifiable indépendamment”