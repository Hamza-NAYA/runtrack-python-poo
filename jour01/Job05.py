
class Point:
    def __init__(self, x, y):
        # Initialisation du constructeur de la classe Point avec des coordonnées x et y fournies en paramètres
        self.horizontal = x  # Attribut pour stocker la coordonnée x en tant que horizontal
        self.vertical = y  # Attribut pour stocker la coordonnée y en tant que vertical

    def afficherLesPoints(self):
        # Méthode qui affiche les coordonnées du point
        print(f"Les coordonnées sont: ({self.horizontal};{self.vertical})")

    def afficherX(self):
        # Méthode qui affiche la coordonnée horizontale du point
        print(f"Coordonnée x: {self.horizontal}")

    def afficherY(self):
        # Méthode qui affiche la coordonnée verticale du point
        print(f"Coordonnée y: {self.vertical}")

    def changerX(self, new_value_x):
        # Méthode pour changer la coordonnée horizontale du point
        self.horizontal = new_value_x

    def changerY(self, new_value_y):
        # Méthode pour changer la coordonnée verticale du point
        self.vertical = new_value_y

# Création d'une variable test pour la classe Point avec des coordonnées 12 pour horizontal et 3 pour vertical
test = Point(12, 3)

# test des différentes méthodes pour afficher, changer et afficher à nouveau les coordonnées du point
test.afficherLesPoints()
test.afficherX()
test.afficherY()
test.changerX(1)
test.changerY(2)
test.afficherLesPoints()