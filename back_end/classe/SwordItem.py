from classe.Item import AbstractItem
from classe.Player import Player
class SwordItem(AbstractItem):

    def __init__(self, name, strength):
        super().__init__(name)
        self.strength = strength

    def use(self, character):
        character.strength += self.strength