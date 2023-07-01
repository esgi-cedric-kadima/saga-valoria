from classe.Character import Character

class Enemy(Character):
    """
    Classe représentant un ennemi dans le jeu.
    Hérite de la classe Character.
    """

    def __init__(self, name, strength, agility):
        """
        Initialise un ennemi avec un nom, une force et une agilité données.
        """
        super().__init__(name, strength, agility)
