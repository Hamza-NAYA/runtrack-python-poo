import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        # Initialisation du paquet de cartes
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)

    def calculer_total(self, main):
        # Calcul du total des points dans une main
        total = 0
        as_present = False

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                as_present = True
                total += 1
            else:
                total += int(carte.valeur)

        # Traitement spécial pour les As
        if as_present and total + 10 <= 21:
            total += 10

        return total

    def afficher_main(self, main, joueur):
        # Affichage de la main d'un joueur avec le total des points
        print(f"\nMain de {joueur}:")
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")
        print(f"Total: {self.calculer_total(main)}")

    def jouer_partie(self):
        # Initialisation des mains du joueur et du croupier
        joueur_main = [self.paquet.pop(), self.paquet.pop()]
        croupier_main = [self.paquet.pop(), self.paquet.pop()]

        while True:
            # Affichage de la main du joueur et prise de décision
            self.afficher_main(joueur_main, "Joueur")

            if input("Voulez-vous prendre une carte ? (Oui/Non): ").lower() == 'oui':
                # Le joueur prend une carte et vérifie s'il a dépassé 21
                joueur_main.append(self.paquet.pop())
                if self.calculer_total(joueur_main) > 21:
                    print("Vous avez dépassé 21. Vous avez perdu!")
                    break
            else:
                break

        # Le croupier prend des cartes jusqu'à atteindre au moins 17 points
        while self.calculer_total(croupier_main) < 17:
            croupier_main.append(self.paquet.pop())

        # Affichage des mains du joueur et du croupier
        self.afficher_main(joueur_main, "Joueur")
        self.afficher_main(croupier_main, "Croupier")

        # Résultat de la partie
        if self.calculer_total(joueur_main) > 21:
            print("Vous avez dépassé 21. Vous avez perdu!")
        elif self.calculer_total(croupier_main) > 21 or self.calculer_total(joueur_main) > self.calculer_total(croupier_main):
            print("Félicitations! Vous avez gagné!")
        elif self.calculer_total(joueur_main) == self.calculer_total(croupier_main):
            print("Égalité!")
        else:
            print("Le croupier a gagné!")
while True:
    jeu = Jeu()
    jeu.jouer_partie()
    rejouer = input("\nVoulez-vous rejouer ? (Oui/Non): ").lower()
    if rejouer != 'oui':
        break