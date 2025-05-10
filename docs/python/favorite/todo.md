# TODO - Gestionnaire de Favoris CLI

## Objectif
Créer un script CLI interactif pour gérer une liste de favoris (titre + URL), sauvegardés dans un fichier `favoris.json`.

---

## Étapes à réaliser

### [x] Initialisation
- [x] Créer le fichier `favoris.json` s'il n'existe pas
- [x] Charger les données (liste de dicts)
- [x] Gérer les erreurs de chargement JSON (try/except)

### [x] Menu principal
- [x] Afficher les options (ajouter / supprimer / lister / quitter)
- [x] Boucle continue jusqu'à quitter volontairement

### [x] Ajouter un favori
- [x] Demander une URL (vérifier qu'elle commence par http(s)/ftp et contient un `.`)
- [x] Tant qu’elle est invalide, redemander
- [x] Demander un titre (non vide)
- [x] Générer un ID (auto ou UUID)
- [x] Ajouter à la liste
- [x] Sauvegarder dans le JSON

### [x] Supprimer un favori
- [x] Afficher les favoris avec ID
- [x] Demander un ID à supprimer
- [x] Vérifier qu’il existe
- [x] Supprimer + sauvegarder

### [x] Lister les favoris
- [x] Afficher tous les favoris avec ID, titre, et URL (format lisible)




