from classe.Character import Character

class Player(Character):
    def __init__(self, name, health, strength, agility, intelligence):
        super().__init__(name, strength, agility)
        self.health = health
        self.intelligence = intelligence
        self.items = []

    def attack(self, enemy):
        return True

    def defence(self, enemy):
        return True

    def escape(self, enemy):
        return True

    def is_dead(self):
        return self.health <= 0

    def add_item(self, item):
        self.items.append(item)

    def use_item(self,):
        pass

    def has_item(self, itemName):
        return self.find_item(itemName) != None

    def find_item(self, itemName):
        return None
