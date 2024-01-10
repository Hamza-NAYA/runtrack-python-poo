
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

# Création d'une instance de la classe Rectangle avec une largeur et une hauteur spécifiques
rectangle = Rectangle(5, 10)

# Appel de la méthode aire de la classe Rectangle et affichage du résultat
print("L'aire du rectangle est:", rectangle.aire())