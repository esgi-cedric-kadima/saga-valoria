from ItemClass import ItemClass
from PlayerClass import Player
from EnemyClass import Enemy
class SwordItemClass(ItemClass):

    def __init__(self, name, damage, durability):
        super().__init__(name)
        self.damage = damage
        self.durability = durability

    def use(self, character, enemy):
        if(self.usable()):
            if(character.strength + self.damage > enemy.strength):
                self.durability -= 1
                return True
            self.durability -= 1
            return False
        return False

    def usable(self):
        if(self.durability > 0):
            return True
        return False