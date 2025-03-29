


# -------------------------------
# Section : Vocabulaire fondamental
# -------------------------------

# Helper :
# Une fonction utilitaire, modulaire, réutilisable dans un projet.
# Exemple : def image_to_ascii(path): ...
# On l'appelle depuis un autre module ou script, mais elle ne fait rien seule.

# Script :
# Un fichier Python autonome, exécutable depuis un terminal.
# Il exécute une tâche spécifique, souvent via argparse.
# Exemple : asciiify.py qui prend une image et affiche du texte.

# Rappel :
# Un helper = une fonction
# Un script = une intention (exécutable indépendamment)


# -------------------------------
# Scripts à venir (idées à développer plus tard)
# -------------------------------

# - Script CLI interactif pour chercher/remplacer du texte dans des fichiers
#   > Demande du texte à chercher, du remplacement, d’un dossier cible
#   > Affiche les résultats trouvés, demande confirmation avant application
#   > Un grep/sed Pythonisé avec prévisualisation et sécurité (dry-run, backup…)

# - Webscraper avec requests + BeautifulSoup
#   > Récupérer les titres, articles ou données depuis un site
#   > Exporter les résultats dans un fichier texte ou CSV
#   > Base solide pour automatiser des veilles, extractions, ou traitements


# -------------------------------
# Mini section : Pause / Tempo avec time.sleep()
# -------------------------------

# Exemple simple : pause entre deux actions
# import time
# print("Début")
# time.sleep(2)  # pause 2 secondes
# print("Fin")

# Exemple cool : compteur visuel
# for i in range(5, 0, -1):
#     print(f"Départ dans {i}...")
#     time.sleep(1)
# print("Go !")
