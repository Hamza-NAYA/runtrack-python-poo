# Importation du module math pour utiliser la veleur de pi pour le calcul de l'aire et de la circongerence du cercle
import math

class Cercle:
    def __init__(self, rayon):
        # Initialisation du constructeur de la classe Cercle avec le rayon fourni en paramètre
        self.radius = rayon  # Attribut pour stocker le rayon du cercle en tant que radius

    def changerRayon(self, nouveau_rayon):
        # Méthode pour changer le rayon du cercle
        self.radius = nouveau_rayon

    def afficherInfos(self):
        # Méthode qui affiche le rayon du cercle
        print(f"Rayon du cercle : {self.radius}")

    def circonference(self):
        # Méthode qui calcule et renvoie la circonférence du cercle arrondie à deux chiffres apres la virgule
        return round(2 * math.pi * self.radius, 2)

    def aire(self):
        # Méthode qui calcule et renvoie l'aire du cercle arrondie à deux chiffres apres la virgule
        return round(math.pi * self.radius ** 2, 2)

    def diametre(self):
        # Méthode qui calcule et renvoie le diamètre du cercle
        return 2 * self.radius

# Création de deux cercles de la classe Cercle avec des rayons différents
cercle_1 = Cercle(12)
cercle_2 = Cercle(3)

# Affichage des informations du premier cercle et calcul de la circonférence, du diamètre et de l'aire.
print("\nCercle 1:")
cercle_1.afficherInfos()
print("Circonférence :", cercle_1.circonference())
print("Diamètre :", cercle_1.diametre())
print("Aire :", cercle_1.aire())


# Affichage des informations du deuxième cercle et calcul de la circonférence, du diamètre et de l'aire.
print("\nCercle 2:")
cercle_2.afficherInfos()
print("Circonférence :", cercle_2.circonference())
print("Diamètre :", cercle_2.diametre())
print("Aire :", cercle_2.aire())