
class Joueur:
    def __init__(self, nom, numero, position):
        # Initialise un joueur avec un nom, un numéro, et une position
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        # Incrémente le nombre de buts marqués par le joueur
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        # Incrémente le nombre de passes décisives effectuées par le joueur
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        # Incrémente le nombre de cartons jaunes reçus par le joueur
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        # Incrémente le nombre de cartons rouges reçus par le joueur
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        # Affiche les statistiques du joueur
        print(f"\nStatistiques de {self.nom} (#{self.numero}, {self.position}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives effectuées: {self.passes_decisives}")
        print(f"Cartons jaunes reçus: {self.cartons_jaunes}")
        print(f"Cartons rouges reçus: {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        # Initialise une équipe avec un nom et une liste de joueurs vide
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        # Ajoute un joueur à la liste des joueurs de l'équipe
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        # Affiche les statistiques de tous les joueurs de l'équipe
        print(f"\nStatistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        # Met à jour les statistiques d'un joueur spécifique de l'équipe
        joueur.buts_marques += buts
        joueur.passes_decisives += passes_decisives
        joueur.cartons_jaunes += cartons_jaunes
        joueur.cartons_rouges += cartons_rouges


# Création des joueurs
joueur_1 = Joueur("Messi", 10, "Attaquant")
joueur_2 = Joueur("Ronaldo", 7, "Attaquant")
joueur_3 = Joueur("Modric", 8, "Milieu")

# Création des équipes
equipe_1 = Equipe("Barcelona")
equipe_2 = Equipe("Real Madrid")

# Ajout des joueurs aux équipes
equipe_1.ajouterJoueur(joueur_1)
equipe_2.ajouterJoueur(joueur_2)
equipe_2.ajouterJoueur(joueur_3)

# Affichage des statistiques avant le match
equipe_1.afficherStatistiquesJoueurs()
equipe_2.afficherStatistiquesJoueurs()

# Simulation d'un match
joueur_1.marquerUnBut()
joueur_2.marquerUnBut()
joueur_2.marquerUnBut()
joueur_2.effectuerUnePasseDecisive()
joueur_1.effectuerUnePasseDecisive()
joueur_3.recevoirUnCartonJaune()
joueur_3.effectuerUnePasseDecisive()

# Mise à jour des statistiques après le match
equipe_1.mettreAJourStatistiquesJoueur(joueur_1, buts=1, passes_decisives=1)

# Affichage des statistiques après le match
equipe_1.afficherStatistiquesJoueurs()
equipe_2.afficherStatistiquesJoueurs()