
class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        # Initialisation du constructeur de la classe Operation avec les valeurs par défaut (12 et 3)
        self.num_1 = nombre1  # Attribut pour stocker le nombre1 en tant que num_1
        self.num_2 = nombre2  # Attribut pour stocker le nombre2 en tant que num_2

    def addition(self):
        # Méthode pour additionner deux nombres et afficher le résultat
        somme = self.num_1 + self.num_2
        print(somme)

# Création d'une variable test pour la classe Operation
test = Operation()

# Appel de la méthode addition de la classe Operation, qui effectue l'addition et affiche le résultat
test.addition()