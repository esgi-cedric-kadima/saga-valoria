class Character:
    def __init__(self, name, health, strength, agility, intelligence):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

        def attack(self):
            print(f"{self.name} attaque avec une force de {self.strength}!")

        def defend(self):
            print(f"{self.name} se défend avec une agilité de {self.agility}!")

        def use_ability(self):
            print(f"{self.name} utilise une capacité avec une intelligence de {self.intelligence}!")
