
class Rectangle:
    def __init__(self, longueur, largeur):
        # Initialisation du constructeur de la classe Rectangle avec une longueur et une largeur
        self._longueur = longueur
        self._largeur = largeur

    def perimetre(self):
        # Méthode qui revnoie le périmètre du rectangle
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        # Méthode qui renvoie la surface du rectangle
        return self._longueur * self._largeur

    def obtenirLongueur(self):
        # Méthode qui renvoie la longueur
        return self._longueur

    def changerLongueur(self, longueur):
        # Méthode pour modifier la longueur
        self._longueur = longueur

    def obtenirLargeur(self):
        # Méthode qui renvoie la largeur
        return self._largeur

    def changerLargeur(self, largeur):
        # Méthode pour modifer la largeur
        self._largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        # Initialise un objet Parallelepipede avec une longueur, une largeur et une hauteur
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        # Méthode qui renvoie le volume du parallélépipède
        return self.surface() * self.hauteur

    def obtenirHauteur(self):
        # Méthode qui renvoie la hauteur
        return self.hauteur

    def changerHauteur(self, hauteur):
        # Méthode pour modifier la hauteur
        self.hauteur = hauteur


# Exemple d'instanciation de la classe Rectangle
rectangle = Rectangle(5, 4)

# Utilisation des méthodes et affichage des résultats
print("Périmètre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())

# Modification des attributs avec les mutateurs
rectangle.changerLongueur(12)
rectangle.changerLargeur(6)

# Affichage des attributs après modification
print("Nouvelle longueur:", rectangle.obtenirLongueur())
print("Nouvelle largeur:", rectangle.obtenirLargeur())

# Exemple d'instanciation de la classe Parallelepipede
parallelpipede = Parallelepipede(10, 5, 2)

# Utilisation de la méthode volume et affichage du résultat
print("Volume du parallélépipède:", parallelpipede.volume())