
class Animal:
    def __init__(self):
        # Initialisation du constructeur de la classe Animal avec des attributs par défaut
        self.age = 0  # Attribut pour stocker l'âge de l'animal en tant que age
        self.prenom = ""  # Attribut pour stocker le prénom de l'animal en tant que prenom

    def vieillir(self):
        # Méthode qui fait vieillir l'animal en incrémentant son âge de 1
        self.age += 1

    def nommer(self, nom):
        # Méthode qui donne un prénom à l'animal
        self.prenom = nom

# Création d'une variable test pour la classe Animal
test = Animal()

# Affichage initial de l'âge de l'animal
print("L'age de l'animal", test.age, "ans")

# Appel de la méthode vieillir pour augmenter l'âge de l'animal
test.vieillir()

# Affichage du nouvel âge de l'animal
print("L'age de l'animal", test.age, "ans")

# Appel de la méthode nommer pour donner un prénom à l'animal
test.nommer("Luna")

# Affichage du prénom de l'animal
print("L'animal se nomme", test.prenom)