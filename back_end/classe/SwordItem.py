from classe.Item import AbstractItem
from classe.Player import Player

class SwordItem(AbstractItem):
    """
    Classe représentant un objet de type épée dans le jeu.
    Hérite de la classe AbstractItem.
    """

    def __init__(self, name, strength):
        """
        Initialise une épée avec un nom et une force donnés.
        Appelle le constructeur de la classe mère (AbstractItem) pour initialiser le nom de l'épée.
        """
        super().__init__(name)
        self.strength = strength

    def use(self, character):
        """
        Utilise l'épée sur un personnage donné.
        Ajoute la force de l'épée à la force du personnage.
        """
        character.strength += self.strength

    def convert_to_dict(self):
        """
        Convertit l'épée en dictionnaire.
        """
        return {
            "class": self.__class__.__name__,
            "name": self.name,
            "strength": self.strength,
        }