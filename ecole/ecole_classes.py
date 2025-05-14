# Ce fichier contient les classes de base pour le projet d'école.
#
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

def __repr__(self):
    return f"Personne(nom={self.nom}, prenom={self.prenom}, age={self.age})"

class Etudiant(Personne):
    def __init__(self, nom: str, prenom: str, age: int, filiere: str, niveau_etude: int):
        super().__init__(nom, prenom, age)
        self.filiere = filiere
        self.niveau_etude = niveau_etude

    def __repr__(self):
        return f"{self.prenom} {self.nom}, {self.age} ans - Étudiant en {self.filiere}, niveau {self.niveau_etude}"

class Professeur(Personne):
    def __init__(self, nom, prenom, age, specialite, annee_experience, annee_etude):
        super().__init__(nom, prenom, age)
        self.specialite = specialite
        self.annee_experience = annee_experience
        self.annee_etude = annee_etude

def __repr__(self):
    return f"(super().__repr__(), Professeur(specialite={self.specialite}, annee_experience={self.annee_experience}, annee_etude={self.annee_etude}))"
