
class Personnage:
    def __init__(self, x, y):
        # Initialisation du constructeur de la classe Personnage avec des coordonnées x et y fournies en paramètres
        self.horizontal = x  # Attribut pour stocker la coordonnée x du personnage en tant que horizontal
        self.vertical = y  # Attribut pour stocker la coordonnée y du personnage en tant que vertical

    def gauche(self):
        # Méthode qui déplace le personnage d'une unité vers la gauche
        self.horizontal -= 1

    def droite(self):
        # Méthode qui déplace le personnage d'une unité vers la droite
        self.horizontal += 1

    def bas(self):
        # Méthode qui déplace le personnage d'une unité vers le bas
        self.vertical -= 1

    def haut(self):
        # Méthode qui déplace le personnage d'une unité vers le haut
        self.vertical += 1

    def position(self):
        # Méthode qui renvoie les coordonnées actuelles du personnage
        return (self.horizontal, self.vertical)

# Création d'une variable test de la classe Personnage avec une position initiale
test = Personnage(0, 0)

# Affichage de la position initiale du personnage
print("Position initiale :", test.position())

# Appel des méthodes de déplacement pour déplacer le personnage 3 fois vers la droite, 1 fois vers le bas et 1 fois vers la gauche
test.droite()
test.droite()
test.droite()
test.bas()
test.gauche()

# Affichage de la nouvelle position du personnage
print("Nouvelle position :", test.position())