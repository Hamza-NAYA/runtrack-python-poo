
class Rectangle:
    def __init__(self, longueur, largeur):
        # Initialisation du constructeur de la classe Rectangle avec longueur et largeur fourni en paramètres
        self.__length = longueur # Attribut pour stocker la longueur du rectangle en tant que length
        self.__width = largeur # Attribut pour stocker la largeur du rectangle en tant que width

    def obtenirLongueur(self):
        # Méthode qui renvoie la longueur du rectangle
        return self.__length

    def obtenirLargeur(self):
        # Méthode qui renvoie la largeur du rectangle
        return self.__width

    def modifierLongueur(self, nouvelle_longueur):
        # Méthode pour modifier la longueuer du rectangle
        self.__length = nouvelle_longueur

    def modifierLargeur(self, nouvelle_largeur):
        # Méthode pour modifier la largeur du rectangle
        self.__width = nouvelle_largeur

# Création d'un rectangle avec les valeurs initiales
rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales
print(f"\nLongueur initiale du rectangle: {rectangle.obtenirLongueur()}")
print(f"Largeur initiale du rectangle: {rectangle.obtenirLargeur()}\n")

# Modification des valeurs
rectangle.modifierLongueur(12)
rectangle.modifierLargeur(3)

# Affichage des nouvelles valeurs
print(f"Nouvelle longueur du rectangle: {rectangle.obtenirLongueur()}")
print(f"Nouvelle largeur du rectangle: {rectangle.obtenirLargeur()}\n")