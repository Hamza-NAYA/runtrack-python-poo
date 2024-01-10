
class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        # Initialisation du constructeur de la clasee Operation avec les valeurs par défaut (12 et 3)
        self.num_1 = nombre1  # Attribut pour stocker le nombre1 en tant que num_1
        self.num_2 = nombre2  # Attribut pour stocker le nombre2 en tant que num_2

# Création d'une variable test pour la classe Operation
test = Operation()

# Affichage des valeurs des attributs num_1 et num_2
print("Le nombre1 est", test.num_1)
print("Le nombre2 est", test.num_2)