
class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        # Initialisation du constructeur de la classe Voiture avec marque, modele, année et kilométrage fournis en paramètre
        self.__brand = marque
        self.__modele = modele
        self.__year = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Assesseurs et mutateurs pour chaque attribut
    def obtenirMarque(self):
        # Méthode qui renvoie la marque de la voiture
        return self.__brand

    def modifierMarque(self, nouvelle_marque):
        # Méthode pour modifier la marque de la voiture
        self.__brand = nouvelle_marque

    def obtenirModele(self):
        # Méthode qui renvoie le modele de la voiture
        return self.__modele

    def modifierModele(self, nouveau_modele):
        # Méthode pour modifier le modele de la voiture
        self.__modele = nouveau_modele

    def obtenirAnnee(self):
        # Méthode qui renvoie l'année de la voiture
        return self.__year

    def modifierAnnee(self, nouvelle_annee):
        # Méthode pour modifier l'année de la voiture
        self.__year = nouvelle_annee

    def obtenirKilometrage(self):
        # Méthode qui renvoie le kilometrage de la voiture
        return self.__kilometrage

    def modifierKilometrage(self, nouveau_kilometrage):
        # Méthode pour modifier le kilometrage de la voiture
        self.__kilometrage = nouveau_kilometrage

    def obtenirEnMarche(self):
        # Méthode qui renvoie True ou False si la voiture est en marche
        return self.__en_marche

    def verifier_plein(self):
        # Méthode privée pour vérifier le niveau du réservoir
        return self.__reservoir > 5

    def demarrer(self):
        # Méthode pour démarrer la voiture
        if self.verifier_plein():
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas")

    def arreter(self):
        # Méthode pour arrêter la voiture
        self.__en_marche = False
        print("La voiture s'arrête\n")

# Creation d'une voiture avec la classe Voiture
voiture = Voiture("Volkswagen", "Touran", 2016, 80025)

# Affichage des informations initiales
print(f"\nMarque : {voiture.obtenirMarque()}")
print(f"Modèle : {voiture.obtenirModele()}")
print(f"Année : {voiture.obtenirAnnee()}")
print(f"Kilométrage : {voiture.obtenirKilometrage()}")
print(f"En marche : {voiture.obtenirEnMarche()}\n")

# Démarrage de la voiture (le réservoir est suffisamment plein)
voiture.demarrer()

# Arrêt de la voiture
voiture.arreter()