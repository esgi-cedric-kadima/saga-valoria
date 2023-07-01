class AbstractItem:
    """
    Classe abstraite représentant un objet du jeu.
    """

    def __init__(self, name):
        """
        Initialise un objet avec un nom donné.
        """
        self.name = name

    def use(self):
        """
        Méthode abstraite pour utiliser l'objet.
        Doit être implémentée par les sous-classes.
        """
        pass

    def usable(self):
        """
        Méthode abstraite pour vérifier si l'objet peut être utilisé.
        Doit être implémentée par les sous-classes.
        """
        pass
