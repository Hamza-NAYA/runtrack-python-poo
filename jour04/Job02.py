
class Personne:
    def __init__(self, age=14):
        # Initialisation du constructeur de la classe Personne avec l'âge par défaut à 14
        self.age = age

    def afficherAge(self):
        # Méthode pour afficher l'âge
        print(f"Age de la personne : {self.age} ans")

    def bonjour(self):
        # Méthode pour afficher "Hello"
        print("Hello")

    def modifierAge(self, nouvel_age):
        # Méthode pour modifier l'âge
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        # Méthode spécifique à la classe Eleve
        print("Je vais en cours")

    def afficherAge(self):
        # Méthode redéfinie pour afficher un message spécifique à l'élève
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        # Constructeur de la classe Professeur avec un attribut supplémentaire
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        # Méthode spécifique à la classe Professeur
        print("Le cours va commencer")

# Création d'un élève
eleve_1 = Eleve()

# Utilisation de la méthode bonjour pour l'élève
eleve_1.bonjour()

# Utilisation de la méthode allerEnCours pour l'élève
eleve_1.allerEnCours()

# Redéfinition de l'âge de l'élève à 15 ans
eleve_1.modifierAge(15)

# Affichage du nouvel âge de l'élève
eleve_1.afficherAge()

# Création d'un professeur
professeur_1 = Professeur(age=40)

# Utilisation de la méthode bonjour pour le professeur
professeur_1.bonjour()

# Utilisation de la méthode enseigner pour le professeur
professeur_1.enseigner()