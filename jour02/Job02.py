
class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        # Initialisation du constructeur de la classe Livre avec titre, auteur et nombres_pages fournies en paramètres
        self.__title = titre # Attribut pour stocker le titre du livre en tant que title
        self.__author = auteur # Attribut pour stocker l'auteur du livre en tant que author
        self.__pages_number = nombre_pages # Attribut pour stocker le nombre_pages du livre en tant que pages_number

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

# Création d'un livre avec les valeurs initiales
livre = Livre("Le Rouge et le Noir", "Stendhal", 640)

# Affichage du livre
print(f"\nTitre : {livre.obtenirTitre()}")
print(f"Auteur : {livre.obtenirAuteur()}")
print(f"Nombre de pages : {livre.obtenirNombrePages()}")

# Changement de livre
livre.modifierTitre("L'Ingénu")
livre.modifierAuteur("Voltaire")
livre.modifierNombrePages(192)

# Affichage du nouveau livre
print(f"\nNouveau titre : {livre.obtenirTitre()}")
print(f"Nouvel auteur : {livre.obtenirAuteur()}")
print(f"Nouveau nombre de pages : {livre.obtenirNombrePages()}\n")

# Vérification de la condition nombte entier et positif et de l'affichage du message d'erreur
livre.modifierNombrePages(-100)