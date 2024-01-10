import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        # Surcharge de la méthode aire pour calculer l'aire du rectangle
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        # Surcharge de la méthode aire pour calculer l'aire du cercle
        return round(math.pi * self.radius**2, 2)

# Création d'une instance de la classe Rectangle avec une largeur et une hauteur spécifiques
rectangle = Rectangle(5, 10)

# Création d'une instance de la classe Cercle avec un rayon spécifique
cercle = Cercle(3)

# Appel de la méthode aire pour le rectangle et affichage du résultat
print("L'aire du rectangle est:", rectangle.aire())

# Appel de la méthode aire pour le cercle et affichage du résultat
print("L'aire du cercle est:", cercle.aire())