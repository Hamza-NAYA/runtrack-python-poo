
class Tache:
    def __init__(self, titre, description, statut="À faire"):
        # Initialise une tâche avec un titre, une description et un statut par défaut "À faire"
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        # Renvoie une représentation sous forme de chaîne de caractères de la tâche
        return f"{self.titre} - {self.description} - {self.statut}"


class ListeDeTaches:
    def __init__(self):
        # Initialise une liste de tâches vide
        self.taches = []

    def ajouterTache(self, tache):
        # Ajoute une tâche à la liste
        self.taches.append(tache)

    def supprimerTache(self, tache):
        # Supprime une tâche de la liste, si elle existe
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"Tâche '{tache.titre}' supprimée")
        else:
            print("Tâche non trouvée.")

    def marquerCommeFinie(self, tache):
        # Modifie le statut d'une tâche à "Terminée", si elle existe dans la liste
        if tache in self.taches:
            tache.statut = "Terminée"
            print(f"Tâche '{tache.titre}' marquée comme terminée")
        else:
            print("Tâche non trouvée")

    def afficherListe(self):
        # Affiche toutes les tâches de la liste
        print("\nListe des tâches:")
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        # Filtre les tâches en fonction du statut spécifié
        filtered_taches = [tache for tache in self.taches if tache.statut == statut]
        return filtered_taches


# Test du code
tache_1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache_2 = Tache("Répondre aux emails", "Répondre aux emails professionnels")
tache_3 = Tache("Faire du sport", "Aller à la salle de sport")

Liste_de_Taches = ListeDeTaches()

# Ajout des tâches à la liste
Liste_de_Taches.ajouterTache(tache_1)
Liste_de_Taches.ajouterTache(tache_2)
Liste_de_Taches.ajouterTache(tache_3)

# Affichage de la liste
Liste_de_Taches.afficherListe()

# Suppression d'une tâche
Liste_de_Taches.supprimerTache(tache_2)

# Affichage de la liste après suppression
Liste_de_Taches.afficherListe()

# Marquer une tâche comme terminée
Liste_de_Taches.marquerCommeFinie(tache_1)

# Affichage de la liste après marquage
Liste_de_Taches.afficherListe()

# Filtrer les tâches par statut
Taches_à_faire = Liste_de_Taches.filterListe("À faire")
print("\nTâches à faire:")
for tache in Taches_à_faire:
    print(tache)