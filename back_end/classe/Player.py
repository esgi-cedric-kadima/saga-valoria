from classe.Character import Character

class Player(Character):

    MAX_DAMAGE = 25

    def __init__(self, name, health, strength, agility, intelligence):
        super().__init__(name, strength, agility)
        self.health = health
        self.intelligence = intelligence
        self.items = []

    def attack(self, enemy):
        if(self.strength > enemy.strength):
            return True
        self.health -= enemy.strength - self.strength
        return False


    def defence(self, enemy):
        self.health -= min(self.MAX_DAMAGE, enemy.strength)
        if(self.is_dead()):
            return False
        return True

    def escape(self, enemy):
        if(self.agility > enemy.agility):
            return True
        return False

    def is_dead(self):
        return not(self.health > 0)

    def add_item(self, item):
        self.items.append(item)

    def use_item(self, item):
        if self.has_item(item.name):
            item.use(self)
            self.items.pop(self.find_item(item.name))

    def has_item(self, itemName):
        return self.find_item(itemName) != None

    def find_item(self, itemName):
        for i in range(len(self.items)):
            if self.items[i].name == itemName:
                return i
        return None
