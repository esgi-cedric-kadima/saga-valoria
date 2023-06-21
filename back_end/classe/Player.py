from classe.Character import Character

class Player(Character):
    def __init__(self, name, health, strength, agility, intelligence):
        super().__init__(name, strength, agility)
        self.health = health
        self.intelligence = intelligence
        self.items = []

        def attack(self, enemy):
            print("You attack the enemy!")

        def defence(self, enemy):
            print("You defend yourself!")

        def escape(self, enemy):
            print("You try to escape!")

        def is_dead(self):
            return self.health <= 0

        def add_item(self, item):
            self.items.append(item)

        def use_item(self):
            pass
