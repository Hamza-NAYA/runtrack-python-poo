
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


# Instanciation d'une personne
personne_1 = Personne()
personne_1.afficherAge()
personne_1.bonjour()
personne_1.modifierAge(48)
personne_1.afficherAge()

# Instanciation d'un élève
eleve_1 = Eleve()
eleve_1.afficherAge()
eleve_1.allerEnCours()

# Instanciation d'un professeur
professeur_1 = Professeur(35, "Mathématiques")
professeur_1.afficherAge()
professeur_1.enseigner()
print("salut")