from classe.Item import AbstractItem
from classe.Player import Player
class PotionItem(AbstractItem):

    def __init__(self, health):
        super().__init__('Potion de vie')
        self.health = health

    def use(self, character):
        character.health += self.health