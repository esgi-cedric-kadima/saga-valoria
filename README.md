# Auteur
Cédric KADIMA & Alexandre Arod

# saga-valoria
Jeu RPG Tour partout. On joue un aventurier qui doit traverser un donjon, à chaque tour / déplacement il est confronté à un évènement différent, plusieurs actions est disponible à un évènement qui peuvent influencer le jeu / le joueur.  La map est un système de grille ou l’objectif est d’aller à un point A à un point B.

# Back-end requirements
- [X] Python 3.11
- Python packages to install not in the standard library:
  - [X] Websockets -> `pip install websockets`

# Back-end test
- Start server before test,
- cd back-end
- python game.py
- cd tests
- python -m unittest

# Utilisation
 Démarrer le socket : python game.py et lancer la page html game.html sur le navigateur

# Depot git
https://github.com/esgi-cedric-kadima/saga-valoria

# Les choix techniques
 - Python pour le back-end pour ca simplicité et sa rapidité de réalisation.
 - Javascript native pour le front-end pour communiquer avec le back-end en websocket.

# Les choix de réalisations de tests
    - Coté back-end on a majoritairement tester, la classe player car elle détient des fonctionnalités cruciales au jeu. On a aussi tester le socket du jeu notemment en y simulant une partie de jeu.
