
class Operation:
    def __init__(self, nombre1=1, nombre2=2):
        # Initialisation du constructeur de la classe Operation avec deux paramètres, par défaut 1 et 2
        self.num_1 = nombre1  # Attribut pour stocker le nombre1 en tant que num_1
        self.num_2 = nombre2  # Attribut pour stocker le nombre2 en tant que num_2

# Création d'une variable test pour la classe Operation
test = Operation()

# Affichage de la variable test, ce qui imprime l'emplacement mémoire par défaut de notre classe Operation
print(test)