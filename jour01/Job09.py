
class Produit:
    def __init__(self, nom, prixHT, tva):
        # Initialisation du constructeur de la classe Produit avec un nom, un prix hors taxe, et un taux de TVA fournie en paramètres
        self.name = nom  # Attribut pour stocker le nom du produit en tant que name
        self.prixHT = prixHT  # Attribut pour stocker le prix HT du produit en tant que prixHT
        self.tva = tva  # Attribut pour stocker le taux de TVA du produit en tant que tva

    def calculerPrixTTC(self):
        # Méthode qui calcule et renvoie le prixTTC du produit
        return self.prixHT * (1 + self.tva / 100)

    def afficher(self):
        # Méthode qui affiche les informations du produit nom, prixHT et tva
        return f"Nom: {self.nom}, Prix HT: {self.prixHT} €, TVA: {self.tva}%"

    def modifierNom(self, nouveau_nom):
        # Méthode pour modifier le nom du produit
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        # Méthode pour modifier le prixHT du produit
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        # Méthode qui renvoie le nom du produit
        return self.nom

    def obtenirPrixHT(self):
        # Méthode qui renvoie le prixHT du produit
        return self.prixHT

    def obtenirTVA(self):
        # Méthode qui renvoie le taux de TVA du produit
        return self.tva

# Création de deux produits de la classe Produit avec des caractéristiques différentes
produit_1 = Produit("Manga", 12.0, 5)
produit_2 = Produit("Ordinateur", 800.0, 20)

# Affichage des informations des deux produits
print(produit_1.afficher())
print(produit_2.afficher())

# Calcul et affichage des prix TTC des deux produits
produit_1_TTC = produit_1.calculerPrixTTC()
produit_2_TTC = produit_2.calculerPrixTTC()

# Affichage des prixTTC des deux produits
print(f"Prix TTC du produit 1: {produit_1_TTC} €")
print(f"Prix TTC du produit 2: {produit_2_TTC} €")

# Modification du nom et du prixHT de chaque produit
produit_1.modifierNom("Livre")
produit_1.modifierPrixHT(15.0)
produit_2.modifierNom("Ordinateur portable")
produit_2.modifierPrixHT(750.0)

# Affichage des nouvelles informations des deux produits
print(produit_1.afficher())
print(produit_2.afficher())

# Affichage des nouveaux noms et prix HT des deux produits
print(f"Nouveau nom du produit 1: {produit_1.obtenirNom()}")
print(f"Nouveau prix HT du produit 1: {produit_1.obtenirPrixHT()} €")

print(f"Nouveau nom du produit 2: {produit_2.obtenirNom()}")
print(f"Nouveau prix HT du produit 2: {produit_2.obtenirPrixHT()} €")