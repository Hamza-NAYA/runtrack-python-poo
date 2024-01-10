
class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        # Initialisation du constructeur de la classe Student avec nom, prenom et numero_etudiant fournies en paramètres
        self.__surname = nom # Attribut pour stocker le nom de l'étudiant en tant que surname
        self.__firstname = prenom # Attribut pour stocker le prenom de l'étudiant en tant que firstname
        self.__student_number = numero_etudiant # Attribut pour stocker le numero_etudiant de l'étudiant en tant que student_number
        self.__credit_number = 0
        self.__level = self.studentEval()

    def ajouterCredits(self, credits):
        # Méthode pour ajouter des crédits
        if credits > 0:
            self.__credit_number += credits
            print(f"Le nombre de credits de {self.__firstname} {self.__surname} est de {self.__credit_number} points")
            self.__level = self.studentEval()
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro")

    def studentEval(self):
        # Méthode privée pour évaluer le niveau de l'étudiant
        if self.__credit_number >= 90:
            return "Excellent"
        elif self.__credit_number >= 80:
            return "Très bien"
        elif self.__credit_number >= 70:
            return "Bien"
        elif self.__credit_number >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        # Méthode pour afficher les informations de l'étudiant
        print(f"\nNom = {self.__surname}")
        print(f"Prénom = {self.__firstname}")
        print(f"id = {self.__student_number}")
        print(f"Niveau = {self.__level}\n")

# Création de l'étudiant John Doe avec le numéro d'étudiant 145
etudiant = Student("Doe","John", 145)

# Ajout de crédits à trois reprises
print()
etudiant.ajouterCredits(30)
etudiant.ajouterCredits(25)
etudiant.ajouterCredits(20)

# Affichage des informations de l'étudiant
etudiant.studentInfo()