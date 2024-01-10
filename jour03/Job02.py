
class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=True):
        # Initialise un compte bancaire avec un numéro de compte, un nom, un prénom, un solde et l'option de découvert.
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        # Affiche les informations du compte bancaire.
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Titulaire : {self.__prenom} {self.__nom}")
        print(f"Solde : {self.__solde} €")
        print(f"Découvert autorisé : {self.__decouvert}")

    def afficherSolde(self):
        # Affiche le solde actuel du compte.
        print(f"Solde du compte : {self.__solde} €")

    def versement(self, montant):
        # Effectue un versement sur le compte et affiche le nouveau solde.
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")

    def retrait(self, montant):
        # Effectue un retrait du compte si le solde est suffisant ou si le découvert est autorisé.
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Opération non autorisée. Solde insuffisant")

    def agios(self):
        # Applique des agios si le solde est négatif
        if self.__solde < 0:
            frais = abs(self.__solde) * 0.05
            self.__solde -= frais
            print(f"Agios appliqués. Nouveau solde : {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        # Effectue un virement vers un autre compte si le solde est suffisant ou si le découvert est autorisé
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès")
        else:
            print("Opération non autorisée. Solde insuffisant")


# Création d'un compte bancaire normal
compte1 = CompteBancaire("123456", "Doe", "John", 1000, False)

# Affichage du compte
compte1.afficher()

# Versement
compte1.versement(500)

# Retrait
compte1.retrait(200)

# Affichage du solde
compte1.afficherSolde()

# Création d'un compte bancaire à découvert
compte2 = CompteBancaire("789012", "Smith", "Alice", -200)

# Virement du compte1 vers le compte2 pour le remettre à zéro
compte1.virement(compte2, 1200)

# Affichage des deux comptes après le virement
print("\nCompte 1:")
compte1.afficher()
print("\nCompte 2:")
compte2.afficher()