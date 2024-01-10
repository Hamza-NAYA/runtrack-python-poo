import time
import random

class Personnage:
    def __init__(self, nom, vie):
        # Initialisation d'un personnage avec un nom et une quantité de vie
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        # Méthode pour gérer l'attaque d'un personnage sur un adversaire
        print(f"{self.nom} attaque {adversaire.nom}!")
        adversaire.vie -= random.randint(8, 15)

class Jeu:
    def __init__(self):
        # Initialisation du jeu avec un niveau par défaut
        self.niveau = 1

    def choisirNiveau(self):
        # Méthode pour permettre au joueur de choisir le niveau de difficulté
        print("Bienvenue dans le jeu de combat ! Choisissez votre niveau de difficulté :")
        self.niveau = int(input("1. Facile\n2. Normal\n3. Difficile\n4. Expert\nVotre choix : "))

    def afficherCombat(self, joueur, ennemi):
        # Méthode pour afficher les détails du combat
        print("\n===================================")
        print(f"{joueur.nom} VS {ennemi.nom}")
        print("===================================")

    def jouer(self):
        # Méthode principale pour gérer le déroulement du jeu
        if self.niveau == 1:
            joueur = Personnage("Joueur", self.niveau * 50)
            ennemi = Personnage("Ennemi", self.niveau * 30)
        elif self.niveau == 2:
            joueur = Personnage("Joueur", self.niveau * 50)
            ennemi = Personnage("Ennemi", self.niveau * 40)
        elif self.niveau == 3:
            joueur = Personnage("Joueur", self.niveau * 50)
            ennemi = Personnage("Ennemi", self.niveau * 45)
        elif self.niveau == 4:
            joueur = Personnage("Joueur", self.niveau * 40)
            ennemi = Personnage("Ennemi", self.niveau * 40)
        else:
            # Gestion du cas où le niveau choisi n'est pas valide
            print("Vous devez choisir parmi les niveaux de difficulté présent")
            self.choisirNiveau()

        print(f"\nLe combat commence ! Niveau {self.niveau}\n")

        while joueur.vie > 0 and ennemi.vie > 0:
            self.afficherCombat(joueur, ennemi)

            joueur.attaquer(ennemi)
            time.sleep(1)

            if ennemi.vie <= 0:
                print("\033[92mFélicitations ! Vous avez vaincu l'ennemi\033[0m")
                break

            ennemi.attaquer(joueur)
            time.sleep(1)

            if joueur.vie <= 0:
                print("\033[91mDommage ! L'ennemi vous a vaincu\033[0m")
                break

            print(f"{joueur.nom} a {joueur.vie} points de vie restants")
            print(f"{ennemi.nom} a {ennemi.vie} points de vie restants")

        rejouer = input("Voulez-vous rejouer ? (Oui/Non): ").lower()
        if rejouer == 'oui':
            self.jouer()

    def lancerJeu(self):
        # Méthode pour lancer le jeu et gérer les redémarrages
        while True:
            self.choisirNiveau()
            self.jouer()
            rejouer = input("Voulez-vous revenir au menu principal ? (Oui/Non): ").lower()
            if rejouer != 'oui':
                break

# Création de l'instance du jeu et lancement
jeu = Jeu()
jeu.lancerJeu()