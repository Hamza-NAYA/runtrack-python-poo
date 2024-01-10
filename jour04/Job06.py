
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        # Affiche les informations générales du véhicule
        print(f"Marque = {self.marque} \nModèle = {self.modele} \nAnnée = {self.annee} \nPrix = {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        # Appelle le constructeur de la classe parente (Vehicule)
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        # Appelle la méthode informationsVehicule de la classe parente (Vehicule)
        super().informationsVehicule()
        # Affiche le nombre de portes de la voiture
        print(f"Nombre de portes = {self.portes}")

    def demarrer(self):
        print("La voiture démarre")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        # Appelle le constructeur de la classe parente (Vehicule)
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        # Appelle la méthode informationsVehicule de la classe parente (Vehicule)
        super().informationsVehicule()
        # Affiche le nombre de roues de la moto
        print(f"Nombre de roues = {self.roues}")

    def demarrer(self):
        print("La moto démarre")

# Instanciation d'un objet Voiture
voiture = Voiture("Mercedes","Classe A", 2020, 18500)

# Appel à la méthode informationsVehicule de la classe Voiture
voiture.informationsVehicule()

# Appel à la méthode demarrer de la classe Voiture
voiture.demarrer()

# Instanciation d'un objet Moto
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)

# Appel à la méthode informationsVehicule de la classe Moto
moto.informationsVehicule()

# Appel à la méthode demarrer de la classe Moto
moto.demarrer()