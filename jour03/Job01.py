
class Ville:
    def __init__(self, nom, nb_habitants):
        # Initialise une ville avec un nom et un nombre d'habitants
        self.__name = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self):
        # Renvoie le nom de la ville
        return self.__name

    def get_nb_habitants(self):
        # Renvoie le nombre d'habitants de la ville
        return self.__nb_habitants

    def augmenter_population(self):
        # Incrémente le nombre d'habitants de la ville
        self.__nb_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        # Initialise une personne avec un nom, un âge et une ville. Augmente la population de la ville
        self.__name = nom
        self.__age = age
        self.__ville = ville
        ville.augmenter_population()

    def get_nom(self):
        # Renvoie le nom de la personne
        return self.__name

    def get_age(self):
        # Renvoie l'âge de la personne
        return self.__age

    def get_ville(self):
        # Renvoie la ville de la personne
        return self.__ville

    def ajouter_population(self):
        # Utilise la méthode de la ville pour augmenter sa population
        self.__ville.augmenter_population()


# Création des objets Ville
Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants de chaque ville
print(f"Population de la ville de {Paris.get_nom()}: {Paris.get_nb_habitants()} habitants")
print(f"Population de la ville de {Marseille.get_nom()}: {Marseille.get_nb_habitants()} habitants")

# Création des objets Personne
persone_1 = Personne("John", 45, Paris)
personne_2 = Personne("Myrtille", 4, Paris)
personne_3 = Personne("Chloé", 18, Marseille)

# Affichage du nombre d'habitants après l'arrivée des nouvelles personnes
print(f"Mise à jour de la population de la ville de {Paris.get_nom()} {Paris.get_nb_habitants()} habitants")
print(f"Mise à jour de la population de la ville de {Marseille.get_nom()} {Marseille.get_nb_habitants()} habitants")