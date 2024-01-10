
class Personne:
    def __init__(self, nom, prenom):
        # Initialisation du constructeur de la classe Personne avec un nom et un prénom fournis en paramètres
        self.surname = nom  # Attribut pour stocker le nom en tant que surname
        self.firstname = prenom  # Attribut pour stocker le prénom en tant que firstname

    def sePresenter(self):
        # Méthode qui renvoie une chaîne de caractères avec les deux attributs présentant la personne
        return f"Je suis {self.firstname} {self.surname}"

# Création de deux personne avec des noms et prénoms différents en utilisant la classe Personne
personne_1 = Personne("Doe", "John")
personne_2 = Personne("Dupond", "Jean")

# Appel de la méthode sePresenter pour afficher nos deux personnages
print(personne_1.sePresenter())
print(personne_2.sePresenter())