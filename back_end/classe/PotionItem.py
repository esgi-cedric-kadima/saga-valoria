from classe.Item import AbstractItem
from classe.Player import Player

class PotionItem(AbstractItem):
    """
    Classe représentant un objet de type potion dans le jeu.
    Hérite de la classe AbstractItem.
    """

    def __init__(self, health):
        """
        Initialise une potion avec une quantité de santé donnée.
        Appelle le constructeur de la classe mère (AbstractItem) pour initialiser le nom de la potion.
        """
        super().__init__('Potion de vie')
        self.health = health

    def use(self, character):
        """
        Utilise la potion sur un personnage donné.
        Ajoute la quantité de santé de la potion à la santé du personnage.
        """
        character.health += self.health

    def convert_to_dict(self):
        """
        Convertit la potion en dictionnaire.
        """
        return {
            "class": self.__class__.__name__,
            "name": self.name,
            "health": self.health,
        }