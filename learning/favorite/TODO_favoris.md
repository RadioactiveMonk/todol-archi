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

### [ ] Ajouter un favori
- [x] Demander une URL (vérifier qu'elle commence par http(s)/ftp et contient un `.`)
- [ ] Tant qu’elle est invalide, redemander
- [ ] Demander un titre (non vide)
- [ ] Générer un ID (auto ou UUID)
- [ ] Ajouter à la liste
- [ ] Sauvegarder dans le JSON

### [ ] Supprimer un favori
- [ ] Afficher les favoris avec ID
- [ ] Demander un ID à supprimer
- [ ] Vérifier qu’il existe
- [ ] Supprimer + sauvegarder

### [ ] Lister les favoris
- [ ] Afficher tous les favoris avec ID, titre, et URL (format lisible)



📚 Refactoring Avancé à venir

Une fois le script finalisé (toutes les fonctions fonctionnelles), il servira de base pour explorer des notions avancées Python dans un contexte simple et maîtrisé. L’objectif sera d’apprendre à :

- [ ] intégrer des helpers (is_valid_url(), print_favori()...)

- [ ] tester des notions avancées de Python :

- [ ] @property (sur une version dataclass d’un favori)

- [ ] *args / **kwargs (helpers ou print dynamiques)

- [ ] yield pour générer ligne par ligne (ex : export CSV paresseux)

- [ ] @lru_cache pour du cache temporaire

- [ ] defaultdict pour regrouper des favoris (par domaine, par type…)

- [ ] := (walrus) dans une boucle interactive

- [ ] création d’un context manager personnalisé

- [ ] apprendre à structurer un script via des modules (cli.py, helpers.py, storage.py…)

🎯 Le but : s’entraîner sur ce script pour être prêt à refactoriser Todol-Archi avec un vrai bagage.

## Bonus (facultatif)
- [ ] Tri par titre
- [ ] Export CSV
- [ ] Confirmation de suppression
- [ ] Sauvegarde automatique de backup (favoris_backup.json)
- [ ] Passer à argparse plus tard pour usage en CLI directe



