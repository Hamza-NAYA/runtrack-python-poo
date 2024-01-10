
class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        # Initialisation du constructeur de la classe Livre avec titre, auteur et nombres_pages fournies en paramètres
        self.__title = titre # Attribut pour stocker le titre du livre en tant que title
        self.__author = auteur # Attribut pour stocker l'auteur du livre en tant que author
        self.__pages_number = nombre_pages # Attribut pour stocker le nombre_pages du livre en tant que pages_number
        self.__disponible = True

    def obtenirTitre(self):
        # Méthode qui renvoie le titre du livre
        return self.__title

    def obtenirAuteur(self):
        # Méthode qui renvoie l'auteur du livre
        return self.__author

    def obtenirNombrePages(self):
        # Méthode qui renvoie le nombre de pages du livre
        return self.__pages_number

    def modifierTitre(self, nouveau_title):
        # Méthode pour modifier le titre du livre
        self.__title = nouveau_title

    def modifierAuteur(self, nouveau_author):
        # Méthode pour modifier l'auteur du livre
        self.__author = nouveau_author

    def modifierNombrePages(self, nouveau_pages_number):
        # Méthode pour modifier le nombre de pages du livre
        # Vérification que le nombre de pages est un entier positif
        if isinstance(nouveau_pages_number, int) and nouveau_pages_number > 0:
            self.__pages_number = nouveau_pages_number
        else:
            print("Erreur: Le nombre de pages doit être un nombre entier positif")

    def verification(self):
        # Méthode pour vérifier si le livre est disponible
        return self.__disponible

    def emprunter(self):
        # Méthode pour emprunter le livre
        if self.verification():
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt")

    def rendre(self):
        # Méthode pour rendre le livre
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Le livre est déjà disponible")

# Création d'un livre avec les valeurs initiales
livre = Livre("Le Rouge et le Noir", "Stendhal", 640)

# Vérification de la disponibilité initiale
print(f"\nLe livre est disponible : {livre.verification()}")

# Emprunter le livre
livre.emprunter()

# Vérification après l'emprunt
print(f"\nLe livre est disponible : {livre.verification()}")

# Vérification après l'emprunt
livre.emprunter()
print()
# Rendre le livre
livre.rendre()

# Vérification après le rendu
print(f"\nLe livre est disponible : {livre.verification()}")

# Vérification après le rendu
livre.rendre()