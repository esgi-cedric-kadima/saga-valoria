class Character:
    """
    Classe représentant un personnage du jeu.
    """

    def __init__(self, name, strength, agility):
        """
        Initialise un personnage avec un nom, une force et une agilité données.
        """
        self.name = name
        self.strength = strength
        self.agility = agility

    def convert_to_dict(self):
        """
        Convertit le personnage en dictionnaire.
        """
        return {
            "name": self.name,
        }
