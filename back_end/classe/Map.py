import random

class Map:
    """
    Classe représentant la carte du jeu.
    """

    def __init__(self, lines, columns):
        """
        Initialise une carte avec un nombre donné de lignes et de colonnes.
        Chaque case de la carte est initialisée à None.
        """
        self.grid = []
        for i in range(lines):
            row = []
            for j in range(columns):
                row.append(None)
            self.grid.append(row)

    def populate(self, events):
        """
        Peuple la carte avec des événements aléatoires à partir d'une liste donnée.
        Chaque case de la carte reçoit un événement aléatoire.
        La case en haut à gauche (ligne 0, colonne 0) est laissée vide (None).
        """
        for line in range(len(self.grid)):
            for column in range(len(self.grid[line])):
                if line == 0 and column == 0:
                    self.grid[line][column] = None
                else:
                    self.grid[line][column] = random.choice(events)
