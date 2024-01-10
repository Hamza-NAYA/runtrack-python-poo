
class Commande:
    def __init__(self, numero):
        # Initialise la commande avec un numéro, une liste de plats vide et un statut "en cours"
        self.__numero = numero
        self.__liste_plats = {}
        self.__statut = "en cours"

    def ajouter_plat(self, plat, prix):
        # Ajoute un plat à la liste seulement si la commande n'est pas annulée
        if self.__statut != "annulée":
            self.__liste_plats[plat] = {"prix": prix, "statut": self.__statut}

    def annuler_commande(self):
        # Change le statut de la commande et annule tous les plats associés
        self.__statut = "annulée"
        for plat in self.__liste_plats:
            self.__liste_plats[plat]["statut"] = "annulée"

    def calculer_total(self):
        # Calcule le total des plats non annulés
        total = 0
        for plat in self.__liste_plats:
            if self.__liste_plats[plat]["statut"] != "annulée":
                total += self.__liste_plats[plat]["prix"]
        return round(total, 2)

    def afficher_commande(self):
        # Affiche les détails de la commande, y compris le total, la TVA et le total à payer
        total = self.calculer_total()
        tva = self.calculer_tva(total)
        total_a_payer = round(total + tva, 2)
        print("Numéro de commande: #", self.__numero)
        print("Liste des plats commandés:")
        for plat in self.__liste_plats:
            print("\t", plat, "Prix:", self.__liste_plats[plat]["prix"], "Statut:", self.__liste_plats[plat]["statut"])
        print("Total:", total)
        print("TVA:", tva)
        print("Total à payer:", total_a_payer)

    def calculer_tva(self, total):
        # Calcule la TVA à 20% du total
        return round(total * 0.2, 2)

# Crée une commande, ajoute des plats, affiche la commande, annule la commande, puis réaffiche la commande
commande = Commande(1)
commande.ajouter_plat("Assiette 1", 11.5)
commande.ajouter_plat("Assiette 2", 15.99)
commande.afficher_commande()
commande.annuler_commande()
commande.afficher_commande()