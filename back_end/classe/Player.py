from classe.Character import Character

class Player(Character):
    """
    Classe représentant le joueur dans le jeu.
    Hérite de la classe Character.
    """

    MAX_DAMAGE = 25

    def __init__(self, name, health, strength, agility, intelligence):
        """
        Initialise un joueur avec un nom, une santé, une force, une agilité et une intelligence donnés.
        """
        super().__init__(name, strength, agility)
        self.health = health
        self.intelligence = intelligence
        self.items = []

    def attack(self, enemy):
        """
        Attaque un ennemi.
        Si la force du joueur est supérieure à celle de l'ennemi, l'attaque réussit.
        Sinon, le joueur perd de la santé en fonction de la différence de force.
        Retourne True si l'attaque réussit, False sinon.
        """
        if self.strength > enemy.strength:
            return True
        self.health -= enemy.strength - self.strength
        return False

    def defence(self, enemy):
        """
        Défend contre une attaque d'ennemi.
        Le joueur perd de la santé en fonction de la force de l'ennemi, avec une limite définie par MAX_DAMAGE.
        Si le joueur meurt, retourne False, sinon retourne True.
        """
        self.health -= min(self.MAX_DAMAGE, enemy.strength)
        if self.is_dead():
            return False
        return True

    def escape(self, enemy):
        """
        Tente de s'échapper d'un combat avec un ennemi.
        Si l'agilité du joueur est supérieure à celle de l'ennemi, l'échappée réussit.
        Retourne True si l'échappée réussit, False sinon.
        """
        if self.agility > enemy.agility:
            return True
        self.health = 0
        return False

    def is_dead(self):
        """
        Vérifie si le joueur est mort.
        Retourne True si le joueur est mort (santé inférieure ou égale à 0), False sinon.
        """
        return not (self.health > 0)

    def add_item(self, item):
        """
        Ajoute un objet à la liste des objets possédés par le joueur.
        """
        self.items.append(item)

    def use_item(self, item):
        """
        Utilise un objet de la liste des objets possédés par le joueur.
        Si l'objet est trouvé dans la liste, il est utilisé sur le joueur et retiré de la liste.
        """
        if self.has_item(item.name):
            item.use(self)
            self.items.pop(self.find_item(item.name))

    def has_item(self, itemName):
        """
        Vérifie si le joueur possède un objet spécifié dans sa liste d'objets.
        Retourne True si l'objet est trouvé, False sinon.
        """
        return self.find_item(itemName) is not None

    def find_item(self, itemName):
        """
        Recherche un objet spécifié dans la liste d'objets du joueur.
        Retourne l'index de l'objet dans la liste s'il est trouvé, None sinon.
        """
        for i in range(len(self.items)):
            if self.items[i].name == itemName:
                return i
        return None

    def convert_to_dict(self):
        """
        Convertit l'objet en dictionnaire.
        """
        return {
            'name': self.name,
            'health': self.health,
            'strength': self.strength,
            'agility': self.agility,
            'intelligence': self.intelligence,
            'items': [item.convert_to_dict() for item in self.items]
        }