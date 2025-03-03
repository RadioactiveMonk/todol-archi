"""🔥 Exercices fonctionnels"""


# ✅ Remplacement de voyelles: translate plus performatant que regex,
# mais moins flexible.
def replace_vowels(txt: str):
    txt = txt.lower()
    vowels, new_chars = "aeuioy", "@3v!0j"
    txttable = str.maketrans(vowels, new_chars)

    return txt.translate(txttable)


leet = replace_vowels("Hello WoRld")
print(leet)


# ✅ Inverser les mots d'une phrase. ✅ .join() est la meilleure approche
# pour concaténer proprement une liste de strings.
def reverse_words(txt: str):
    return " ".join(txt.split()[::-1])


print(reverse_words("Python est puissant"))


# ✅ Trouver le mot le plus fréquent d'un texte. Depuis python 3.9,
# | permet de remplacer Union et optional. Meilleur approche.
from collections import Counter


def most_frequent(txt: str, ignore_case: bool = False) -> str | None:

    if ignore_case:
        text = txt.lower().split()
    else:
        text = txt.split()

    count = Counter(text)
    most_common = count.most_common(1)
    return most_common[0][0]


print(most_frequent("chat chien chat oiseau chien chat"))


# ✅ sorted(list, key=len).
# key permet de choisir on fonction de quoi on trie !!
word_list = ["Yo", "pepe", "how's", "it", "going so far"]
print(sorted(word_list, key=len))  # trie en fonction de la longueur du mot


# ✅ Trouver le nombre manquant dans une liste ordonnée
# set.difference permet de faire la difference avec un autre type de structure (liste, tupple, ..)
def find_int(data: list):
    full_set = set(range(data[0], data[-1] + 1))
    diff = full_set.difference(data)
    return diff.pop()


data = [1, 2, 3, 5]
print(find_int(data))


# ✅ Vérifie si palindrome
def is_palindrom(object: int | str) -> bool:
    return str(object) == str(object)[::-1]


print(is_palindrom("kayak"))

from collections import Counter

""" 🔥🔥 En Python, les classes sont super utiles quand :

    On veut garder un état (ex: un compteur, une base de données en mémoire).
    On veut ajouter des fonctionnalités facilement (ex: reset() ou get_most_common()).
    On veut encapsuler la logique et éviter de polluer le code avec des variables globales."""


# ✅ Créer un compteur qui garde en mémoire le nombre d’occurrences des objets qu’on lui ajoute.
class CounterClass:
    def __init__(self):
        self.counts = Counter()

    def add(self, item: str) -> None:
        """Ajoute un élément au compteur."""
        self.counts[item] += 1

    def reset(self) -> None:
        """Réinitialise le compteur."""
        self.counts.clear()

    def most_common(self, n: int = 1) -> list[tuple[str, int]]:
        """Retourne les `n` éléments les plus fréquents."""
        return self.counts.most_common(n)


# Test
counter = CounterClass()
counter.add("pomme")
counter.add("banane")
counter.add("pomme")
counter.add("orange")
counter.add("pomme")

print(counter.counts)  # ➝ {'pomme': 3, 'banane': 1, 'orange': 1}
print(counter.most_common())  # ➝ [('pomme', 3)]
counter.reset()
print(counter.counts)  # ➝ {}
